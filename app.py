import streamlit as st
import gspread
import json

# 設定頁面標題
st.set_page_config(page_title="工程科排隊系統", page_icon="👨‍💼")

# 讀取雲端金鑰 (之後我們會在網站設定裡放入這些資料)
creds_dict = json.loads(st.secrets["GCP_SERVICE_ACCOUNT"])
gc = gspread.service_account_from_dict(creds_dict)
sh = gc.open('工程科排隊系統').sheet1

st.title("👨‍💼 工程科諮詢預約系統")

# 讀取長官狀態 (D2 欄位)
boss_status = sh.acell('D2').value
st.subheader(f"長官目前狀態: :blue[{boss_status}]")

# 分頁顯示
tab1, tab2 = st.tabs(["同仁排隊區", "長官管理後台"])

with tab1:
    name = st.text_input("請輸入您的姓名")
    if st.button("加入排隊"):
        if name:
            sh.append_row([name, "等待中", ""])
            st.success(f"{name} 已成功加入排隊！")
        else:
            st.warning("請輸入姓名")

with tab2:
    st.subheader("長官狀態管理")
    new_status = st.radio("更新長官狀態", ["在辦公室", "外出中", "會議中"])
    if st.button("更新狀態"):
        sh.update_acell('D2', new_status)
        st.rerun()

    st.subheader("目前排隊名單")
    data = sh.get_all_values()
    st.table(data[1:]) # 顯示所有資料