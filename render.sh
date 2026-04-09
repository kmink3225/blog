#!/usr/bin/env bash
# render.sh — bash에서 render-changed.ps1을 실행하는 래퍼
# 사용법:
#   bash render.sh            # 변경된 .qmd 렌더링 → push
#   bash render.sh --skip     # 렌더링 스킵 → git add -A → push만

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PS_SCRIPT="$SCRIPT_DIR/render-changed.ps1"

if [[ ! -f "$PS_SCRIPT" ]]; then
    echo "ERROR: render-changed.ps1 not found at $PS_SCRIPT" >&2
    exit 1
fi

# --skip 인수 처리
SKIP_FLAG=""
if [[ "${1:-}" == "--skip" ]]; then
    SKIP_FLAG="-SkipRender"
fi

# PowerShell로 위임
powershell.exe -ExecutionPolicy Bypass \
    -File "$PS_SCRIPT" \
    $SKIP_FLAG
