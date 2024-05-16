import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_function(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Grafico della funzione quadratica')
    st.pyplot()

def main():
    st.title('Pagina Streamlit con Grafico Interattivo')

    st.write("""
    Questa pagina mostra un grafico interattivo di una funzione quadratica.
    Puoi modificare i parametri della funzione utilizzando i controlli qui sotto.
    """)

    a = st.slider('Coefficiente a', min_value=-10, max_value=10, value=1)
    b = st.slider('Coefficiente b', min_value=-10, max_value=10, value=0)
    c = st.slider('Coefficiente c', min_value=-10, max_value=10, value=0)

    plot_function(a, b, c)

if __name__ == '__main__':
    main()
