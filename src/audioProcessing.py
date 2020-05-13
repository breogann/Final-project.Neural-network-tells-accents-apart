from pydub import AudioSegment
import os

#2.PRE-PROCESS AUDIO

#2.1. Putting it together
def getConcatenatedAudio(language):
    #Create one .wav file with all english audios concatenated.
    total = 0
    for i in f"{language}names":
        total += AudioSegment.from_file(f"../input/{language}/{i}.mp3", format = 'mp3')
    total.export(f"output/total{language}.wav", format='wav')

getConcatenatedAudio("spanish")
getConcatenatedAudio("english")

#2.2. Slicing it into even parts
def sliceAudio(itv, ovl, language):
    #Slice audio in even parts with an overlap
    total = AudioSegment.from_wav(f"output/total{language}.wav") 
    
    interval = itv * 1000 #Every 20s
    overlap = ovl * 1000 #Overlap 10s

    counter = 1
    n = len(total) 
    start = 0
    end = 0

    output_path = f'output/{language}chunks/'
    os.mkdir(output_path) #Creates a folder where the sliced audios will be
    
    for i in range(0, 2*n, interval): 
        if i == 0: 
            start = 0
            end = interval 
        else: 
            start = end - overlap 
            end = start + interval  

        if end >= n: 
            end = n
            break

        chunk = total[start:end] 
        filename = f"{output_path}{language}chunk"+str(counter)+".wav"
        chunk.export(filename, format ="wav") 

        counter += 1

sliceAudio(20, 10, "spanish")
sliceAudio(20, 10, "english")
