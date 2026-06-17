# 📊 Sistema Bancário - Explicação do Diagrama UML

Este documento descreve o funcionamento do diagrama UML de um sistema bancário simples, explicando suas classes, interfaces, atributos, métodos e relacionamentos.

---

# 🧠 Visão Geral do Sistema

O sistema representa um banco básico com:

- Clientes (Pessoa Física)
- Contas bancárias
- Histórico de transações
- Transações (Depósito e Saque)

O objetivo é simular operações bancárias como:
- Criar conta
- Depositar dinheiro
- Sacar dinheiro
- Registrar histórico de operações

---

# 🧩 Classes e Responsabilidades

## 👤 Cliente

Representa o cliente do banco.

### Atributos:
- `endereco: str` → Endereço do cliente  
- `contas: list` → Lista de contas associadas ao cliente  

### Métodos:
- `realizar_transacao(conta, transacao)` → Executa uma transação em uma conta
- `adicionar_conta(conta)` → Associa uma nova conta ao cliente

### Relacionamento:
- Um cliente pode ter **várias contas (1:N)**

---

## 🧍 PessoaFisica (herda Cliente)

Representa um cliente pessoa física.

### Atributos adicionais:
- `cpf: str` → CPF do cliente  
- `nome: str` → Nome completo  
- `data_nascimento: date` → Data de nascimento  

### Observação:
- Especializa a classe Cliente (herança)

---

## 🏦 Conta

Representa uma conta bancária genérica.

### Atributos:
- `saldo: float` → Saldo atual da conta  
- `numero: int` → Número da conta  
- `agencia: str` → Agência bancária  
- `cliente: Cliente` → Dono da conta  
- `historico: Historico` → Histórico de transações  

### Métodos:
- `saldo()` → Retorna saldo atual  
- `nova_conta(cliente, numero)` → Cria nova conta  
- `sacar(valor)` → Realiza saque  
- `depositar(valor)` → Realiza depósito  

### Relacionamento:
- Cada conta pertence a **um cliente**
- Cada conta possui **um histórico**

---

## 💳 ContaCorrente (herda Conta)

Especialização de Conta com regras adicionais.

### Atributos:
- `limite: float` → Limite de crédito  
- `limite_saques: int` → Número máximo de saques permitidos  

### Observação:
- Adiciona regras específicas de conta corrente

---

## 📜 Historico

Responsável por armazenar todas as transações da conta.

### Métodos:
- `adicionar_transacao(transacao)` → Adiciona uma transação ao histórico  

### Relacionamento:
- Um histórico pertence a **uma conta**
- Um histórico contém **várias transações**

---

## 🔁 Interface Transacao

Define o comportamento padrão de qualquer transação bancária.

### Método obrigatório:
- `registrar(conta: Conta)` → Executa a transação na conta

### Implementações:
- Depósito
- Saque

---

## ➕ Deposito (implementa Transacao)

### Atributos:
- `valor: float` → Valor a ser depositado  

### Comportamento:
- Adiciona valor ao saldo da conta
- Registra no histórico

---

## ➖ Saque (implementa Transacao)

### Atributos:
- `valor: float` → Valor a ser sacado  

### Comportamento:
- Remove valor do saldo da conta (se possível)
- Respeita saldo e limites
- Registra no histórico

---

# 🔗 Relacionamentos Importantes

## Cliente → Conta
- Um cliente pode ter várias contas
- Cada conta pertence a um cliente

## Conta → Histórico
- Cada conta possui um histórico único
- O histórico registra todas as transações

## Histórico → Transação
- O histórico armazena várias transações

## Transação → Conta
- Toda transação é executada em uma conta

## Herança
- `PessoaFisica` herda `Cliente`
- `ContaCorrente` herda `Conta`
- `Deposito` e `Saque` implementam `Transacao`

---

# ⚙️ Fluxo de Funcionamento

1. Cliente é criado (Pessoa Física)
2. Conta é criada e associada ao cliente
3. Cliente realiza uma transação
4. Transação é enviada para a conta
5. Conta atualiza saldo
6. Histórico registra a transação

---

# 💡 Resumo

Esse sistema simula um banco real de forma simplificada, aplicando conceitos importantes de:

- Programação orientada a objetos (POO)
- Herança
- Interfaces
- Encapsulamento
- Relacionamentos entre classes

---

# 🚀 Possíveis melhorias

- Adicionar autenticação de cliente
- Criar extrato detalhado
- Implementar múltiplas contas por agência
- Criar sistema de transferência entre contas
- Persistência em banco de dados