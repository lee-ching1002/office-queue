import streamlit as st
import gspread
import json

# 讀取 Secrets
json_str = st.secrets["GCP_JSON"]

# 這一行會確保 JSON 字串內的 \n 能被真正轉換成換行符號
creds_dict = json.loads(json_str.encode('utf-8').decode('unicode_escape'))

gc = gspread.service_account_from_dict(creds_dict)
sh = gc.open('工程科排隊系統').sheet1
