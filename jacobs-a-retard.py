def main():
    d = int(input("Enter the # of whole US dollars you have: "))
    z = int(input("Enter 1 for dollarstoyen; 2 for dollars to pesos; 3 for dollarstoeuros; 4 for dollarstoyuan; 5 for "
                  "dollarstobglev: "))
    if z == 1:
        dollarstoyen(d)
    elif z == 2:
        dollarstopesos(d)
    elif z == 3:
        dollarstoeuros(d)
    elif z == 4:
        dollarstoyuan(d)
    elif z == 5:
        dollarstobglev(d)
    else:
        print("Input a value that leads to a function!")


def dollarstoyen(d):
    a = d * 108.14
    print("Yen:" + str(a))


def dollarstopesos(d):
    b = d * 19.05
    print("Pesos:" + str(b))


def dollarstoeuros(d):
    c = d * 0.91
    print("Euros:" + str(c))


def dollarstoyuan(d):
    e = d * 6.99
    print("Yuan:" + str(e))


def dollarstobglev(d):
    f = d * 1.77
    print("Bulgarian Lev:" + str(f))


if __name__ == '__main__':
    main()
