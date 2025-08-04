# vendas = [941, 852, 783, 714, 697, 686, 685, 
# 670, 631, 453, 386, 371, 294, 269, 259]
# vendedores = ['Maria','José', 'Antônio', 'João', 
# 'Francisco', 'Ana', 'Luiz',
# 'Paulo', 'Carlos', 'Fernanda', 'Juliana', 
# 'Sandro', 'Fábio', 'Tatiane', 'Célia']

# meta = 700
# abaixo = 500

# vendedores_acima = [vendedores for vendedores, vendas in zip(vendedores, vendas) if vendas >= meta]
# vendedores_normais = [vendedores for vendedores, vendas in zip(vendedores, vendas) if vendas < meta and vendas > abaixo]
# vendedores_abaixo = [vendedores for vendedores, vendas in zip(vendedores, vendas) if vendas <= abaixo]

# print(f'Os vendedores que venderam mais de {meta} foram: {vendedores_acima}')
# print(f'Os vendedores que venderam entre {abaixo} e {meta} foram: {vendedores_normais}')
# print(f'Os vendedores que ficaram abaixo de {abaixo} foram: {vendedores_abaixo}')


