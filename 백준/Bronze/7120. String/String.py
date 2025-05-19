word=input()
string=word[0]
for i in range(len(word)-1):
    if word[i] != word[i+1]:
        string += word[i+1]
print(string)