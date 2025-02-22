this script sets macos system settings to use left cmd key press ONCE for dictation
it uses the keyboard library to listen for the left cmd key press
please set the left cmd key press TWICE for dictation in MacOS system settings
it uses the subprocess library to run the AppleScript

#pip install keyboard (required). install in venv.
import keyboard
import subprocess
#script needs to be run using sudo or it will not work
