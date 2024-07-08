from collections import deque

def is_palindrome(s):
    # Приведення рядка до нижнього регістру та видалення пробілів
    s = s.lower().replace(" ", "")
    
    # Створення двосторонньої черги та додання символів рядка
    char_deque = deque(s)
    
    # Порівняння символів з обох кінців черги
    while len(char_deque) > 1:
        front = char_deque.popleft()
        back = char_deque.pop()
        if front != back:
            return False
    
    return True

# Тести
print(is_palindrome("кит на морі романтик"))  
print(is_palindrome("ротор"))                     
print(is_palindrome("УДАР - в Раду!"))                       
print(is_palindrome("А роза упала на лапу Азора"))  
print(is_palindrome("Привіт Пайтон"))            
