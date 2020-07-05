import scipy.io.wavfile
import scipy.signal
import sys

RATE = 20800


def resample(in_filename, out_filename):
    (rate, signal) = scipy.io.wavfile.read(in_filename)

    if rate != RATE:
        coef = RATE / rate
        samples = int(coef * len(signal))
        signal = scipy.signal.resample(signal, samples)
        scipy.io.wavfile.write(out_filename, RATE, signal)

if __name__ == '__main__':
    resample(sys.argv[1], sys.argv[2])
