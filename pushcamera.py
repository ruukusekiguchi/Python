videoopen = './video.mp4'
url = "https://notify-api.line.me/api/notify"
access_token = '2D9XDGEZwLDpE2koEpyWXUMRDc1vjMGM647PUlCc0uR'
headers = {'Authorization': 'Bearer ' + access_token}

files = {'imageFile': open(videoopen, 'rb')}
message = '送信中'
payload = {'message':':' + message} 
r = requests.post(url, headers = headers, params = payload , files = files)
print(r.text)