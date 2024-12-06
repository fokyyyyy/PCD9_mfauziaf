import imageio.v3 as i
import matplotlib.pyplot as plt
import numpy as np

img = i.imread("C:\\Users\\KOPUTER JARKOM 19\\Downloads\\zee.jpg", mode ='F')

sobelX =np.array([
    [-1,0,1],
    [-2,0,2],
    [-1,0,1]
])

sobelY = np.array([
    [-1,-2,-1],
    [0,0,0],
    [1,2,1]
])

imgpad = np.pad(img,pad_width=1,mode='constant', constant_values=0)
Gx = np.zeros_like(img)
Gy = np.zeros_like(img)

for y in range(1, imgpad.shape[0]-1):
    for x in range(1, imgpad.shape[1]-1):
        area = imgpad[y-1:y+2,x-1:x+2]
        Gx[y-1,x-1] = np.sum(area * sobelX)
        Gy[y-1,x-1] = np.sum(area * sobelY)

G = np.sqrt(Gx**2 + Gy**2)
G = (G/G.max())*255
G = np.clip(G,0,255)
G = G.astype(np.uint8)

plt.figure(figsize=(10,10))

plt.subplot(2,2,1)
plt.imshow(img)

plt.subplot(2,2,2)
plt.imshow(Gx, cmap='gray')

plt.subplot(2,2,3)
plt.imshow(Gy, cmap='gray')

plt.subplot(2,2,4)
plt.imshow(G, cmap='gray')

plt.show()