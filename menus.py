# -*- coding: utf-8 -*-
from funcoes import (
    # Funções de lógica de negócio
    cadastrar_aluno, listar_alunos,
    cadastrar_disciplina, listar_disciplinas,
    matricular_aluno, lancar_notas, cadastrar_horario,
    exibir_horario_formatado, exibir_horario_geral,
    exibir_historico_aluno, alunos_em_comum
)

# Importa a função de limpar a tela do arquivo principal
from utils import limpar_tela

# --- FUNÇÕES PRINCIPAIS (MENU) ---
# Tópico: Funções, Estrutura de Repetição (while), Condicionais (if/elif/else)

def exibir_menu_principal():
    print("\n" + "="*30)
    print("  SIGAA (Lite) - Menu Principal")
    print("="*30)
    print("1. Gerenciar Alunos")
    print("2. Gerenciar Disciplinas")
    print("3. Gerenciar Matrículas")
    print("4. Gerenciar Horários (Matrizes)")
    print("5. Relatórios")
    print("0. Salvar e Sair")
    return input("Escolha uma opção: ").strip()

def menu_gerenciar_alunos(alunos_db):
    while True:
        print("\n--- Gerenciar Alunos ---")
        print("1. Cadastrar Novo Aluno")
        print("2. Listar Todos os Alunos")
        print("0. Voltar ao Menu Principal")
        opcao = input("Opção: ").strip()
        
        if opcao == '1':
            cadastrar_aluno(alunos_db)
        elif opcao == '2':
            listar_alunos(alunos_db)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        limpar_tela()

def menu_gerenciar_disciplinas(disciplinas_db, prerequisitos_db):
    while True:
        print("\n--- Gerenciar Disciplinas ---")
        print("1. Cadastrar Nova Disciplina")
        print("2. Listar Todas as Disciplinas")
        print("0. Voltar ao Menu Principal")
        opcao = input("Opção: ").strip()
        
        if opcao == '1':
            cadastrar_disciplina(disciplinas_db, prerequisitos_db)
        elif opcao == '2':
            listar_disciplinas(disciplinas_db, prerequisitos_db)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        limpar_tela()

def menu_gerenciar_matriculas(alunos_db, disciplinas_db, prerequisitos_db, matriculas_db):
    while True:
        print("\n--- Gerenciar Matrículas ---")
        print("1. Matricular Aluno em Disciplina")
        print("2. Lançar Notas")
        print("0. Voltar ao Menu Principal")
        opcao = input("Opção: ").strip()
        
        if opcao == '1':
            matricular_aluno(alunos_db, disciplinas_db, prerequisitos_db, matriculas_db)
        elif opcao == '2':
            lancar_notas(matriculas_db, alunos_db, disciplinas_db)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        limpar_tela()

def menu_gerenciar_horarios(horarios_db, disciplinas_db):
    while True:
        print("\n--- Gerenciar Horários (Matrizes) ---")
        print("1. Cadastrar/Editar Horário de Disciplina")
        print("2. Exibir Horário de uma Disciplina")
        print("3. Exibir Horário Geral (Todas as Disciplinas)")
        print("0. Voltar ao Menu Principal")
        opcao = input("Opção: ").strip()

        if opcao == '1':
            cadastrar_horario(horarios_db, disciplinas_db)
        elif opcao == '2':
            exibir_horario_formatado(horarios_db)
        elif opcao == '3':
            exibir_horario_geral(horarios_db)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        limpar_tela()

def menu_relatorios(alunos_db, disciplinas_db, matriculas_db):
    while True:
        print("\n--- Relatórios e Consultas ---")
        print("1. Exibir Histórico Escolar do Aluno")
        print("2. Consultar Alunos em Comum (Sets)")
        print("0. Voltar ao Menu Principal")
        opcao = input("Opção: ").strip()
        
        if opcao == '1':
            exibir_historico_aluno(alunos_db, disciplinas_db, matriculas_db)
        elif opcao == '2':
            alunos_em_comum(matriculas_db, alunos_db)
        elif opcao == '0':
            break
        else:
            print("Opção inválida.")
        input("\nPressione Enter para continuar...")
        limpar_tela()
