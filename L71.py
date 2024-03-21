#Lab 7 Part A
#Emma and Viviana and Sydney

def total_length(list):
    sum_length = 0
    for s in list:
        sum_length += len(s)
    print(sum_length)

total_length(["Queen","rules"])
total_length([])
total_length(["balloons"])
total_length(["",'',"",''])

s="Tenochtitlan"
index = 0
while index < len(s):
    index += 1
    print(s[:index])

#index = 0 gives the index a starting point to add "1" on.
#index < len(s) just to have a true statement for while the index is less than the length of the string
#index += 1 adds 1 to the value of the index
#s[:index] prints each character and then that character plus the next etc.
