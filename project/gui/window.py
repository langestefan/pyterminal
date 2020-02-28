import gi
import threading
import time
import os

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, GObject


class MyWindow(Gtk.Window):

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("glade/test.glade")
        self.window = builder.get_object("window")
        self.window.connect("destroy", Gtk.main_quit)

    def example_target(self):
        print('test')
