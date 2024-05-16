import streamlit as st

def main():
    st.title("Pagina Semplice con Streamlit")
    
    st.write("""
    Benvenuto nella nostra pagina Streamlit! 
    Qui di seguito, troverai un testo e un'immagine.
    """)

    # Aggiungi un'immagine dalla directory locale
    st.image("image.jpg", caption="Immagine di esempio")

    st.write("""
    Grazie per aver visitato la nostra pagina. 
    Speriamo ti sia divertito!
    """)

if __name__ == "__main__":
    main()
