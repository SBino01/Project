import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    st.title("App Streamlit con Grafico Interattivo")

    # Carica dati di esempio
    df = sns.load_dataset('iris')

    # Opzioni per selezionare il tipo di grafico
    chart_type = st.sidebar.selectbox("Seleziona il tipo di grafico", 
                                      ["Grafico a barre", "Grafico a dispersione"])

    if chart_type == "Grafico a barre":
        # Calcola la media dei valori numerici per ogni specie
        avg_data = df.groupby('species').mean()

        # Visualizza il grafico a barre
        st.bar_chart(avg_data)

    elif chart_type == "Grafico a dispersione":
        # Seleziona due colonne per il grafico a dispersione
        x_col = st.sidebar.selectbox("Seleziona la colonna x", df.columns[:-1])
        y_col = st.sidebar.selectbox("Seleziona la colonna y", df.columns[:-1])

        # Visualizza il grafico a dispersione
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=df, x=x_col, y=y_col, hue='species')
        st.pyplot()

if __name__ == "__main__":
    main()
