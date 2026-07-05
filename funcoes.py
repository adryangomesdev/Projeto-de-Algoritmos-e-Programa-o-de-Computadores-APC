# --- FUNÇÕES DE GERENCIAMENTO DE ALUNOS ---
# Tópicos: Dicionários, Listas, Tuplas, Strings

def cadastrar_aluno(alunos_db):
    print("\n--- Cadastro de Novo Aluno ---")
    # Tópico: Strings (strip, title)
    nome = input("Nome completo: ").strip().title()
    cpf = input("CPF (apenas números): ").strip()
    
    # Validação simples (Condicional e Lógica)
    if not nome or not cpf.isnumeric():
        print("Erro: Nome e CPF são obrigatórios e CPF deve ser numérico.")
        return

    # Gera um ID simples
    novo_id = str(len(alunos_db) + 1001) 
    
    # Tópico: Tuplas (para dados imutáveis do aluno)
    alunos_db[novo_id] = (novo_id, nome, cpf)
    print(f"Aluno '{nome}' cadastrado com sucesso! (ID: {novo_id})")

def listar_alunos(alunos_db):
    print("\n--- Lista de Alunos Cadastrados ---")
    if not alunos_db:
        print("Nenhum aluno cadastrado.")
        return
        
    # Tópico: Repetição (for) e Dicionários (items)
    for aluno_id, dados_tupla in alunos_db.items():
        # Tópico: Strings (f-strings e formatação)
        print(f"ID: {dados_tupla[0]:<5} | Nome: {dados_tupla[1]:<30} | CPF: {dados_tupla[2]}")

# --- FUNÇÕES DE GERENCIAMENTO DE DISCIPLINAS ---
# Tópicos: Dicionários, Conjuntos (Sets), Repetição (while)

def cadastrar_disciplina(disciplinas_db, prerequisitos_db):
    print("\n--- Cadastro de Nova Disciplina ---")
    # Tópico: Strings (upper)
    codigo = input("Código da disciplina (ex: COMP123): ").strip().upper()
    nome = input("Nome da disciplina: ").strip().title()
    professor = input("Nome do professor: ").strip().title()
    
    if not codigo or not nome:
        print("Erro: Código e Nome são obrigatórios.")
        return
        
    if codigo in disciplinas_db:
        print("Erro: Já existe uma disciplina com esse código.")
        return
        
    # Tópico: Tuplas
    disciplinas_db[codigo] = (codigo, nome, professor)
    
    # Tópico: Conjuntos (Sets) para garantir pré-requisitos únicos
    prerequisitos_db[codigo] = set()
    
    print("\n--- Adicionar Pré-requisitos (digite 0 para parar) ---")
    # Tópico: Repetição (while True)
    while True:
        prereq_cod = input(f"Código do pré-requisito para '{nome}' (ou 0): ").strip().upper()
        
        if prereq_cod == '0':
            break # Encerra a repetição
            
        # Tópico: Condicional e Lógica
        if prereq_cod in disciplinas_db and prereq_cod != codigo:
            prerequisitos_db[codigo].add(prereq_cod)
            print(f"Pré-requisito '{prereq_cod}' adicionado.")
        else:
            print("Erro: Código de disciplina inválido ou é a própria disciplina.")
            
    print(f"Disciplina '{nome}' cadastrada com sucesso!")

def listar_disciplinas(disciplinas_db, prerequisitos_db):
    print("\n--- Lista de Disciplinas Cadastradas ---")
    if not disciplinas_db:
        print("Nenhuma disciplina cadastrada.")
        return
        
    for cod, dados_tupla in disciplinas_db.items():
        print(f"Cód: {dados_tupla[0]:<8} | Nome: {dados_tupla[1]:<30} | Prof.: {dados_tupla[2]}")
        
        prereqs = prerequisitos_db.get(cod)
        # Tópico: Condicional
        if prereqs:
            # Tópico: Conjuntos (join)
            print(f"    └> Pré-requisitos: {', '.join(prereqs)}")

