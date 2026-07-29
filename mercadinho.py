class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            return True
        return False

    def repor_estoque(self, quantidade):
        self.estoque += quantidade


class Mercadinho:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        if not self.produtos:
            print("\nNenhum produto cadastrado.")
            return
        
        print("\n--- PRODUTOS DISPONÍVEIS ---")
        for i, produto in enumerate(self.produtos, start=1):
            print(f"{i}. {produto.nome} - R$ {produto.preco:.2f} (Estoque: {produto.estoque})")


# --- SISTEMA INTERATIVO (O MENU) ---

mercado = Mercadinho("Mercadinho do Bairro")

# Adicionando alguns produtos iniciais
mercado.adicionar_produto(Produto("Arroz", 25.90, 150))
mercado.adicionar_produto(Produto("Feijão", 8.50, 150))
mercado.adicionar_produto(Produto("Café", 14.00, 500))

while True:
    print(f"\n=== {mercado.nome.upper()} ===")
    print("1. Ver lista de produtos")
    print("2. Comprar produto (Cliente)")
    print("3. Repor/Vender estoque (Fornecedor)")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mercado.listar_produtos()

    elif opcao == "2":
        mercado.listar_produtos()
        if mercado.produtos:
            try:
                num = int(input("\nDigite o número do produto que deseja comprar: ")) - 1
                if 0 <= num < len(mercado.produtos):
                    produto = mercado.produtos[num]
                    qtd = int(input(f"Quantas unidades de '{produto.nome}' você quer? "))
                    
                    if produto.vender(qtd):
                        total = qtd * produto.preco
                        print(f"Compra realizada! Total: R$ {total:.2f}")
                    else:
                        print(f"Estoque insuficiente! Temos apenas {produto.estoque} unidades.")
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Por favor, digite um número válido.")

    elif opcao == "3":
        mercado.listar_produtos()
        if mercado.produtos:
            try:
                num = int(input("\nDigite o número do produto para atualizar estoque: ")) - 1
                if 0 <= num < len(mercado.produtos):
                    produto = mercado.produtos[num]
                    qtd = int(input(f"Quantidade a adicionar ao estoque de '{produto.nome}': "))
                    produto.repor_estoque(qtd)
                    print(f"Novo estoque de {produto.nome}: {produto.estoque} unidades.")
                else:
                    print("Opção inválida.")
            except ValueError:
                print("Por favor, digite um número válido.")

    elif opcao == "4":
        print("\nSaindo... Volte sempre!")
        break
    else:
        print("\nOpção inválida, tente novamente.")
