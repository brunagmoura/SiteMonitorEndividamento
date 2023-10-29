import streamlit as st

st.title(":bar_chart: Monitor do endividamento dos brasileiros")

# Conteúdos da página
st.markdown("""
<div style='text-align: left; color: #555555; font-size: 1em; margin-bottom: 20px;'>
    Sobre o monitor
</div>
""", unsafe_allow_html=True)

st.write("sobre")

st.markdown("""
<div style='text-align: left; color: #555555; font-size: 1em; margin-bottom: 20px;'>
    Dados e atualização
</div>
""", unsafe_allow_html=True)

st.write("sobre os dados e atualização")

st.markdown("""
<div style='text-align: left; color: #555555; font-size: 1em; margin-bottom: 20px;'>
    Bibliotecas utilizadas
</div>
""", unsafe_allow_html=True)

st.write("bibliotecas utilizadas")

st.markdown("""
<div style='text-align: left; color: #555555; font-size: 1em; margin-bottom: 20px;'>
    Termos mais utilizados
</div>
""", unsafe_allow_html=True)
st.write("dicionário termos")

st.markdown("""
<div style='text-align: left; color: #555555; font-size: 1em; margin-bottom: 20px;'>
    Entre em contato conosco
</div>
""", unsafe_allow_html=True)

st.write("texto texto texto texto texto")

# Input para propostas de melhorias
with st.expander("Enviar Proposta de Melhoria"):
    proposta = st.text_area("Digite sua proposta aqui:")
    if st.button("Enviar Proposta"):
        st.success("Proposta enviada com sucesso!")
