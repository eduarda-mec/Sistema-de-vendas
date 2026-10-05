import streamlit as st
import pandas as pd 
import plotly.express as px

# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas") #uma hashtag deixa o texo grande, duas deixa o texto pequeno

# secao de cadrastro de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("produto", ["Notebook", "celular", "Fone"])
quantidade =  st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar venda")

#logica de cadrasto
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda cadastrada.")

# secao de vendas cadastradas
st.write("## Vendas cadastradas")
st.dataframe(tabela_vendas)

# secao de dashboard
st.write("## Dashboard")

# card/metrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R$ {faturamento}")

# grafico de barra/coluna -> Venda Por Vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# grafico de pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)