# --- FUNÇÃO DE RECURSIVIDADE ---
# Tópico: Recursividade

def checar_prerequisitos_recursivo(aluno_id, disciplina_cod, matriculas_db, prerequisitos_db):
    """
    Verifica recursivamente se um aluno cumpre todos os pré-requisitos
    para uma disciplina, incluindo os pré-requisitos dos pré-requisitos.
    """
    prereqs = prerequisitos_db.get(disciplina_cod)
    
    # 1. Caso Base: A disciplina não tem pré-requisitos
    if not prereqs:
        return True # Aluno pode cursar
        
    # 2. Caso Geral: A disciplina TEM pré-requisitos
    historico_aluno = matriculas_db.get(aluno_id, {})
    
    for req_cod in prereqs:
        # 2a. Aluno não cursou o pré-requisito
        if req_cod not in historico_aluno:
            print(f"    [Falha] Falta cursar: {req_cod}")
            return False
            
        # 2b. Aluno cursou mas não foi aprovado
        if historico_aluno[req_cod]['Status'] != 'Aprovado':
            print(f"    [Falha] Não foi aprovado em: {req_cod}")
            return False
            
        # 2c. (Chamada Recursiva) Verifica os pré-requisitos DO pré-requisito
        if not checar_prerequisitos_recursivo(aluno_id, req_cod, matriculas_db, prerequisitos_db):
            # Se a chamada recursiva falhar, a verificação inteira falha
            return False
            
    # 3. Sucesso: Passou por todos os pré-requisitos no loop
    return True

# --- FUNÇÕES DE GERENCIAMENTO DE MATRÍCULAS ---
# Tópicos: Dicionários Aninhados, Condicionais, Lógica

def matricular_aluno(alunos_db, disciplinas_db, prerequisitos_db, matriculas_db):
    print("\n--- Matricular Aluno em Disciplina ---")
    aluno_id = input("ID do Aluno: ").strip()
    disciplina_cod = input("Código da Disciplina: ").strip().upper()
    
    # Tópico: Condicionais e Lógica (and, or, not)
    if aluno_id not in alunos_db or disciplina_cod not in disciplinas_db:
        print("Erro: Aluno ou Disciplina não encontrado(a).")
        return
        
    print(f"Verificando pré-requisitos para {disciplinas_db[disciplina_cod][1]}...")
    
    # Chama a função recursiva
    if not checar_prerequisitos_recursivo(aluno_id, disciplina_cod, matriculas_db, prerequisitos_db):
        print("Matrícula falhou: Aluno não cumpre todos os pré-requisitos em cadeia.")
        return
        
    print("Verificação de pré-requisitos OK!")

    # Tópico: Dicionários (setdefault, aninhamento)
    # Garante que o aluno exista no DB de matrículas
    matriculas_db.setdefault(aluno_id, {})
    
    if disciplina_cod in matriculas_db[aluno_id]:
        print("Erro: Aluno já está matriculado nesta disciplina.")
        return
        
    # Cria o registro de matrícula
    matriculas_db[aluno_id][disciplina_cod] = {
        'P1': 0.0,
        'P2': 0.0,
        'Media': 0.0,
        'Status': 'Cursando'
    }
    print(f"Matrícula de {alunos_db[aluno_id][1]} em {disciplinas_db[disciplina_cod][1]} realizada!")

