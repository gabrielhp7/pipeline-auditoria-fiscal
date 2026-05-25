from flask import Flask, jsonify

app = Flask(__name__)

# Simulação de um banco de dados interno da contabilidade (Ex: Domínio/Gestta)
banco_dados_fiscal = [
    {"id": 1, "cliente": "Madeireira Silva", "cnpj": "12.345.678/0001-99", "faturamento": 185000.00, "status_documentos": "Completo"},
    {"id": 2, "cliente": "Mercado Central", "cnpj": "98.765.432/0001-11", "faturamento": 92000.00, "status_documentos": "Pendente"},
    {"id": 3, "cliente": "Oficina Jaguariaíva", "cnpj": "55.666.777/0001-22", "faturamento": 28000.00, "status_documentos": "Completo"},
    {"id": 4, "cliente": "Logística Vale", "cnpj": "44.333.222/0001-88", "faturamento": 240000.00, "status_documentos": "Pendente"}
]

# O "Porquê": Criar uma rota API REST (Mapeamento de End-point)
# Quando o n8n chamar essa URL, ele receberá o JSON bruto dos clientes
@app.route('/api/v1/fiscal', methods=['GET'])
def obter_dados_fiscais():
    return jsonify(banco_dados_fiscal)

if __name__ == '__main__':
    # Roda o servidor localmente na porta 5000
    app.run(debug=True, port=5000)