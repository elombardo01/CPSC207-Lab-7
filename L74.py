#Lab 7 part
#Emma viviana and sydney

def until_dot(string):
    index = 0
    s = string
    while index < len(s) and s[index] != ".":
        index += 1
    print(s[:index])

until_dot("this is a sentence. this is another.")
until_dot("192.168.200.2")
until_dot("no dots here")


def no_repeating():
    words=[]
    while True:
        word = input("Tell me a word:")
        if word in words:
            print("You told me that word already!")
            break
        words.append(word)
    return words

no_repeating()

def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                #print(x)
                #print(y)
                print( f"{x} * {y} == 512")
                break
        

find_512()
