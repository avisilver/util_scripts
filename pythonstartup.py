# Add auto-completion and a stored history file of commands to your Python
# interactive interpreter. Requires Python 2.0+, readline. Autocomplete is
# bound to the Esc key by default (you can change it - see readline docs).
#
# Store the file in ~/.pystartup, and set an environment variable to point
# to it:  "export PYTHONSTARTUP=/home/user/.pystartup" in bash.
#
# Note that PYTHONSTARTUP does *not* expand "~", so you have to put in the
# full path to your home directory.

import atexit
import os
import readline
import rlcompleter

historyPath = os.path.expanduser("~/.pyhistory")

def save_history(historyPath=historyPath):
    import readline
    readline.write_history_file(historyPath)

if os.path.exists(historyPath):
    readline.read_history_file(historyPath)

atexit.register(save_history)
readline.parse_and_bind('tab: complete')

del os, atexit, readline, rlcompleter, save_history, historyPath



def dirp(object_or_module):
    """dirp(object_or_module) -> string

    Print the object's or currently imported module's attributes as shown
    in  dir() on separate lines with docstrings"""
    for attr in dir(object_or_module):
        doc = object_or_module.__getattribute__(attr).__doc__
        doc = doc if doc else ""
        indented_doc = "\n".join(doc.split("\n"))
        print ("\n{line}\n{attr}\n{doc}".format(
            line="-"*80,
            attr=attr,
            doc=indented_doc
        ))
