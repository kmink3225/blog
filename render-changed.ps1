# render-changed.ps1
# 변경되거나 새로 추가된 .qmd 파일만 렌더링 후 git push
# 사용법: .\render-changed.ps1

Set-Location $PSScriptRoot

# 1. 변경/신규 .qmd 파일 수집 (git 기준)
$staged    = git diff --name-only --cached 2>$null | Where-Object { $_ -match "\.qmd$" }
$unstaged  = git diff --name-only         2>$null | Where-Object { $_ -match "\.qmd$" }
$untracked = git ls-files --others --exclude-standard 2>$null | Where-Object { $_ -match "\.qmd$" }

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
    conda run -n blog quarto render $file
    if ($LASTEXITCODE -ne 0) {
        Write-Host "ERROR: $file 렌더 실패" -ForegroundColor Red
        exit 1
    }
}

# 3. 블로그 index 재렌더 (목록/네비게이션 업데이트)
Write-Host "`n[index 업데이트]" -ForegroundColor Cyan
conda run -n blog quarto render docs/blog/index.qmd

# 4. git add, commit, push
Write-Host "`n=== Git Push ===" -ForegroundColor Cyan
git add -A
$msg = "Update blog: $($targets -join ', ')"
git commit -m "$msg`n`nCo-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
git push origin

Write-Host "`n=== 완료 ===" -ForegroundColor Green
