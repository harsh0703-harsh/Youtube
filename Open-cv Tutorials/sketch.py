import cv2
# img=cv2.imread("dog1.jpeg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img_invert = cv2.bitwise_not(img_gray)
# img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)

# def Remove(x, y):
#     return cv2.divide(x, 255 - y, scale=256)
#     ## 
# final_img = Remove(img_gray, img_smoothing)
# cv2.imshow("Sketch",final_img)
# cv2.waitKey()
# cv2.destroyAllWindows()

video=cv2.VideoCapture(0)

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
            cv2.imshow("Simple Frame",frame)
            cv2.imshow("frame",final_img)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
video.release()
cv2.destroyAllWindows()