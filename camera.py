import cv2
import os

# VideoCapture オブジェクトを取得します
capture = cv2.VideoCapture(1)

while(True):
    ret, frame = capture.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

# # カメラが認識されているかのチェック
# for i1 in range(0, 20): 
#     cap1 = cv2.VideoCapture( i1, cv2.CAP_DSHOW )
#     if cap1.isOpened(): 
#         print("VideoCapture(", i1, ") : Found")
#     else:
#         print("VideoCapture(", i1, ") : None")
#     cap1.release() 