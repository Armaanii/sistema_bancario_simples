## Sistema Bancário Simples - RoBank
Este é um sistema bancário simples desenvolvido em Python, que simula operações básicas de depósito, saque e extrato. 
É um projeto inicial para demonstrar o uso de estruturas condicionais e de repetição em Python, ideal para quem está começando a programar.
Sistema criado em uma atividade do BootCamp open academy Santander 2025.

--------------------------------------------------------------------------------------------------------------------------------------------

🚀  ***Funcionalidades***

O sistema oferece as seguintes funcionalidades:

- **Depósito**: Permite adicionar fundos à sua conta.
- **Saque**: Permite retirar fundos, com limites diários e por transação.
- **Extrato**: Exibe o histórico de todas as movimentações (depósitos e saques) e o saldo atual.
- **Sair**: Encerra o sistema.

--------------------------------------------------------------------------------------------------------------------------------------------

✨  Como Usar
1. Clone o repositório (se estiver em um repositório Git) ou baixe o arquivo main.py
(ou o nome do seu arquivo Python).

2. Execute o arquivo Python a partir do seu terminal:

````
bash

python main.py
````
3. Ao iniciar, o sistema pedirá seu nome para personalização.

4. Um menu será exibido com as opções disponíveis:

- [D] para Depósito
- [S] para Saque
- [E] para Extrato
- [Q] para Sair
  
5. Siga as instruções na tela para realizar as operações desejadas.

____________________________________________________________________________________________________________

💡 Regras de Negócio
- Depósito:
  - Apenas valores positivos são aceitos.

- Saque:
  - O valor do saque não pode exceder o saldo disponível.
  - O valor do saque não pode exceder o limite de R$ 500,00 por transação.
  - Há um limite de 3 saques diários.
  - Apenas valores positivos são aceitos.

- Extrato:
  - Exibe todas as transações (depósitos e saques) e o saldo final.
  - Informa se não houve movimentações.

____________________________________________________________________________________________________________

🛠️ Tecnologias Utilizadas
Python 3.x

Contribuição
Este projeto é um exemplo didático e não está aberto a contribuições externas neste momento. 
No entanto, sinta-se à vontade para bifurcá-lo (fork) e adaptá-lo para seus próprios estudos.

____________________________________________________________________________________________________________

Autor
Desenvolvido por Rodrigo Guedes de barros
