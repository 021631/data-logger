import sounddevice as sd
import scipy.io.wavfile
from scipy import signal
import scipy.io.wavfile
import numpy as np
import json

n_window = pow(2, 12)
n_overlap = n_window / 2
n_fft = n_window
fs = 16000

span = input("time in minutes: ")
duration = 60 * int(span)
try:
    audiodata = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='float64')
    sd.wait()
    data = audiodata.transpose()
    wav_data = data
    scipy.io.wavfile.write('audio_data.wav', fs, wav_data)
    [F, pxx] = scipy.signal.welch(data, fs=fs, window='hanning', nperseg=n_window, noverlap=n_overlap,
                                  nfft=n_fft,
                                  detrend=False, return_onesided=True, scaling='density')
    temp_data = np.array(pxx).astype(float)
    data = temp_data.tolist()

    audio_json = {
        "sound_data": [
            {
                "values": data[0]
            },
        ]
    }

    with open("test.json", 'w') as f:
        json.dump(audio_json, f)
        f.close()

except Exception as e:
    print("whoops!: {}".format(e))
