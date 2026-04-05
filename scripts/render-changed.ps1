# render-changed.ps1
# Renders only .qmd files changed since the last commit.
# Usage: .\scripts\render-changed.ps1

$root = Split-Path $PSScriptRoot -Parent
Set-Location $root

# Changed .qmd files (staged + unstaged + untracked)
$changed = @()
$changed += git --no-pager diff --name-only HEAD -- "*.qmd" 2>$null
$changed += git --no-pager diff --name-only --cached -- "*.qmd" 2>$null
$changed += git --no-pager ls-files --others --exclude-standard -- "*.qmd" 2>$null

# Deduplicate and filter out excluded patterns
$targets = $changed | Sort-Object -Unique | Where-Object {
    $_ -and
    $_ -notmatch "^_" -and
    $_ -notmatch "TBD\.qmd$"
}

if ($targets.Count -eq 0) {
    Write-Host "No changed .qmd files found."
    exit 0
}

Write-Host "Render targets: $($targets.Count)"
$targets | ForEach-Object { Write-Host "  $_" }
Write-Host ""

$success = 0
$fail = 0

foreach ($file in $targets) {
    $fullPath = Join-Path $root $file
    if (-not (Test-Path $fullPath)) {
        Write-Host "SKIP (File not found): $file"
        continue
    }
    Write-Host "Rendering: $file"
    quarto render $fullPath 2>&1
    if ($LASTEXITCODE -eq 0) { $success++ } else { $fail++; Write-Host "FAIL: $file" }
}

Write-Host ""
Write-Host "Finished - Success: $success, Failure: $fail"
