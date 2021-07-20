import cv2


imagem = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow("image",imagem)
cv2.imwrite("saida.jpg",imagem)
cv2.waitKey(0)

