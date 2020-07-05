#!/usr/bin/env bash

if [[ "$#" -ne 1 && "$#" -ne 2 ]]; then
    echo "Usage: resample.sh input.wav [ output.wav ]"
    echo "Resamples to 20800Hz. If output is ommited, by default will save on output.wav"
    exit 1
fi

echo "Resampling to 20800Hz..."
# Resample to 20800hz
# Remove frequencies lower than 10Hz to remove DC components affecting the
# contrast of the image (caused when the FM demodulator does not follow the
# doppler shift of the satellite)
# Also filter frequencies higher than 4500, could be useful on some noisy files
sox "$1" -r 20800 "${2:-output.wav}" highpass 10 lowpass 4500