def lancar_notas(matriculas_db, alunos_db, disciplinas_db):
    print("\n--- Lançamento de Notas ---")
    aluno_id = input("ID do Aluno: ").strip()
    disciplina_cod = input("Código da Disciplina: ").strip().upper()

    # Tópico: Dicionários (aninhamento)
    if (aluno_id not in matriculas_db or 
        disciplina_cod not in matriculas_db[aluno_id]):
        print("Erro: Matrícula não encontrada.")
        return

    try:
        p1 = float(input("Nota P1: "))
        p2 = float(input("Nota P2: "))
        
        media = (p1 + p2) / 2
        
        # Tópico: Estruturas Condicionais (if/elif/else)
        if media >= 7.0:
            status = 'Aprovado'
        elif media >= 4.0:
            status = 'Recuperacao'
        else:
            status = 'Reprovado'
            
        # Atualiza o dicionário aninhado
        matricula = matriculas_db[aluno_id][disciplina_cod]
        matricula['P1'] = p1
        matricula['P2'] = p2
        matricula['Media'] = media
        matricula['Status'] = status
        
        print(f"Notas lançadas. Média: {media:.1f} | Status: {status}")
        
    except ValueError:
        print("Erro: Notas devem ser valores numéricos.")

# --- FUNÇÕES DE RELATÓRIOS ---

def exibir_historico_aluno(alunos_db, disciplinas_db, matriculas_db):
    print("\n--- Histórico Escolar ---")
    aluno_id = input("ID do Aluno: ").strip()
    
    if aluno_id not in alunos_db:
        print("Erro: Aluno não encontrado.")
        return
        
    aluno_nome = alunos_db[aluno_id][1]
    historico = matriculas_db.get(aluno_id, {})
    
    print(f"\nHistórico de: {aluno_nome} (ID: {aluno_id})")
    
    if not historico:
        print("Aluno não possui matrículas.")
        return
        
    soma_medias = 0
    total_disciplinas_validas = 0
    
    # Tópico: Repetição (for) e Dicionários (items)
    for disciplina_cod, dados_matricula in historico.items():
        nome_disciplina = disciplinas_db.get(disciplina_cod, ("?", "Disciplina Excluída", "?"))[1]
        
        print(f"  - {nome_disciplina:<15} | Média: {dados_matricula['Media']:<4.1f} | Status: {dados_matricula['Status']}")
        
        # Tópico: Lógica
        if dados_matricula['Status'] in ['Aprovado', 'Reprovado']:
            soma_medias += dados_matricula['Media']
            total_disciplinas_validas += 1
            
    # Cálculo do Coeficiente de Rendimento (CR)
    if total_disciplinas_validas > 0:
        cr = soma_medias / total_disciplinas_validas
        print(f"\nCoeficiente de Rendimento (CR): {cr:.2f}")
    else:
        print("\nCR: (Não aplicável, nenhuma disciplina concluída)")


def alunos_em_comum(matriculas_db, alunos_db):
    print("\n--- Alunos em Comum entre Duas Disciplinas ---")
    cod_a = input("Código da Disciplina A: ").strip().upper()
    cod_b = input("Código da Disciplina B: ").strip().upper()

    # Tópico: Conjuntos (Sets)
    alunos_a = set()
    alunos_b = set()
    
    # Tópico: Repetição (for)
    for aluno_id, disciplinas_cursadas in matriculas_db.items():
        if cod_a in disciplinas_cursadas:
            alunos_a.add(aluno_id)
        if cod_b in disciplinas_cursadas:
            alunos_b.add(aluno_id)
            
    # Tópico: Operações com Conjuntos (& = interseção)
    alunos_comum = alunos_a & alunos_b
    
    if not alunos_comum:
        print("Nenhum aluno em comum encontrado.")
        return
        
    print(f"\nAlunos matriculados em '{cod_a}' E '{cod_b}':")
    for aluno_id in alunos_comum:
        print(f"  - {alunos_db[aluno_id][1]} (ID: {aluno_id})")
        
# --- FUNÇÕES DE GERENCIAMENTO DE HORÁRIOS ---

