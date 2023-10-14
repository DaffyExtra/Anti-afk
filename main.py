import time
import pygetwindow as gw
import pyautogui
import subprocess

# Define the time interval in seconds (1 minute)
interval = 60
jump_count = 0  # Initialize the jump count

while True:
    subprocess.run("jump.exe")
    # Specify the common title of the programs you want to focus
    common_program_title = "Counter-Strike 2"

    # Find all program windows with the same title
    program_windows = gw.getWindowsWithTitle(common_program_title)
    time.sleep(0.5)

    if program_windows:
        # Loop through all program windows and bring each one to the foreground
        for program_window in program_windows:
            program_window.activate()
            time.sleep(0.5)
            # Simulate pressing and holding the Control key
            subprocess.run("jump.exe")
            time.sleep(0.5)
            jump_count += 1  # Increment the jump count
            print(f"Player ({jump_count}) Jumped ")
    else:
        print(f"No programs found with the title '{common_program_title}'.")

    # Sleep for the specified interval (1 minute)
    time.sleep(interval)
