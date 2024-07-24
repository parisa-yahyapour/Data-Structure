import re
pattern = r'[: ]'
num_test = int(input())
for i in range(num_test):
    p = input()
    p_parts = re.split(pattern, p)
    p_parts[0] = int(p_parts[0])
    p_parts[1] = int(p_parts[1])
    if p_parts[2] == "PM" and p_parts[0] != 12:
        p_parts[0] += 12
    if p_parts[2] == "AM" and p_parts[0] == 12:
            p_parts[0] = 0
    n = int(input())
    result = ""
    for j in range(n):
        temp = input()
        a = re.split(pattern, temp)
        a[0]= int(a[0])
        a[1]= int(a[1])
        a[3]= int(a[3])
        a[4]= int(a[4])
        if a[2] == "PM" and a[0] != 12:
            a[0] += 12
        if a[5] == "PM" and a[3] != 12:
            a[3] += 12
        if a[2] == "AM" and a[0] == 12:
            a[0] = 0
        if a[5] == "AM" and a[3] == 12:
            a[3] = 0
        if ((p_parts[0] > a[0]) or (p_parts[0] == a[0] and p_parts[1] >= a[1])) and ((p_parts[0] < a[3]) or (p_parts[0] == a[3] and p_parts[1] <= a[4])):
            result += "1"
        else:
            result += "0"
    print(result)



