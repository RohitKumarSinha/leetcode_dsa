def encode(message):
    encoded = ''

    count = 1

    for index in range(1, len(message)):
        if (message[index] == message[index-1]):
            count += 1 

        else:
            encoded += message[index - 1] + str(count)
            count = 1

    encoded += message[-1] + str(count)

    return encoded



ans = encode('cbbbeeeff')
print(ans)