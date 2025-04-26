from PIL import Image, ImageSequence, ImageDraw
import numpy as np
import os

# Load the background image
background_path = "Capture1.PNG"
bg_image = Image.open(background_path).convert("RGBA")
width, height = bg_image.size

# Settings for animation
num_frames = 10
num_petals = 30
petal_radius = 10
fall_distance = 60  # total fall over all frames
frames = []

# Generate random starting positions for petals
np.random.seed(42)
start_x = np.random.randint(0, width, size=num_petals)
start_y = np.random.randint(0, 2*height // 3, size=num_petals)  # start from upper half
fall_speeds = np.random.uniform(3, 7, size=num_petals)  # varied speeds
sway = np.random.uniform(-2, 2, size=num_petals)

# Generate frames
for frame_idx in range(num_frames):
    frame = bg_image.copy()
    draw = ImageDraw.Draw(frame)

    for i in range(num_petals):
        # Compute new position
        x = start_x[i] + int(np.sin(frame_idx / 2.0) * sway[i] * frame_idx)
        y = int(start_y[i] + fall_speeds[i] * frame_idx)
        # Draw petal (simple jade-green circle)
        draw.ellipse((x - petal_radius, y - petal_radius, x + petal_radius, y + petal_radius),
                     fill=(0, 128, 102, 180))  # jade green with some transparency

    frames.append(frame)

# Save as GIF
gif_path = "jade_blossoms_falling.gif"
frames[0].save(gif_path, save_all=True, append_images=frames[1:], optimize=False, duration=150, loop=0)
gif_path
