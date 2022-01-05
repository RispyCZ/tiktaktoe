# Vypiš hrací pole
def vypis_hraci_pole(hraci_pole : list):
    radek = ""
    for i,x in enumerate(hraci_pole):
        if((i+1) % 3 == 0):
            radek += " " + x + "\n"
        else:
           radek += " " + x
    print(radek) 
   
def main():
    hraci_pole = ["*", "*", "*", "*", "*", "*","*", "*", "*"]
    pocet = 0
    hrac = ""
    hraci = ["X", "O"]
    
    while True:
        # Výběr strany
        while hrac not in hraci:
            hrac = input("Vyber si stranu (X nebo O): ")

        while True:
            tah = int(input(f"Hraješ za {hrac} Zadej číslo (1-9): "))-1
            if(hraci_pole[tah] not in hraci):
                hraci_pole[tah] = hrac
                break

        # Prohození stran
        if(hrac == "X"):
            hrac = "O"
        else: 
            hrac = "X"
        

        vypis_hraci_pole(hraci_pole)

if __name__ == "__main__":
    main()