##### Importy
from Shapes_Catalog.rectangle import draw_rectangle
from Shapes_Catalog.triangle import draw_triangle

##### Powitanie
def wydrukuj_menu():
    print("#####################")
    print("--- Paint Python ---")
    print("#####################")
    print()
    print("Wybierz kod projekt:")
    print("1 - Prostokąt")
    print("2 - Trójkąt")

wydrukuj_menu()
kod = int(input("Kod: "))
if kod == 1:
    draw_rectangle()
if kod == 2:
    draw_triangle()
