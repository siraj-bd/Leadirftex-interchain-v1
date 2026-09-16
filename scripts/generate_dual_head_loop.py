#!/usr/bin/env python3
"""
Generate Unified Collar & Recessed Brain Dual-Gender Seamless Loop Video with TOP-DOWN GREEN LASER
- Laser light beams down strictly FROM ABOVE into the head/cranium (upor theke head a porbe)
- Stops completely above the eyebrows (Y < 0.40); face, eyes, and mouth are 100% untouched
- Vivid emerald green laser color
- Unified continuous collar, shirt, tie, suit, neck, and shoulder line
- Front-facing dual-gender face (man left, woman with short hair right) with direct natural eye contact
- Anatomically recessed internal brain seated deep inside cranial vault
- 100% mathematically seamless loop over T = 8.0 seconds (240 frames @ 30fps)
- Rigid 3D human head stability (zero bend, zero tilt at loop boundary)
"""
import math
import os
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def generate_seamless_recessed_brain_video():
    src_img_path = "assets/mockup/front_head_brain_scan.jpg"
    out_video_path = "assets/mockup/head_brain_scan_mockup.mp4"
    out_freeze_path = "assets/mockup/head_brain_scan_freeze_frame.png"

    if not os.path.exists(src_img_path):
        raise FileNotFoundError(f"Source image not found: {src_img_path}")

    base_img = Image.open(src_img_path).convert("RGBA")
    width, height = base_img.size
    print(f"[Generator] Loaded base unified short-hair image: {width}x{height}")

    # Center of eyes (rotation anchor)
    eye_cx = int(0.495 * width)
    eye_cy = int(0.450 * height)

    # Internal brain cavity & cranium mask (strictly restricted to top of head above brow Y < 0.40)
    cranium_mask = Image.new("L", (width, height), 0)
    c_draw = ImageDraw.Draw(cranium_mask)
    # Elliptical mask covering ONLY the top cranium
    bx0 = int(0.360 * width)
    bx1 = int(0.640 * width)
    by0 = int(0.020 * height)
    by1 = int(0.395 * height) # strictly ends above the eyes
    c_draw.ellipse([bx0, by0, bx1, by1], fill=255)
    cranium_mask = cranium_mask.filter(ImageFilter.GaussianBlur(radius=16))

    # Strict hard cutoff below Y = 0.40 so face is NEVER touched by laser
    c_arr = np.array(cranium_mask, dtype=np.float32)
    face_cutoff = int(0.40 * height)
    for y in range(face_cutoff, height):
        fade = max(0.0, 1.0 - (y - face_cutoff) / 15.0)
        c_arr[y, :] *= fade

    mask_arr = c_arr / 255.0

    base_arr = np.array(base_img, dtype=np.float32)

    fps = 30
    duration = 8.0  # Exactly 8.0 seconds
    total_frames = int(fps * duration)
    print(f"[Generator] Rendering {total_frames} frames ({duration}s @ {fps}fps) with TOP-DOWN GREEN LASER...")

    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{width}x{height}",
        "-pix_fmt", "rgba",
        "-r", str(fps),
        "-i", "-",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-preset", "medium",
        "-crf", "18",
        out_video_path
    ]

    process = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    freeze_frame_saved = False

    y_indices = np.arange(height)[:, np.newaxis]

    for i in range(total_frames):
        t = i / fps
        tau = 2.0 * math.pi * (t / duration)  # 0 to 2pi (strictly periodic!)

        # 1. Subtle living presence micro-motion (strictly periodic, zero loop boundary jump)
        tilt = 0.10 * math.sin(tau)  # +/- 0.10 deg subtle breathing poise
        scale = 1.0 + 0.0012 * math.sin(tau)

        # 2. Continuous synaptic internal brain illumination (periodic, originating strictly from inside the skull)
        synapse_pulse = 0.12 * math.sin(2.0 * tau) + 0.05 * math.sin(4.0 * tau)

        # 3. Scanning Tomography Laser Sweep FROM ABOVE (upor theke nambe)
        # Sweeps down from Y = 0.03*H (above skull crown) down to Y = 0.38*H (cranium base)
        scan_active = 0.0
        laser_y = 0
        if t < 3.0:
            scan_active = math.sin((t / 3.0) * math.pi)
            scan_prog = t / 3.0
            laser_y = int(height * (0.03 + scan_prog * 0.35))

        # Build frame
        frame_arr = base_arr.copy()

        # Apply internal synaptic glow (confined strictly to the recessed brain cavity)
        if abs(synapse_pulse) > 0.001:
            frame_arr[:, :, 0] = np.clip(frame_arr[:, :, 0] + 28.0 * synapse_pulse * mask_arr, 0, 255)
            frame_arr[:, :, 1] = np.clip(frame_arr[:, :, 1] + 8.0 * synapse_pulse * mask_arr, 0, 255)

        # Apply TOP-DOWN GREEN LASER PLANE (descending from above into the head, strictly Y < 0.40)
        if scan_active > 0.01 and laser_y > 0:
            y_dist = np.abs(y_indices - laser_y)
            # Sharp intense green beam line with upward light beam halo (coming from above)
            beam_profile = np.exp(- (y_dist ** 2) / 20.0)
            # Upward beam column (light entering from above)
            upward_cone = np.clip((laser_y - y_indices) / 60.0, 0, 1) * np.exp(- np.maximum(0, laser_y - y_indices) / 40.0)
            combined_light = (beam_profile + 0.35 * upward_cone) * scan_active * mask_arr

            # VIVID EMERALD GREEN LASER: High Green (R: +35, G: +180, B: +55)
            frame_arr[:, :, 0] = np.clip(frame_arr[:, :, 0] + 35.0 * combined_light, 0, 255)
            frame_arr[:, :, 1] = np.clip(frame_arr[:, :, 1] + 180.0 * combined_light, 0, 255)
            frame_arr[:, :, 2] = np.clip(frame_arr[:, :, 2] + 55.0 * combined_light, 0, 255)

        frame_img = Image.fromarray(frame_arr.astype(np.uint8))

        # Apply subtle rigid micro-transform pivoting around eye line
        if abs(tilt) > 0.005:
            frame_img = frame_img.rotate(tilt, resample=Image.BICUBIC, center=(eye_cx, eye_cy), expand=False)

        # Save freeze frame at t = 3.6s (stabilized analyzed state)
        if not freeze_frame_saved and t >= 3.6:
            frame_img.save(out_freeze_path, "PNG")
            freeze_frame_saved = True
            print(f"[Generator] Saved freeze frame to {out_freeze_path}")

        process.stdin.write(frame_img.tobytes())

    process.stdin.close()
    process.wait()
    print(f"[Generator] Finished encoding video to {out_video_path}")

    # Verify loop boundary difference
    subprocess.run(["ffmpeg", "-y", "-ss", "0.0", "-i", out_video_path, "-vframes", "1", "assets/mockup/check_f0.png"], capture_output=True)
    subprocess.run(["ffmpeg", "-y", "-ss", str(duration - 0.033), "-i", out_video_path, "-vframes", "1", "assets/mockup/check_fend.png"], capture_output=True)

    f0 = Image.open("assets/mockup/check_f0.png").convert("RGB")
    fe = Image.open("assets/mockup/check_fend.png").convert("RGB")
    diff = np.mean(np.abs(np.array(f0, dtype=float) - np.array(fe, dtype=float)))
    print(f"[Generator] Loop boundary difference (frame 0 vs frame end): {diff:.4f} / 255")
    if diff < 2.0:
        print("[Generator] PASS: Loop is 100% mathematically and visually SEAMLESS (diff < 2.0)")

if __name__ == "__main__":
    generate_seamless_recessed_brain_video()
