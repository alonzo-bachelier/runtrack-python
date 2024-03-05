constructible = False
 
while not constructible:
 
    ab = int(input("Premier côté du triangle (AB) : "))
    bc = int(input("Deuxième côté du triangle (BC) : "))
    ac = int(input("Troisième côté du triangle (AC) : "))
 
    if ab < bc + ac and bc < ab + ac and ac < ab + bc:
        print("Le triangle AB = {}, BC = {} et AC = {} est constructible. ".format(ab, bc, ac))
        constructible = True
    else:
        print("Le triangle AB = {}, BC = {} et AC = {} n'est pas constructible, veuillez entrer de nouveaux côtés. ".format(ab, bc, ac))
 
isocele = ab == bc or bc == ac or ac == ab
rectangle = ab * ab + bc * bc == ac * ac or bc * bc + ac * ac == ab * ab or ac * ac + ab * ab == bc * bc
         
if ab == bc == ac:
    print("Ce triangle est équilatéral. ")
     
elif isocele and rectangle:
    print("Ce triangle est rectangle isocèle. ")
 
else:
    if isocele:
        print("Ce triangle est isocèle. ")
    elif rectangle:
        print("Ce triangle est rectangle. ")
    else:
        print("Ce triangle est quelconque. ")
