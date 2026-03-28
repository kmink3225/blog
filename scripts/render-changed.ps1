# render-changed.ps1
# 마지막 커밋 이후 변경된 .qmd 파일만 렌더링한다.
# 사용: .\scripts\render-changed.ps1

$root = Split-Path $PSScriptRoot -Parent
Set-Location $root

# 변경된 .qmd 파일 목록 (staged + unstaged + untracked)
$changed = @()
$changed += git --no-pager diff --name-only HEAD -- "*.qmd" 2>$null
$changed += git --no-pager diff --name-only --cached -- "*.qmd" 2>$null
$changed += git --no-pager ls-files --others --exclude-standard -- "*.qmd" 2>$null

# 중복 제거 및 제외 패턴
$targets = $changed | Sort-Object -Unique | Where-Object {
    $_ -and
    $_ -notmatch "^_" -and
    $_ -notmatch "TBD\.qmd$"
}

if ($targets.Count -eq 0) {
    Write-Host "변경된 .qmd 파일 없음"
    exit 0
}

Write-Host "렌더링 대상: $($targets.Count)개"
$targets | ForEach-Object { Write-Host "  $_" }
Write-Host ""

$success = 0
$fail = 0

foreach ($file in $targets) {
    $fullPath = Join-Path $root $file
    if (-not (Test-Path $fullPath)) {
        Write-Host "SKIP (파일 없음): $file"
        continue
    }
    Write-Host "렌더링: $file"
    quarto render $fullPath 2>&1
    if ($LASTEXITCODE -eq 0) { $success++ } else { $fail++; Write-Host "FAIL: $file" }
}

Write-Host ""
Write-Host "완료 — 성공: $success, 실패: $fail"
