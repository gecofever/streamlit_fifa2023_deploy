import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("Projeto Streamlit FIFA/datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.markdown("# FIFA 2023 OFFICIAL DATASET!!")
st.sidebar.markdown("Desenvolvido por [Fusão de Dados](https://fusaodedados.com.br)")

btn = st.link_button("Acesse os dados no Kaggle", "https://www.kaggle.com/datasets/")

st.markdown(
    """
    FIFA 23 é um jogo eletrônico de simulação de futebol desenvolvido pela Electronic Arts.
    O jogo é o último a utilizar a marca FIFA no nome e foi lançado dia 27 de setembro de 2022, 
    para Xbox Series S/X, Xbox One, PlayStation 5, PlayStation 4,Microsoft Windows e Nintendo Switch, 
    com uma versão reduzida.

    O jogador Kylian Mbappé, do Paris Saint-Germain, e a jogadora Sam Kerr, do Chelsea, 
    serão os protagonistas. É a primeira vez que uma mulher aparece na capa global do jogo eletrônico.

    Modos de jogo
    FIFA 23 contará com diversos modos de jogo, são eles: Modo Carreira, Ultimate Team, 
    Pro Clubs e Volta Football. O jogo também será o primeiro da série a contar com a 
    tecnologia de crossplay no lançamento. Isto significa que jogadores de Xbox Series, 
    PlayStation e Microsoft Windows poderão competir entre si.
    """
)