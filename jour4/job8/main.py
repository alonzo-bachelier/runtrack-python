l = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
long = len(l)
somp = 0
for i in range(long) :
     if l[i] %2 == 0 :
          somp = somp + l[i]
print ("Somme des valeurs paires : ", somp)