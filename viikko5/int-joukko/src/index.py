from int_joukko import IntJoukko

def main():
    joukko = IntJoukko()

    joukko.add(1)
    joukko.add(2)
    joukko.add(3)
    joukko.add(2)

    print(joukko.to_int_list())


if __name__ == "__main__":
    main()
