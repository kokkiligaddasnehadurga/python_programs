#String is palindrome 
def isPalindrome(s):
    return s==s[ ::-1]
s=input()
p=isPalindrome(s)
if p:
    print('yes')
else:
    print('no')
