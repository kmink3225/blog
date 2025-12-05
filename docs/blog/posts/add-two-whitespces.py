import re

file_path = r'c:\Users\kmkim\Desktop\projects\blog\docs\blog\posts\Agent\10-Retriever\09-TimeWeightedVectorStoreRetriever.qmd'

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
    
    print('Successfully added trailing spaces')
else:
    print('YAML header not found')
"

완료했습니다! YAML 헤더 이후의 모든 행 끝에 공백 2칸을 추가했습니다.