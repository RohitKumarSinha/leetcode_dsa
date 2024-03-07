def reverseWords(s):

    #split the word 
    word = s.split()

    #reverse the word in array
    word = word[::-1]

    # trim the word 
    return " ".join(word)

ans = reverseWords('My Name Is Rohit')
print(ans)