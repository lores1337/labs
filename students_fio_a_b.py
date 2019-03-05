s = input()
k = 0
p, z, q = "", "", ""
for i in s.split(";"):
    if k == 0:
        p = i
    elif k == 1:
        z = i
    elif k == 2:
        q = i
    if k == 2:
        k = -1
        if (p[1] == "А" or p[1] == "Б"):
            print(p + " " + q + " " + z)
        p = ""
    k += 1    
