carrinho = []

carrinho.append(('Prdoto 1', 30))
carrinho.append(('Prdoto 2', 20))
carrinho.append(('Prdoto 3', 50))

valor = [v[1] for v in carrinho]

print(f'Valor total: {sum(valor)}')
