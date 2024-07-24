s = input()
flag = False
for i in range(1,len(s)):
    flag = False
    a1 = int(s[0:i])
    for j in range(i + 1, len(s)):
        a2 = int(s[i:j])
        a3 = a1 + a2
        s_ = s[j:]
        if s_.find(str(a3)) == 0:
            flag = True
            a1_ = a2
            a2_ = a3
            s_ = s[len(str(a3)) + len(str(a2)) + len(str(a1)):]
            while len(s_) != 0:
                a3_ = a1_ + a2_
                if s_.find(str(a3_)) == 0:
                    a1_ = a2_
                    a2_ = a3_
                    s_ = s_[len(str(a3_)):]
                else:
                    flag = False
                    break
            if flag:
                break
    if flag:
        print("YES")
        break
if flag == False:
    print("NO")
