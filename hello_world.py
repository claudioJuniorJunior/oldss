#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hello World - Primeiro script Python do projeto
Autor: Claudio Junior
"""


def saudacao(nome="Mundo"):
    """Retorna uma mensagem de saudacao."""
    return f"Ola, {nome}! Bem-vindo ao projeto!"


def main():
    print("=" * 40)
    print("   Hello, World!")
    print("=" * 40)
    print()
    print(saudacao())
    print(saudacao("Claudio"))
    print()
    print("Projeto: oldss - Automacao de Testes ViaCEP")
    print("Branch: CFlymaneiro")
    print("Linguagem: Python 3")


if __name__ == "__main__":
    main()
