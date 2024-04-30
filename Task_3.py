def check_delimiters(s):
    stack = []
    opening = "([{"
    closing = ")]}"
        
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return "Asymmetric"
            last_opening = stack.pop()
            if opening.index(last_opening) != closing.index(char):
                return "Asymmetric"
    
    if stack:
        return "Asymmetric"
    else:
        return "Symmetric"
    
print(check_delimiters('( ){[ 1 ]( 1 + 3 )( ){ }}:'))  
print(check_delimiters('( 23 ( 2 - 3);:'))            
print(check_delimiters('( 11 }:'))                    
