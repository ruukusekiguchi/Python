# 2D9XDGEZwLDpE2koEpyWXUMRDc1vjMGM647PUlCc0uR
import requests

# LINEへ送る設定
url = "https://notify-api.line.me/api/notify"
access_token = '2D9XDGEZwLDpE2koEpyWXUMRDc1vjMGM647PUlCc0uR'
headers = {'Authorization': 'Bearer ' + access_token}

# for int i=0; i < 11;i += 1:と同じ意味
for i in range(1, 11):
    if i % 2 ==0: 
        # メッセージを送信内容
        message = '送信中'
        message2 = 'だお'
        payload = {'message': str(i) +':' + message + message2} 
        r = requests.post(url, headers=headers, params=payload,)