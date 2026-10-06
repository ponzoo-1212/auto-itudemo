#!/usr/bin/env python3
"""表記ルールのチェック: 漢数字の混入と、12時間表記（午前/午後）を検出する。"""
import re
import sys
from pathlib import Path

KANJI_NUM = re.compile(r"[一二三四五六七八九〇零十百千]|(?<![0-9])万")
AMPM = re.compile(r"午前|午後|(?:朝|夜|昼)の?(?:[1-9]|1[0-2])時")

targets = sys.argv[1:] or [str(p) for p in sorted(Path("story").glob("*.md"))]
found = 0
for t in targets:
    for no, line in enumerate(Path(t).read_text(encoding="utf-8").splitlines(), 1):
        if KANJI_NUM.search(line):
            print(f"[漢数字] {t}:{no}: {line.strip()}")
            found += 1
        if AMPM.search(line):
            print(f"[12時間表記] {t}:{no}: {line.strip()}")
            found += 1

print(f"\n違反候補: {found}件")
sys.exit(1 if found else 0)
