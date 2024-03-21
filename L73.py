#Lab 7 part C and D
#Emma Viviana Sydney

def count_character(word, character):
    count = 0
    for ch in word:
        if ch == character:
            count = count + 1
    return count

print(count_character("bonobos","o"))

index = 0
s = "Mind the gap!"
while index < len(s) and s[index] != " ":
    index += 1
print(s[:index])

#index < len(s) considers index value while its less than the length of s
#s[index] != " " means s doesn't equal blank space
#index += 1 adds one to the value of index
#print(s[index]) just prints 
