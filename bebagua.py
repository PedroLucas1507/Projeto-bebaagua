"""Projeto Beba Água: lembretes simples executados pelo terminal.
"""

from datetime import datetime, timedelta
from time import sleep


def ler_inteiro(mensagem, minimo, maximo):
    """Pede um número inteiro e repete a pergunta até ele ser válido."""
    while True:
        try:
            valor = int(input(mensagem))
            if minimo <= valor <= maximo:
                return valor
            print(f"Digite um número entre {minimo} e {maximo}.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def gerar_horarios(intervalo_minutos, horas_ativas):
    """Monta a lista de horários previstos para os lembretes."""
    agora = datetime.now()
    horarios = []

    # Cada repetição avança o horário pelo intervalo escolhido.
    for minuto in range(intervalo_minutos, horas_ativas * 60 + 1, intervalo_minutos):
        horario = agora + timedelta(minutes=minuto)
        horarios.append(horario.strftime("%H:%M"))

    return horarios


def mostrar_agenda(intervalo_minutos, horas_ativas):
    """Exibe no terminal os horários estimados da sessão."""
    horarios = gerar_horarios(intervalo_minutos, horas_ativas)
    print("\nHorários previstos:")
    for horario in horarios:
        print(f"- {horario}")
    print()


def iniciar_lembretes(intervalo_minutos, horas_ativas):
    """Espera os intervalos e mostra um alarme no terminal."""
    quantidade = (horas_ativas * 60) // intervalo_minutos
    print("\nLembretes iniciados. Pressione Ctrl+C para interromper.")

    try:
        for numero in range(1, quantidade + 1):
            sleep(intervalo_minutos * 60)
            horario_atual = datetime.now().strftime("%H:%M")
            print(f"\n\a[ALARME {numero}/{quantidade}] Hora de beber água! ({horario_atual})")
    except KeyboardInterrupt:
        print("\nSessão de lembretes interrompida.")
    else:
        print("\nSessão de lembretes concluída.")


def exibir_menu():
    """Mostra as opções disponíveis no programa."""
    print("=== BEBA ÁGUA ===")
    print("1. Ver agenda de lembretes")
    print("2. Iniciar lembretes")
    print("3. Registrar copos consumidos")
    print("4. Sair")


def main():
    """Controla o menu e mantém o total de copos da sessão."""
    copos_consumidos = 0

    while True:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção (1 a 4): ", 1, 4)

        # A condição escolhe a ação correspondente à opção digitada.
        if opcao == 1:
            intervalo = ler_inteiro("Intervalo entre lembretes em minutos (1 a 240): ", 1, 240)
            horas = ler_inteiro("Duração da sessão em horas (1 a 16): ", 1, 16)
            mostrar_agenda(intervalo, horas)
        elif opcao == 2:
            intervalo = ler_inteiro("Intervalo entre lembretes em minutos (1 a 240): ", 1, 240)
            horas = ler_inteiro("Duração da sessão em horas (1 a 16): ", 1, 16)
            iniciar_lembretes(intervalo, horas)
        elif opcao == 3:
            copos = ler_inteiro("Quantos copos você bebeu? ", 1, 100)
            copos_consumidos += copos
            print(f"Total registrado nesta sessão: {copos_consumidos} copo(s).\n")
        else:
            print("Até a próxima. Cuide da sua hidratação!")
            break


if __name__ == "__main__":
    main()