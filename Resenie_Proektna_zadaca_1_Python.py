# Проект: Kredokard.mk
# Пресметувач на рати за кредит
# deadline: 26.02.2025
try: 
    iznos=float(input("Vnesete go iznosot na kreditot vo denari: "))
    print("Uspesno vnesovte iznos na kredit",iznos)
except ValueError:
    print("Vnesovte pogresen tip na podatok")
    breakpoint
    exit()
try: 
    kamatna_stapka=float(input("Vnesete ja godisnata kamatna stapka: "))
    print("Uspesno vnesovte kamatna stapka",kamatna_stapka)
except ValueError:
    print("Vnesovte pogresen tip na podatok")
    breakpoint
    exit()
try:
    period=float(input("Vnesete go vremeto na otplata na kreditot vo meseci: "))
    print("Uspesno vnesovte iznos na traenje na kreditot")
except ValueError:
    print("Vnesovte pogresen tip na podatok")
    breakpoint
    exit()
if iznos>0 and iznos<=20000000:
    P=iznos
else:
    print("Vnesete soodvetna vrednost za iznosot na kreditot ")
    breakpoint
    exit()
if kamatna_stapka>0 and kamatna_stapka<30:
    R=kamatna_stapka/1200
else:
    print("Vnesete soodvetna decimalna vrednost za godisnata kamatna stapka")
    breakpoint
    exit()
if period>=0 and period<=360:
    N=period
else:
    print("Vnesete soodvetna decimalna vrednost za vremeto na otplata: ")
    breakpoint
    exit()
EMI=P*R*(1 + R)**N/((1+R)**N-1)
print(f"Vasata mesecna rata za isplata na kreditot e {(round(EMI,2))} denari")
print(f"Vkupniot iznos za otplata iznesuva {(round(EMI*N,2))}")
