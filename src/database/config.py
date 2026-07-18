import streamlit as st
from supabase import create_client, Client

print("SUPABASE_URL:", st.secrets["SUPABASE_URL"])
print("SUPABASE_KEY starts with:", st.secrets["SUPABASE_KEY"][:20])

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)