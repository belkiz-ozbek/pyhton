# asal sayı bulma

def asalSayiCagirma():
    sayi = int(input("bir sayi gir"))

    for i in range(2, sayi):
        if (sayi % i) == 0:
            print("not asal")
            break;
        else:
            print("asal")
            break;

asalSayiCagirma()
