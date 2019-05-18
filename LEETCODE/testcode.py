
S = "a-bC-dEf-ghIj"
S = list(S)
i, j = 0, -1
while i + abs(j) <= len(S)-1:
    if S[i].isalpha() == True and S[j].isalpha() == True:
        S[i], S[j] = S[j], S[i]
        i += 1
        j -= 1
        continue
    if S[i].isalpha() == False and S[j].isalpha() == False:
        i += 1
        j -= 1
        continue
    if S[i].isalpha() == True and S[j].isalpha() == False:
        j -= 1
        continue
    if S[i].isalpha() == False and S[j].isalpha() == True:
        i += 1
        continue
S = ''.join(S)
print(S)

# "j-Ih-gfE-dCba"
