import time
import os

def clear_screen():
    # Function to clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_stick_figure(frame):
    # Function to draw a stick figure based on the frame
    if frame == 1:
        return [
            "   O",
            "  /|\\",
            "  / \\",
        ]
    elif frame == 2:
        return [
            "   O",
            "  /|\\",
            "  /",
        ]
    elif frame == 3:
        return [
            "   O",
            "  /|\\",
            "   |",
        ]
    elif frame == 4:
        return [
            "   O",
            "  /|",
            "   |",
        ]

# Number of frames in the flipbook
num_frames = 4

# Loop through frames
for i in range(num_frames):
    clear_screen()
    stick_figure_frame = draw_stick_figure(i + 1)

    # Print the stick figure frame
    for line in stick_figure_frame:
        print(line)

    # Wait for a short duration to simulate animation
    time.sleep(0.5)

# Clear the screen after the animation is complete
clear_screen()
