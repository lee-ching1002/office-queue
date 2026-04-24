import streamlit as st
import gspread
import json

# 直接讀取
json_str = st.secrets["GCP_JSON"]
creds_dict = json.loads(json_str.encode('utf-8').decode('unicode_escape'))
gc = gspread.service_account_from_dict(creds_dict)
sh = gc.open('工程科排隊系統').sheet1
