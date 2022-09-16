#4. Faça um programa que calcule a área total (m2) de uma casa com 4 cômodos. O usuário deve inserir a largura e comprimento de cada um dos cômodos, calcular a área individual de cada um e por fim exibir a área total da casa

def area_comodo(largura,comprimento):
  return largura * comprimento

print('Cômodo 1')
l1 = float(input('Largura: '))
c1 = float(input('Comprimento: '))
area1 = area_comodo(l1,c1)

print('Cômodo 2')
l2 = float(input('Largura: '))
c2 = float(input('Comprimento: '))
area2 = area_comodo(l2,c2)

print('Cômodo 3')
l3 = float(input('Largura: '))
c3 = float(input('Comprimento: '))
area3 = area_comodo(l3,c3)

print('Cômodo 4')
l4 = float(input('Largura: '))
c4 = float(input('Comprimento: '))
area4 = area_comodo(l4,c4)

area_casa = area1 + area2 + area3 + area4

print('A área total da casa é de',area_casa,'m².')