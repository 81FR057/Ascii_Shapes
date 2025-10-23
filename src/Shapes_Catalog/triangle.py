def draw_triangle():
    print("Wysokość: ")
    wysokosc = int(input())
    print("symbol: ")
    symbol = input()


    spacje = wysokosc // 2
    srodek = 1

    print(spacje * " " + symbol)
    for zmienna in range(wysokosc // 2):
        spacje -= 1
        print(spacje * " " + symbol + srodek * " " + symbol)
        srodek +=2
    print(symbol * (wysokosc + 1))



