import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img_resized = cv2.imread('../Resources/qrcode_chrome.png')
cap = cv2.VideoCapture(1)

while True:
    _, img = cap.read()
    for barcode in decode(img):
        # print(barcode.data)
        myData = barcode.data.decode('utf-8')
        # print(myData)
        pts = np.array([barcode.polygon], np.int32)
        print(pts)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, pts, True, (255, 0, 255), 5)
        # data = myData
        # cv2.putText(img_resized, data, (pts[0], pts[1]), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 2)

    cv2.imshow("qr_code_scanner", img)
    if cv2.waitKey(1) == 27:
        break

