import streamlit as st
import gspread

# 1. 直接定義權限字典 (這已經避開了所有格式轉譯問題)
creds_dict = {
    "type": "service_account",
    "project_id": "officequeuesystem-494313",
    "private_key_id": "7a146a8cdc169c92fd11b0b102f7b897544f662c",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDKk9bcM4YMYK6v\nnajsySGvMDuaTU1kmESzLn6XqtskZnRspDpPUVmmqsqgjkVNMJBAktrOza2n55KY\nnPz09lseVFPxm8tuwOxWav5WKPYgWRYPIhI8Jn+o4SCD9yAESD3BIO/melSKLYRq\nnNscq/0t4C1XDRx8Rrvnd71HUENkeZ2SIDJROnbXtgVWwbrPrijTA8NBKwz+ozQ\nnlmyCxnzyO2fdvFKAMsi8hvEq1sMFlx55YxyU967j8zUHOSCnZ8CX8Pr6BhIwFoEf\nnXzesk3RrqjzyC9fc1yR4GPMkqMU2RSuvaeb0IRVIOJry4yuArjRWBCjB/N3/M/qg\nnnOwESvKgDAgMBAAECggEAUTCKWB9TynofyzmKtctJ7UJSbmIig2j1USDpHoheuXW\nnN2JfZWHkK3Up1YUwCUZeGbfYGNFONcev8DXEkbN19RpVET/W48sIqpMOgCQGcj1QW\nnNXpUzVqFcHlfxUKq7QI6BXYS0Wlmbpj7bbxskloOmzexBfwK2BWU5OohJpgA1tN\nnNfkpRZTWdKK+lqebWYXYGafxPL50PhOGmfrkPJ+uCQhwtX5sfnJ4AYUH7Lw5Dao17\nnnehRp3QbiLAUNqN/aEqk01PB06F+C/TxvkyNot07Ztc2L5b0h9sbEgp1lIQk9ZyY\nnNX4FSK0AkJgjB/BGi3DGHlIsRhdKZYYilnxBrrcbsQKBgQdxB94S61smytmyNYDy\nnhGngxqxgbAIEjkhugbiA8dQJ8EDJ1IoxgOxm1KwgAGXY62GZ171VqvQ3xHaN5g\nna8/uev8CGOkX4RSdUdP7nbUW2vBGMpSJofdWIgusgGm8NseDrmPeHYW7CgJYxmq\nncme1XMZJ3cpDBiqWhRDdXIYCmQKBgQdy+pXk8WpQPAxsg6qEKrs8F6HNIDs5g\nnzvvlKNpYAYJbhCrowv8AG2IMpFU30/MYJomqUWzav+2hmg9C3H93KZm/sYlaF31\nn7UHPAF/NnjB4LUlu1bcIfsRvRq4IEHtKxkYlfb07EkiCVxKLQRUJWcUdT750pkK\nu4x1P8h0+wKBgQcC8tBP7Y6ioVoBsXZYVapnEtz26bR3NlTfbrf3jICn+7N28\nNTWF3QV3ZHhf8TvLOC40173ULF/izRyWvKA1EfyQT5Dpm+bzACCm439DZjTCIEE7r\nNzmbN6h51FIxkZJBcgr/31xwVHKGOMKdfW/I9ALlaDVbNqTWZGHd1Hw+DiQKBgFTK\nniHyaIFX6WapjpBP8KZJBRzdcZ06XwXeE6TnfF5Tg0MyxWoZlcX6SJx7AaS1\n8mp7cw763xbBJKwZukV6s8gOONBigtTyI9byZ2AfZouHscoAzUrxSs0UsjznU2\nNjMycluat+OV/tIsLyUgAs=\n-----END PRIVATE KEY-----",
    "client_email": "queue-bot@officequeuesystem-494313.iam.gserviceaccount.com",
    "client_id": "103861113200576232454",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/queue-bot%40officequeuesystem-494313.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

# 2. 確保私鑰換行正確
creds_dict["private_key"] = creds_dict["private_key"].replace('\\n', '\n')

# 3. 建立連線
gc = gspread.service_account_from_dict(creds_dict)
sh = gc.open('工程科排隊系統').sheet1

# 4. 接下來是您的 UI 程式碼...
st.title("工程科諮詢預約系統")
# ... (您的其他顯示程式碼)
