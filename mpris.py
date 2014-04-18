#!/usr/bin/env python3
import dbus

class MPRISController(object):
    def __init__(self, busname):
        self.bus = dbus.SessionBus()
        self.busname = busname
        self.proxy = self.bus.get_object(self.busname, '/org/mpris/MediaPlayer2')
        self.player = dbus.Interface(self.proxy, 'org.mpris.MediaPlayer2.Player')
    def play(self):
        self.player.Play()
    def pause(self):
        self.player.Pause()
    def playpause(self):
        self.player.PlayPause()
    def forward(self):
        self.player.Next()
    def previous(self):
        self.player.Previous()
    def prev(self):
        self.previous()
    def props(self):
        return dbus.Interface(self.proxy, "org.freedesktop.DBus.Properties")
    def metadata(self):
        return self.props().Get("org.mpris.MediaPlayer2.Player", "Metadata")
    def title(self):
        return self.metadata()["xesam:title"].encode('utf-8')
    def album(self):
        data = self.metadata()
        if "xesam:album" in data:
            return data["xesam:album"].encode('utf-8')
        else:
            return None
    def artist(self):
        data = self.metadata()
        if "xesam:artist" in data:
            return data["xesam:artist"][0].encode('utf-8')
        else:
            return None

class DummyController(MPRISController):
    def __init__(self):
        pass
    def play(self):
        pass
    def pause(self):
        pass
    def playpause(self):
        pass
    def forward(self):
        pass
    def previous(self):
        pass
    def prev(self):
        pass
    def props(self):
        return None
    def metadata(self):
        return None
    def title(self):
        return None
    def album(self):
        return None
    def artist(self):
        return None
