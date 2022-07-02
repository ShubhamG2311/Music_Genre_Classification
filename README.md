# Music_Genre_Classification

## Introduction:
Audio processing is one of the most complex tasks in data science as compared to image processing and other classification techniques. One such application is music genre classification which aims to classify the audio files in certain categories of sound to which they belong. The application is very important and requires automation to reduce the manual error and time because if we have to classify the music manually then one has to listen out each file for the complete duration. So To automate the process I have used Machine learning and Deep Learning Algorithms for it.

## Approach:
In short, the problem statement is to categorise various audio files into different music genres like hip hop, disco etc.

## About Dataset: 
The dataset I have used is named the GTZAN genre collection dataset which is a very popular audio collection dataset. It contains approximately 1000 audio files that belong to 10 different classes. Each audio file is in .wav format (extension). The classes to which audio files belong are Blues, Hip-hop, classical, pop, Disco, Country, Metal, Jazz, Reggae, and Rock. 

## Models used: 
I haved used various classification models such as Random Forest Classifier, LightGBM, Gradient Boosting and SVM(various kernels). After that I trained all these models on the training dataset and then predicted the result on the testing dataset. I visualised and analysed the results and I came to conclusion that SVM(Support Vector Machine) with RBF came out to be the best model with highest accuracy.

