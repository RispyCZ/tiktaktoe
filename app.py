# Vypiš hrací pole
def vypis_hraci_pole(hraci_pole : list):
    radek = ""
    for i,x in enumerate(hraci_pole):
        if (i+1) % 3 == 0:
            radek += " " + x + "\n"
        else:
           radek += " " + x
    print(radek) 
   
def main():
    hraci_pole = ["*", "*", "*", "*", "*", "*","*", "*", "*"]
    pocet = 1
    vyhra = [[1,2,3], [4,5,6], [7,8,9], [7,4,1], [8,5,2], [9,6,3], [1,5,9], [3,5,7]]
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

        # Validace výhry
        for w in vyhra:
            print(hraci_pole[w[0]-1])
            if(hraci_pole[w[0]-1] == hrac and hraci_pole[w[1]-1] == hrac and hraci_pole[w[2]-1] == hrac):
                print(f"{hrac} win! Congrats!")
                break

        # Prohození stran
        if(hrac == "X"):
            hrac = "O"
        else: 
            hrac = "X"
        
        vypis_hraci_pole(hraci_pole)

        # Počet game loopů
        if pocet >= len(hraci_pole):
            break
        else:
            pocet += 1


if __name__ == "__main__":
    main()