import cv2,os
haarcascade="haarcascade_frontalface_default.xml"
f="Data_sets"
print(cv2.__version__)
subdata="Krish"
path=os.path.join(f,subdata)
if not os.path.isdir(path):
    os.mkdir(path)

(widht,height) = (130,100)
face=cv2.CascadeClassifier(haarcascade)
webcam=cv2.VideoCapture(0)
count=1
while count<=30:
    (c,d)=webcam.read()
    gray=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)
    faces=face.detectMultiScale(gray,1.3,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(d,(x,y),(x+w,y+h),(0,0,255),3)
        g=gray[y:y+h,x:x+w]
        faceresize=cv2.resize(g,(widht,height))
        cv2.imwrite('%s/%s.png'%(path,count),faceresize)
    count+=1
    cv2.imshow("Krish",d)

cv2.waitKey(0)

cv2.destroyAllWindows()