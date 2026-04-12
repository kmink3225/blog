#!/usr/bin/env python3
"""
tutoring_topic_picker.py
========================
Writing / SQL / Algorithm 튜터 통합 주제 선정 스크립트.

guides/{writing-topics,sql-topics,algo-topics}.md 를 파싱하여
지정된 레벨·그룹·트랙에서 uniform random으로 주제를 선정하고 JSON으로 출력한다.

JSON 출력 형식은 Claude Code, Gemini, GPT 등 모든 AI 에이전트가
공통으로 읽을 수 있는 표준 인터페이스로 설계됐다.

Usage
-----
  # SQL Lv.1 랜덤
  python scripts/tutoring_topic_picker.py --tutor sql --level 1

  # SQL Lv.2 그룹 키워드 지정
  python scripts/tutoring_topic_picker.py --tutor sql --level 2 --group join

  # SQL Lv.2 그룹 번호 지정
  python scripts/tutoring_topic_picker.py --tutor sql --level 2 --group 3

  # Algo DS Lv.2 랜덤
  python scripts/tutoring_topic_picker.py --tutor algo --track DS --level 2

  # Algo AIE Lv.3 그룹 키워드 지정
  python scripts/tutoring_topic_picker.py --tutor algo --track AIE --level 3 --group dfs

  # Algo 공통 Lv.1 랜덤
  python scripts/tutoring_topic_picker.py --tutor algo --track 공통 --level 1

  # Writing Lv.5 그룹 지정 (기존 writing_topic_picker.py 인터페이스 통일)
  python scripts/tutoring_topic_picker.py --tutor writing --level 5 --group art

  # seed 고정 (재현 가능)
  python scripts/tutoring_topic_picker.py --tutor sql --level 1 --seed 42

  # plain text 출력
  python scripts/tutoring_topic_picker.py --tutor sql --level 1 --format text

Output (JSON, default)
----------------------
SQL:
  {
    "tutor": "sql",
    "level": 1,
    "group_id": 3,
    "group_name": "DISTINCT·NULL처리",
    "topic": "IS NULL · IS NOT NULL 조건 필터",
    "seed": null
  }

Algo:
  {
    "tutor": "algo",
    "track": "DS",
    "level": 1,
    "group_id": 2,
    "group_name": "문자열처리",
    "topic": "split + join + replace 조합",
    "seed": null
  }

Writing:
  {
    "tutor": "writing",
    "group_id": 13,
    "group_name": "예술·창작",
    "tier": "C",
    "level": 5,
    "topic": "...",
    "seed": null
  }
"""

import argparse
import json
import os
import random
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
GUIDES_DIR = SCRIPT_DIR.parent / "guides"

ALGO_TRACKS = ("DS", "AIE", "공통")

# 영문 키워드 → 한국어 그룹명 부분 문자열 번역 테이블
# _resolve_group_generic에서 키워드 매칭 전에 적용한다
_KEYWORD_TRANSLATE: dict[str, str] = {
    "backtrack": "백트래킹",
    "backtracking": "백트래킹",
    "simulation": "시뮬레이션",
    "binary": "이진탐색",
    "binary search": "이진탐색",
    "graph": "그래프",
    "advanced graph": "고급그래프",
    "tree": "트리",
    "heap": "힙",
    "prefix": "누적합",
    "prefix sum": "누적합",
    "sliding": "슬라이딩윈도우",
    "window": "슬라이딩윈도우",
    "sort": "정렬",
    "sorting": "정렬",
    "string": "문자열",
    "implementation": "구현",
    "impl": "구현",
    "segment": "세그먼트",
    "segment tree": "세그먼트트리",
    "trie": "trie",
    "union": "union",
    "union find": "union-find",
    "dp": "dp",
    "dynamic": "dp",
    "greedy": "그리디",
    "two pointer": "two pointer",
    "pointer": "two pointer",
    "divide": "분할정복",
    "divide conquer": "분할정복",
}

# ── 유틸 ──────────────────────────────────────────────────────────────────────


def _exit_error(msg: str) -> None:
    print(json.dumps({"error": msg}, ensure_ascii=False), file=sys.stderr)
    sys.exit(1)


def _make_rng(seed_arg):
    """seed_arg가 None이면 os.urandom()으로 진짜 난수 seed를 생성한다."""
    if seed_arg is None:
        true_seed = int.from_bytes(os.urandom(8), "big")
    else:
        true_seed = seed_arg
    return random.Random(true_seed)


# ── SQL ───────────────────────────────────────────────────────────────────────


def parse_sql_topics(md_path: Path) -> dict:
    """
    sql-topics.md 파싱.

    헤더: ### 레벨 N - 그룹 M: GROUP_NAME
    토픽: | topic text |

    반환: {level: {group_id: {"name": str, "topics": [str]}}}
    """
    content = md_path.read_text(encoding="utf-8")
    result: dict = {}
    current_level: int | None = None
    current_gid: int | None = None

    for line in content.splitlines():
        m = re.match(r"^### 레벨 (\d+) - 그룹 (\d+):\s*(.+)", line)
        if m:
            current_level = int(m.group(1))
            current_gid = int(m.group(2))
            group_name = m.group(3).strip()
            result.setdefault(current_level, {})[current_gid] = {
                "name": group_name,
                "topics": [],
            }
            continue

        if current_level is not None and current_gid is not None and line.startswith("| "):
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if parts and parts[0] not in ("topic", "---", "-"):
                result[current_level][current_gid]["topics"].append(parts[0])

    return result


