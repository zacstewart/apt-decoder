# NOAA APT Decoder

Decode analog, APT signals from the NOAA weather satellites.

## Installation on Linux

    sudo apt install git sox
    pip install pillow numpy scipy
    git clone https://github.com/zacstewart/apt-decoder
    cd apt-decoder

## Usage

Previously you need to resample your sound file to 20800Hz, and then decode the
image:

    ./resample.sh recording.wav resampled.wav
    python ./apt.py resampled.wav image_out.png

Images will probably look upside down if the satellite passed from south to
north instead of north to south. In fact, the following examples are upside
down.

## Examples

![Example image](./examples/example.png)
![Example image](./examples/example2.png)

## Alternatives

You can also try [wxtoimg](http://wxtoimg.com/) but looks dead.

Alternatively [atp-dec/apt-dec](https://github.com/csete/aptdec) works really
good. Keep in mind that the [1.7
release](https://github.com/csete/aptdec/releases) looks newer than the [repo's
master branch](https://github.com/csete/aptdec).
