d1 = {10:100 ,20:200 }
d2 = {20:300, 30:300}

for i in d2:
    if i in d1.keys():
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]
print(d1)


