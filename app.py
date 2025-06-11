import streamlit as st
import pandas as pd


if __name__ == "__main__":
    try:
        st.set_page_config(page_title="RACA_Joaíma_MG_2025",
                           page_icon="icon.ico", layout="wide", initial_sidebar_state='auto')
        hide_footer_style = '''
        <style>
        header {visibility: hidden;}
        '''
        st.markdown(hide_footer_style, unsafe_allow_html=True)

        hide_menu_style = '''
        <style>
        #MainMenu {visibility: hidden;}
        '''
        st.markdown(hide_menu_style, unsafe_allow_html=True)
        
        st.header("Levantamento da Rede de Atendimento da Criança e Adolescentes de Joaíma MG 2025")
            
        st.html('''<p> De acordo com a  Lei 8069/90   e Lei Municipal 1842 de 2 de junho de 2015 regulamenta a Política Municipal dos Direitos das Crianças e 
                    dos Adolescentes de Joaíma-MG. Com intuito de garantir fluxo de atendimento e mapeamento da rede de atendimento, solicitamos dos parceiros 
                    o preenchimento do formulário para registro da rede de atendimento das crianças e adolescentes do Município de Joaíma.</p>''')
        
        col1, col2, col3 = st.columns(3)
        col2.image("logo.jpg")


        with st.form("meu_questionario", clear_on_submit=True):
            
            st.subheader("1 - IDENTIFICAÇÃO DO RESPONSÁVEL PELO PREENCHIMENTO:")
            email_colaborador = st.text_input("E-mail")
            nome_colaborador = st.text_input("Nome pessoa responsável pelo Preenchimento")
            nome_instituicao = st.text_input("Nome da Instituição ou serviço?")
            orgao_vinculado = st.text_input("Órgão ao qual serviço/setor/ está vinculado (Exemplo Secretaria Municipal ou Estadual)")
            endereco_intitucional = st.text_input("Endereço Institucional (nome rua, número bairro, cep.:")
            telefone_intitucional = st.text_input("Telefone  Institucional")
            email_intitucional = st.text_input("E-mail  Institucional")
            responsavel_instituicao = st.text_input("Nome Responsável Legal pela Instituição /serviço (coordenador, diretor, secretário, presidente...)")
            telefone_responsavel = st.text_input("Telefone responsável legal pela Instituição/serviço")
            email_responsavel = st.text_input("E-mail responsável legal pela instituição /serviço")

            st.subheader("2 - CARACTERÍSTICAS DA INSTITUIÇÃO/SERVIÇOS")

            df_politicas_publicas_vinculadas = st.data_editor({
                "Política Pública ao qual a Instituição/ serviço está vinculado(a)": ["Assistência Social", 
                                                                                      "Educação", 
                                                                                      "Esporte", 
                                                                                      "Cultura e Lazer", 
                                                                                      "Saúde", 
                                                                                      ""],
                "Caixa de seleção": [False, False, False, False, False, False]},
                use_container_width=True
            )
            
            df_politicas_alvo_atendimento = st.data_editor({
                "Público Alvo de Atendimento": ["Adolescente", "Adulto", "Criança", "Criança e adolecentes", "Família", "Pessoa com Deficiência", ""],
                "Caixa de seleção": [False, False, False, False, False, False, False]},
                use_container_width=True
            )
            
            faixa_etaria_atendimento = st.multiselect(
                "Faixa Etária de Atendimento",
                ["0 a 4 anos", "0 a 6 anos", "0 a 12 anos", "0 a 18 anos", "5 a 12 anos", "12 a 18 anos", "14 a 18 anos", "18 a 24 anos", "acima de 24 anos"],
            )
            
            horario_funcionamento = st.text_input("Horário de Funcionamento")
            
            periodo_atendimento = st.selectbox(
                'Período de Atendimento?',
                ('Diário', 'Semanal', 'Quinzenal',
                 'Mensal', 'Bimestral', 'Anual')
            )

            st.subheader("3 - IDENTIFICANDO O PERFIL DOS ATENDIMENTOS DA INSTITUIÇÃO/SERVIÇO")
            
            n_pessoas_atendimento = st.multiselect(
                "Números de Pessoas Atendidas",
                ["Até 10 Pessoas", "Acima de 15 pessoas", "Acima de 25 pessoas", "Acima de 50 pessoas", "de 51 a 100 pessoas", "De 101 a 200 pessoas", "Acima de 200 pessoas"],
            )
            
            df_perfil_publico_atendimento = st.data_editor({
                "Perfil público atendido": ["Cadastrado Cadastro Único", "Demanda espontânea", "Renda", "Encaminhado pela rede de Atendimento", 
                "Já ser atendido pela instituição em outros serviços/programas e projetos", "Receber Bolsa Família", "Ser selecionado pela Instituição",
                "Violação de Direito", "Nenhuma das opções acima", "Todas as opções acima", ""],
                "Caixa de seleção": [False, False, False, False, False, False, False, False, False, False, False]},
                use_container_width=True
            )
            
            
            total_atendimento_2024 = st.text_input(
                "Total de Pessoas atendidas no Ano de 2024")
            
            total_atendimento_jan_maio_2025 = st.text_input(
                "Total de Pessoas atendidas de Janeiro a maio de  2025")

            st.subheader("4 - VIOLAÇÕES DE DIREITOS")
            
            df_tipo_violacao_direitos = st.data_editor({
                "Tipos de Violação de Direitos Identificados/atendidos pela instituição /serviços": ["Violência Sexual", "Exploração Sexual", "Violência Física", 
                "Violência Psicológia", 
                "Abandono", "Negligência ( privação de cuidados básicos como saúde, alimentação, higiene e proteção contra as inclemências do meio ambiente.)",
                "Trabalho Infantil", "Discriminação: atos de preconceitos baseados em raça, gênero, orientação sexual, religião...",
                "Nenhuma das opções acima", "Não  foram identificadas nenhuma violação de direito a criança e adolescentes nos anos de 2023 a 2025",""],
                "Caixa de seleção": [False, False, False, False, False, False, False, False, False, False, False]},
                use_container_width=True
            )
            
            df_violacao_direito_orgao_responsaveis = st.data_editor({
                "Se houve identificação de violação de direito, para qual órgão de garantia de direitos a demanda foi encaminhada?": ["Conselho Tutelar", 
                "CRAS", "Equipe de Proteção Social Especial", "Polícia Militar", 
                "Polícia Cívil", "Ministério Público", "Não realizemos nenhum encaminhamento da demanda", "Não sei informar", ""],
                "Caixa de seleção": [False, False, False, False, False, False, False, False, False]},
                use_container_width=True
            )
            
            instituicao_campanha_contra_violencia = st.multiselect(
                "A Instituição/serviço realiza campanha para enfrentamento da violência contra criança e adolescentes?",
                ["Sim, apenas nas 18 de maio: Dia Nacional de Combate ao Abuso e à Exploração Sexual )", 
                "Sim, 12 de junho: Dia Nacional de Combate ao Trabalho Infantil.", 
                "Sim, no mês de maio e junho",
                "Não realizamos ações preventivas nem campanhas",
                "Não sei informar"],
            )

            st.subheader("5 - SISTEMA DE GARANTIA DE DIREITOS")
            
            conhece_papel_conselho_tutelar = st.selectbox(
                'A Instituição/serviço conhece o papel do Conselho Tutelar',
                ('Sim', 'Não', 'Conheço mas tenho dúvidas a respeito da atuação',
                 'Não conheço, não sei as atribuições do Conselheiro tutelar')
            )
            
            df_instituicao_realizou_acao_coselho_tutelar = st.data_editor({
                "A Instituição / serviço já realizou ação conjunta com conselho Tutelar do Município?": ["Campanhas educativas, blitz, palestras, capacitações", 
                "Capacitação", 
                "Não realizamos ações conjuntas com conselho tutelar",
                ""],
                "Caixa de seleção": [False, False, False, False]},
                use_container_width=True
            )
            
            df_orgao_responsável_fiscalizar_política = st.data_editor({
                "Diante do conhecimento institucional , qual o órgão é responsável por fiscalizar e garantir o funcionamento da Política dos Direitos das Crianças e dos Adolescentes em Joaíma?": ["Conselho Municipal dos Direitos das Crianças e dos Adolescentes", 
                "Ministério Público", 
                "Prefeitura Municipal",
                "Secretaria Municipal de Assistência Social",
                ""],
                "Caixa de seleção": [False, False, False, False, False]},
                use_container_width=True
            )
            
            df_identifique_fragilidades = st.data_editor({
                "Identifique as fragilidades para que as crianças e adolescentes tenham seus direitos garantidos de acordo com Estatuto da Criança e do Adolescente - ECA":["Fragilidade na rede de atendimento em identificação e acompanhamento dos casos", 
                "Ausência de equipamentos para atendimento das crianças e adolescentes vítimas de violência", 
                "Ausência fluxo de atendimento onde estão definidos os papeis de cada serviço/setor do municípios para que os direitos sejam garantidos",
                "Não temos caso de violação de direito no Município",
                "Todos os casos são atendidos e os direitos das crianças e adolescentes são acompanhados",
                "Não existe atendimento a criança e adolescente no município",
                ""],
                "Caixa de seleção": [False, False, False, False, False, False, False]},
                use_container_width=True
            )
            
           
            submitted = st.form_submit_button("Salvar")
            if submitted:
                if 'data' not in st.session_state:
                    st.session_state.data = pd.DataFrame(columns=["email_colaborador",
                                                                "nome_colaborador",
                                                                "nome_instituicao",
                                                                "orgao_vinculado",
                                                                "endereco_intitucional",
                                                                "telefone_intitucional",
                                                                "email_intitucional",
                                                                "responsavel_instituicao",
                                                                "telefone_responsavel",
                                                                "email_responsavel",
                                                                "df_politicas_publicas_vinculadas",
                                                                "df_politicas_alvo_atendimento",
                                                                "faixa_etaria_atendimento",
                                                                "horario_funcionamento",
                                                                "periodo_atendimento",
                                                                "n_pessoas_atendimento",
                                                                "df_perfil_publico_atendimento",
                                                                "total_atendimento_2024",
                                                                "df_total_atendimento_jan_maio_2025",
                                                                "df_tipo_violacao_direitos",
                                                                "violacao_direito_orgao_responsaveis",
                                                                "instituicao_campanha_contra_violencia",
                                                                "conhece_papel_conselho_tutelar",
                                                                "df_instituicao_realizou_acao_coselho_tutelar",
                                                                "df_orgao_responsável_fiscalizar_política",
                                                                "df_identifique_fragilidades"
                                                                ])

                dados = {"email_colaborador": email_colaborador,
                        "nome_colaborador": nome_colaborador,
                        "nome_instituicao": nome_instituicao,
                        "orgao_vinculado": orgao_vinculado,
                        "endereco_intitucional": endereco_intitucional,
                        "telefone_intitucional": telefone_intitucional,
                        "email_intitucional": email_intitucional,
                        "responsavel_instituicao": responsavel_instituicao,
                        "telefone_responsavel": telefone_responsavel,
                        "email_responsavel": email_responsavel,
                        "df_politicas_publicas_vinculadas": str(df_politicas_publicas_vinculadas),
                        "df_politicas_alvo_atendimento": str(df_politicas_alvo_atendimento),
                        "faixa_etaria_atendimento": str(faixa_etaria_atendimento),
                        "horario_funcionamento": horario_funcionamento,
                        "periodo_atendimento": periodo_atendimento,
                        "n_pessoas_atendimento": str(n_pessoas_atendimento),
                        "df_perfil_publico_atendimento": str(df_perfil_publico_atendimento),
                        "total_atendimento_2024": total_atendimento_2024,
                        "total_atendimento_jan_maio_2025": total_atendimento_jan_maio_2025,
                        "df_tipo_violacao_direitos": str(df_tipo_violacao_direitos),
                        "df_violacao_direito_orgao_responsaveis": str(df_violacao_direito_orgao_responsaveis),
                        "instituicao_campanha_contra_violencia": str(instituicao_campanha_contra_violencia),
                        "conhece_papel_conselho_tutelar": conhece_papel_conselho_tutelar,
                        "instituicao_realizou_acao_coselho_tutelar": str(df_instituicao_realizou_acao_coselho_tutelar),
                        "orgao_responsável_fiscalizar_política": str(df_orgao_responsável_fiscalizar_política),
                        "identifique_fragilidades": str(df_identifique_fragilidades)
                        }

                df = pd.DataFrame(dados, index=[0])
                st.session_state.data = pd.concat(
                    [st.session_state.data, df], ignore_index=True)

                st.write("Gravado com sucesso!")

        st.write("Fim formulário!")

        st.write('## Tabela resultado: ')

        if 'data' in st.session_state:
            st.write(st.session_state.data)

        st.write("## Download")
        if 'data' in st.session_state:
            st.download_button(
                "📥 Download", st.session_state.data.to_csv(index=False), "dados_questionario.csv", mime="text/csv")

    except Exception as e:
        st.error(f'Erro: {e}')
