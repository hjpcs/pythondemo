def list_sum(l):
    sum = 0
    for i in l:
        if(isinstance(i, int)):
            sum += i
        else:
            sum += 0
    return sum

# l = [1, 'asd', 2, 3, 'a', 8]
# print(list_sum(l))


