import random, cv2, os, numpy as np, matplotlib.pyplot as plt


def copyToNew(newImg, img, xCoord, yCoord):

    width, height = img.shape[0], img.shape[1]
    pos_y, pos_x = yCoord, xCoord

    for i in range(len(img)):
        for j in range(len(img[i])):
            if 255 not in img[i,j]:
                newImg[pos_y+i, pos_x+j] = img[i, j]

    return newImg


def removeBG(root, filepath, iter):

    img = os.path.join(root, filepath)
    src = cv2.imread(img, 1)
    tmp1, tmp2, tmp3 = cv2.split(src)
    (thresh, alpha1) = cv2.threshold(tmp1, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    (thresh, alpha2) = cv2.threshold(tmp2, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    (thresh, alpha3) = cv2.threshold(tmp3, 120, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    rgba = [alpha1, alpha2, alpha3]
    dst = cv2.merge(rgba, 4)


    kernel = np.ones((2, 2), np.uint8)
    dst = cv2.erode(dst, kernel, iterations=iter)

    return dst


def zoom(img, new_height = 250):

    new_width = None

    ori_width, ori_height = img.shape[:2]

    new_width = (new_height*ori_width)//ori_width

    resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)

    return resized


def main():
    root = os.getcwd()
    os.chdir("C:/Users/ADITYA/Desktop/Form OCR/with_photos")
    filename = os.listdir(os.getcwd())
    os.chdir("C:/Users/ADITYA/Desktop/Form OCR/signatures")
    photos = os.listdir(os.getcwd())
    coord = {0: (450, 1232), 1: [(1142, 730),(60, 1710)], 2:[(500, 620), (60,920)], }
    count = 58 + 90 + 9 + 15 + 30 + 10
    print(len(photos))
    for i in range(180, 240, 3):
        # try:
        j = random.randrange(11)
        img = cv2.imread("C:/Users/ADITYA/Desktop/Form OCR/with_photos/" + filename[i])
        k = removeBG(os.getcwd(), photos[j], 0)
        k = zoom(k, 450)

        # newImg = zoom(newImg, random.randrange(100, 140))
        newImg = copyToNew(img, k, random.randrange(1800, 2000), random.randrange(400, 1110))
        # newImg = copyToNew(yes, newImg, random.randrange(300, 340), random.randrange(240, 280))

        plt.imshow(newImg)
        plt.show()
        slash = filename[i].find('.')
        cv2.imwrite(root+'/new_folder/' + filename[i][:slash] + "(" + str(count) + ")" + filename[i][slash:], newImg)
        count += 1
        # except:
        #     pass

    # for i in range(0,300, 12):
    #     img = cv2.imread("C:/Users/ADITYA/Desktop/Form OCR/with_photos/" + filename[i])
    #     plt.imshow(img)
    #     plt.show()

if __name__ == '__main__':
    main()