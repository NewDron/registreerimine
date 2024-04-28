import random
import string
def registreerimine(i:list,p:list)->any:
    """
    """

    print("Registreerimiseks sisestage kasutajanimi. ")
    nimi=input("Nimi: ")
    print("Registreerimiseks sisestage parool. Parool peab sisaldama suuri ja väikeseid tähti, numbreid ja sümboleid. ")
    choice=input("Kas soovite parooli genereerida(0) või teha ise(1)? ")
    print(choice)
    if choice=="0":
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str0+str1+str2+str3
        ls = list(str4)
        print(ls)
        random.shuffle(ls)
        print(ls)
        # Извлекаем из списка 12 произвольных значений
        psword = ''.join([random.choice(ls) for x in range(12)])
        # Пароль готов
        print(psword)
        i.append(nimi)
        p.append(psword)

        #def salasona(k: int):
        #    sala=""
        #    for i in range(k):
        #        t=choice(string.ascii_letters) #Aa...Zz
        #        num=choice([1,2,3,4,5,6,7,8,9,0])
        #        t_num=[t,str(num)]
        #        sala+=choice(t_num)
        #    return sala        

    elif choice=="1":
        parool=input("Parool: ")
        res = any(chr.isdigit() for chr in parool)
        res2 = any(chr.islower() for chr in parool)
        res3 = any(chr.isupper() for chr in parool)
        if len(parool) >= 8 and len(parool) <13 and res == True and res2 == True and res3 == True :
            print("Kasutaja ja parool loodud!")
            i.append(nimi)
            p.append(parool)
        else:
            print("Parool peab sisaldama suuri tähti, numbreid ja sümboleid.\n")
    else:
         print("Viga. Proovi uuesti!\n")
    return i,p

def autoriseerimine(i:list,p:list)->any:
    """
    """

    auth=input("Sisestage oma kasutajanimi: ")
    authpass=input("Sisestage oma parool: ")
    if auth in i and authpass in p:
        print("\nOlete sisse logitud!\n")
    else:
        print("\nVale kasutajanimi või parool!\n")
    return i,p

def muutmine(i:list,p:list)->any:
    """
    """
    change=input("Soovite muuta kasutajanime või parooli? (kasutajanimi - 0, parool - 1)\n ")
    if change =="0":
        muut=input("Sisestage kasutajanimi, mida soovite muuta:")
        if muut in i:
            uus=input("Sisestage uus kasutajanimi:")
            vahetus=i.index(muut)
            i.pop(vahetus)
            i.insert(vahetus, uus)
        else:
            print("Vale kasutajanimi!\n")           
    else:
        muut=input("Sisestage kasutajanimi, mille parooli soovite muuta:")
        if muut in i:
            check=input("Sisestage parool:")
            if check in p:
                uus=input("Sisestage uus parool:")
                vahetus=p.index(check)
                p.pop(vahetus)
                p.insert(vahetus, uus)
            else:
                print("Viga! Proovige uuesti\n")         
        else:
            print("Viga! Proovige uuesti\n")         
    return i,p

def taastamine(i:list,p:list)->any:
    """
    """
    revive=input("Soovite unustanud parooli taastada? Jah - 0, Ei - 1\n")
    if revive == "0":
        taas=input("Sisestage kasutajanimi, kelle parooli soovite taastada:")
        if taas in i:
            print("Teie e-mailile on saadetud kiri uue parooliga\n")
        else:
            print("Vale kasutajanimi!\n")           
    else:
        print(" ")
    return i,p

def lõpetamine(i:list,p:list)->any:
    """
    """
    exit=input("Soovite lahkuda? Jah - 0, Ei - 1\n")
    if exit == "0":
        print("Head aega!\n")
    else:
        print("\n")
    return i,p
