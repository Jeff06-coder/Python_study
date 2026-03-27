def relatorio_vendas(*args, **kwargs):
    print("=== RELATÓRIO DE VENDAS ===")
    
    # args → valores posicionais
    print("\nProdutos vendidos:")
    for produto in args: # Iterando sobre os argumentos posicionais usando um loop for
        print(f"- {produto}") # Imprimindo cada produto passado como argumento posicional usando um loop for
    
    # kwargs → pares chave=valor
    print("\nInformações adicionais:")
    for chave, valor in kwargs.items(): # Transformando o dicionário kwargs em uma lista de tuplas (chave, valor) usando o método items()
        print(f"{chave}: {valor}") # Imprimindo cada chave e valor do dicionário kwargs


# Chamando a função
relatorio_vendas(
    "Notebook",
    "Mouse",
    "Teclado",
    vendedor="Antonio",
    total=3500,
    pago=True
)