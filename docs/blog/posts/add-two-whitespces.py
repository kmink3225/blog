import os
from pathlib import Path

def add_trailing_spaces_to_qmd(file_path):
    """qmd 파일의 각 줄 끝에 공백 2칸을 추가하는 함수"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # YAML 헤더 찾기
        yaml_end = content.find('---', 3)
        if yaml_end != -1:
            yaml_header = content[:yaml_end + 3]
            body = content[yaml_end + 3:]
            
            # 본문의 각 줄 끝에 공백 2칸 추가 (이미 공백 2칸이 있는 줄은 제외)
            lines = body.split('\n')
            processed_lines = []
            for line in lines:
                if line and not line.endswith('  '):
                    processed_lines.append(line + '  ')
                else:
                    processed_lines.append(line)
            
            new_content = yaml_header + '\n' + '\n'.join(processed_lines)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f'✓ {file_path}')
            return True
        else:
            print(f'✗ {file_path} - YAML header not found')
            return False
    except Exception as e:
        print(f'✗ {file_path} - Error: {str(e)}')
        return False

def process_folder(folder_path):
    """특정 폴더 하위의 모든 qmd 파일을 재귀적으로 처리"""
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f'Error: Folder not found - {folder_path}')
        return
    
    # 모든 qmd 파일 찾기 (하위 폴더 포함)
    qmd_files = list(folder.rglob('*.qmd'))
    
    if not qmd_files:
        print(f'No .qmd files found in {folder_path}')
        return
    
    print(f'Found {len(qmd_files)} .qmd file(s) in {folder_path}')
    print('-' * 80)
    
    success_count = 0
    for qmd_file in qmd_files:
        if add_trailing_spaces_to_qmd(qmd_file):
            success_count += 1
    
    print('-' * 80)
    print(f'Completed: {success_count}/{len(qmd_files)} files processed successfully')

# 사용 예시
if __name__ == '__main__':
    # 처리할 폴더 경로 지정
    target_folder = r'c:\Users\kmkim\Desktop\projects\blog\docs\blog\posts\Agent\13-Cloud-RAG'
    
    print(f'Processing folder: {target_folder}')
    print('=' * 80)
    process_folder(target_folder)


