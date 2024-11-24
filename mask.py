import cv2
import numpy as np

# 이미지 크기에 맞는 빈 마스크 생성
image = cv2.imread('image_folder/face.png')
mask = np.zeros(image.shape[:2], dtype=np.uint8)

# 특정 영역 (x, y, width, height)에 흰색 마스크 설정
x, y, width, height = 470, 20, 200, 220
mask[y:y+height, x:x+width] = 255

# 마스크 저장
cv2.imwrite('mask_folder/face.png', mask)