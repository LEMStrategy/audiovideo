#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:37:52 2025

@author: cygnus_x1
"""

import zipfile
import re
from pathlib import Path
import xml.etree.ElementTree as ET


def detect_javascript(epub_path):
    #
    book_path = Path(epub_path)
    if book_path.is_dir():
        book_list = [book for book in book_path.iterdir() if book.suffix == '.epub']
        for epub_book in book_list:
            with zipfile.ZipFile(epub_book, 'r') as zip_ref:
                for file in zip_ref.namelist():
                    if file.endswith('.js'):
                        print(f"JavaScript file found: {file}")
                    elif file.endswith('.html') or file.endswith('.xhtml'):
                        with zip_ref.open(file) as f:
                            content = f.read().decode('utf-8')
                            if re.search(r'<script>', content):
                                print(f"Embedded JavaScript found in: {file}")
                    elif file.endswith('.xml'):
                        # print(f"XML file found: {file}")
                        try:
                            with zip_ref.open(file) as f:
                                content = f.read().decode('utf-8')
                                # Check for XXE injection vulnerabilities
                                if re.search(r'<!ENTITY', content):
                                    print(f"Potential XXE vulnerability found in: {file}")
                                # Check for embedded scripts (less common in XML)
                                if re.search(r'<script>', content):
                                    print(f"Embedded script found in: {file}")
                                # Parse XML to check for suspicious elements
                                try:
                                    root = ET.fromstring(content)
                                    for elem in root.iter():
                                        if elem.tag == 'script':
                                            print(f"Embedded script tag found in: {file}")
                                except ET.ParseError:
                                    print(f"Failed to parse XML in: {file}")
                        except Exception as e:
                            print(f"Error processing {file}: {e}")