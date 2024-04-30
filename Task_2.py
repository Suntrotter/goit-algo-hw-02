from collections import deque

def is_palindrome(s):    
    s = s.lower().replace(" ", "")    
    queue = deque()
    for char in s:
        queue.append(char)
    
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            print("This is not a palindrome")
            return False
    print("This is a palindrome")
    return True


is_palindrome("12 34321")
is_palindrome("123123")
is_palindrome("765Uiu56 7")

