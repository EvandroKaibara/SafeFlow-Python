
# Dados______________________________________________________________________________
rotas = [
    {"id": 1, "nome": "Rua A", "status": "segura"},
    {"id": 2, "nome": "Avenida B", "status": "bloqueada"},
    {"id": 3, "nome": "Travessa C", "status": "segura"}
]

abrigos = [
    {"id": 1, "nome": "Escola Central", "distancia_km": 0.8, "ocupacao": 75, "ativo": True},
    {"id": 2, "nome": "Ginásio Municipal", "distancia_km": 1.5, "ocupacao": 90, "ativo": True},
    {"id": 3, "nome": "Igreja São João", "distancia_km": 2.3, "ocupacao": 60, "ativo": False}
]

alertas = [
    {"id": 1, "mensagem": "Rota bloqueada na Avenida B", "tipo": "visual+sonoro", "rota_id": 2}
]

def mostrarRotas():
    try:
        print("\nROTAS DISPONÍVEIS:")
        for rota in rotas:
            print(f"- {rota['nome']}: {rota['status']}")
    except Exception as e:
        print(f"Erro ao exibir rotas: {e}")

def mostrarAbrigos():
    try:
        print("\nABRIGOS ATIVOS:")
        ativos = sorted([a for a in abrigos if a['ativo']], key=lambda x: (x['distancia_km'], x['ocupacao']))
        for abrigo in ativos:
            print(f"- {abrigo['nome']} (Distância: {abrigo['distancia_km']}km, Ocupação: {abrigo['ocupacao']}%)")
    except Exception as e:
        print(f"Erro ao exibir abrigos: {e}")

def mostrarAlertas():
    try:
        print("\nALERTAS ATIVOS:")
        for alerta in alertas:
            print(f"- {alerta['mensagem']} ({alerta['tipo']})")
    except Exception as e:
        print(f"Erro ao exibir alertas: {e}")

def mostrarDicas():
    try:
        dicas = [
            "Mantenha documentos importantes em sacos plásticos.",
            "Evite andar em áreas alagadas.",
            "Desligue a energia ao perceber risco de inundação.",
            "Prepare um kit de emergência com água, alimentos e medicamentos."
        ]
        print("\nDICAS DE SEGURANÇA:")
        for dica in dicas:
            print(f"- {dica}")
    except Exception as e:
        print(f"Erro ao exibir dicas: {e}")

def encontrarMelhorAbrigo():
    try:
        ativos = [a for a in abrigos if a['ativo']]
        if not ativos:
            print("\nNenhum abrigo disponível no momento.")
            return
        abrigo = min(ativos, key=lambda x: x['distancia_km'] + (x['ocupacao'] / 100.0))
        rota = next((r for r in rotas if r['status'] == 'segura'), None)
        print("\nABRIGO MAIS PRÓXIMO COM ROTA SEGURA:")
        print(f"Abrigo: {abrigo['nome']} (Distância: {abrigo['distancia_km']}km)")
        if rota:
            print(f"Rota Sugerida: {rota['nome']}")
        else:
            print("Nenhuma rota segura disponível no momento.")
    except Exception as e:
        print(f"Erro ao encontrar abrigo: {e}")

# Menu_______________________________________________________________________________
while True:
    try:
        print("\n=== SAFE FLOW ===")
        print("1. Ver rotas")
        print("2. Ver abrigos")
        print("3. Ver alertas")
        print("4. Ver dicas de segurança")
        print("5. Procurar abrigo mais próximo")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            mostrarRotas()
        elif opcao == '2':
            mostrarAbrigos()
        elif opcao == '3':
            mostrarAlertas()
        elif opcao == '4':
            mostrarDicas()
        elif opcao == '5':
            encontrarMelhorAbrigo()
        elif opcao == '0':
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except Exception as e:
        print(f"Erro ao processar a opção: {e}")
