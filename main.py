# Implementação da Torre de Hanoi de forma recursiva
def hanoi(discos, haste_principal, haste_auxiliar, haste_destino):
    if discos == 1:
        print(
            f"Mova o disco 1 de haste {haste_principal} para haste {haste_destino}."
        )
        return
    hanoi(discos - 1, haste_principal, haste_destino, haste_auxiliar)
    print(
        f"Mova o disco {discos} de haste {haste_principal} para haste {haste_destino}."
    )
    hanoi(discos - 1, haste_auxiliar, haste_principal, haste_destino)


discos = int(input("Digite o número de discos: "))
hanoi(discos, "1", "2", "3")
