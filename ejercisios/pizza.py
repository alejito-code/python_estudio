"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas
a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza
vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes
disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate
que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana
o no y todos los ingredientes que lleva."""

pizza = input("Desea pizza vegetariana o no vegetariana: ").lower()

if pizza == "vegetariana":
    adicion = input("Escoja una adicion para su pizza vegetariana: pimenton o tofu: ").lower()
    if adicion == "pimenton":
        print("Ha escogido una pizza vegetariana con tomate mozarrella y pimenton")
        import sys
        sys.exit()
    elif adicion == "tofu":
        print("Ha escogido una pizza vegetariana con tomate mozarrella y tofu")
        import sys
        sys.exit()
    else: 
        print("No ha escogido ninguna adicion de las que se le ofrecieron, por favor vuelva a escoger")
elif pizza == "no vegetariana":
    adicion = input("Escoja una adicion para su pizza no vegetariana: peperoni, jamon o salmon: ").lower()
    if adicion == "peperoni":
        print("Ha escogido una pizza no vegetariana con tomate mozarrella y peperoni")
        import sys
        sys.exit()
    elif adicion == "jamon":
        print("Ha escogido una pizza no vegetariana con tomate mozarrella y jamon")
        import sys
        sys.exit()
    elif adicion == "salmon":
        print("Ha escogido una pizza no vegetariana con tomate mozarrella y salmon")
        import sys
        sys.exit()
    else: 
        print("No ha escogido ninguna adicion de las que se le ofrecieron, por favor vuelva a escoger")
else: 
    print("No ha escojido ninguna de las pizzas que se le ofrecieron, porfavor escoja")