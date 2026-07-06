# -*- coding: utf-8 -*-
import json  
import os

# --- NOME DO ARQUIVO DE BANCO DE DADOS ---
DB_FILE = "siga_lite_db.json"

# Importa funções de utilidade
from utils import limpar_tela
# --- FUNÇÕES DE UTILIDADE (ARQUIVOS) ---
# Tópico: Arquivos (Leitura e Escrita)

def carregar_dados():
    """
    Carrega os dados do arquivo JSON.
    Se o arquivo não existir, retorna bancos de dados vazios.
    """
    if not os.path.exists(DB_FILE):
        return {}, {}, {}, {}, {}

    try:
        with open(DB_FILE, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            
            
            prereqs_db = dados.get('prerequisitos', {})
            prerequisitos_convertidos = {
                disciplina: set(lista_prereqs) 
                for disciplina, lista_prereqs in prereqs_db.items()
            }
            
            
            return (
                dados.get('alunos', {}),
                dados.get('disciplinas', {}),
                prerequisitos_convertidos,
                dados.get('matriculas', {}),
                dados.get('horarios', {})
            )
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return {}, {}, {}, {}, {}

def salvar_dados(alunos, disciplinas, prerequisitos, matriculas, horarios):
    """
    Salva todos os bancos de dados em um único arquivo JSON.
    """
    try:
        # Converte os CONJUNTOS (Sets) de pré-requisitos em listas para salvar em JSON
        prereqs_para_salvar = {
            disciplina: list(set_prereqs) 
            for disciplina, set_prereqs in prerequisitos.items()
        }

        dados_completos = {
            'alunos': alunos,
            'disciplinas': disciplinas,
            'prerequisitos': prereqs_para_salvar,
            'matriculas': matriculas,
            'horarios': horarios
        }
        
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(dados_completos, f, indent=4, ensure_ascii=False)
        print("\n[Sistema] Dados salvos com sucesso!")
        
    except Exception as e:
        print(f"\n[Sistema] Erro ao salvar dados: {e}")

# Importa as funções de menu do novo arquivo
from menus import (
    exibir_menu_principal,
    menu_gerenciar_alunos,
    menu_gerenciar_disciplinas,
    menu_gerenciar_matriculas,
    menu_gerenciar_horarios,
    menu_relatorios
)

def main():
    alunos_db, disciplinas_db, prerequisitos_db, matriculas_db, horarios_db = carregar_dados()

    limpar_tela()
    print("Bem-vindo ao SIGAA (Lite)!")
    print(f"Carregados {len(alunos_db)} alunos e {len(disciplinas_db)} disciplinas.")
    input("\nPressione Enter para iniciar...")

    # Tópico: Estrutura de Repetição (while True)
    while True:
        limpar_tela()
        opcao = exibir_menu_principal()
        
        # Tópico: Estruturas Condicionais (if/elif/else)
        if opcao == '1':
            menu_gerenciar_alunos(alunos_db)
        elif opcao == '2':
            menu_gerenciar_disciplinas(disciplinas_db, prerequisitos_db)
        elif opcao == '3':
            menu_gerenciar_matriculas(alunos_db, disciplinas_db, prerequisitos_db, matriculas_db)
        elif opcao == '4':
            menu_gerenciar_horarios(horarios_db, disciplinas_db)
        elif opcao == '5':
            menu_relatorios(alunos_db, disciplinas_db, matriculas_db)
        elif opcao == '0':
            # Tópico: Funções
            salvar_dados(alunos_db, disciplinas_db, prerequisitos_db, matriculas_db, horarios_db)
            print("Saindo... Até logo!")
            break # Encerra o loop principal
        else:
            print("Opção inválida. Tente novamente.")

# Ponto de entrada do script
if __name__ == "__main__":
    main()
