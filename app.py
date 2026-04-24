import streamlit as st
import gspread
import os

# 獲取 app.py 所在的資料夾路徑
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, 'service-account.json')

# 使用完整路徑讀取
gc = gspread.service_account(filename=json_path)
sh = gc.open('工程科排隊系統').sheet1
