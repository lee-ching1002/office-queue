import streamlit as st
import gspread

# 1. 權限設定 (確保格式無誤)
creds_dict = {
    "type": "service_account",
    "project_id": "officequeuesystem-494313",
    "private_key_id": "7a146a8cdc169c92fd11b0b102f7b897544f662c",
    "private_key": "-----BEGIN PRIVATE KEY-----\n" +
                   "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDKk9bcM4YMYK6v\n" +
                   "najsySGvMDuaTU1kmESzLn6XqtskZnRspDpPUVmmqsqgjkVNMJBAktrOza2n55KY\n" +
                   "nPz09lseVFPxm8tuwOxWav5WKPYgWRYPIhI8Jn+o4SCD9yAESD3BIO/melSKLYRq\n" +
                   "nNscq/0t4C1XDRx8Rrvnd71HUENkeZ2SIDJROnbXtgVWwbrPrijTA8NBKwz+ozQ\n" +
                   "nlmyCxnzyO2fdvFKAMsi8hvEq1sMFlx55YxyU967j8zUHOSCnZ8CX8Pr6BhIwFoEf\n" +
                   "nXzesk3RrqjzyC9fc1yR4GPMkqMU2RSuvaeb0IRVIOJry4yuArjRWBCjB/N3/M/qg\n" +
                   "nOwESvKgDAgMBAAECggEAUTCKWB9TynofyzmKtctJ7UJSbmIig2j1USDpHoheuXW\n" +
                   "N2JfZWHkK3Up1YUwCUZeGbfYGNFONcev8DXEkbN19RpVET/W48sIqpMOgCQGcj1QW\n" +
                   "NXpUzVqFcHlfxUKq7QI6BXYS0Wlmbpj7bbxskloOmzexBfwK2BWU5OohJpgA1tN\n" +
                   "NfkpRZTWdKK+lqebWYXYGafxPL50PhOGmfrkPJ+uCQhwtX5sfnJ4AYUH7Lw5Dao17\n" +
                   "nehRp3QbiLAUNqN/aEqk01PB06F+C/TxvkyNot07Ztc2L5b0h9sbEgp1lIQk9ZyY\n" +
                   "NX4FSK0AkJgjB/BGi3DGHlIsRhdKZYYilnxBrrcbsQKBgQdxB94S61smytmyNYDy\n" +
                   "hGngxqxgbAIEjkhugbiA8dQJ8EDJ1IoxgOxm1KwgAGXY62GZ171VqvQ3xHaN5g\n" +
                   "a8/uev8CGOkX4RSdUdP7nbUW2vBGMpSJofdWIgusgGm8NseDrmPeHYW7CgJYxmq\n" +
                   "cme1XMZJ3cpDBiqWhRDdXIYCmQKBgQdy+pXk8WpQPAxsg6qEKrs8F6HNIDs5g\n" +
                   "zvvlKNpYAYJbhCrowv8AG2IMpFU30/MYJomqUWzav+2hmg9C3H93KZm/sYlaF31\n" +
                   "7UHPAF/NnjB4LUlu1bcIfsRvRq4IEHtKxkYlfb07EkiCVxKLQRUJWcUdT750pkK\n" +
                   "4x1P8h0+wKBgQcC8tBP7Y6ioVoBsXZYVapnEtz26bR3NlTfbrf3jICn+7N28\n" +
                   "TWF3QV3ZHhf8TvLOC40173ULF/izRyWvKA1EfyQT5Dpm+bzACCm439DZjTCIEE7r\n" +
                   "zmbN6h51FIxkZJBcgr/31xwVHKGOMKdfW/I9ALlaDVbNqTWZGHd1Hw+DiQKBgFTK\n" +
                   "niHyaIFX6WapjpBP8KZJBRzdcZ06XwXeE6TnfF5Tg0MyxWoZlcX6SJx7AaS1\n" +
                   "8mp7cw763xbBJKwZukV6s8gOONBigtTyI9byZ2AfZouHscoAzUrxSs0UsjznU2\n" +
                   "NjMycluat+OV/tIsLyUgAs=\n" +
                   "-----END PRIVATE KEY-----",
    "client_email": "queue-bot@officequeuesystem-494313.iam.gserviceaccount.com",
    "client_id": "103861113200576232454",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/queue-bot%40officequeuesystem-494313.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# 2. 格式轉換
creds_dict["private_key"] = creds_dict["private_key"].replace('\\n', '\n')

# 3. 建立連線
gc = gspread.service_account_from_dict(creds_dict)
sh = gc.open('工程科排隊系統').sheet1

# 4. 系統介面
st.title("工程科諮詢預約系統")
st.write("連線已成功建立！")

# 獲取長官狀態
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
    st.write("這裡是長官管理後台內容...")
