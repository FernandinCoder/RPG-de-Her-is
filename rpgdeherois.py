print("Bem vindo ao RPG de Heróis!")
print("Escolha sua classe:")
print("1 - Guerreiro (Mais dano,menos defesa)")
print("2 - Mago (Mais defesa e menos dano,mas pode usar magias)")
print("3 - Arqueiro (Dano médio,defesa média,mas pode atacar de longe)")
classe = int(input("Digite o número da classe escolhida: "))
if classe == 1:
    print("Você escolheu a classe Guerreiro")
    print("Defesa:50")
    print("Dano:95") 
elif classe == 2:
    print("Você escolheu a classe Mago")
    print("Defesa:80")
    print("Dano:50")
elif classe == 3:
    print("Você escolheu a classe Arqueiro")
    print("Defesa:65")
    print("Dano:75")
else:
    print("Opção inválida,você será um camponês pelado")
    print("Defesa:10")
    print("Dano:10")
mochila = []
print("Você encontrou um baú do tesouro,escolha um item para colocar na sua mochila:")
print("1 - Espada de Fogo (Dano + 60)")
print("2 - Escudo Lendário (Defesa + 50)")
print("3 - Poção de Cura (Restaura 50 de vida)")
item = input("Digite o nome do item: ")
mochila.append(item)
print(f"Sua mochila agora contém: {mochila}")
print("Você encontrou o Dragão Lendário,prepare-se para a batalha!")
print("Escolha sua ação: ")
print("1 - Atacar com tudo")
print("2 - Fugir desesperadamente")
escolha = input("Digite o número da ação escolhida: ")
if escolha == "1":
    print("Você atacou o Dragão Lendário com tudo que tinha!")
    print("O Dragão Lendário foi derrotado,parabéns!")
elif escolha == "2":
    print("Você fugiu desesperadamente,mas o Dragão Lendário te alcançou e te derrotou,fim de jogo!")
else:
    print("Você congelou de medo e o dragão te derrotou,fim de jogo!")

