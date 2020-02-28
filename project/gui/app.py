import threading
import time
import gi

from gi.repository import GLib, Gtk, GObject

gi.require_version('Gtk', '3.0')
from project.gui.window import MyWindow


def app_main():
    win = MyWindow()
    win.window.show_all()

    thread = threading.Thread(target=win.example_target)
    thread.daemon = True
    thread.start()


if __name__ == "__main__":
    app_main()
    Gtk.main()
