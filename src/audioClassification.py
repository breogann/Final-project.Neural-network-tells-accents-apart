from pydub import AudioSegment
import pandas as pd
import numpy as np
import os
from scipy.fftpack import fft
import json
from keras.models import load_model
from keras.models import model_from_json

path = "../input/test1.m4a"

def generateDataframe (path):
    
    #Conversion to a .wav
    total = AudioSegment.from_file(path, format = 'm4a')
    output_path = "../output/"
    file_name = "recording.wav"
    complete_path = output_path+file_name
    total.export(complete_path, format='wav')
    
    #Extraction of features, Fourier transformation & dataframe
    audioarray = []

    for _ in os.listdir(output_path):
        sound = AudioSegment.from_file(complete_path, format="wav")
        samples = sound.get_array_of_samples()
        fft_out = abs(fft(samples, 200000))
        audioarray.append(np.array(fft_out))

    df_recording=pd.DataFrame({'audios':audioarray})
    return df_recording

#gendf = generateDataframe (path)

def runModel(gendf):
   
    trained_model = ("0.7741-accuracy-200000-50epochs-loss1.4109")
    #Load the trained neural network model
    print("Loading neural network...")
    with open(f'../output/{trained_model} .json','r') as f:
        model_json = json.load(f)
        model = model_from_json(model_json)
        model.load_weights(f"../output/{trained_model} .h5")
    
    #Prediction
    print("Predicting...")
    x_prueba=np.vstack(gendf['audios'])
    x_prueba.shape
    language = model.predict(x_prueba)
    l=language[0].tolist()
    
    #Return of info to the user
    print("Evaluating...")
    lang = l.index(max(l))
    if lang == 0:
        return("🇪🇸 Spanish native speaker with a likelihood of {}%".format((round(l[0]*100, 1))))
    elif lang == 1:
        return("🇺🇸 English native speaker with a likelihood of {}%".format((round(l[1]*100, 1))))

#runModel(gendf)