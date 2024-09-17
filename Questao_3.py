import json

def carregar_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        dados = json.load(f)
    faturamento_diario = [dia['valor'] for dia in dados]
    return faturamento_diario

def calcular_faturamento(faturamento_diario):
    faturamento_valido = [f for f in faturamento_diario if f > 0]

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    dias_acima_da_media = len([f for f in faturamento_valido if f > media_mensal])

    return menor_faturamento, maior_faturamento, dias_acima_da_media

caminho_arquivo = r"C:\Users\Gabriel\Desktop\Dados\dados.json" #Mudar local do arquivo

faturamento_diario = carregar_json(caminho_arquivo)

menor_faturamento, maior_faturamento, dias_acima_da_media = calcular_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
