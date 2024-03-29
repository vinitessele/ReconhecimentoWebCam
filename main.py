import cv2

video = cv2.VideoCapture(0)
classificadorFace = cv2.CascadeClassifier('cascades\\haarcascade_frontalface_default.xml')
while True:
    conectado, frame = video.read()
    #print(conectado)
    #print(frame)
    frameCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceDetectadas = classificadorFace.detectMultiScale(frameCinza,minSize(70,70))
    for (x,y,l,a) in faceDetectadas:
        cv2.rectangle(frame,(x,y),(x+l,y+a),(0,0,255))

    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()