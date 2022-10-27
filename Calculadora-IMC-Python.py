#calculadora IMC em python *Portifolio Anhanguera

altura = float(input("Digite sua altura amigo :}")) #Input/Entrada de dados 01
peso = float(input("Digite também seu peso amigo :}")) #Input/Entrada de dados 02

imc = peso / altura**2 #Calculo IMC onde o imc é a divisão do peso pela autura elevado a 2

print("Seu IMC é: %.4f" % imc) #Concatenação do valor na interface do usuario

#Aqui fazemos uma series de condições para trazer um resultado mais adequado ao valor dado pelo usuario
if imc < 16:
    print("Magreza grave")
elif imc < 17:
    print("Magreza moderada")
elif imc < 19:
    print("magreva leve")
elif imc < 25:
    print("Saudável")
elif imc < 30:
	print("Sobrepeso")
else:
	print("Obesidade")