#! /usr/bin/python
# taken from http://stackoverflow.com/questions/30619740/python-downsampling-wav-audio-file

import wave
import audioop
import sys
import os


# PATH_TRAIN_IN_WAVS = '../birdclef_data/TrainingSet/wav/LIFECLEF2015_BIRDAMAZON_XC_WAV_RN16099.wav'
# PATH_TRAIN_IN_16KWAVS = '../birdclef_data/TrainingSet/wav_16khz/ALIFECLEF2015_BIRDAMAZON_XC_WAV_RN16099.wav'

PATH_TRAIN_IN_WAVS = '../birdclef_data/TrainingSet/wav/'
PATH_TRAIN_IN_16KWAVS = '../birdclef_data/TrainingSet/wav_16khz/'

# src = PATH_TRAIN_IN_WAVS
# dst = PATH_TRAIN_IN_16KWAVS
dirmp3  = '../birdclef_data/TrainingSet/mp3/'
dirPath = '../birdclef_data/TrainingSet/wav/'
dstPath = '../birdclef_data/TrainingSet/wav_16khz/'



# 用來將mp3轉成wav
# ##############################################################################
# 請注意 這只能處理一層資料夾
# 例如 ../birdclef_data/TrainingSet/wav/wav01 --> ../birdclef_data/TrainingSet/wav_16khz/wav01_16khz
#     ../birdclef_data/TrainingSet/wav/wav02 --> ../birdclef_data/TrainingSet/wav_16khz/wav02_16khz
#     ../birdclef_data/TrainingSet/wav/wav03 --> ../birdclef_data/TrainingSet/wav_16khz/wav03_16khz
# 如果 資料夾下還有子資料夾，他會被混在自己的 "目標母資料夾" 內
# 例如 ../birdclef_data/TrainingSet/wav/wav01/wav01_01 
# 就會被丟到 ../birdclef_data/TrainingSet/wav_16khz/wav01_16khz 中
# ##############################################################################


from pydub import AudioSegment


# 用來將mp3轉成wav

def loadmp3s(dirmp3, dirPath):
#    sub_path = os.listdir(dirmp3)
#    for sub_path in sub_path:
#         print(sub_path)
    for path, subdirs, files in os.walk(dirmp3):
        for name in files:
            if name.endswith(".mp3"):
                src = path + '/' + name
                dst = dirPath + '/' + name.split(".")[0] + ".wav"
                    
                if not os.path.exists(os.path.dirname(dst)):
                    os.makedirs(os.path.dirname(dst))
                    
                sound = AudioSegment.from_mp3(src)
                sound.export(dst, format="wav")
                print(src, ' to ', dst)
                    
    return print("......convert mp3 to wav finishied............")


print('....................loadmp3s....')
loadmp3s(dirmp3, dirPath)



# 這會將 44100khz 的 wav 轉成 16khz 的 wav
# 

def downsampleWav(src, dst, inrate=44100, outrate=16000, inchannels=1, outchannels=1):
    if not os.path.exists(src):
        print( 'Source not found!')
        return False

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    try:
        s_read = wave.open(src, 'r')
        s_write = wave.open(dst, 'w')
    except:
        print( 'Failed to open files!')
        return False

    n_frames = s_read.getnframes()
    data = s_read.readframes(n_frames)

    try:
        converted = audioop.ratecv(data, 2, inchannels, inrate, outrate, None)
        if outchannels == 1 & inchannels != 1:
            converted[0] = audioop.tomono(converted[0], 2, 1, 0)
    except:
        print( 'Failed to downsample wav')
        return False

    try:
        s_write.setparams((outchannels, 2, outrate, 0, 'NONE', 'Uncompressed'))
        s_write.writeframes(converted[0])
    except:
        print( 'Failed to write wav')
        return False

    try:
        s_read.close()
        s_write.close()
    except:
        print( 'Failed to close wav files')
        return False

    return True



# function to load the wave files from dirPath
# ##############################################################################
# 請注意 這只能處理一層資料夾
# 例如 ../birdclef_data/TrainingSet/wav/wav01 --> ../birdclef_data/TrainingSet/wav_16khz/wav01_16khz
#     ../birdclef_data/TrainingSet/wav/wav02 --> ../birdclef_data/TrainingSet/wav_16khz/wav02_16khz
#     ../birdclef_data/TrainingSet/wav/wav03 --> ../birdclef_data/TrainingSet/wav_16khz/wav03_16khz
# 如果 資料夾下還有子資料夾，他會被混在自己的 "目標母資料夾" 內
# 例如 ../birdclef_data/TrainingSet/wav/wav01/wav01_01 
# 就會被丟到 ../birdclef_data/TrainingSet/wav_16khz/wav01_16khz 中
# ##############################################################################

# dirmp3  = '../birdclef_data/TrainingSet/mp3/'
# dirPath = '../birdclef_data/TrainingSet/wav/'
# dstPath = '../birdclef_data/TrainingSet/wav_16khz/'

def loadWavs(dirPath, dstPath):
#    sub_path = os.listdir(dirPath)
#    for sub_path in sub_path:
    for path, subdirs, files in os.walk(dirPath):
        for name in files:
            if name.endswith(".wav"):
                src = path + '/' + name
                dst = dstPath + name.split(".")[0] + ".wav"
                downsampleWav(src, dst) 
                print(src, ' to ', dst)
                    
    return print("......convert all finishied............")


print('..............loadWavs............')
loadWavs(dirPath, dstPath)