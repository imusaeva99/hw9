import re

with open('Повесть временных лет.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    text = '\n'.join(lines)
    regex = re.sub('\s{2,}', '\n', text)

with open('result.txt', 'w', encoding='utf-8') as result:
    result.write(regex)