def cadastrar_horario(horarios_db, disciplinas_db):
    print("\n--- Cadastrar Horário (Matriz) ---")
    cod_disciplina = input("Código da Disciplina para o horário:\n(OBS: Crie uma disciplina antes se não tiver criado ainda!)").strip().upper()
    
    if cod_disciplina not in disciplinas_db:
        print("Erro: Disciplina não encontrada.")
        return

    # Tópico: Matrizes (Lista de Listas
    # Representa [Dia, H1, H2, H3, H4]
    matriz_horario = [
        ["HORA:", "08:00-10:00", "10:00-12:00", "14:00-16:00", "16:00-18:00"],
        ["SEG", "LIVRE", "LIVRE", "LIVRE", "LIVRE"],
        ["TER", "LIVRE", "LIVRE", "LIVRE", "LIVRE"],
        ["QUA", "LIVRE", "LIVRE", "LIVRE", "LIVRE"],
        ["QUI", "LIVRE", "LIVRE", "LIVRE", "LIVRE"],
        ["SEX", "LIVRE", "LIVRE", "LIVRE", "LIVRE"]
    ]
    
    while True:
        try:
            print("\nDias: 1=SEG, 2=TER, 3=QUA, 4=QUI, 5=SEX")
            dia = int(input("Digite o dia (1-5) ou 0 para sair: "))
            if dia == 0:
                break
            if not 1 <= dia <= 5:
                raise ValueError
                
            print("Horários: 1='08-10', 2='10-12', 3='14-16', 4='16-18'")
            horario = int(input("Digite o horário (1-4): "))
            if not 1 <= horario <= 4:
                raise ValueError
            
            # Atualiza a matriz
            matriz_horario[dia][horario] = cod_disciplina
            print("Horário alocado!")
            
        except ValueError:
            print("Erro: Entrada inválida. Digite apenas os números indicados.")

    horarios_db[cod_disciplina] = matriz_horario
    print("Horário salvo.")

def exibir_horario_formatado(horarios_db):
    print("\n--- Exibir Horário de Disciplina ---")
    cod_disciplina = input("Código da Disciplina: ").strip().upper()
    
    matriz = horarios_db.get(cod_disciplina)
    
    if not matriz:
        print("Nenhum horário cadastrado para esta disciplina.")
        return

    print(f"\nHorário de: {cod_disciplina}")
    # Tópico: Repetição Aninhada (para percorrer a Matriz)
    for linha in matriz:
        for celula in linha:
            # Formatação de string para alinhar colunas
            print(f"{celula:<12}", end="")
        print()  

def exibir_horario_geral(horarios_db):
    """
    Consolida e exibe um horário geral com todas as disciplinas.
    Identifica e mostra conflitos de horário.
    """
    print("\n--- Horário Geral Consolidado ---")
    if not horarios_db:
        print("Nenhum horário cadastrado no sistema.")
        return

    # Cria uma matriz geral vazia
    matriz_geral = [
        ["HORA:", "08:00-10:00", "10:00-12:00", "14:00-16:00", "16:00-18:00"],
        ["SEG", "LIVRE", "LIVRE", "LIVRE", "LIVRE"],
        ["TER", "LIVRE", "LIVRE", "LIVRE", "LIVRE"],
        ["QUA", "LIVRE", "LIVRE", "LIVRE", "LIVRE"],
        ["QUI", "LIVRE", "LIVRE", "LIVRE", "LIVRE"],
        ["SEX", "LIVRE", "LIVRE", "LIVRE", "LIVRE"]
    ]

    # Preenche a matriz geral com os horários de todas as disciplinas
    for cod_disciplina, matriz_disciplina in horarios_db.items():
        for i in range(1, 6):  # Linhas (dias)
            for j in range(1, 5):  # Colunas (horários)
                if matriz_disciplina[i][j] != "LIVRE":
                    if matriz_geral[i][j] == "LIVRE":
                        matriz_geral[i][j] = cod_disciplina
                    else:
                        # Conflito de horário!
                        matriz_geral[i][j] += f"/{cod_disciplina}"

    # Exibe a matriz geral formatada
    for linha in matriz_geral:
        for celula in linha:
            print(f"{celula:<12}", end="")
        print()
