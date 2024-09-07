alunos = {}

def AdicionarAluno():
    global alunos
    matricula = input("Matrícula do aluno: ").strip()
    nome = input("Nome do aluno: ").strip()
    
    if matricula in alunos:
        print("Erro: Já existe essa matrícula.")
    else:
        alunos[matricula] = nome
        print("Aluno adicionado com sucesso!")

def RemoverAluno():
    global alunos
    matricula = input("Digite a matrícula que deseja remover: ").strip()
    
    if matricula in alunos:
        del alunos[matricula]
        print("Aluno removido com sucesso!")
    else:
        print("Erro: Aluno não encontrado.")

def AtualizarAluno():
    global alunos
    matricula = input("Digite o número de matrícula do aluno a ser atualizado: ").strip()
    
    if matricula in alunos:
        novo_nome = input("Digite o novo nome do aluno: ").strip()
        alunos[matricula] = novo_nome
        print("Nome do aluno atualizado com sucesso!")
    else:
        print("Erro: Aluno não encontrado.")

def VerAlunos():
    global alunos
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Lista de Alunos:")
        for matricula, nome in alunos.items():
            print(f"Matrícula: {matricula}, Nome: {nome}")

def menu():
    """ Exibe o menu e chama a função correspondente com base na escolha do usuário. """
    while True:
        print("\nMenu:")
        print("1 - Adicionar aluno")
        print("2 - Remover aluno")
        print("3 - Atualizar aluno")
        print("4 - Ver alunos")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            AdicionarAluno()
        elif opcao == '2':
            RemoverAluno()
        elif opcao == '3':
            AtualizarAluno()
        elif opcao == '4':
            VerAlunos()
        elif opcao == '0':
            print("Obrigado, Volte Sempre.")
            break
        else:
            print("Opção inválida. Tente um número válido de 0 à 4.")

if __name__ == "__main__":
    menu()
