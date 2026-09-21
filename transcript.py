# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:55:10 2026

@author: 

Extract a speaker-labelled transcript with WhisperX.
"""

import sys
import subprocess
import os
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
os.environ["OMP_NUM_THREADS"] = "4"
os.environ["MKL_NUM_THREADS"] = "4"
# os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"

import socket
from pathlib import Path
import numpy  # noqa: F401  # load MKL OpenMP first

import torch
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True
print("Torch:", torch.__version__)
# print("Original torch.load:", torch.load)

from omegaconf import ListConfig, DictConfig
from omegaconf.base import ContainerMetadata
try:
    torch.serialization.add_safe_globals([ListConfig, DictConfig, ContainerMetadata])
except Exception:
    pass

def upgrade_checkpoint():
    """
    Runs the PyTorch Lightning checkpoint upgrade command.
    """
    # Define the path to the checkpoint file
    checkpoint_path = r"C:\Users\molin\miniforge3\envs\audiovideo\Lib\site-packages\whisperx\assets\pytorch_model.bin"
    
    # Construct the command
    # Note: 'python -m pytorch_lightning.utilities.upgrade_checkpoint' is the CLI entry point
    command = [
        sys.executable, 
        "-m", 
        "pytorch_lightning.utilities.upgrade_checkpoint",
        checkpoint_path
    ]
    
    try:
        # Execute the command
        result = subprocess.run(
            command, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True
        )
        # print("Upgrade successful.")
        # print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Upgrade failed with error code {e.returncode}")
        print(e.stderr)
    return

try:
    if Upgraded:
        pass
except Exception:
        upgrade_checkpoint()   
        Upgraded = True
        print("**** UPGRADED ****")

import functools
_original_load = torch.load
@functools.wraps(_original_load)
def _robust_load(*args, **kwargs):
    kwargs["weights_only"] = False
    return _original_load(*args, **kwargs)

    
try: 
    if robust_loaded:
        pass
except Exception:
        torch.load = _robust_load
        robust_loaded = True
        print("**** ROBUST LOADED ****")
        

from inspect import signature
import whisperx
from whisperx.diarize import DiarizationPipeline

# from importlib.metadata import version
# print("WhisperX:", version("whisperx"))
# print("PyTorch:", version("torch"))
# print("Torchaudio:", version("torchaudio"))
# print("Pyannote:", version("pyannote.audio"))
# print("HuggingFace Hub:", version("huggingface_hub"))

# import inspect
# print(inspect.signature(whisperx.load_align_model))

from typing import Iterable, Sequence



# hostname -> (model_size, device_index, compute_type)
HOST_MODELS = {
    "LEM-Z440": ("large-v3", 0, "float16"),  # Titan RTX 24GB; use 1 for the 2080 Super
    # "OFFICE-PC": ("turbo", 0, "float16"),
    # "LAPTOP-X": ("small", 0, "int8_float16"),
    }

DEFAULT = ("small", 0, "int8")

# FFMPEG supported Audio/Video Extensions
AUDIO_EXTS = [".wav", ".wave", ".mp3", ".m4a", ".aac", ".flac", ".ogg", ".oga", 
              ".opus", ".wma", ".aiff", ".aif", ".aifc", ".amr",  ".mp2", ".mpga", 
              ".mka", ".caf", ".ac3", ".eac3", ".dts", ".weba"
              ]

# LIST 3 — video (audio track extracted)
VIDEO_EXTS = [ ".mp4", ".m4v", ".mkv", ".webm", ".mov", ".avi", ".wmv", ".flv",
              ".mpeg", ".mpg", ".mpe", ".m2v", ".ts", ".m2ts", ".mts", ".3gp", 
              ".3g2", ".ogv", ".asf", ".vob", ".f4v"
              ]

ALL_EXTS = AUDIO_EXTS + VIDEO_EXTS

MIN_DURATION = 1.00      # seconds on screen (BBC-ish floor)
HOLD_AFTER = 1.00        # extra after last spoken word (try 1.0–1.5)
MIN_GAP = 0.080          # 80 ms so players can clear the previous cue
MAX_DURATION = 7.00      # Netflix cap
MAX_LINE_CHARS = 42


model = None

def media_files(path: str | Path, extensions: Sequence[str]) -> list[Path]:
    """Return files under *path* whose suffix is in *extensions*.

    *path* may be a file or a directory.
    Extensions may be given with or without a leading dot and are
    matched case-insensitively.
    """
    path = Path(path)
    allowed = {
        ext.lower() if ext.startswith(".") else f".{ext.lower()}"
        for ext in extensions
    }

    if path.is_file():
        return [path] if path.suffix.lower() in allowed else []

    if path.is_dir():
        return sorted(
            p for p in path.iterdir()
            if p.is_file() and p.suffix.lower() in allowed
        )

    return []

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

def ts(t: float) -> str:
    t = max(0.0, float(t))
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    ms = int(round((s % 1) * 1000))
    if ms == 1000:
        s, ms = s + 1, 0
    return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{ms:03d}"

def _line(text: str) -> str:
    text = " ".join((text or "").split())
    return text if text.startswith("- ") else f"- {text}"

def segments_to_dialogue_cues(segments):
    cues = []
    for seg in segments:
        words = seg.get("words") or []
        if not words:
            text = (seg.get("text") or "").strip()
            if text:
                cues.append((seg["start"], seg["end"], text))
            continue

        cur_spk = words[0].get("speaker", seg.get("speaker"))
        buf, t0 = [], words[0]["start"]
        last_end = words[0]["end"]

        for w in words:
            spk = w.get("speaker", cur_spk)
            if spk != cur_spk and buf:
                cues.append((t0, last_end, " ".join(buf).strip()))
                buf, t0, cur_spk = [], w["start"], spk
            token = (w.get("word") or "").strip()
            if token:
                buf.append(token)
            last_end = w.get("end", last_end)

        if buf:
            cues.append((t0, last_end, " ".join(buf).strip()))
    return cues


def write_dialogue_srt(
    cues,
    path,
    min_duration=MIN_DURATION,
    hold_after=HOLD_AFTER,
    min_gap=MIN_GAP,
    max_duration=MAX_DURATION,
                    ):
    """
    cues: iterable of (start, end, text) from segments_to_dialogue_cues().
    Extends each cue for reading time, then either dual-line merges
    overlapping turns or trims the previous out-time.
    """
    raw = []
    for start, end, text in cues:
        text = " ".join((text or "").split())
        if text:
            raw.append([float(start), float(end), text])
    raw.sort(key=lambda c: (c[0], c[1]))

    timed = []
    for start, end, text in raw:
        end = max(end, start + min_duration, end + hold_after)
        end = min(end, start + max_duration)
        if end > start:
            timed.append([start, end, text])

    resolved = []
    for start, end, text in timed:
        if not resolved:
            resolved.append([start, end, text])
            continue

        prev = resolved[-1]
        limit = start - min_gap

        if prev[1] <= limit:
            resolved.append([start, end, text])
            continue

        # Collision: prefer a dual-speaker (or two-beat) 2-line cue
        merged_text = f"{_line(prev[2])}\n{_line(text)}"
        merged_ok = (
            merged_text.count("\n") == 1
            and all(len(line) <= MAX_LINE_CHARS + 2 for line in merged_text.splitlines())
        )
        if merged_ok:
            prev[1] = min(max(prev[1], end), prev[0] + max_duration)
            prev[2] = merged_text
            continue

        # Cannot merge: chain — keep speech in-time of next, shorten previous
        if limit > prev[0] + 0.3:
            prev[1] = limit
            resolved.append([start, end, text])
        else:
            # Next starts almost immediately; attach as second line anyway
            prev[1] = min(max(prev[1], end), prev[0] + max_duration)
            prev[2] = merged_text

    out = Path(path)
    with out.open("w", encoding="utf-8") as f:
        n = 1
        for start, end, text in resolved:
            if end <= start:
                continue
            body = text if "\n" in text else _line(text)
            f.write(f"{n}\n{ts(start)} --> {ts(end)}\n{body}\n\n")
            n += 1
    return out

def extract_transcript(
    media_path: str | Path,
    language: str | None = None,
    save: bool = True,
    num_speakers: int | None = None,
    batch_size: int = 16,
    save_srt: bool = False
                        ) -> dict:
    
    global model
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
    params = signature(DiarizationPipeline.__init__).parameters
    # print("diarize args", list(params))

    print("---->Extrating Audio")
    audio = whisperx.load_audio(str(path))
    vad_method="silero"

    # print("LOAD_MODEL with modelsize={}, device={}, device_index={}, compute_type={}, vad_method={}, language={}".format(
    #         model_size,
    #         wx_device,
    #         index,
    #         compute_type,
    #         vad_method,
    #         language
    #         )
    #     )
    
    if model is None:
        print("---->Loading Model")
        model = whisperx.load_model(
                model_size,
                device=wx_device,    # "cuda" or "cpu" only
                device_index=index,  # 0 = Titan if nvidia-smi lists it first        
                compute_type=compute_type,
                vad_method=vad_method,
                language=language,   # skip extra language-detect pass if you know it
                )
    
    # inner = model.model
    # print(inner)
    # print(getattr(inner, "model", inner))
    print("---->Transcribing")
    asr = model.transcribe(audio, batch_size=batch_size, language=language)
    detected_language = asr.get("language") or language or "en"
    print("---->Alligning Model")
    align_model, metadata = whisperx.load_align_model(
        language_code=detected_language,
        device=wx_device,
        )
    print("---->Alligning")
    asr = whisperx.align(
        asr["segments"],
        align_model,
        metadata,
        audio,
        wx_device,
        return_char_alignments=False,
        )
      
    
    diarize_kwargs = {"device": wx_device}  # "cuda" is fine here (PyTorch path)
    if hf_token:
        if "token" in params:
            diarize_kwargs["token"] = hf_token
        elif "use_auth_token" in params:
            diarize_kwargs["use_auth_token"] = hf_token
    try:
        diarize_model = DiarizationPipeline(**diarize_kwargs)
    except TypeError:
        diarize_kwargs.pop("token", None)
        if hf_token:
            diarize_kwargs["use_auth_token"] = hf_token  # older whisperx
        diarize_model = DiarizationPipeline(**diarize_kwargs)
    print("---->Diarinzing")
    if num_speakers is not None:
        diarize_segments = diarize_model(audio, num_speakers=num_speakers)
    else:
        diarize_segments = diarize_model(audio)
        
    print("---->Assigning Speakers")
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
        print("---->Saving")
        if save_srt:
            out = path.with_suffix("{}.srt".format("."+detected_language if (detected_language is not None) else ""))
            cues = segments_to_dialogue_cues(result["segments"])
            write_dialogue_srt(cues,out, min_duration=1.0, hold_after=1.5)
        else:
            out = path.with_suffix(".txt")
            out.write_text(text, encoding="utf-8")
            result["output_path"] = str(out)

    return result

if __name__ == "__main__":
    raw = input("Enter path to Directory or video/audio file: ").strip().strip('"')
    save_srt = False
    response = input("Write Transcript in SRT (y/n): ")
    if response=='y' or response=='Y'  :
        save_srt = True
    all_raw = media_files(raw, ALL_EXTS)
    for raw in all_raw:
        print('--------------------------------------------------------')
        print(f"Proccesing: {str(raw)}")
        data = extract_transcript(media_path=raw, 
                                  language= None,
                                  save= True,
                                  num_speakers = None,
                                  batch_size = 16,
                                  save_srt=save_srt)
        print(f"PC: {data['pc']}")
        # print(f"Device: {data['device']} ({data['compute_type']})")
        # print(f"Language: {data['language']}")
        print(data["text"][:50])
        
    
    
    
   