# General objective
Separate the existing withdrawal, deposit and statement functions into functions. Create two new functions: register users (customer) and register bank account.

(Separe as funções existentes de retirada, depósito e extrato em funções. Crie duas novas funções: cadastrar usuários (cliente) e cadastrar conta bancária.)

## Challenge (Desafio)
Make the code more modularized, create functions for existing operations and view extracts. Create two new functions: create user and create current account (link with user)

(Torne o código mais modularizado, crie funções para operações existentes e visualize extrações. Crie duas novas funções: criar usuário e criar conta corrente (vincular com usuário))

### Separation into functions
Create functions for all system operations. Each function will have a rule for passing arguments.

(Crie funções para todas as operações do sistema. Cada função terá uma regra para passar argumentos.)

### Bank withdrawal
The function must only receive arguments by name (keyword only).

(A função só deve receber argumentos por nome (somente palavra-chave).)

### Bank deposit
This function must only receive positional arguments.(Esta função deve receber apenas argumentos posicionais.)

### Extract
Just must only receive arguments by name and positional

### New functions
Create the user and current account

User consists of: name, date of birth, social security number and address. The address is a string with the format: street. Only the CPF numbers must be stored, you cannot have 2 identical CPF numbers

(O usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço é uma string com o formato: rua. Somente os números de CPF devem ser armazenados, não é possível ter 2 números de CPF idênticos)

Current account consists of: you must store accounts in a list made up of: agency, account number and user. The account number is sequential, starting at 1. Agency number is fixed "0001", the user can have more than one account.

(Você deve armazenar as contas em uma lista composta por: agência, número da conta e usuário. O número da conta é sequencial, começando em 1. O número da agência é fixo “0001”, o usuário pode ter mais de uma conta.)

# File with the name "Original" is made as per the request (Arquivo com o nome "Original" é feito conforme solicitação)