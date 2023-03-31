import cv2 

video=cv2.VideoCapture(0)

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
t=0
while True:
    print("run")
    ret,frame=video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(frame, 1.3, 5)
    for x,y,w,h in faces:
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)
        #roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(frame, 1.8, 20)
        for (sx, sy, sw, sh) in smiles:
            t=t+1
            cv2.rectangle(frame, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)
    print(t)    
    cv2.imshow("Frame", frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
