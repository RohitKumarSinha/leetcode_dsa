def minAddToMakeValid(s):

    balance = 0
    result = 0

    for i in s:
        if i == '(':
            balance += 1

        elif i == ')':
            if balance > 0:
                balance -= 1
            
            else:
                result += 1

    result += balance

    return result 

ans = minAddToMakeValid(')(())')
print(ans)