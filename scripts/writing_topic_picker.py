#!/usr/bin/env python3
"""
writing_topic_picker.py
=======================
Writing 튜터 주제 선정 스크립트.

guides/writing-topics.md를 파싱하여 지정된 레벨·그룹에서
uniform random으로 주제를 선정하고 JSON으로 출력한다.

JSON 출력 형식은 Claude Code, Gemini, GPT 등 모든 AI 에이전트가
공통으로 읽을 수 있는 표준 인터페이스로 설계됐다.

Usage
-----
  # 레벨만 지정 (그룹 random)
  python scripts/writing_topic_picker.py --level 5

  # 그룹 키워드 지정
  python scripts/writing_topic_picker.py --level 2 --group art

  # 그룹 번호 지정
  python scripts/writing_topic_picker.py --level 7 --group 13

  # seed 고정 (재현 가능)
  python scripts/writing_topic_picker.py --level 5 --seed 42

  # 날짜 seed (오늘의 주제 고정)
  python scripts/writing_topic_picker.py --level 5 --seed 20260408

  # plain text 출력 (사람이 읽는 용도)
  python scripts/writing_topic_picker.py --level 5 --format text

Output (JSON, default)
----------------------
  {
    "group_id": 13,
    "group_name": "예술·창작",
    "tier": "C",
    "level": 5,
    "topic": "문화 산업화는 예술의 비판적 기능을 구조적으로 약화시키는가",
    "seed": 42
  }
"""

import argparse
import json
import os
import random
import re
import sys
from pathlib import Path

# ── 상수 정의 ─────────────────────────────────────────────────────────────────

GROUP_NAMES = {
    1: "교육",
    2: "기술·AI",
    3: "환경·기후",
    4: "사회·문화",
    5: "경제·노동",
    6: "정치·제도",
    7: "윤리·도덕",
    8: "건강·의료",
    9: "미디어·정보",
    10: "법률·정의",
    11: "관계·공동체",
    12: "과학·연구",
    13: "예술·창작",
    14: "역사·문명",
    15: "스포츠·여가",
}

# 영문/한글 키워드 → 그룹 번호
GROUP_ALIASES: dict[str, int] = {
    "education": 1, "교육": 1,
    "tech": 2, "ai": 2, "기술": 2,
    "environment": 3, "env": 3, "환경": 3,
    "society": 4, "culture": 4, "사회": 4,
    "economy": 5, "labor": 5, "경제": 5,
    "politics": 6, "정치": 6,
    "ethics": 7, "moral": 7, "윤리": 7,
    "health": 8, "medical": 8, "건강": 8,
    "media": 9, "information": 9, "미디어": 9,
    "law": 10, "justice": 10, "법률": 10,
    "community": 11, "relationship": 11, "관계": 11,
    "science": 12, "research": 12, "과학": 12,
    "art": 13, "arts": 13, "예술": 13,
    "history": 14, "역사": 14,
    "sports": 15, "leisure": 15, "스포츠": 15,
}

# 레벨 → 티어
LEVEL_TO_TIER: dict[int, str] = {
    1: "A", 2: "A",
    3: "B", 4: "B",
    5: "C", 6: "C",
    7: "D",
}

# ── 파서 ──────────────────────────────────────────────────────────────────────

def parse_topics(md_path: Path) -> dict[int, dict[str, list[str]]]:
    """
    writing-topics.md를 파싱하여
    {group_id: {"A": [...], "B": [...], "C": [...], "D": [...]}} 구조로 반환한다.
    """
    content = md_path.read_text(encoding="utf-8")
    topics: dict[int, dict[str, list[str]]] = {
        i: {"A": [], "B": [], "C": [], "D": []} for i in range(1, 16)
    }
    current_group: int | None = None

    for line in content.splitlines():
        # 그룹 헤더: ### 그룹 N: 이름
        m = re.match(r"^### 그룹 (\d+):", line)
        if m:
            current_group = int(m.group(1))
            continue

        # 테이블 데이터 행
        if current_group and line.startswith("| "):
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 3 and parts[0] in ("A", "B", "C", "D"):
                tier, _, topic = parts[0], parts[1], parts[2]
                if topic:
                    topics[current_group][tier].append(topic)

    return topics

# ── 선정 로직 ─────────────────────────────────────────────────────────────────

def resolve_group(group_arg: str, rng: random.Random) -> int:
    """그룹 인수(random / 번호 / 키워드)를 그룹 번호(1~15)로 변환한다."""
    if group_arg.lower() == "random":
        return rng.randint(1, 15)
    if group_arg.isdigit():
        gid = int(group_arg)
        if gid not in range(1, 16):
            _exit_error(f"그룹 번호는 1~15 범위여야 한다: {gid}")
        return gid
    alias = group_arg.lower()
    if alias not in GROUP_ALIASES:
        _exit_error(f"알 수 없는 그룹 키워드: {group_arg}")
    return GROUP_ALIASES[alias]


def pick_topic(
    level: int,
    group_id: int,
    topics: dict[int, dict[str, list[str]]],
    rng: random.Random,
) -> dict:
    """레벨과 그룹 ID를 받아 주제를 선정하고 결과 dict를 반환한다."""
    tier = LEVEL_TO_TIER[level]
    candidates = topics[group_id][tier]
    if not candidates:
        _exit_error(f"그룹 {group_id} 티어 {tier}에 등록된 주제가 없다.")
    topic = rng.choice(candidates)
    return {
        "group_id": group_id,
        "group_name": GROUP_NAMES[group_id],
        "tier": tier,
        "level": level,
        "topic": topic,
    }

# ── 유틸 ──────────────────────────────────────────────────────────────────────

def _exit_error(msg: str) -> None:
    print(json.dumps({"error": msg}, ensure_ascii=False), file=sys.stderr)
    sys.exit(1)

# ── 진입점 ────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Writing 튜터 주제 선정 스크립트 — JSON 출력"
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
        help="난수 seed (미지정 시 시스템 시간 사용 — 매번 다른 결과)"
    )
    parser.add_argument(
        "--format", choices=["json", "text"], default="json",
        help="출력 형식 (기본값: json)"
    )
    args = parser.parse_args()

    # writing-topics.md 경로: 스크립트 위치 기준
    topics_path = Path(__file__).parent.parent / "guides" / "writing-topics.md"
    if not topics_path.exists():
        _exit_error(f"writing-topics.md 를 찾을 수 없다: {topics_path}")

    topics = parse_topics(topics_path)
    # seed 미지정 시 os.urandom()으로 진짜 난수 seed 생성
    # random.Random(None)은 Windows에서 빠른 연속 호출 시 같은 시간 기반 seed를 쓸 수 있다
    if args.seed is None:
        true_seed = int.from_bytes(os.urandom(8), "big")
    else:
        true_seed = args.seed
    rng = random.Random(true_seed)

    group_id = resolve_group(args.group, rng)
    result = pick_topic(args.level, group_id, topics, rng)
    result["seed"] = args.seed  # None이면 seed 없이 실행됐음을 명시

    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"[그룹 {result['group_id']}: {result['group_name']}] {result['topic']}")


if __name__ == "__main__":
    main()
