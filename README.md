
# Sistema Bancário Simples

Este é um sistema bancário simples implementado em Python, que permite ao usuário realizar operações bancárias básicas, como depósito, saque e consulta de saldo. O programa possui um limite de saldo e de saques por dia.

## Funcionalidades

O sistema oferece as seguintes opções no menu:

1. **Depositar**: Permite ao usuário adicionar uma quantia ao saldo.
2. **Sacar**: Permite ao usuário realizar saques, respeitando o limite de valor por saque e o número máximo de saques diários.
3. **Extrato**: Exibe o saldo atual do usuário.
4. **Criar usuário**: Cria um novo usuário.
5. **Criar conta**: Cria uma nova conta.
6. **Sair**: Encerra o programa.

## Limites do Sistema

- O limite máximo para saque é de R$500,00 por vez.
- O usuário pode realizar até **3 saques** por dia.
- O saldo inicial do usuário é **R$0,00**.
- Não é permitido realizar saques com valor superior ao saldo disponível.

## Exemplo de Funcionamento

Quando o programa é iniciado, o usuário vê um menu com as opções de operações. Dependendo da escolha, ele pode realizar depósitos, saques ou visualizar o saldo.

### 1. Depósito

O usuário escolhe a opção **Depositar** e insere o valor a ser depositado. O saldo é atualizado com o valor inserido.

### 2. Saque

O usuário escolhe a opção **Sacar** e insere o valor a ser sacado. O sistema verifica:
- Se o valor não ultrapassa o limite de R$500,00.
- Se o valor do saque não é maior que o saldo disponível.
- Se o número de saques diários (máximo de 3) não foi excedido.

Se todas as condições forem atendidas, o saque é realizado e o saldo é atualizado.

### 3. Extrato

O usuário pode escolher a opção **Extrato** para visualizar o saldo disponível.

### 4. Sair

A opção **Sair** encerra o programa.

## Como Executar

Para rodar o programa, basta ter o Python instalado e executar o código em um terminal ou editor que suporte Python.

```bash
python sistema_bancario.py
```
