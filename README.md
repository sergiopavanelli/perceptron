# Projeto: Modelos de Perceptron para Decisões Simples

Este repositório contém três exemplos de uso do modelo `Perceptron` da biblioteca `scikit-learn` para tomar decisões simples com base em dados de entrada. Cada exemplo aborda um cenário diferente, demonstrando como o Perceptron pode ser aplicado para resolver problemas de classificação binária.

## Tarefas Realizadas

### 1. Previsão de Levar Guarda-Chuva

Neste exemplo, o Perceptron é treinado para decidir se é necessário levar um guarda-chuva com base em duas entradas:
- **Nuvens**: 0 (sem nuvens) ou 1 (com nuvens).
- **Previsão de Chuva**: 0 (não chove) ou 1 (chove).

O modelo é treinado com os seguintes dados:

```python
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0, 1, 1, 1]  # 0 = Não levar, 1 = Levar
Após o treinamento, o modelo é testado com todas as combinações possíveis de entradas para prever se é necessário levar o guarda-chuva.

### 2. Decisão de Ir ao Parque
Neste cenário, o Perceptron decide se é uma boa ideia ir ao parque com base em três fatores:

Tempo Ensolarado: 0 (não) ou 1 (sim).

Final de Semana: 0 (não) ou 1 (sim).

Parque Lotado: 0 (não) ou 1 (sim).

Os dados de treinamento são:

```python

X = [
    [0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0],
    [0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]
]
Y = [0, 1, 1, 1, 0, 0, 0, 0]  # 0 = Não ir, 1 = Ir
O modelo é testado com todas as combinações possíveis para decidir se é recomendável ir ao parque.

### 3. Decisão sobre Comer Fora ou Cozinhar em Casa
Neste exemplo, o Perceptron ajuda a decidir se é melhor comer fora ou cozinhar em casa com base em quatro fatores:

Cansado: 0 (não) ou 1 (sim).

Ingredientes em Casa: 0 (não) ou 1 (sim).

Restaurante Aberto: 0 (não) ou 1 (sim).

Pagamento Recente: 0 (não) ou 1 (sim).

Os dados de treinamento são:

```python

X = [
    [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [0, 0, 1, 0],
    [1, 1, 1, 1], [0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1]
]
Y = [0, 1, 0, 1, 1, 0, 0, 0]  # 0 = Cozinhar em casa, 1 = Comer fora
O modelo é testado com todas as combinações possíveis para decidir se é melhor comer fora ou cozinhar em casa.

## Como Executar o Código
Instale as dependências:
Certifique-se de ter o Python instalado e instale a biblioteca scikit-learn com o comando:


pip install scikit-learn
Execute o script:
Salve o código em um arquivo Python (por exemplo, perceptron_examples.py) e execute-o:

python perceptron_examples.py
Analise os resultados:
O script imprimirá as previsões para cada um dos três cenários, mostrando como o Perceptron toma decisões com base nos dados fornecidos.

### Conclusão
Este projeto demonstra a aplicação do Perceptron em três cenários diferentes, mostrando como modelos simples de aprendizado de máquina podem ser usados para tomar decisões binárias com base em dados de entrada. Cada exemplo ilustra a flexibilidade e a utilidade do Perceptron em problemas de classificação.
