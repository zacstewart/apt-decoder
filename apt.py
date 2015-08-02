import numpy
import scipy.io.wavfile
import scipy.signal
import sys
import PIL


class APT(object):

    RATE = 20800
    NOAA_LINE_LENGTH = 2080

    def __init__(self, filename):
        (rate, self.signal) = scipy.io.wavfile.read(filename)
        if rate != self.RATE:
            raise Exception("Resample audio file to {}".format(self.RATE))
        truncate = self.RATE * int(len(self.signal) // self.RATE)
        self.signal = self.signal[:truncate]

    def decode(self, outfile=None):
        hilbert = scipy.signal.hilbert(self.signal)
        filtered = scipy.signal.medfilt(numpy.abs(hilbert), 5)
        reshaped = filtered.reshape(len(filtered) // 5, 5)
        digitized = self._digitize(reshaped[:, 2])
        lines = int(len(digitized) / self.NOAA_LINE_LENGTH)
        matrix = digitized.reshape((lines, self.NOAA_LINE_LENGTH))
        image = PIL.Image.fromarray(matrix)
        if not outfile is None:
            image.save(outfile)
        image.show()
        return matrix

    def _digitize(self, signal, plow=0.5, phigh=99.5):
        (low, high) = numpy.percentile(signal, (plow, phigh))
        delta = high - low
        data = numpy.round(255 * (signal - low) / delta)
        data[data < 0] = 0
        data[data > 255] = 255
        return data.astype(numpy.uint8)

if __name__ == '__main__':
    apt = APT(sys.argv[1])

    if len(sys.argv) > 2:
        outfile = sys.argv[2]
    else:
        outfile = None
    apt.decode(outfile)
