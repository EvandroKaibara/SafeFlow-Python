
# 🛟 Safe Flow - Sistema de Informações de Emergência

Este é um sistema simples em Python que simula a gestão de informações de emergência, como rotas seguras, abrigos, alertas e dicas de segurança. Ideal para situações de desastre onde é importante saber rapidamente as opções disponíveis.

## 📋 Funcionalidades

- **Ver rotas disponíveis**: Lista rotas seguras e bloqueadas.
- **Ver abrigos**: Mostra os abrigos ativos ordenados por proximidade e menor ocupação.
- **Ver alertas**: Apresenta alertas ativos relacionados às rotas.
- **Ver dicas de segurança**: Exibe orientações úteis em situações de emergência.
- **Procurar abrigo mais próximo**: Sugere o abrigo mais próximo com rota segura.

## ▶️ Como executar

1. Certifique-se de ter o Python instalado na sua máquina.
2. Salve o código em um arquivo, por exemplo `safe_flow.py`.
3. Execute o script pelo terminal:

```bash
python safe_flow.py
```

4. Navegue pelo menu interativo usando os números correspondentes às opções.

## 💡 Exemplo de Uso

Ao rodar o script, você verá um menu como este:

```
=== SAFE FLOW ===
1. Ver rotas
2. Ver abrigos
3. Ver alertas
4. Ver dicas de segurança
5. Procurar abrigo mais próximo
0. Sair
```

Digite o número da opção desejada e pressione Enter.

## 🧱 Estrutura de Dados

O sistema utiliza listas de dicionários para simular os dados de:

- Rotas
- Abrigos
- Alertas

Esses dados podem ser facilmente expandidos ou conectados a uma base de dados real futuramente.

## 📌 Requisitos

- Python 3.x

Não são necessárias bibliotecas externas.

## 📃 Licença

Este projeto é de uso livre para fins educacionais.
