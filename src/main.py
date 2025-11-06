##### Importy
from Shapes_Catalog.rectangle import draw_rectangle
from Shapes_Catalog.triangle import draw_triangle
from Shapes_Catalog.square import draw_square

##### Powitanie
def wydrukuj_menu():
    print("#####################")
    print("--- Paint Python ---")
    print("#####################")
    print()
    print("Wybierz kod projekt:")
    print("1 - Prostokąt")
    print("2 - Trójkąt")
    print("3 - Kwadrat")

wydrukuj_menu()
kod = int(input("Kod: "))
if kod == 1:
    draw_rectangle()
if kod == 2:
    draw_triangle()
if kod == 3:
    draw_square()
