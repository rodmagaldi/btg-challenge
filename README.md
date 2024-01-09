# Desafio técnico BTG PME - Back

Este repositório se refere ao back-end do desafio técnico para a vaga de Software Engineer no time de PME.

Foi implementada uma aplicação simples com um jogo de [Pedra, Papel, Tesoura, Lagarto ou Spock](https://fagocitandooplaneta.wordpress.com/2010/10/19/pedra-papel-tesoura-versao-nerd/).

A aplicação foi implementada em Flask, utilizando o [Strategy Pattern](https://refactoring.guru/design-patterns/strategy) para possibilitar a implementação de outras variações do jogo.

# Para rodar a aplicação

```bash
$ pip install -r requirements.txt
```

```
$ flask --debug run
```

# Para testar a aplicação

Usamos `pytest` e `coverage`.

Para rodar os testes (também rodam em PRs para a branch `main`):

```bash
$ coverage run -m pytest
```

Para ver estatísticas de cobertura:

```bash
$ coverage report
```

```bash
$ coverage html
```