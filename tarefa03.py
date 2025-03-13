# Importando biblioteca
from sklearn.linear_model import Perceptron

# --- Código 3: Decisão sobre Comer Fora ou Cozinhar em Casa ---
# Definindo os dados de entrada (Cansado, Ingredientes em casa, Restaurante aberto, Pagamento recente)
X = [
    [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [0, 0, 1, 0],
    [1, 1, 1, 1], [0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1]
]

# Saídas desejadas (Comer fora? 0 = Não, 1 = Sim)
Y = [0, 1, 0, 1, 1, 0, 0, 0]

# Criando e treinando o modelo Perceptron
modelo_comer_fora = Perceptron()
modelo_comer_fora.fit(X, Y)

# Testando o modelo
print("Previsões para decidir se vai comer fora ou cozinhar em casa:")

testes = [
    [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [0, 0, 1, 0],
    [1, 1, 1, 1], [0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1]
]

for teste in testes:
    previsao = modelo_comer_fora.predict([teste])
    print(
        f"Cansado: {teste[0]}, Ingredientes em casa: {teste[1]}, Restaurante aberto: {teste[2]}, Pagamento recente: {teste[3]} => Comer fora? {'Sim' if previsao[0] == 1 else 'Não'}"
    )
