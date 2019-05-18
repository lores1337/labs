s = input()
k = 0
p, z, q = "", "", ""
for i in s.split(';'):
    if k < 3:
        p += i + " "
    elif k == 3:
        z = i
    elif k == 4:
        q = i
    if k == 4:
        k = -1
        print(p[1:] + " " + q + " " + z)
        p = ""
    k += 1    
