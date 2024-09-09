from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init()

def exibir_perguntas(perguntas):
    pontuacao = 0
    total_perguntas = len(perguntas)
    
    for pergunta in perguntas:
        print(Fore.CYAN + pergunta["pergunta"] + Style.RESET_ALL)
        for alternativa in pergunta["alternativas"]:
            print(Fore.YELLOW + alternativa + Style.RESET_ALL)
        resposta_usuario = input(Fore.GREEN + "Digite a alternativa correta (a, b, c ou d): " + Style.RESET_ALL).strip().lower()
        
        if resposta_usuario == pergunta["resposta"]:
            print(Fore.GREEN + "Resposta correta!" + Style.RESET_ALL + "\n")
            pontuacao += 1
        else:
            resposta_correta = next(alternativa for alternativa in pergunta["alternativas"] if alternativa.startswith(pergunta["resposta"]))
            print(Fore.RED + f"Resposta incorreta. A resposta correta é: {resposta_correta}" + Style.RESET_ALL + "\n")
    
    return pontuacao, total_perguntas

def quiz():
    print(Fore.BLUE + "Seja bem-vindo ao Quiz Bíblico!" + Style.RESET_ALL)
    print(Fore.YELLOW + "Digite 1 para responder o quiz do Antigo Testamento ou 2 para o quiz do Novo Testamento:" + Style.RESET_ALL)
    escolha = input(Fore.GREEN + "Sua escolha: " + Style.RESET_ALL).strip()
    
    if escolha == "1":
        perguntas = [
            {
                "pergunta": "1. Quem foi o rei que perdeu seu direito ao reinado por ter entregado sacrifício a Deus antes do profeta chegar?",
                "alternativas": ["a) Salomão", "b) Saul", "c) Acabe", "d) Nenhuma das alternativas"],
                "resposta": "b"
            },
            {
                "pergunta": "2. Quais são os 5 primeiros livros da Bíblia (em ordem)?",
                "alternativas": ["a) Gênesis, Êxodo, Números, Juízes e Deuteronômio", "b) Gênesis, Êxodo, Levítico, Números e Deuteronômio", "c) Gênesis, Êxodo, Jó, Obadias e Levítico", "d) Gênesis, Êxodo, Números, 1 Samuel e 2 Samuel"],
                "resposta": "b"
            },
            {
                "pergunta": "3. Qual era o nome do profeta que exortou Davi quando pecou com Bate-Seba?",
                "alternativas": ["a) Naamã", "b) Eliseu", "c) Natã", "d) Samuel"],
                "resposta": "c"
            },
            {
                "pergunta": "4. Qual era o ofício de Gomer, mulher de Oseias?",
                "alternativas": ["a) Dona de casa", "b) Padeira", "c) Vinicultora", "d) Prostituta"],
                "resposta": "d"
            }
        ]
    elif escolha == "2":
        perguntas = [
            {
                "pergunta": "1. Quem cantou com Paulo na prisão e o chão tremeu?",
                "alternativas": ["a) Barnabé", "b) Silas", "c) Timóteo", "d) Cefas"],
                "resposta": "b"
            },
            {
                "pergunta": "2. Pedro/Simão e André eram filhos de:",
                "alternativas": ["a) Jonas/João", "b) Simeão", "c) Caifás", "d) Tadeu"],
                "resposta": "a"
            },
            {
                "pergunta": "3. O Apóstolo João escreveu quantos livros na bíblia?",
                "alternativas": ["a) 5", "b) 4", "c) 3", "d) Nenhuma das alternativas"],
                "resposta": "a"
            },
            {
                "pergunta": "4. Quem escreveu os Atos dos Apóstolos?",
                "alternativas": ["a) Paulo", "b) Pedro/Simão", "c) Mateus", "d) Lucas"],
                "resposta": "d"
            }
        ]
    else:
        print(Fore.RED + "Escolha inválida. Encerrando o quiz." + Style.RESET_ALL)
        return

    pontuacao, total_perguntas = exibir_perguntas(perguntas)
    print(Fore.CYAN + f"Sua pontuação final é {pontuacao} de {total_perguntas}." + Style.RESET_ALL)
    print(Fore.CYAN + f"Você respondeu corretamente a {pontuacao} perguntas de um total de {total_perguntas}." + Style.RESET_ALL)
    
    # Pausa a execução para que o usuário veja o resultado
    input(Fore.GREEN + "Pressione Enter para sair..." + Style.RESET_ALL)

if __name__ == "__main__":
    quiz()