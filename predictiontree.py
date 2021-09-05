import cv2
import numpy as np
from keras.models import load_model

file=cv2.imread('tree2.jpg')
model=load_model('treedetect.h5')

img=cv2.resize(file,(20,20))
imgarray=np.array(img)
imgarray=np.reshape(imgarray,(1,20,20,3))

imgarray=imgarray/255
pred=model.predict(imgarray)
pred=pred[0]
prediction=np.argmax(pred)

if prediction== 1:
    cv2.putText(file,'Trees' ,(4,200),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,255),3)
else:
    cv2.putText(file,'No Trees',(4,200),cv2.FONT_HERSHEY_DUPLEX,2,(0,255,255),3)
cv2.imshow('Screen', file)
cv2.waitKey()
cv2.destroyAllWindows()






