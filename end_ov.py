s = input()
q = ""
for i in s.split(";"):
    for j in i.split(" "):
        for k in j.split(","):
            for p in k.split("."):
                if (p[len(p) - 2:] == "ов"):
                    q += p + " "
print(q)                    
