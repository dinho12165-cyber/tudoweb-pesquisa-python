excelente_count = 0
ruim_count = 0

# a estrutura de repetição for é utilizada pois sabemos que o numero de repetições são 10.
for i in range(1, 11):
    print(f"\n--- CLIENTE {i} ---")
    nome = input("Digite seu nome: =>> ")
    idade = input("Digite sua idade: =>> ")
    resposta = input("Digite a resposta (1 - excelente, 2 - boa, 3 - ruim): =>> ")
    
    # Estruturas de repetição for para loop de entrevistas.
  # Estruturas condicionais (`if`, `elif`, `else`) para validação das notas

    if resposta == "1":
        excelente_count += 1
    elif resposta == "3":
        ruim_count += 1

# eles só vão rodar depois que o loop de 10 clientes terminar.
# print("\n=============================")

print(f"Total de respostas excelentes: {excelente_count}")
print(f"Total de respostas ruins: {ruim_count}")
print("=============================")