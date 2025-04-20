def palindrome():
    x=int(input("Enter a number: "))
    sum=0    
    y=x
    while x>0:
        r=x % 10
        sum=sum*10+r
        x=x // 10
    if y==sum:
        return "It is a palindrome"
    else:
        return "It is not a palindrome"
print(palindrome())    

    