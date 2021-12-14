import cv2
import os
import requests

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(1)

fps = int(capture.get(cv2.CAP_PROP_FPS))# カメラのFPSを取得
w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
video = cv2.VideoWriter('video.mp4', fourcc, fps, (w, h))

while(True):
    ret, frame = capture.read()
    # resize the window
    windowsize = (800, 600)
    frame = cv2.resize(frame, windowsize)

    ret, frame = capture.read()# フレームを取得
    cv2.imshow('capture', frame)# フレームを画面に表示
    video.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # cv2.imshow('title',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

    # if key == ord('c'):
    #     cv2.imwrite('{}_{}.{}'.format(img, n, ext), frame)
    #     n += 1
    # elif key == ord('q'):
    #     break

# cv.imwrite('test.tif' , image_array)

# videoopen = 'video.mp4'
# url = "https://notify-api.line.me/api/notify"
# access_token = '2D9XDGEZwLDpE2koEpyWXUMRDc1vjMGM647PUlCc0uR'
# headers = {'Authorization': 'Bearer ' + access_token}
# files = {'imageFile': open(videoopen, 'rb')}

message = '送信中'
payload = {files} 
payload = {'message':':' + message} 
r = requests.post(url, headers = headers , files = files)

capture.release()
cv2.destroyAllWindows()
