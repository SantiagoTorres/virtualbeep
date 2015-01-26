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
import time

from numpy import array, pi, sin, arange

DEFAULT_SECONDS = 2
DEFAULT_FREQUENCY = 440.0
DEFAULT_DELAY = 0

"""
    Play a beep of the specified frequency as notefreq and for secs seconds
    long
"""
def play_beep(secs = DEFAULT_SECONDS, notefreq = DEFAULT_FREQUENCY,
        delay = DEFAULT_DELAY):

    # define the length of the beep
    fs = 44100
    vectorsize = int(fs * secs)

    # define the frequency of the beep
    noteperiod = fs / notefreq
    noteoffset = noteperiod / 2

    # create a vector and play it 
    beep = array([ float((x % noteperiod) - noteoffset)/noteoffset for x in
        range(1, vectorsize)])

    a.play(beep, fs=fs)
    time.sleep(delay)


"""
    Play a beep of the specificad frequeny for secs seconds. This beep is 
    a smoother sinusoidal wave (play_beep defaults to a sawtooth).
"""
def play_sin_beep(secs = DEFAULT_SECONDS, notefreq = DEFAULT_FREQUENCY,
        delay = DEFAULT_DELAY):

    # define the length of the beep
    fs = 44100
    vectorstep  = 1/float(fs)

    # create the sinusoidal vector
    sin_vect = sin([2 * pi * notefreq * x for x in arange(0, secs, vectorstep)])
    normalization_const = max(sin_vect)

    beep = array([x/normalization_const for x in sin_vect])

    a.play(beep, fs=fs)
    time.sleep(delay)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--length','-l', metavar = 'length', 
        default = DEFAULT_SECONDS, dest = 'secs', nargs = '?',
        help='defines the duration of the beep in seconds (default 2 seconds)')
    parser.add_argument('--frequency', '-f', metavar = 'frequency', 
        default=DEFAULT_FREQUENCY, dest = 'notefreq', nargs = '?',
        help='defines a custom frequency to play in hz')
    parser.add_argument('-d', '-D', '--delay', metavar = 'delay',
        default = DEFAULT_DELAY, dest = 'delay', nargs = '?',
        help = 'defines a custom delay after playing the beep')

    args = parser.parse_args()

    play_beep(float(args.secs), float(args.notefreq), float(args.delay))

