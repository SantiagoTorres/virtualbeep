#!/usr/bin/env python
"""
    <Name>
        Virtualbeep

    <Description>
        This is a simple module that leverages scikits.audiolab to play custom
        frequencies in the default output of the computer

    <Usage>
        Run as a program:
            ./virtualbeep.py -h

    <Author>
        Santiago Torres (torresariass@gmail.com)

    <License>
        Beerware I guess. Do whatever you want with this snippet
"""
import scikits.audiolab as a 
import argparse

from numpy import array

DEFAULT_SECONDS = 2
DEFAULT_FREQUENCY = 440.0

"""
    Play a beep of the specified frequency as notefreq and for secs seconds
    long
"""
def play_beep(secs, notefreq):

    # define the length of the beep
    fs = 44100
    vectorsize = fs * secs

    # define the frequency of the beep
    noteperiod = fs / notefreq
    noteoffset = noteperiod / 2

    # create a vector and play it 
    beep = array([ float((x % noteperiod) - noteoffset)/noteoffset for x in
        range(1, vectorsize)])

    a.play(beep, fs=fs)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--length','-l', metavar = 'length', 
        default = DEFAULT_SECONDS, dest = 'secs', nargs = '?',
        help='defines the duration of the beep in seconds (default 2 seconds)')
    parser.add_argument('--frequency', '-f', metavar = 'frequency', 
        default=DEFAULT_FREQUENCY, dest = 'notefreq', nargs = '?',
        help='defines a custom frequency to play in hz')
    args = parser.parse_args()

    play_beep(int(args.secs), float(args.notefreq))

   
