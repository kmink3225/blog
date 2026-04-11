# render-changed.ps1
# 변경되거나 새로 추가된 .qmd 파일만 렌더링 후 Netlify에 직접 배포 + git push
# 사용법:
#   .\render-changed.ps1               # 변경된 .qmd 감지 → 렌더링 → Netlify 배포 → git push
#   .\render-changed.ps1 -SkipRender   # 렌더링 이미 완료된 경우 → Netlify 배포 → git push만

param(
    [switch]$SkipRender   # 렌더링을 건너뛰고 git add -A → commit → push만 실행
)

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

Set-Location $PSScriptRoot

if (-not $SkipRender) {
    # 1. 변경/신규 .qmd 파일 수집 (git 기준)
    # @() 강제 배열 변환 — 단일 파일일 때 문자열 연결 버그 방지
    $staged    = @(git diff --name-only --cached 2>$null | Where-Object { $_ -match "\.qmd$" })
    $unstaged  = @(git diff --name-only         2>$null | Where-Object { $_ -match "\.qmd$" })
    $untracked = @(git ls-files --others --exclude-standard 2>$null | Where-Object { $_ -match "\.qmd$" })

    $targets = ($staged + $unstaged + $untracked) | Sort-Object -Unique | Where-Object { $_ -ne "" }

    if ($targets.Count -eq 0) {
        Write-Host "변경된 .qmd 파일 없음. 렌더링 스킵." -ForegroundColor Yellow
        exit 0
    }

    Write-Host "=== 변경된 파일 $($targets.Count)개 렌더링 ===" -ForegroundColor Cyan
    $targets | ForEach-Object { Write-Host "  - $_" }

    # 2. 변경된 파일만 렌더
    foreach ($file in $targets) {
        Write-Host "`n[렌더] $file" -ForegroundColor Green
        quarto render $file
        if ($LASTEXITCODE -ne 0) {
            Write-Host "ERROR: $file 렌더 실패" -ForegroundColor Red
            exit 1
        }
    }

    # 3. 블로그 index 재렌더 (목록/네비게이션 업데이트)
    Write-Host "`n[index 업데이트]" -ForegroundColor Cyan
    quarto render docs/blog/index.qmd
} else {
    Write-Host "=== 렌더링 스킵 (-SkipRender 옵션) ===" -ForegroundColor Yellow
    $targets = @()
}

# 4. Netlify에 직접 배포 (서버 빌드 없이 로컬 _site/ 업로드)
Write-Host "`n=== Netlify 배포 ===" -ForegroundColor Cyan
quarto publish netlify --no-render --no-browser
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Netlify 배포 실패" -ForegroundColor Red
    exit 1
}

# 5. git add -A, commit, push (소스 .qmd만)
Write-Host "`n=== Git Push ===" -ForegroundColor Cyan
git add -A
$msg = if ($targets.Count -gt 0) { "Update blog: $($targets -join ', ')" } else { "Update blog" }
git commit -m "$msg`n`nCo-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
git push origin
Write-Host "`n=== 완료 ===" -ForegroundColor Green
