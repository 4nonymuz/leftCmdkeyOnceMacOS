#this script sets macos system settings to use left cmd key press ONCE for dictation
#it uses the keyboard library to listen for the left cmd key press
#please set the left cmd key press TWICE for dictation in MacOS system settings
#it uses the subprocess library to run the AppleScript
#pip install keyboard (required). install in venv.
import keyboard
import subprocess
#script needs to be run using sudo or it will not work

def run_applescript(script):
    """Runs an AppleScript using osascript."""
    try:
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running AppleScript: {e}")
        print(f"stderr: {e.stderr}")  # Print stderr for debugging
        return None

def on_cmd_press():
    """Starts or stops dictation using AppleScript."""

    # AppleScript to check if dictation is running.
    check_script = """
    tell application "System Events"
        tell process "SystemUIServer"
            try
                set isDictationRunning to (exists (menu bar item 1 of menu bar 1 whose description contains "dictation"))
            on error
                set isDictationRunning to false
            end try
        end tell
    end tell
    return isDictationRunning
    """

    is_running = run_applescript(check_script)

    if is_running == "true":
        # AppleScript to stop dictation (simulate pressing Left Cmd key twice)
        # bug: does not print dictation stopped, always prints dictation started
        # does not matter, it works as intended, if running, then press cmd key once to stop
        stop_script = """
        tell application "System Events"
            key code 55
            key code 55
        end tell
        """
        run_applescript(stop_script)
        print("Dictation stopped.")

    elif is_running == "false":
        # AppleScript to start dictation (simulate pressing Left Cmd key twice).
        start_script = """
        tell application "System Events"
            key code 55
            key code 55
        end tell
        """
        run_applescript(start_script)
        print("Dictation started.")

    else:
        print(f"Error: Could not determine dictation status.  is_running = {is_running}")

    # DO NOT exit; keep the script running

if __name__ == "__main__":
    keyboard.add_hotkey('cmd', on_cmd_press)
    print("Press ESC to stop.")
    keyboard.wait('esc')