import json
from keras import layers
from keras import models
from keras.layers.normalization import BatchNormalization
from keras.models import model_from_json
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import tensorflow
import numpy as np
from audioFeatures import bothDF

#4 TRAINING THE NEURAL NETWORK

X = np.vstack(bothDF.audios)
y = bothDF.language

def modelTraining (X, y):

    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2)

    number_classes=2 #native or non-native
    inshape=(X_train.shape[1],)

    model = models.Sequential()  #creates the neural network layers:
    
    model.add(layers.Dense(512, activation='relu', input_shape=inshape))
    model.add(layers.Dense(256, activation='relu'))
    model.add(BatchNormalization())
    model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(64, activation='relu'))

    model.add(layers.Dense(number_classes, activation='softmax'))
    model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    #Fitting of the model
    model.fit(X_train,
            y_train,
            epochs=50,
            batch_size=20,
            validation_data=(X_test, y_test))
    
    name="output/0.7741-accuracy-200000-50epochs-loss1.4109"

    #Prediction of the model
    predictions = model.predict(X_test)
    print(predictions)

    #Export model for future use
    model_json = model.to_json()
    with open(name+'.json', "w") as json_file:
        json.dump(model_json, json_file)
    model.save_weights(name+'.h5')

modelTraining (X, y)