def _resolve_group_generic(group_arg: str, groups: dict, context: str, rng: random.Random) -> int:
    """group_arg (random / 번호 / 키워드) → group_id 정수 반환. SQL·Algo 공용."""
    if not groups:
        _exit_error(f"{context}에 등록된 그룹이 없다.")

    if group_arg.lower() == "random":
        return rng.choice(list(groups.keys()))

    if group_arg.isdigit():
        gid = int(group_arg)
        if gid not in groups:
            _exit_error(f"{context}: 그룹 {gid}가 없다. 가능한 범위: {sorted(groups.keys())}")
        return gid

    # 영문 키워드를 번역 테이블로 변환한 후 부분 문자열 매칭
    raw_keyword = group_arg.lower()
    keyword = _KEYWORD_TRANSLATE.get(raw_keyword, raw_keyword)
    matches = [gid for gid, g in groups.items() if keyword in g["name"].lower()]
    if not matches:
        _exit_error(f"{context}: '{group_arg}' 키워드와 일치하는 그룹이 없다.")
    return rng.choice(matches) if len(matches) > 1 else matches[0]


def pick_sql_topic(level: int, group_arg: str, seed_arg, sql_data: dict) -> dict:
    rng = _make_rng(seed_arg)
    groups = sql_data.get(level, {})
    context = f"SQL 레벨 {level}"
    group_id = _resolve_group_generic(group_arg, groups, context, rng)
    group = groups[group_id]
    if not group["topics"]:
        _exit_error(f"SQL 레벨 {level} 그룹 {group_id}에 토픽이 없다.")
    topic = rng.choice(group["topics"])
    return {
        "tutor": "sql",
        "level": level,
        "group_id": group_id,
        "group_name": group["name"],
        "topic": topic,
        "seed": seed_arg,
    }


# ── ALGO ──────────────────────────────────────────────────────────────────────


def parse_algo_topics(md_path: Path) -> dict:
    """
    algo-topics.md 파싱.

    헤더: ### TRACK - 레벨 N - 그룹 M: GROUP_NAME
    토픽: | topic text |

    반환: {track: {level: {group_id: {"name": str, "topics": [str]}}}}
    """
    content = md_path.read_text(encoding="utf-8")
    result: dict = {}
    current_track: str | None = None
    current_level: int | None = None
    current_gid: int | None = None

    for line in content.splitlines():
        m = re.match(r"^### (\S+) - 레벨 (\d+) - 그룹 (\d+):\s*(.+)", line)
        if m:
            current_track = m.group(1).strip()
            current_level = int(m.group(2))
            current_gid = int(m.group(3))
            group_name = m.group(4).strip()
            result.setdefault(current_track, {}).setdefault(current_level, {})[current_gid] = {
                "name": group_name,
                "topics": [],
            }
            continue

        if (
            current_track is not None
            and current_level is not None
            and current_gid is not None
            and line.startswith("| ")
        ):
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if parts and parts[0] not in ("topic", "---", "-"):
                result[current_track][current_level][current_gid]["topics"].append(parts[0])

    return result


def pick_algo_topic(track: str, level: int, group_arg: str, seed_arg, algo_data: dict) -> dict:
    rng = _make_rng(seed_arg)
    groups = algo_data.get(track, {}).get(level, {})
    context = f"Algo {track} 레벨 {level}"
    group_id = _resolve_group_generic(group_arg, groups, context, rng)
    group = groups[group_id]
    if not group["topics"]:
        _exit_error(f"Algo {track} 레벨 {level} 그룹 {group_id}에 토픽이 없다.")
    topic = rng.choice(group["topics"])
    return {
        "tutor": "algo",
        "track": track,
        "level": level,
        "group_id": group_id,
        "group_name": group["name"],
        "topic": topic,
        "seed": seed_arg,
    }


# ── WRITING ───────────────────────────────────────────────────────────────────

_WRITING_GROUP_NAMES = {
    1: "교육", 2: "기술·AI", 3: "환경·기후", 4: "사회·문화",
    5: "경제·노동", 6: "정치·제도", 7: "윤리·도덕", 8: "건강·의료",
    9: "미디어·정보", 10: "법률·정의", 11: "관계·공동체",
    12: "과학·연구", 13: "예술·창작", 14: "역사·문명", 15: "스포츠·여가",
}

