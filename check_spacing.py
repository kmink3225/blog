import re
filepath = 'docs/blog/posts/Statistics/72-common-families-continuous-beta-distribution.qmd'
with open(filepath, encoding='utf-8') as f:
    lines = f.readlines()
korean = re.compile(r'[\uAC00-\uD7A3]')
violations = []
for i, line in enumerate(lines, 1):
    for m in re.finditer(r'\$', line):
        pos = m.start()
        after = line[pos+1] if pos+1 < len(line) else ''
        before = line[pos-1] if pos > 0 else ''
        if korean.match(after):
            violations.append((i, 'after$', line.rstrip()))
            break
        if korean.match(before):
            violations.append((i, 'before$', line.rstrip()))
            break
for v in violations:
    print(f'L{v[0]} [{v[1]}]: {v[2]}')
print(f'Total violations: {len(violations)}')
print(f'Total lines: {len(lines)}')
