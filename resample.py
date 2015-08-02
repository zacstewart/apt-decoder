import scipy.io.wavfile
import scipy.signal
import sys

RATE = 20800


def resample(filename):
    (rate, signal) = scipy.io.wavfile.read(filename)
    if rate != RATE:
        coef = RATE / rate
        samples = int(coef * len(signal))
        signal = scipy.signal.resample(signal, samples)
        scipy.io.wavfile.write("resampled.wav", RATE, signal)

if __name__ == '__main__':
    resample(sys.argv[1])
