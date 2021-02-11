import cv2
import os


video=cv2.VideoCapture(0)
i=0
while True:
        ret,frame=video.read()
        frame=cv2.flip(frame,1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        img_invert = cv2.bitwise_not(gray)
        img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
        def REMOVE(x, y):
            return cv2.divide(x, 255 - y, scale=80)
        final_img = REMOVE(gray, img_smoothing)
        if ret==True:
            if not os.path.exists("images"):
                os.makedirs("images")
            cv2.imshow("Simple Frame",frame)
            cv2.imshow("frame",final_img)
            k=cv2.waitKey(1)
            if k%256==27:
                break
            elif k%256==32:
                cv2.imwrite("images/harsh_{}.jpeg".format(i),final_img)
                i=i+1
video.release()
cv2.destroyAllWindows()
