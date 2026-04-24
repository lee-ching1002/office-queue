import streamlit as st
import gspread
import json

# 直接讀取 Secrets
json_str = st.secrets["GCP_JSON"]

# 這一行是關鍵，有些時候金鑰被多加了引號，這裡我們進行清理
if json_str.startswith("'") and json_str.endswith("'"):
    json_str = json_str[1:-1]
elif json_str.startswith('"') and json_str.endswith('"'):
    json_str = json_str[1:-1]

creds_dict = json.loads(json_str)
gc = gspread.service_account_from_dict(creds_dict)
sh = gc.open('工程科排隊系統').sheet1