_WRITING_GROUP_ALIASES: dict[str, int] = {
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

_LEVEL_TO_TIER: dict[int, str] = {
    1: "A", 2: "A",
    3: "B", 4: "B",
    5: "C", 6: "C",
    7: "D",
}


def parse_writing_topics(md_path: Path) -> dict:
    """
    writing-topics.md 파싱 (기존 형식 유지).

    반환: {group_id: {"A": [...], "B": [...], "C": [...], "D": [...]}}
    """
    content = md_path.read_text(encoding="utf-8")
    topics: dict = {i: {"A": [], "B": [], "C": [], "D": []} for i in range(1, 16)}
    current_group: int | None = None

    for line in content.splitlines():
        m = re.match(r"^### 그룹 (\d+):", line)
        if m:
            current_group = int(m.group(1))
            continue

        if current_group and line.startswith("| "):
            parts = [p.strip() for p in line.split("|") if p.strip()]
            if len(parts) >= 3 and parts[0] in ("A", "B", "C", "D"):
                tier, topic = parts[0], parts[2]
                if topic:
                    topics[current_group][tier].append(topic)

    return topics


def _resolve_writing_group(group_arg: str, rng: random.Random) -> int:
    if group_arg.lower() == "random":
        return rng.randint(1, 15)
    if group_arg.isdigit():
        gid = int(group_arg)
        if gid not in range(1, 16):
            _exit_error(f"Writing 그룹 번호는 1~15 범위여야 한다: {gid}")
        return gid
    alias = group_arg.lower()
    if alias not in _WRITING_GROUP_ALIASES:
        _exit_error(f"알 수 없는 Writing 그룹 키워드: {group_arg}")
    return _WRITING_GROUP_ALIASES[alias]


def pick_writing_topic(level: int, group_arg: str, seed_arg, writing_data: dict) -> dict:
    rng = _make_rng(seed_arg)
    group_id = _resolve_writing_group(group_arg, rng)
    tier = _LEVEL_TO_TIER[level]
    candidates = writing_data[group_id][tier]
    if not candidates:
        _exit_error(f"Writing 그룹 {group_id} 티어 {tier}에 등록된 주제가 없다.")
    topic = rng.choice(candidates)
    return {
        "tutor": "writing",
        "group_id": group_id,
        "group_name": _WRITING_GROUP_NAMES[group_id],
        "tier": tier,
        "level": level,
        "topic": topic,
        "seed": seed_arg,
    }


# ── 진입점 ────────────────────────────────────────────────────────────────────


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Writing / SQL / Algo 튜터 통합 주제 선정 스크립트 — JSON 출력"
    )
    parser.add_argument(
        "--tutor", required=True, choices=["writing", "sql", "algo"],
        help="튜터 종류 (writing / sql / algo)"
    )
    parser.add_argument(
        "--level", type=int, required=True,
        metavar="LEVEL",
        help="레벨 (writing: 1~7 / sql·algo: 1~5)"
    )
    parser.add_argument(
        "--track", type=str, default=None,
        help="Algo 트랙 (DS / AIE / 공통) — --tutor algo 시 필수"
    )
    parser.add_argument(
        "--group", type=str, default="random",
        help="그룹 지정: random(기본) / 번호(정수) / 키워드(join, dfs, hash, ...)"
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

    # ── 레벨 범위 검증
    if args.tutor == "writing" and args.level not in range(1, 8):
        _exit_error("Writing 레벨은 1~7이어야 한다.")
    if args.tutor in ("sql", "algo") and args.level not in range(1, 6):
        _exit_error("SQL · Algo 레벨은 1~5이어야 한다.")

    # ── Algo 트랙 검증
    if args.tutor == "algo":
        if not args.track:
            _exit_error("--tutor algo 사용 시 --track DS|AIE|공통 이 필수다.")
        if args.track not in ALGO_TRACKS:
            _exit_error(f"알 수 없는 트랙: {args.track}. DS / AIE / 공통 중 선택한다.")

    # ── 실행
    if args.tutor == "writing":
        md_path = GUIDES_DIR / "writing-topics.md"
        if not md_path.exists():
            _exit_error(f"writing-topics.md 를 찾을 수 없다: {md_path}")
        data = parse_writing_topics(md_path)
        result = pick_writing_topic(args.level, args.group, args.seed, data)

    elif args.tutor == "sql":
        md_path = GUIDES_DIR / "sql-topics.md"
        if not md_path.exists():
            _exit_error(f"sql-topics.md 를 찾을 수 없다: {md_path}")
        data = parse_sql_topics(md_path)
        result = pick_sql_topic(args.level, args.group, args.seed, data)

    else:  # algo
        md_path = GUIDES_DIR / "algo-topics.md"
        if not md_path.exists():
            _exit_error(f"algo-topics.md 를 찾을 수 없다: {md_path}")
        data = parse_algo_topics(md_path)
        result = pick_algo_topic(args.track, args.level, args.group, args.seed, data)

    # ── 출력
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        tutor = result["tutor"]
        if tutor == "writing":
            print(f"[그룹 {result['group_id']}: {result['group_name']}] {result['topic']}")
        elif tutor == "sql":
            print(
                f"[SQL Lv.{result['level']} - 그룹 {result['group_id']}: "
                f"{result['group_name']}] {result['topic']}"
            )
        else:
            print(
                f"[Algo {result['track']} Lv.{result['level']} - 그룹 {result['group_id']}: "
                f"{result['group_name']}] {result['topic']}"
            )


if __name__ == "__main__":
    main()
