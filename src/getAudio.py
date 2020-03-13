from pydub import AudioSegment
import pandas as pd

#1.GET DATA

#From the dataframe we obtain the name of all the files
data = pd.read_csv("../input/speakers_all.csv")
df = pd.DataFrame(data)

#Native english speakers & spanish native speakers
dataespen = data[data['native_language'].notnull() & ((data['native_language'] == "english")|(data['native_language'] == "spanish"))]
nombrestotal = sorted(list(dataespen.filename))

#Made into a list
    #Not necessary if we want to use all of them. Only if we wanted to pass a deeper filter
englishnames = []
spanishnames = []
for i in nombrestotal:
    if i.startswith('english'):
        englishnames.append(i)
    elif i.startswith('spanish'):
        spanishnames.append(i)
