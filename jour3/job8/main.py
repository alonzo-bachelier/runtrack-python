def fruit(type, saison):
    if type == "fruit" and saison == "hiver":
        print('orange, mandarine et kiwi')
    elif type == "fruit" and saison == "été":
        print('Poire, fraise, cassis')
    elif type == "legume" and saison == "hiver":
        print('carotte, topinambour, endive')
    elif type == "legume" and saison == "été":
        print('artichaut, aubergine, navet')

fruit("fruit", "hiver")

fruit("legume", "été")