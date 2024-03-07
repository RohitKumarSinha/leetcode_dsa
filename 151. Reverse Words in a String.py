def reverseWords(s):

    #split the words
    words = s.split()

    #reverse the words in array 
    words = words[::-1]

    #trim the words 
    return ' '.join(words)

ans = reverseWords('My Name Is Rohit')
print(ans)