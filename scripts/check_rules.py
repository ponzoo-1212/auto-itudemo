#!/usr/bin/env python3
"""表記ルールのチェック: 漢数字の混入と、12時間表記（午前/午後）を検出する。"""
import re
import sys
from pathlib import Path

KANJI_NUM = re.compile(r"[一二三四五六七八九〇零十百千]|(?<![0-9])万")
# 数を表さない慣用表現は許可（一緒・一番など）
ALLOW = re.compile(r"一緒|一番|一瞬|一気|一生|一切|一言|一方|一部|一覧|一人称|一斉|一杯|十分|万一|一応|一旦|一体|一種|一面|四角|四季|三角|二度寝|三日月|二重|統一|一文|同一|一致")
AMPM = re.compile(r"午前|午後")

targets = sys.argv[1:] or [str(p) for p in sorted(Path("works").glob("*/*.md"))]
found = 0
for t in targets:
    for no, line in enumerate(Path(t).read_text(encoding="utf-8").splitlines(), 1):
        if KANJI_NUM.search(ALLOW.sub("", line)):
            print(f"[漢数字] {t}:{no}: {line.strip()}")
            found += 1
        if AMPM.search(line):
            print(f"[12時間表記] {t}:{no}: {line.strip()}")
            found += 1

print(f"\n違反候補: {found}件")
sys.exit(1 if found else 0)
