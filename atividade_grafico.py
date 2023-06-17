import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

caminho_arquivo = "A:/Curso/Módulo_18/Atividade/gasolina.csv"
df = pd.read_csv(caminho_arquivo)
df.head()

sns.lineplot(x="dia", y="venda", data=df)

plt.savefig("A:/Curso/Módulo_18/Atividade/grafico.png")