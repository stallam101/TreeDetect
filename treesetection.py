import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
import keras

data=[]
labels=[]
categories=['trainedtrees','nottrees']
df='treeimages'
files=os.listdir(df)
print(files)
files.pop(0)
print(files)
for i in range(0,2,1):
    path=os.path.join(df,categories[i])
    images=os.listdir(path)
    for eachimage in images:
        imagepath=(path+'/'+eachimage)
        print(imagepath)
        if eachimage != ".DS_Store":
            imgarr=cv2.imread(imagepath)
            imgarr=cv2.resize(imgarr,(20,20))
            data.append(imgarr)
            if path == 'treeimages/nottrees':
                labels.append(0)
            else:
                labels.append(1)

labels=np.array(labels)
data=np.array(data)
(train_images, test_images, train_labels, test_labels)=train_test_split(data, labels, test_size = 0.2)

train_images = train_images/255
test_images = test_images/255



##model= keras.Sequential([
##    keras.layers.Flatten(input_shape=(20,20,3)),
##    keras.layers.Dense(128, activation='relu'),
##    keras.layers.Dense(2, activation='softmax')
##    ])
##model.compile(optimizer='adam',
##              loss='sparse_categorical_crossentropy',
##              metrics=['accuracy'])
##model.fit(train_images,train_labels, epochs=6)
##
##test_loss,test_acc = model.evaluate(test_images, test_labels, verbose=2)
##print(test_acc)
##model.save('treedetect.h5')



    

