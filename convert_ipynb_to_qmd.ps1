# RAG 섹션의 모든 .ipynb 파일을 .qmd로 변환하고 YAML 헤더를 추가하는 스크립트

$baseDir = "c:\Users\kmkim\Desktop\projects\blog\docs\blog\posts\RAG"

# 캐시 폴더는 제외하고 .ipynb 파일 찾기
$ipynbFiles = Get-ChildItem -Path $baseDir -Recurse -Filter "*.ipynb" | 
    Where-Object { $_.FullName -notlike "*\.jupyter_cache\*" }

Write-Host "총 $($ipynbFiles.Count)개의 .ipynb 파일을 찾았습니다." -ForegroundColor Green
Write-Host ""

# 폴더별로 그룹화
$filesByFolder = $ipynbFiles | Group-Object -Property { $_.Directory.FullName }

foreach ($folder in $filesByFolder) {
    $folderPath = $folder.Name
    $folderName = Split-Path $folderPath -Leaf
    $files = $folder.Group
    
    Write-Host "=== $folderName 폴더 처리 중 ($($files.Count)개 파일) ===" -ForegroundColor Cyan
    
    # 해당 폴더로 이동
    Push-Location $folderPath
    
    foreach ($file in $files) {
        $fileName = $file.Name
        $baseName = $file.BaseName
        $qmdFile = "$baseName.qmd"
        
        Write-Host "  변환 중: $fileName -> $qmdFile" -ForegroundColor Yellow
        
        # Quarto 변환 실행
        try {
            quarto convert $fileName 2>&1 | Out-Null
            
            if (Test-Path $qmdFile) {
                Write-Host "    ✓ 변환 완료" -ForegroundColor Green
            } else {
                Write-Host "    ✗ 변환 실패" -ForegroundColor Red
            }
        } catch {
            Write-Host "    ✗ 오류 발생: $_" -ForegroundColor Red
        }
    }
    
    # 원래 위치로 복귀
    Pop-Location
    Write-Host ""
}

Write-Host "=== 변환 작업 완료 ===" -ForegroundColor Green
Write-Host ""
Write-Host "다음 단계:" -ForegroundColor Yellow
Write-Host "1. 변환된 .qmd 파일들의 YAML 헤더를 확인하세요"
Write-Host "2. 필요한 경우 YAML 헤더를 개선하세요"
Write-Host "3. 확인 후 원본 .ipynb 파일들을 삭제하세요"
Write-Host ""
Write-Host "원본 .ipynb 파일 삭제 명령어:"
Write-Host 'Get-ChildItem -Path "' + $baseDir + '" -Recurse -Filter "*.ipynb" | Where-Object { $_.FullName -notlike "*\.jupyter_cache\*" } | Remove-Item -Force' -ForegroundColor Magenta
