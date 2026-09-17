# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:55:10 2026

@author: 

Extract a speaker-labelled transcript with WhisperX.
"""

import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "4"
os.environ["MKL_NUM_THREADS"] = "4"
os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"

import socket
from pathlib import Path

import numpy  # noqa: F401  # load MKL OpenMP first
import torch
from omegaconf import ListConfig, DictConfig
from omegaconf.base import ContainerMetadata

try:
    torch.serialization.add_safe_globals([ListConfig, DictConfig])
except Exception:
    pass

import whisperx

# hostname -> (model_size, device_index, compute_type)
HOST_MODELS = {
    "LEM-Z440": ("large-v3", 0, "float16"),  # Titan RTX 24GB; use 1 for the 2080 Super
    # "OFFICE-PC": ("turbo", 0, "float16"),
    # "LAPTOP-X": ("small", 0, "int8_float16"),
    }

DEFAULT = ("small", 0, "int8")


def pc_name() -> str:
    return (
        os.environ.get("COMPUTERNAME")
        or os.environ.get("HOSTNAME")
        or socket.gethostname()
        ).split(".")[0].upper()


def _pick_device() -> tuple[str, str]:
    try:
        import torch
        if getattr(torch.version, "cuda", None) and torch.cuda.is_available():
            return "cuda", "float16"
    except Exception:
        pass
    try:
        import ctranslate2
        if ctranslate2.get_cuda_device_count() > 0:
            return "cuda", "float16"
    except Exception:
        pass
    return "cpu", "int8"


def _format_transcript(segments: list[dict]) -> str:
    lines = []
    last_speaker = None
    for seg in segments:
        speaker = seg.get("speaker") or "SPEAKER_??"
        text = (seg.get("text") or "").strip()
        if not text:
            continue
        start = seg.get("start", 0.0)
        if speaker != last_speaker:
            lines.append(f"\n[{start:7.2f}s] {speaker}: {text}")
            last_speaker = speaker
        else:
            lines.append(text)
    return "\n".join(lines).strip()


def extract_transcript(
    media_path: str | Path,
    language: str | None = None,
    save: bool = True,
    num_speakers: int | None = None,
    batch_size: int = 16,
                        ) -> dict:
    path = Path(media_path).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(path)

    host = pc_name()
    model_size, device_index, host_compute = HOST_MODELS.get(host, DEFAULT)

    device, auto_compute = _pick_device()
    compute_type = host_compute if device == "cuda" else auto_compute
    index = device_index if device == "cuda" else 0

    use_torch_cuda = False
    try:
        use_torch_cuda = bool(getattr(torch.version, "cuda", None)) and torch.cuda.is_available()
    except Exception:
        pass
    
    if device == "cuda" and use_torch_cuda:
        torch.cuda.set_device(index)
        wx_device = "cuda"
    elif device == "cuda":
        wx_device = "cuda"
    else:
        wx_device = "cpu"
        index = 0
        batch_size = 4
        
    hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")

    audio = whisperx.load_audio(str(path))

    model = whisperx.load_model(
            model_size,
            device=wx_device,          # "cuda" or "cpu" only
            device_index=index,        # 0 = Titan if nvidia-smi lists it first
            compute_type=compute_type,
            )
    
    asr = model.transcribe(audio, batch_size=batch_size, language=language)
    detected_language = asr.get("language") or language or "en"

    align_model, metadata = whisperx.load_align_model(
        language_code=detected_language,
        device=wx_device,
        )
    asr = whisperx.align(
        asr["segments"],
        align_model,
        metadata,
        audio,
        wx_device,
        return_char_alignments=False,
        )

    diarize_kwargs = {"device": wx_device}
    if hf_token:
        diarize_kwargs["token"] = hf_token
    try:
        diarize_model = whisperx.DiarizationPipeline(**diarize_kwargs)
    except TypeError:
        diarize_kwargs.pop("token", None)
        if hf_token:
            diarize_kwargs["use_auth_token"] = hf_token
        diarize_model = whisperx.DiarizationPipeline(**diarize_kwargs)

    if num_speakers is not None:
        diarize_segments = diarize_model(audio, num_speakers=num_speakers)
    else:
        diarize_segments = diarize_model(audio)

    asr = whisperx.assign_word_speakers(diarize_segments, asr)
    segments = asr.get("segments") or []
    text = _format_transcript(segments)

    result = {
        "pc": host,
        "model": model_size,
        "device": wx_device,
        "device_index": index,
        "compute_type": compute_type,
        "language": detected_language,
        "text": text,
        "segments": segments,
        }

    if save:
        out = path.with_suffix(".txt")
        out.write_text(text, encoding="utf-8")
        result["output_path"] = str(out)

    return result

if __name__ == "__main__":
    raw = input("Enter path to video or audio file: ").strip().strip('"')
    data = extract_transcript(raw)
    print(f"PC: {data['pc']}")
    print(f"Device: {data['device']} ({data['compute_type']})")
    print(f"Language: {data['language']}")
    print(data["text"][:500])
    print(f"Saved: {data['output_path']}")