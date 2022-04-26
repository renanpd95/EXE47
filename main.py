import os,math

r = float(input("Digite o raio:"))
os.system('clear')
if (r > 0):
  r = math.pow(r,2)
  a = 3.14 * r
  print("A area do raio é:",a)
else:
  print("O valor do raio é invalido")