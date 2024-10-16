import streamlit as st

from db.postgres import get_orientadores

import pandas as pd


def get_authenticated_page():
    if not st.session_state["orientadores_received"]:
        st.session_state["orientadores_received"] = None
        orientadores = get_orientadores()
        if orientadores is not None:
            st.session_state["orientadores_received"] = orientadores

    # Show app title and description.
    st.set_page_config(page_title="Orientadores da PPGE", page_icon="🤓")
    st.title("🤓 Orientadores")
    st.write(
        """
        Nesta aplicação podemos editar algumas informações do banco interno de orientadores
        """
    )

    # Create a random Pandas dataframe with existing tickets.
    if "df" not in st.session_state:

        # Generate the dataframe with 100 rows/tickets.
        data = st.session_state["orientadores_received"]
        df = pd.DataFrame(data)

        # Save the dataframe in session state (a dictionary-like object that persists across
        # page runs). This ensures our data is persisted when the app updates.
        st.session_state.df = df

    # Show section to view and edit existing tickets in a table.
    st.header("Orientadores cadastrados")
    st.write(f"#: `{len(st.session_state.df)}`")
    st.info("É possível fazer a alteração dos dados diretamente na tabela. ", icon="✍️")

    # Show the tickets dataframe with `st.data_editor`. This lets the user edit the table
    # cells. The edited data is returned as a new dataframe.
    edited_df = st.data_editor(
        st.session_state.df,
        use_container_width=False,
        hide_index=True,
        key="data_editor",
        # Disable editing the ID and Date Submitted columns.
        disabled=["ID", "Date Submitted"],
        width=2000,
    )
