#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from mpris import MPRISController
import argparse

class SpotifyController(MPRISController):
    def __init__(self):
        MPRISController.__init__(self, 'org.mpris.MediaPlayer2.spotify')
    def main(self):
        parser = argparse.ArgumentParser(description='Control Spotify from CLI through DBus')
        parser.add_argument('--play', '-p', action="store_true", help='Starts playing. (Warning: it\'s buggy.)')
        parser.add_argument('--pause', '-s', action="store_true", help='Stops playing.')
        parser.add_argument('--toggle', '-t', action="store_true", help='Starts playing if it\'s paused. Stops if started.')
        parser.add_argument('--next', '-n', action="store_true", help='Skips to the next track.')
        parser.add_argument('--previous', '--prev', '-b', action="store_true", help='Skips to the previous track.')
        parser.add_argument('--title', action="store_true", help='Prints title.')
        parser.add_argument('--album', action="store_true", help='Prints album.')
        parser.add_argument('--artist', action="store_true", help='Prints artist.')
        args = parser.parse_args()
        if args.play:
            self.play()
        if args.pause:
            self.pause()
        if args.toggle:
            self.playpause()
        if args.next:
            self.next()
        if args.previous:
            self.previous()
        if args.title:
            print(self.title())
        if args.album:
            print(self.album())
        if args.artist:
            print(self.artist())

if __name__ == '__main__':
	SpotifyController().main()
