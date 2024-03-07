def f():
    f = int(input("Entrez un nombre: "))
    if (f % 2) == 0:
        print("{0} est Paire".format(f))
    else:
        print("{0} est Impaire".format(f))

f()