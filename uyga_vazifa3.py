fin  = open("input.txt", "r")
fout = open("output.txt","w")
max1 = 0
for i in e:
    j = i.split()

for i in range(len(j)):
    for k in range(i+1, len(j)):
        for n in range(k+1, len(j)):
            if int(j[i])+int(j[k])>int(j[n]) and int(j[n])+int(j[k])>int(j[i]) and int(j[i])+int(j[n])>int(j[k]) and max1<int(j[i])+int(j[k])+int(j[n]):
                a, b, c = j[i], j[k], j[n]
                max1 = int(a)+int(b)+int(c)
if int(max1)==0:
    fout.write('-1')
else:
    fout.write(a+' '+b+' '+c)





fin.close()
fout.close()
