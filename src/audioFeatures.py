from pydub import AudioSegment
from scipy.fftpack import fft
import os
import numpy as np
import pandas as pd

#3 EXTRACT FEATURES AND CREATE DATAFRAMES

def extractFeatures (language):
    i=0
    array = []
    path = f"output/{language}chunks"

    for _ in os.listdir(path) :
        i+=1
        if i < len(os.listdir(path)):
            sound = AudioSegment.from_file(f"output/{language}chunks/{language}chunk{i}.wav")
            samples = sound.get_array_of_samples()
            fft_out = abs(fft(samples, 200000)) #Fourier transformation of the sliced audios
            array.append(np.array(fft_out))
        else:
            break

    df_total = pd.DataFrame({'audios':array})
    return df_total

df_total = "global"

extractFeatures ("spanish")
extractFeatures ("english")

def dataFrames (df_total, language):
    df_total.audios = df_total.audios.apply(lambda x: np.array(x.tolist()))
    df_total.insert(column='GT', loc=1, value=f'{language}')

dataFrames (df_total, "spanish")
dataFrames (df_total, "english")

def mergeDF (language1, language2):
    both = pd.concat(language1, language2)
    return both

mergeDF("spanish", "english")
bothDF = mergeDF("spanish", "english")