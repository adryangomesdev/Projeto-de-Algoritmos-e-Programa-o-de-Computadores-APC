# Projeto de Algoritmos e Programação de Computadores (APC)

SIGAA Lite - Resumo do Projeto
---
O SIGAA Lite é um sistema de gestão académica executado no terminal (CLI), desenvolvido inteiramente em Python. O projeto serve para aplicar os conceitos lecionados na disciplina de Algoritmos e Programação de Computadores (APC) num cenário real.

Principais Funcionalidades:

Gestão e Cadastros: Registo de alunos e disciplinas, permitindo configurar a alocação de pré-requisitos.

Matrículas Inteligentes e Notas: O sistema utiliza validação recursiva para garantir que um aluno só se matricula se tiver cumprido toda a cadeia de pré-requisitos. Permite também o registo de notas com cálculo automático do estado (Aprovado, Reprovado, Recuperação).

Controlo de Horários: Alocação de aulas numa matriz semanal, detetando automaticamente quaisquer conflitos ou sobreposições de horário.

Relatórios Académicos: Geração de históricos escolares com o cálculo do Coeficiente de Rendimento (CR) e identificação de estudantes matriculados simultaneamente em disciplinas distintas.

Guarda de Dados: Todo o estado do programa (alunos, notas, horários) é guardado e carregado automaticamente num ficheiro .json.

Aspetos Técnicos:
O código não utiliza bibliotecas externas. Está estruturado em módulos e faz uso de estruturas de dados nativas (listas, tuplas, dicionários e conjuntos/sets), matrizes, lógica de recursividade e manipulação de ficheiros locais.
