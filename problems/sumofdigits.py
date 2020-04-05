def digital_root(n):
    string_n = str(n)
    length = len(string_n)
    sum = n
    while length > 1:
        sum = 0 
        cnt = 0
        for x in range(length): 
            sum = sum + int(string_n[cnt]) 
            cnt = cnt + 1
        string_n = str(sum)
        length = len(string_n)
    return sum
