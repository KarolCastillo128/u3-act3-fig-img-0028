import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# Karol Castillo NC 0028
print("Karol Castillo")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_iagen = cv2.imread('Duki.jpg')
plt.imshow(mi_iagen)
plt.title('Duki y Karol Castillo 0028')
plt.show()
print("+-+-+- puntos sobre la imagen +-+-+-+")
plt.imshow(mi_iagen)
x = [100,100,300,250]
y = [100,400,500,200]
plt.scatter(x, y, s=20,c='red')
plt.show()
