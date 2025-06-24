def sumofodd(list):
    sum = 0
    for i in list:
        if i % 2 != 0:
            sum += i
    print(sum)
