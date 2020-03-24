<p align="center">
  <img width="600" height="200" src="https://github.com/breogann/-neural-network-to-tell-accents-apart/blob/master/Images/cover.png)" alt="What's my accent?">
</p>

# Accent recogntion 🇪🇸 🇺🇸 

This API aims to evaluate whether someone is a native speaker of English or Spanish through accent detection. With over 450 recordings for each accent, a deep learning model was trained so it could discriminate between them.

At the moment the API can be executed locally.

This app was programed in Python, using (CNN) Convolutional Neural Networks 🤖from Keras.

## Data 📊 ##
### /ˈdeɪtə/ ###

The speech accent archive (https://accent.gmu.edu) has a compilation of a huge variety of speakers with different backgrounds that read the same paragraph so it can be analyzed.

In this case, only spanish and english speakers were used to train the model. Although speakers were not limited to a particular region, most of them belong to either the US and Spain.

## The text 📚 ## 
### /ðə tɛkst/ ###

* "Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob.  We also need a small plastic snake and a big toy frog for the kids.  She can scoop these things into three red bags, and we will go meet her Wednesday at the train station."

## Data processing & Training 🛠 ## 
### ˈdeɪtə ˈprɑsɛsɪŋ ænd ˈtreɪnɪŋ ###
Three scripts (getAudio.py, audioProcessing.py, audioFeatures.py) show how, by introducing your own data, you can prepare manipulate the audio.

The rest of .py files are what the ones used to make the API and CNN model work. 

Used technologies 🔌:
- Flask
- PyDub (AudioSegment)
- SciPy
- Tensorflow
- Deep convolutional neural networks (Keras)
