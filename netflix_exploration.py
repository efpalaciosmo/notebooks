import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium", sql_output="pandas")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    return pd, plt


@app.cell
def _(pd):
    df = pd.read_csv("./data/netflix_titles.csv")
    df.head()
    return (df,)


@app.cell
def _(df):
    df.info()
    return

@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df.isnull().sum()
    return


@app.cell
def _(df):
    df['director'] = df['director'].fillna('Unknown')
    df['cast'] = df['cast'].fillna('Unknown')
    df['country'] = df['country'].fillna('Unknown')
    df['rating'] = df['rating'].fillna('Not Rated')
    return


@app.cell
def _(df, plt):
    type_counts = df['type'].value_counts()
    plt.pie(type_counts,
            labels=type_counts.index,      # Etiquetas de las categorías
            autopct='%1.1f%%',             # Porcentajes en el gráfico
            startangle=90)                 # Rotación inicial

    plt.title('Distribución por Tipo')    # Título del gráfico
    plt.tight_layout()                     # Ajusta el espacio automáticamente
    plt.show()
    return (type_counts,)


@app.cell
def _(plt, type_counts):
    bar_labels = ['red', 'blue']
    bar_colors = ['tab:red', 'tab:blue']
    plt.figure(figsize=(8, 6))
    plt.bar(
        type_counts.index,
        type_counts.values,
        label=bar_labels,
        color=bar_colors
    )
    plt.xlabel("Tipo")  # Etiqueta del eje X
    plt.ylabel("Cantidad")  # Etiqueta del eje Y
    plt.title("Conteo por tipo")
    plt.xticks(rotation=45)  # Rota las etiquetas si son largas
    plt.tight_layout()
    plt.show()
    return


@app.cell
def _(df, plt):
    plt.figure(figsize=(12, 6))
    top_countries = df[df['country'] != "Unknown"]['country'].value_counts(10)
    plt.bar(
        top_countries.index,
        top_countries.values,

    )
    return


if __name__ == "__main__":
    app.run()
