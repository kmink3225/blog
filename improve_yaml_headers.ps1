# RAG 섹션의 모든 .qmd 파일의 YAML 헤더를 개선하는 스크립트

$baseDir = "c:\Users\kmkim\Desktop\projects\blog\docs\blog\posts\RAG"

# 폴더별 주제 매핑
$folderTopics = @{
    "01-Basic" = @{
        "subtitle_prefix" = "LangChain 기초"
        "description" = "LangChain의 기본 개념과 OpenAI API 활용법을 다룬다."
    }
    "02-Prompt" = @{
        "subtitle_prefix" = "프롬프트 엔지니어링"
        "description" = "효과적인 프롬프트 템플릿 설계 및 관리 기법을 다룬다."
    }
    "03-OutputParser" = @{
        "subtitle_prefix" = "출력 파싱"
        "description" = "LLM 출력을 구조화된 데이터로 변환하는 다양한 파서를 다룬다."
    }
    "04-Model" = @{
        "subtitle_prefix" = "언어 모델"
        "description" = "다양한 LLM 제공자와 모델 활용법을 다룬다."
    }
    "05-Memory" = @{
        "subtitle_prefix" = "대화 메모리"
        "description" = "대화 컨텍스트를 관리하는 다양한 메모리 시스템을 다룬다."
    }
    "06-DocumentLoader" = @{
        "subtitle_prefix" = "문서 로더"
        "description" = "다양한 형식의 문서를 LangChain으로 로드하는 방법을 다룬다."
    }
    "07-TextSplitter" = @{
        "subtitle_prefix" = "텍스트 분할"
        "description" = "효율적인 문서 청킹을 위한 다양한 텍스트 분할 전략을 다룬다."
    }
    "08-Embeddings" = @{
        "subtitle_prefix" = "임베딩"
        "description" = "텍스트를 벡터로 변환하는 다양한 임베딩 모델을 다룬다."
    }
    "09-VectorStore" = @{
        "subtitle_prefix" = "벡터 스토어"
        "description" = "임베딩 벡터를 저장하고 검색하는 벡터 데이터베이스를 다룬다."
    }
    "10-Retriever" = @{
        "subtitle_prefix" = "검색기"
        "description" = "문서 검색을 위한 다양한 Retriever 패턴과 최적화 기법을 다룬다."
    }
    "11-Reranker" = @{
        "subtitle_prefix" = "재순위화"
        "description" = "검색 결과의 관련성을 개선하는 Reranker 모델을 다룬다."
    }
    "12-RAG" = @{
        "subtitle_prefix" = "RAG 시스템"
        "description" = "검색 증강 생성(RAG) 시스템의 구축과 고급 기법을 다룬다."
    }
}

# 04-Model 폴더는 이미 처리되었으므로 제외
$excludeFolders = @("04-Model")

# .qmd 파일 찾기 (04-Model 제외)
$qmdFiles = Get-ChildItem -Path $baseDir -Recurse -Filter "*.qmd" | 
    Where-Object { 
        $_.FullName -notlike "*\.jupyter_cache\*" -and
        $_.Name -ne "index.qmd" -and
        -not ($excludeFolders | Where-Object { $_.FullName -like "*\$_\*" })
    }

Write-Host "총 $($qmdFiles.Count)개의 .qmd 파일을 처리합니다." -ForegroundColor Green
Write-Host ""

$processedCount = 0
$errorCount = 0

foreach ($file in $qmdFiles) {
    $filePath = $file.FullName
    $fileName = $file.Name
    $folderName = Split-Path (Split-Path $filePath -Parent) -Leaf
    
    # 폴더 주제 정보 가져오기
    $topic = $folderTopics[$folderName]
    if (-not $topic) {
        Write-Host "  ⚠ $folderName 폴더의 주제 정보가 없습니다. 건너뜁니다." -ForegroundColor Yellow
        continue
    }
    
    try {
        # 파일 내용 읽기
        $content = Get-Content -Path $filePath -Raw -Encoding UTF8
        
        # 현재 YAML 헤더 처리 (다양한 형식 지원)
        $currentTitle = ""
        
        # 패턴 1: title이 있는 경우
        if ($content -match '(?s)^---\s*\ntitle:\s*([^\n]+)') {
            $currentTitle = $matches[1].Trim().Trim('"').Trim("'")
        }
        # 패턴 2: title이 없는 경우 (jupyter만 있음) - 파일명에서 추출
        elseif ($content -match '(?s)^---\s*\njupyter:') {
            $currentTitle = $fileName -replace '\.qmd$', '' -replace '^\d+-', '' -replace '-', ' '
        }
        
        if ($currentTitle) {
            # 새로운 YAML 헤더 생성
            $newYaml = @"
---
title: "$currentTitle"
subtitle: $($topic.subtitle_prefix)
description: |
  $($topic.description)
categories:
  - AI
  - RAG
  - LangChain
author: Kwangmin Kim
date: 12/31/2024
format: 
  html:
    page-layout: full
    code-fold: true
    toc: true
    number-sections: true
draft: False
execute:
    eval: false
---
"@
            
            # YAML 헤더 교체
            $newContent = $content -replace '(?s)^---.*?---', $newYaml
            
            # 파일에 쓰기
            $newContent | Out-File -FilePath $filePath -Encoding UTF8 -NoNewline
            
            Write-Host "  ✓ $folderName/$fileName" -ForegroundColor Green
            $processedCount++
        }
        else {
            Write-Host "  ✗ $folderName/$fileName - YAML 헤더를 찾을 수 없습니다." -ForegroundColor Red
            $errorCount++
        }
    }
    catch {
        Write-Host "  ✗ $folderName/$fileName - 오류: $_" -ForegroundColor Red
        $errorCount++
    }
}

Write-Host ""
Write-Host "=== 처리 완료 ===" -ForegroundColor Green
Write-Host "성공: $processedCount 개" -ForegroundColor Green
Write-Host "실패: $errorCount 개" -ForegroundColor Red
Write-Host ""
Write-Host "다음 단계: 원본 .ipynb 파일 삭제" -ForegroundColor Yellow
Write-Host 'Get-ChildItem -Path "' + $baseDir + '" -Recurse -Filter "*.ipynb" | Where-Object { $_.FullName -notlike "*\.jupyter_cache\*" } | Remove-Item -Force' -ForegroundColor Magenta
