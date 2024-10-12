import matplotlib.pyplot as plt
import cv2
# ================================================================================================================
# openCV + plt
# ================================================================================================================
def show_img(img, width=10, length=8):
    # Convertir de BGR a RGB para que matplotlib lo muestre correctamente
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(width,length)) 
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def show_imgs(imgs, width=10, length=8):

    img1 = cv2.cvtColor(imgs[0], cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(imgs[1], cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(width, length))
    plt.subplot(1, 2, 1)
    plt.imshow(img1)
    plt.title('Image 1')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(img2)
    plt.title('Image 2')
    plt.axis('off')

    plt.show()

def show_3_imgs(img1, name1, img2, name2, img3, name3, width=10, length=8):

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(width, length))
    plt.subplot(1, 3, 1)
    plt.imshow(img1)
    plt.title(name1)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(img2)
    plt.title(name2)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(img3)
    plt.title(name3)
    plt.axis('off')

    plt.show()
