import cv2


imagem = cv2.imread('image.jpg')

print(imagem)
print(imagem.shape)

cv2.imshow('image',imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()