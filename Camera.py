import cv2

# camera object gets from webcam
cam = cv2.VideoCapture(0)

# overlay from image
overlay = cv2.imread("overlay.png");



while (True):
    
    # get frames from camera
    ret, frame = cam.read()
    out = cv2.addWeighted(overlay,0.8,frame,0.5,0)
    
    
    # make full screen
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)

    
    
    # dispay frame with camera output
    cv2.imshow('frame', out )


    
    # quit on q key
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
        
        
cam.release()
cv2.destroyAllWindows()
