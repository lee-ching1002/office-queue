import streamlit as st
import gspread

# 直接讀取檔案，不要使用 dict，這是最穩定的連線方式
gc = gspread.service_account(filename='service-account.json')
sh = gc.open('工程科排隊系統').sheet1

st.title("工程科諮詢預約系統")
st.write("系統連線成功！")
