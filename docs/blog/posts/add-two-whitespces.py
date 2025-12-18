import os
import sys
from pathlib import Path

# 고정된 기본 경로
BASE_PATH = r'c:\Users\kmkim\Desktop\projects\blog\docs\blog\posts'

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
    # 명령행 인자로 폴더 또는 파일 이름 받기
    if len(sys.argv) < 2:
        print('Usage: python add-two-whitespces.py <folder_or_file_path>')
        print(f'Example (folder, relative): python add-two-whitespces.py Agent\\13-Cloud-RAG')
        print(f'Example (folder, absolute): python add-two-whitespces.py "C:\\Users\\kmkim\\Desktop\\projects\\blog\\docs\\blog\\posts\\Engineering"')
        print(f'Example (file, absolute): python add-two-whitespces.py "C:\\Users\\kmkim\\Desktop\\projects\\blog\\docs\\blog\\posts\\Engineering\\file.qmd"')
        print(f'Base path (for relative paths): {BASE_PATH}')
        sys.exit(1)
    
    # 입력받은 경로 처리
    input_path = sys.argv[1]
    
    # 절대경로인지 확인
    if os.path.isabs(input_path):
        # 절대경로면 그대로 사용
        target_path = input_path
        print(f'Using absolute path: {target_path}')
    else:
        # 상대경로면 BASE_PATH와 결합
        target_path = os.path.join(BASE_PATH, input_path)
        print(f'Base path: {BASE_PATH}')
        print(f'Relative path: {input_path}')
        print(f'Full path: {target_path}')
    
    print('=' * 80)
    
    # 파일인지 폴더인지 확인
    if os.path.isfile(target_path):
        # 단일 파일 처리
        if target_path.endswith('.qmd'):
            print(f'Processing single file...')
            print('-' * 80)
            if add_trailing_spaces_to_qmd(target_path):
                print('-' * 80)
                print('Completed: 1/1 file processed successfully')
            else:
                print('-' * 80)
                print('Failed to process file')
        else:
            print(f'Error: File is not a .qmd file')
    elif os.path.isdir(target_path):
        # 폴더 재귀 처리
        process_folder(target_path)
    else:
        print(f'Error: Path not found - {target_path}')


