from db.postgres import get_orientadores
from ui.login import login
from ui.authenticated import get_authenticated_page

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if "orientadores_received" not in st.session_state:
    st.session_state["orientadores_received"] = None


if st.session_state["authenticated"]:
    get_authenticated_page()
else:
    login()
