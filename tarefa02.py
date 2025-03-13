# Importando biblioteca
from sklearn.linear_model import Perceptron

# --- Código 2: Decisão de ir ao parque ---
# Definindo os dados de entrada (Tempo ensolarado, Final de semana, Parque lotado)
X = [
    [0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0],
    [0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]
]

# Saídas desejadas (Ir ao parque? 0 = Não, 1 = Sim)
Y = [0, 1, 1, 1, 0, 0, 0, 0]

# Criando e treinando o modelo Perceptron
modelo_parque = Perceptron()
modelo_parque.fit(X, Y)

# Testando o modelo
print("\nPrevisões para decidir se vamos ao parque:")

testes = [
    [0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0],
    [0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]
]

for teste in testes:
    previsao = modelo_parque.predict([teste])
    print(
        f"Ensolarado: {teste[0]}, Final de semana: {teste[1]}, Parque lotado: {teste[2]} => Ir ao parque? {'Sim' if previsao[0] == 1 else 'Não'}"
    )
