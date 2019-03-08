import json
import wave
import os
import struct
import math
from scipy import frombuffer, int16
from pypinyin import pinyin, lazy_pinyin, Style

json_file='YOUR_JSON_FILE.json'
wav_file='YOUR_WAVE_FILE.wav'
confidence_threshold=0

confidences={}
timestamps={}

with open(json_file,'rb') as f:
    speechText=json.load(f)
    for sentence in speechText['results']:
        for i in range(len(sentence['alternatives'][0]['timestamps'])):

            # extract basic information of a word
            word=sentence['alternatives'][0]['timestamps'][i]
            wordConfi=sentence['alternatives'][0]['word_confidence'][i][1]
            wordCount=len(word[0])
            
            # process every syllable of a word
            for j in range(wordCount):
                wordPy=lazy_pinyin(word[0])[j]
                wordT0=word[1]+(word[2]-word[1])/wordCount*j
                wordT1=word[1]+(word[2]-word[1])/wordCount*(j+1)

                # case that one syllable has multiple samples
                if wordPy in confidences:
                    wordPy=wordPy+'_2'
                while wordPy in confidences:
                    wordPy=wordPy.split('_')[0]+'_'+str(int(wordPy.split('_')[1])+1)

                # regard a word less confident if it has more than one syllable
                if wordConfi/wordCount>confidence_threshold:
                    confidences[wordPy]=wordConfi/wordCount
                    timestamps[wordPy]=[wordT0,wordT1]

                    

# extract basic information of the wave file

audio=wave.open(wav_file,'r')
ch = audio.getnchannels()
width = audio.getsampwidth()
fr = audio.getframerate()
fn = audio.getnframes()
data = audio.readframes(fn)
audioContent = frombuffer(data, dtype=int16)

# split the wave file

if not os.path.exists('./output'):
    os.makedirs('./output')
for name in timestamps:
    segment=audioContent[int(timestamps[name][0]*fr*ch):int(timestamps[name][1]*fr*ch)]
    outd = struct.pack("h" * len(segment), *segment)
    ww = wave.open('./output/'+name+'.wav', 'w')
    ww.setnchannels(ch)
    ww.setsampwidth(width)
    ww.setframerate(fr)
    ww.writeframes(outd)
    ww.close()
    
