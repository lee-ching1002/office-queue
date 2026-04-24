import streamlit as st
import gspread
import json

# 直接從 secrets 讀取並轉換成字典
json_str = st.secrets["GCP_JSON"]
creds_dict = json.loads(json_str)

# 建立連線
gc = gspread.service_account_from_dict(creds_dict)
sh = gc.open('工程科排隊系統').sheet1
