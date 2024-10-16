import psycopg2
import streamlit as st
import json


# Function to connect to the database
def get_connection():
    conn = psycopg2.connect(
        host=st.secrets["DB_HOST"],
        database=st.secrets["DB_NAME"],
        user=st.secrets["DB_USER"],
        password=st.secrets["DB_PASSWORD"],
        port=st.secrets["DB_PORT"],
    )
    return conn


def get_orientadores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "select id,numero_usp,nome,tipo,categoria,data_inicial_credenciamento,data_final_credenciamento,email, ativo from orientadores order by  ativo desc , nome"
    )
    orientadores = cursor.fetchall()
    cursor.close()
    conn.close()
    r = None
    resposta = []
    for o in orientadores:
        r = dict()
        r["id"] = o[0]
        r["numero_usp"] = o[1]
        r["nome"] = o[2]
        r["tipo"] = o[3]
        r["categoria"] = o[4]
        r["data_inicial_credenciamento"] = o[5]
        r["data_final_credenciamento"] = o[6]
        r["email"] = o[7]
        r["ativo"] = o[8]
        resposta.append(r)
    return resposta
