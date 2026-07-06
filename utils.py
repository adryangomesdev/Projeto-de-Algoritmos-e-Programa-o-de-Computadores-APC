# -*- coding: utf-8 -*-
import os

def limpar_tela():
    """Limpa o terminal para uma melhor experiência de usuário."""
    # 'nt' é para Windows, 'posix' é para Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')
