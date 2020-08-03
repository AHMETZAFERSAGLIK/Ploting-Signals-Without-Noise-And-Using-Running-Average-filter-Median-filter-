import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import math
import contextlib
import numpy as np
from scipy import signal as ss



sampleRate = 11025
cutOffFrequency = 400
freqRatio = (cutOffFrequency/sampleRate)

N = int(math.sqrt(0.196 + freqRatio**2)/freqRatio)



def convolution(A,B):
    lengthA = np.size(A)
    lengthB = np.size(B)
    C = np.zeros(lengthA + lengthB -1)
    for m in np.arange(lengthA):
        for n in np.arange(lengthB):
            C[m+n] = C[m+n] + A[m]*B[n]
    return C 
def running_mean(x, w):
    mask=np.ones((1,11))/11
    mask=mask[0,:]
    #convolved_data=ss.medfilt(channels[0],11)
    convolved_data=convolution(x,mask)
    return convolved_data

def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

    if sample_width == 1:
        dtype = np.uint8 
    elif sample_width == 2:
        dtype = np.int16 
 

    channels = np.frombuffer(raw_bytes, dtype=dtype)
    if interleaved:
        
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
       
        channels.shape = (n_channels, n_frames)

    return channels

with contextlib.closing(wave.open("test.wav",'rb')) as spf:
    sampleRate = spf.getframerate()
    ampWidth = spf.getsampwidth()
    nChannels = spf.getnchannels()
    nFrames = spf.getnframes()

   
    signal = spf.readframes(nFrames*nChannels)
    spf.close()
    channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

    freqRatio = (cutOffFrequency/sampleRate)
    N = int(math.sqrt(0.196196 + freqRatio**2)/freqRatio)

    
    filtered = running_mean(channels[0], N).astype(channels.dtype)
    
 
    wav_file = wave.open("average.wav", "w")
    wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
    plt.plot(filtered)
    plt.show()
    wav_file.writeframes(filtered.tobytes('C'))
    wav_file.close()
    
    

