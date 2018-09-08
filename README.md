# NOAA APT Decoder

Decode analog, APT signals from the NOAA weather satellites.

## Usage

Previously you need to resample your sound file to 20800Hz, then:

    python apt.py soundfile.wav image_out.png

## Examples

![Example image](./examples/example.png)

## Alternatives

You can also try [wxtoimg](http://wxtoimg.com/) but looks dead.

Alternatively [atp-dec/apt-dec](https://github.com/csete/aptdec) works really
good. Keep in mind that the [1.7
release](https://github.com/csete/aptdec/releases) looks newer than the [repo's
master branch](https://github.com/csete/aptdec).
