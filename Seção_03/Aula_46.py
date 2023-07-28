frase = 'Pedro Paulo Pereira Pinto, pequeno pintor português, pintava\
        portas, paredes,portais. Porém, pediu para parar porque preferiu\
        pintar panfletos. Partindo para Piracicaba, pintou prateleiras\
        para poder progredir. Posteriormente, partiu para Pirapora.\
        Pernoitando, prosseguiu para Paranavaí, pois pretendia praticar\
        pinturaspara pessoas pobres. Porém, pouco praticou, porque Padre\
        Paulo pediu para pintar panelas, porém posteriormente pintou pratos\
        para poder pagar promessas.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}x'
)