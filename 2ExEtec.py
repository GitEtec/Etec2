
'''
2) LEia um conjunto de 20 pessoas contendo altura e sexo(M e F) e depois apresente
a - a maior e a menor altura do grupo
b - a media de altura das mulheres
c - o numero de homens
d - diferença percentual entre homens e mulheres
'''
tot = 0
mulher = 0
homem = 0
maioraltura = []
menoraltura = []
alturamulher = 0

while True:
    alt = float(input('Altura: '))
    maioraltura.append(alt)
    menoraltura.append(alt)
    sexo = str(input('Sexo: [M|F] ').upper())
    tot += 1
    perg = str(input('Deseja continuar ? [S|N]: ')).upper().strip()[0]
    if sexo == 'F':
        alturamulher +=alt
        mulher += 1
    if sexo == 'M':
        homem+=1
    if sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [M|F]: ').upper()).upper().strip()[0]
    if perg == 'N':
        break

media = alturamulher/mulher
maior = max(maioraltura)
menor = min(menoraltura)
perhomem = (homem/tot)*100
permulher = (mulher/tot)*100
difperc = (homem/tot)*100-(mulher/tot)*100
print(f'Mulheres {mulher}.')
print(f'Media de altura das mulheres: {media:.2f}.')
print(f'Maior do grupo: {maior}.')
print(f'Menor do grupo: {menor}.')
print(f'Total {tot}')
print(f'Percentual Homens {perhomem:.0f}%.')
print(f'Percentual Mulheres {permulher:.0f}%.')
print(f'Diferencia percentual entre homens e mulheres {difperc:.0f}%')