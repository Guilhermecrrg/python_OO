class AgendaDePagamentos:
    def __init__(self):
        self.eventos = {}
    
    def adicionar_evento(self, data, pagamento):
        if data in self.eventos:
            print("Essa data ja esta presente na agenda\n")
        else:
            self.eventos[data] = pagamento
            print(f"Evento adicionado a agenda na data {data} com o custo de R${pagamento}\n")
    
    def excluir_evento(self, data):
        if data not in self.eventos:
            print("Não foi possivel excluir esse evento de pagamento, nenhum evento para essa data\n")
        else:
            del self.eventos[data]
            print(f"Evento da data {data} execluido\n")

    def exibir_lista(self):
        print("Lista de pagamentos:\n")
        for data, pagamento in self.eventos.items():
            print(f"Data:{data} Valor:{pagamento}\n")

agenda_de_pagamentos = AgendaDePagamentos()

while True:
    print("\n-----------------Lista de opções-----------------\n")
    print("Digite 1 para adicionar um evento de pagamento")
    print("Digite 2 para excluir um evento de pagamento")
    print("Digite 3 para exibir a lista de eventos de pagamento")
    print("Digite 4 para sair do programa")
    opcao = input("Digite sua opção: ")

    if opcao == "1":
        data = input("Digite a data (DDMM): ")
        pagamento = float(input("Digite o valor do pagamento: "))
        agenda_de_pagamentos.adicionar_evento(data, pagamento)

    elif opcao == "2":
        data = input("Digite a data do evento a ser excluído (DDMM): ")
        agenda_de_pagamentos.excluir_evento(data)
    elif opcao == "3":
        agenda_de_pagamentos.exibir_lista()
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")


