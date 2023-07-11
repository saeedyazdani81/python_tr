numbers = [1, 12, 31, 42, 5, 67, 47, 80, 9, 100, 11]

for i in range(0,len(numbers)) :
    daste = numbers[i:i+3]
    if len(daste)==3 :
        print(daste)
