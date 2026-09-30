meta_litros = float(input("Digite sua meta diária de água em litros: "))

while meta_litros < 0:
    print("Valor inválido. A meta não pode ser negativa.")
    meta_litros = float(input("Digite sua meta diária de água em litros: "))

meta_ml = meta_litros * 1000

total_ml = 0
meta_atingida = False

while True:

    quantidade = int(input("Quantos ml de água você bebeu? "))

    while quantidade < 0:
        print("Valor inválido. A quantidade não pode ser negativa.")
        quantidade = int(input("Quantos ml de água você bebeu? "))

    total_ml += quantidade

    if total_ml < meta_ml:

        faltam = meta_ml - total_ml

        print(f"\nVocê já ingeriu {total_ml} ml.")
        print(f"Faltam {faltam} ml para atingir sua meta.\n")

    else:

        if not meta_atingida:
            print(f"\n🎉 Parabéns! Você atingiu sua meta de {meta_ml:.0f} ml!")
            meta_atingida = True
        else:
            print(f"\nTotal registrado: {total_ml} ml.\n")

        resposta = input("Deseja continuar registrando água? (s/n): ")

        if resposta.lower() == "s":

            print("\nContinuando o registro...\n")

        else:

            print("\nPrograma encerrado.")
            break