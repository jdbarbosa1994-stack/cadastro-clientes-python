import streamlit as st

st.title("Cadastro de Clientes")

nome = st.text_input("Cliente")
endereco = st.text_input("Endereço")
telefone = st.text_input("Telefone")
email = st.text_input("email")
dt_nasc = st.date_input("Data de nasc")
tipo_cliente = st.selectbox("Tipo de cliente", ["Pessoa fisica", "Pessoa juridica"])

cadastrar = st.button("Cadastrar Cliente")

if cadastrar:
    with open("Clientes.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome}, {endereco}, {dt_nasc}, {tipo_cliente}, {telefone}, {email}\n")
        st.success("Cliente cadastrado com sucesso!!!")

   