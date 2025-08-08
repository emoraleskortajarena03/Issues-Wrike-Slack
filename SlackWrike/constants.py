import pandas as pd
import os
import certifi


# Archivo de certificacion, en producción cuando se sube a la nube cambiarlo por el comentario
SSL = certifi.where()#"./cert_Salto_SSL.cer"


# Constantes de Slack
ACCESS_TOKEN_SLACK = "xoxb-9003719705777-9303145886055-aJSG4VGdCzqTwTfJ9KP7zl7K"

BASE_URL_SLACK = "https://slack.com/api/"
HEADERS_SLACK = {
    "Authorization": f"Bearer {ACCESS_TOKEN_SLACK}",
    "Content-Type": "application/json"
}


#Constantes de Wrike
url_claud = 'https://saltogroup-my.sharepoint.com/personal/e_morales_saltosystems_com/_layouts/15/download.aspx?share=EQBhZwyyAsdBrteCfKMRFEUB9ag9w7Fokxm3HTjmFEu57w'
# Leer token desde Excel
df = pd.read_excel(
    url_claud,
    sheet_name='Sheet1'
)

ACCESS_TOKEN_WRIKE = df.loc[0, 'access_token']

BASE_URL_WRIKE = "https://app-eu.wrike.com/api/v4"
HEADERS_WRIKE = {
    "Authorization": f"Bearer {ACCESS_TOKEN_WRIKE}",
    "Content-Type": "application/json"
}