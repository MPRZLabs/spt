#!/usr/bin/env python3
from mpris import MPRISController
import time, dbus, argparse, subprocess

class SpotifyController(MPRISController):
    def __init__(self):
        MPRISController.__init__(self, 'org.mpris.MediaPlayer2.spotify')
    def main(self):
        parser = argparse.ArgumentParser(description='Control Spotify from CLI through DBus')
        parser.add_argument('--play', '-p', action="store_true", help='Starts playing. (Warning: it\'s buggy.)')
        parser.add_argument('--pause', '-s', action="store_true", help='Stops playing.')
        parser.add_argument('--toggle', '-t', action="store_true", help='Starts playing if it\'s paused. Stops if started.')
        parser.add_argument('--forward', '--next', '-f', '-n', action="store_true", help='Skips to the next track.')
        parser.add_argument('--previous', '--prev', '-b', action="store_true", help='Skips to the previous track.')
        parser.add_argument('--pretty', '-o', action="store_true", help='Prints out track metadata nicely.')
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
        if args.forward:
            self.forward()
        if args.previous:
            self.previous()
        if args.title:
            print(self.title().decode())
        if args.album:
            print(self.album().decode())
        if args.artist:
            print(self.artist().decode())
        if args.pretty:
            print("You are now listening to %s by %s from album %s" % (self.title().decode(), self.artist().decode(), self.album().decode()))

if __name__ == '__main__':
	SpotifyController().main()
