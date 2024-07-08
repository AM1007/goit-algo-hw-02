def is_balanced(s):
    stack = []
    opening = "({["
    closing = ")}]"
    matches = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if stack and stack[-1] == matches[char]:
                stack.pop()
            else:
                return "Несиметрично"
    
    return "Симетрично" if not stack else "Несиметрично"

# Тести
print(is_balanced("( ){[ 1 ]( 1 + 3 )( ){ }}"))  
print(is_balanced("( 23 ( 2 - 3);"))             
print(is_balanced("( 11 }"))                    
print(is_balanced("{[()]}"))                    
print(is_balanced("[(])"))                       
print(is_balanced("{[(])}"))                    

# Додатковий тест для перевірки порожнього рядка
print(is_balanced(""))                           
