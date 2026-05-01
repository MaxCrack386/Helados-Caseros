import json

with open('app.js', 'r', encoding='utf-8') as f:
    text = f.read()

def check_balance(text):
    stack = []
    pairs = {'{': '}', '[': ']', '(': ')'}
    inverse = {v: k for k, v in pairs.items()}
    line_num = 1
    
    in_string = False
    string_char = ''
    in_comment = False
    in_block_comment = False
    
    i = 0
    while i < len(text):
        c = text[i]
        
        if c == '\n':
            line_num += 1
            in_comment = False
            
        if in_comment:
            i += 1
            continue
            
        if in_block_comment:
            if c == '*' and i + 1 < len(text) and text[i+1] == '/':
                in_block_comment = False
                i += 1
            i += 1
            continue
            
        if in_string:
            if c == '\\':
                i += 2
                continue
            if c == string_char:
                in_string = False
            i += 1
            continue
            
        if c in ['\'', '\"', '`']:
            in_string = True
            string_char = c
            i += 1
            continue
            
        if c == '/' and i + 1 < len(text):
            if text[i+1] == '/':
                in_comment = True
                i += 1
                continue
            elif text[i+1] == '*':
                in_block_comment = True
                i += 1
                continue
                
        if c in pairs:
            stack.append((c, line_num))
        elif c in inverse:
            if not stack:
                print(f'Unmatched closing {c} at line {line_num}')
                return
            top, ln = stack.pop()
            if top != inverse[c]:
                print(f'Mismatched {c} at line {line_num}. Expected {pairs[top]} from line {ln}')
                return
                
        i += 1

    if stack:
        print(f'Unclosed {stack[-1][0]} from line {stack[-1][1]}')
    else:
        print('Braces are balanced!')

check_balance(text)
