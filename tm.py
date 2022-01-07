import cv2
import mss
import numpy as np

target = cv2.imread('connect_wallet.png')
h, w, _ = target.shape

with mss.mss() as sct:
    monitor = {
        'left': 0, # x1
        'top': 0, # y1
        'width': 1024,
        'height': 1024,
        'mon': 0
    }

    img = np.array(sct.grab(monitor))
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR) # 4ch -> 3ch

res = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

print(min_val, max_val)
# -0.43574756383895874 0.44410526752471924 # wrong
# -0.522121012210846 0.9999995827674866 # got it!

if max_val > 0.8:
    cv2.rectangle(img, pt1=top_left, pt2=bottom_right, color=(0, 0, 255), thickness=3)

cv2.imshow('img', img)
cv2.imshow('res', res)
cv2.waitKey(0)