# import numpy as np
# import pandas as pd
# import wave
# import librosa
# import librosa.display
# import matplotlib.pyplot as plt
# import sklearn
# from librosa import feature
# import numpy as np
# import csv
# from sklearn.svm import SVC

# music_data= pd.read_csv('features_30_sec.csv')
# music_data=music_data.drop(columns=["filename","length","chroma_stft_var","perceptr_var","spectral_bandwidth_var", "spectral_centroid_var", "rolloff_var", "zero_crossing_rate_var","harmony_var","rms_var","harmony_var","mfcc1_var","mfcc2_var","mfcc3_var","mfcc4_var", "mfcc5_var", "mfcc6_var", "mfcc7_var","mfcc8_var","mfcc9_var","mfcc10_var","mfcc11_var","mfcc12_var","mfcc13_var","mfcc14_var", "mfcc15_var", "mfcc16_var", "mfcc17_var","mfcc18_var","mfcc19_var","mfcc20_var","harmony_mean", "perceptr_mean"],axis=1)
# # Import label encoder
# from sklearn import preprocessing
 
# # label_encoder object knows how to understand word labels.
# label_encoder = preprocessing.LabelEncoder()
# array = ['label']
# # Encode labels in column 'species'.
# music_data['label']= label_encoder.fit_transform(music_data[array])
# encoded = {0: 'blues',1: 'classical',2: 'country',3: 'disco',4: 'hiphop',5: 'jazz',6: 'metal',7: 'pop',8: 'reggae',9: 'rock'}
# music_x=music_data
# music_x=music_x.drop(['label'], axis = 1)
# music_y=music_data['label']

# from sklearn.model_selection import train_test_split
# train_x, test_x, train_y, test_y = train_test_split(music_x, music_y, random_state=3,test_size=0.33)

# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# train_x = scaler.fit_transform(train_x)
# # we must apply the scaling to the test set that we computed for the training set
# test_x = scaler.transform(test_x)






# classes = {'pop':0, 'blues':1, 'hiphop':2, 'classical':3, 'disco':4, 'metal':5, 'country':6, 'blues':7, 'reggae':8, 'jazz':9, 'rock':10}

# fn_list_i = [
#         feature.chroma_stft,feature.rms,feature.spectral_centroid,
#        feature.spectral_bandwidth, feature.spectral_rolloff, feature.zero_crossing_rate
       
# ]

# out__put= {0: 'blues',
#  1: 'classical',
#  2: 'country',
#  3: 'disco',
#  4: 'hiphop',
#  5: 'jazz',
#  6: 'metal',
#  7: 'pop',
#  8: 'reggae',
#  9: 'rock'}

# def input_audio(audiofile_given):
#     y, sr = librosa.load(audiofile_given)
#     hop_length = 512# Compute local onset autocorrelation
#     oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
#     times = librosa.times_like(oenv, sr=sr, hop_length=hop_length)
#     tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=sr,
#                                         hop_length=hop_length)# Estimate the global tempo for display purposes
#     tempo = librosa.beat.tempo(onset_envelope=oenv, sr=sr,
#                             hop_length=hop_length)[0]
#     norm_audios_feat = []
#     y , sr = librosa.load(audiofile_given,sr=None)
#     feature_vector =get_feature_vector(y, sr)
#     feature_vector.append(tempo)
#     data=features_extractor(audiofile_given)
#     data=data.tolist()
#     feature_vector=feature_vector + data
#     norm_audios_feat.append(feature_vector) 
#     norm_output = '/content/drive/MyDrive/Music_data/output_music_001.csv'
#     header =[
#     'chroma_stft_mean', 'rms_mean', 'spectral_centroid_mean',
#         'spectral_bandwidth_mean', 'rolloff_mean', 'zero_crossing_rate_mean',
#         'tempo', 'mfcc1_mean', 'mfcc2_mean', 'mfcc3_mean', 'mfcc4_mean',
#         'mfcc5_mean', 'mfcc6_mean', 'mfcc7_mean', 'mfcc8_mean', 'mfcc9_mean',
#         'mfcc10_mean', 'mfcc11_mean', 'mfcc12_mean', 'mfcc13_mean',
#         'mfcc14_mean', 'mfcc15_mean', 'mfcc16_mean', 'mfcc17_mean',
#         'mfcc18_mean', 'mfcc19_mean', 'mfcc20_mean'
#     ]
#     with open(norm_output,'+w') as f:
#         csv_writer = csv.writer(f, delimiter = ',')
#         csv_writer.writerow(header)
#         csv_writer.writerows(norm_audios_feat)
#     return csv.writer
    

# def get_feature_vector(y,sr): 
#    feat_vect_i = [ np.mean(funct(y,sr)) for funct in fn_list_i]
#    feature_vector = feat_vect_i 
#    return feature_vector

# def features_extractor(file):
#     audio, sample_rate = librosa.load(file, res_type='kaiser_fast') 
#     mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=20)
#     mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    
#     return mfccs_scaled_features

# def predict_output(x_test):
#     svclassifier = SVC(kernel = 'rbf', C=7)
#     svclassifier.fit(train_x, train_y)
#     y_output= svclassifier.predict(x_test)
#     y_out= y_output.tolist()
#     return out__put[y_out[0]]


# # def final_features(audiofile_given):
# #     norm_audios_feat = []
# #     y , sr = librosa.load(audiofile_given,sr=None)
# #     feature_vector =get_feature_vector(y, sr)
# #     feature_vector.append(tempo)
# #     feature_vector=feature_vector + data
# #     norm_audios_feat.append(feature_vector) 



# # extracted_features=[]