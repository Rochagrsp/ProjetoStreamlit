import streamlit as st
import random 

#sidebar
st.sidebar.title("Menu")

pagina = st.sidebar.selectbox(
    "Escolha uma página",
    ["Home","Gráfico"]
)

#para rodar no terminal coloque "python -m streamlit run index.py" ou "run streamlit index.py"

#home
if pagina == "Home":
    st.title("Página home")

    st.write('Sistema usando o Streamlit')
    
    #input
    nome=st.text_input("Digite seu nome:")

    #selectbox
    curso=st.selectbox(
        "Escolha um curso:",
        ["Python",'JS',"Banco de dados"]
                )
    #Slider
    idade= st.slider(
        "Escolha a sua Idade:",
        16,
        80,
        16
    )
    #checkbox
    mostrar=st.checkbox("Mostrar Mensagem")
    if mostrar:
        st.success("Checkbox marcado")
    #botão
    if st.button("Enviar"):
        st.write (f"Nome :{nome}")
        st.write (f"Curso :{curso}")
        st.write (f"Idade:{idade}")
    #subtitulo
    st.subheader("Colunas")
    col1,col2,col3= st.columns(3)
    with col1:
        st.info("Informações coluna 1")
    with col2:
        st.warning("Informações coluna 2 ")
    with col3:
        st.success("Infomações coluna 3")
elif pagina=='Gráfico':
    st.title("Página de gráfico")
    valores=[]
    for i in range (5):
        valores.append(random.randint(1,100))
    st.bar_chart(valores)


    