import random
#Biblioteca para interfaces simples
import tkinter as tk

# Variáveis globais armazenando pontuação e as opções do jogo
usuario_vence = 0
computador_vence = 0
opcoes = ["pedra", "papel", "tesoura"]

# Função principal do jogo
def jogar(usuario_input):
    global usuario_vence, computador_vence
    if usuario_input not in opcoes:
        return "Escolha inválida. Tente novamente."
    
# Variáveis que vão gerar o número aleatório escolhido pelo computador
    numero_aleatorio = random.randint(0, 2)
    escolha_computador = opcoes[numero_aleatorio]

# Define empate no if, no elif pontuação para o player e no else pontuação para o computador    
    if usuario_input == escolha_computador:
        return f"Empate! Ambos escolheram {escolha_computador}"
    elif (usuario_input == "pedra" and escolha_computador == "tesoura") or \
         (usuario_input == "papel" and escolha_computador == "pedra") or \
         (usuario_input == "tesoura" and escolha_computador == "papel"):
        usuario_vence += 1
        return f"Você venceu! Computador escolheu {escolha_computador}"
    else:
        computador_vence += 1
        return f"Você perdeu! Computador escolheu {escolha_computador}"

def resultado_final():
    return f"Você ganhou {usuario_vence} vezes.\nO computador ganhou {computador_vence} vezes."

# Função para jogar a partir da interface
def jogar_interface(escolha):
    resultado = jogar(escolha)
    resultado_label.config(text=resultado)
    placar_label.config(text=resultado_final())

# Criação da janela principal
janela = tk.Tk()
janela.title("Jogue: Pedra, Papel e Tesoura")

# Escolha de opção
instrucoes = tk.Label(janela, text="Escolha uma opção:", font=("Arial", 16))
instrucoes.pack(pady=10)

# Botões para as escolhas
botao_pedra = tk.Button(janela, text="Pedra", command=lambda: jogar_interface('pedra'), font=("Arial", 12))
botao_pedra.pack(side=tk.LEFT, padx=10)

botao_papel = tk.Button(janela, text="Papel", command=lambda: jogar_interface('papel'), font=("Arial", 12))
botao_papel.pack(side=tk.LEFT, padx=10)

botao_tesoura = tk.Button(janela, text="Tesoura", command=lambda: jogar_interface('tesoura'), font=("Helvetica", 12))
botao_tesoura.pack(side=tk.LEFT, padx=10)

# Label onde mostra o resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 14))
resultado_label.pack(pady=20)

# Label onde mostra o placar
placar_label = tk.Label(janela, text=resultado_final(), font=("Arial", 14))
placar_label.pack(pady=10)

# Botão para sair do script
botao_sair = tk.Button(janela, text="SAIR", command=janela.quit, font=("Arial", 12))
botao_sair.pack(pady=10)

# Inicia o loop  da interface
janela.mainloop()
