from MyModule import *

i=['User1']
p=['AAaa123!']
while True:

    print(i)
    print(p)

    print("\n0-registreerimine\n1-autoriseerimine\n2-nime või parooli muutmine\n3-unustanud parooli taastamine\n4-lõpetamine\n")
    vastus=int(input())
    if vastus==0:
        registreerimine(i,p)
    elif vastus==1:
        i,p=autoriseerimine(i,p)
    elif vastus==2:
        i,p=muutmine(i, p)
    elif vastus==3:
        i, p=taastamine(i, p)
    elif vastus==4:
        i, p=lõpetamine(i, p)
    else:
        print("\n")
