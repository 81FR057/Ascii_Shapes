
def draw_square():
    print("Wysokość")
    wysokosc = int(input())
    print("symbol")
    symbol = input()

    print((symbol + " ") * wysokosc)
    for zmienna  in range(wysokosc - 2):
        print(symbol + (" " * ((wysokosc * 2) - 3)) + symbol)
    print((symbol + " ") * wysokosc)
