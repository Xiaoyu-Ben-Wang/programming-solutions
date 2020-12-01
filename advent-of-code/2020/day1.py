f = open("day1.txt", "r")

l = f.readlines()
for i in l:
    for j in l:
        for k in l:
            if int(i.strip())+int(j.strip())+int(k.strip()) == 2020:
                print(i,j,k,int(i)*int(j)*int(k))

f.close()
