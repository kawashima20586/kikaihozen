import streamlit as st
import gspread

from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'API.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

st.title('機械保全学科試験過去問')

nendo = st.sidebar.selectbox(
    '何年度の問題を実施しますか？',
    list(range(2014,2021)))

SP_SHEET_KEY = '11cJmn4lggpvbI3G4XfLLru8YJVjWINTIFAeyehjfYo0'

sh = gc.open_by_key(SP_SHEET_KEY)

if nendo < 2015:
    SP_SHEET = '2014'
elif nendo < 2016:
   SP_SHEET = '2015'
elif nendo < 2017:
   SP_SHEET = '2016'
elif nendo < 2018:
   SP_SHEET = '2017'
elif nendo < 2019:
   SP_SHEET = '2018'
elif nendo < 2020:
   SP_SHEET = '2019'   
elif nendo < 2021:
   SP_SHEET = '2020'
elif nendo < 2022:
   SP_SHEET = '2021'

worksheet = sh.worksheet(SP_SHEET)
data = worksheet.get_all_values()

st.write(nendo,'年度学科')

for j in range(50):
    st.write(data[j+1][0])
    st.write(data[j+1][1])
    st.write('■選択肢')
    for i in range(4):
        st.write(data[j+1][i+2])

    expander = st.expander('★回答')
    expander.write(data[j+1][6])
    expander.write(data[j+1][7])



#gspread==5.0.0
#gspread-dataframe==3.2.2