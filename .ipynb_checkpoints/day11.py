import cv2
vid=cv2.VideoCapture(0)
while True:
    flag, img = vid.read()
    if flag:
        #processing code
        img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        th,img_bw=cv2.threshold(img_gray,100,255,cv2.THRESH_BINARY_INV)
        #x,y,w,h=(250,200,100,100)
        x,y,w,h=(100,100,100,100)
        img_cropped=img[y:y+h,x:x+w,:]
        cv2.imshow('preview',img_cropped)
        key=cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        print('No frames')
        break
vid.release()            
cv2.destroyAllWindows()  