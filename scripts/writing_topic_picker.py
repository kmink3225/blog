#!/usr/bin/env python3
"""
writing_topic_picker.py — backward-compatible wrapper
======================================================
tutoring_topic_picker.py 로 통합됐다.
이 파일은 기존 호출 인터페이스를 유지하는 thin wrapper다.

Usage (기존과 동일):
  python scripts/writing_topic_picker.py --level 5
  python scripts/writing_topic_picker.py --level 2 --group art
  python scripts/writing_topic_picker.py --level 7 --group 13
  python scripts/writing_topic_picker.py --level 5 --seed 42
  python scripts/writing_topic_picker.py --level 5 --format text

통합 스크립트 직접 호출 (권장):
  python scripts/tutoring_topic_picker.py --tutor writing --level 5 --group art
"""

import sys
from pathlib import Path

# 같은 scripts/ 디렉터리의 tutoring_topic_picker 모듈을 임포트한다
sys.path.insert(0, str(Path(__file__).parent))

import argparse
import json
from tutoring_topic_picker import (
    GUIDES_DIR,
    _exit_error,
    _make_rng,
    parse_writing_topics,
    pick_writing_topic,
    _WRITING_GROUP_NAMES,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Writing 튜터 주제 선정 스크립트 (tutoring_topic_picker.py 위임)"
    )
    parser.add_argument(
        "--level", type=int, required=True, choices=range(1, 8),
        metavar="LEVEL", help="글쓰기 레벨 (1~7)"
    )
    parser.add_argument(
        "--group", type=str, default="random",
        help="그룹 지정: random(기본) / 번호(1~15) / 키워드(art, law, ...)"
    )
    parser.add_argument(
        "--seed", type=int, default=None,
        help="난수 seed (미지정 시 os.urandom() — 매번 다른 결과)"
    )
    parser.add_argument(
        "--format", choices=["json", "text"], default="json",
        help="출력 형식 (기본값: json)"
    )
    args = parser.parse_args()

    md_path = GUIDES_DIR / "writing-topics.md"
    if not md_path.exists():
        _exit_error(f"writing-topics.md 를 찾을 수 없다: {md_path}")

    data = parse_writing_topics(md_path)
    result = pick_writing_topic(args.level, args.group, args.seed, data)

    # backward compat: 기존 출력에는 "tutor" 키가 없었다 — 제거하여 호환성 유지
    result_compat = {k: v for k, v in result.items() if k != "tutor"}

    if args.format == "json":
        print(json.dumps(result_compat, ensure_ascii=False, indent=2))
    else:
        print(f"[그룹 {result['group_id']}: {result['group_name']}] {result['topic']}")


if __name__ == "__main__":
    main()
