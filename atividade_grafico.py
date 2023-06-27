import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

caminho_arquivo = "A:/Curso/Módulo_18/Atividade/gasolina.csv"
df = pd.read_csv(caminho_arquivo)
df.head()

plt.style.use("ggplot")
plt.figure(figsize=(15,5))
sns.lineplot(data=df, x="dia", y="venda")
plt.title("Histórico de vendas", fontweight="bold")
plt.xlabel("Dia da venda!")
plt.ylabel("Valor vendido!")

plt.savefig("A:/Curso/Módulo_18/Atividade/grafico.png")