import streamlit as st
import gspread
import json

# 為了確保讀取正確，我們直接檢查 st.secrets 的內容
# 如果您在網頁版設定的是 GCP_JSON，程式碼如下：
if "GCP_JSON" in st.secrets:
    json_str = st.secrets["GCP_JSON"]
    creds_dict = json.loads(json_str)
    gc = gspread.service_account_from_dict(creds_dict)
    sh = gc.open('工程科排隊系統').sheet1
else:
    st.error("找不到 GCP_JSON 設定！請檢查 Streamlit Cloud 的 Secrets 設定。")
    st.stop()
