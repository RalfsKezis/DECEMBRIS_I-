ievaditais_skaitlis = int(input("Ievadiet veselu skaitli: "))

faktorials = 1

for skaitlis in range(1, ievaditais_skaitlis + 1):
    faktorials *= skaitlis

print(f"{ievaditais_skaitlis} faktoriāls ir: {faktorials}")
