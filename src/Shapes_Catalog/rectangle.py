######### Wersja Robocza #########
def draw_rectangle():
    print("wysokosc: ")
    wysokosc = int(input())
    print("symbol: ")
    symbol = input()
    print(symbol + symbol * wysokosc + symbol)
    for zmienna in range(wysokosc - 2):
        print(symbol + wysokosc * " " + symbol)
    print(symbol + symbol * wysokosc + symbol)