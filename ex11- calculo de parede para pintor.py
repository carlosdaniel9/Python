print('calculo de valor do trabalho, e o tato de tinta que irá precisar para a obra.')
largura = float(input('digite a largura da sua parede!'))
altura = float(input('digite a altura da sua parede!'))
preco_por_metro = float(input('Qual o preço por metro quadrado?'))
area = largura * altura 
resultado1 = area * preco_por_metro
tinta = area / 2

print('Sua parede mede {:.2f}m²'.format(area))
print('O preço por metro é R$ {:.2f}, e sua parede mede {:.0f} m², você irar para R$ {:.2f} pela sua obra'.format(preco_por_metro, area, resultado1))
print('para pintar {}m², você vai precisa de {} litros de tinta'.format(area, tinta))


# carlos daniel 27/08/2023