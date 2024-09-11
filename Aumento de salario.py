salario = float(input("salario atual: "))
aumento_do_salario = float(input("aumento desejado em porcentagem: "))

salarioN = salario+salario*aumento_do_salario/100
valor = salario*aumento_do_salario/100

print("valor ganho é de: ",valor)
print("O seu novo salario total é : " ,salarioN)
