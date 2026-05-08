# Objetivo
Devo fazer um sistema com: *Decorador de log*, *Gerador de relatórios* e *Iterador personalizado*

**Decorador de log**: Implemente um decorador que seja aplicado a todas as funções de transações (depósito, saque, criação de conta, etc). Esse decorador deve egistrar (printar) a data e hora de cada transação, bem como o tipo de transação.

**Gerar relátorios**: Crie um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos).

**Iterador personalizado**: Implemente um iterador personalizado Contalterador que permite iterar sobre todas as contas do banco, retornando informações básicas de cada conta (números, saldo atual, etc).