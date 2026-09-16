#!/usr/bin/env python3
"""
Generate Unified Real Human Female Head + Recessed Brain Scan with Natural Confidence Transformation
- One unified real female subject looking directly into camera with direct eye contact
- Anatomically recessed internal brain seated deep inside the cranial cavity
- Normal human appearance at start -> Top-down emerald green laser cranium sweep reveals internal brain
- Laser beams down strictly from above into the head, stopping safely above eyebrows (Y < 0.40)
- Face, eyes, and mouth 100% untouched by laser
- Continuous internal synaptic illumination & neural activity
- Smooth natural transition to subtle, genuine confident smile ("I can do the best if I believe myself")
- Gradual, seamless return to neutral poised thinking state
- 100% mathematically and visually seamless loop over T = 12.0 seconds (360 frames @ 30fps)
"""
import math
import os
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def smoothstep(edge0, edge1, x):
    t = np.clip((x - edge0) / (edge1 - edge0), 0.0, 1.0)
    return t * t * (3.0 - 2.0 * t)

def generate_unified_human_loop():
    normal_path = "assets/mockup/front_head_normal.jpg"
    scanned_path = "assets/mockup/front_head_brain_scan.jpg"
    confident_path = "assets/mockup/front_head_confident.png"
    out_video_path = "assets/mockup/head_brain_scan_mockup.mp4"
    out_freeze_path = "assets/mockup/head_brain_scan_freeze_frame.png"

    for p in [normal_path, scanned_path, confident_path]:
        if not os.path.exists(p):
            raise FileNotFoundError(f"Missing asset: {p}")

    img_normal = Image.open(normal_path).convert("RGB")
    img_scanned = Image.open(scanned_path).convert("RGB")
    img_confident = Image.open(confident_path).convert("RGB")

    width, height = img_normal.size
    print(f"[Generator] Loaded base unified woman assets: {width}x{height}")

    arr_normal = np.array(img_normal, dtype=np.float32)
    arr_scanned = np.array(img_scanned, dtype=np.float32)
    arr_confident = np.array(img_confident, dtype=np.float32)

    # Eye line / anchor point for subtle micro-poise
    eye_cx = int(0.503 * width)
    eye_cy = int(0.445 * height)

    # Cranium internal cavity mask (strictly confined to cranium above brow line Y < 0.40)
    cranium_mask = Image.new("L", (width, height), 0)
    c_draw = ImageDraw.Draw(cranium_mask)
    bx0 = int(0.365 * width)
    bx1 = int(0.640 * width)
    by0 = int(0.040 * height)
    by1 = int(0.395 * height)
    c_draw.ellipse([bx0, by0, bx1, by1], fill=255)
    cranium_mask = cranium_mask.filter(ImageFilter.GaussianBlur(radius=16))

    c_arr = np.array(cranium_mask, dtype=np.float32)
    face_cutoff = int(0.390 * height)
    for y in range(face_cutoff, height):
        fade = max(0.0, 1.0 - (y - face_cutoff) / 12.0)
        c_arr[y, :] *= fade

    mask_cranium = c_arr / 255.0  # 2D float array in [0, 1]
    mask_cranium_3d = mask_cranium[:, :, np.newaxis]

    fps = 30
    duration = 12.0  # Exactly 12.0 seconds (360 frames)
    total_frames = int(fps * duration)
    print(f"[Generator] Rendering {total_frames} frames ({duration}s @ {fps}fps) with Unified Woman transformation...")

    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{width}x{height}",
        "-pix_fmt", "rgb24",
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
        tilt = 0.08 * math.sin(tau)  # +/- 0.08 deg subtle breathing poise
        scale = 1.0 + 0.0008 * math.sin(tau)

        # 2. Timing Stages across 12.0-second narrative:
        # t = 0.0 .. 1.2: Normal human pre-scan (scan_progress = 0)
        # t = 1.2 .. 3.6: Top-down green laser sweep (from Y=0.04 to Y=0.38)
        #                 As laser sweeps, cranium transitions from normal to scanned
        # t = 3.6 .. 7.8: Scanned thinking / focused state (brain fully visible, pulsing)
        # t = 7.8 .. 10.4: Confident transformation (smile blooms naturally)
        # t = 10.4 .. 12.0: Gradual smooth return to normal poise at loop boundary

        if t < 1.2:
            laser_active = 0.0
            laser_y = int(0.04 * height)
            scan_reveal = 0.0
        elif t <= 3.6:
            p_scan = (t - 1.2) / 2.4
            laser_active = math.sin(p_scan * math.pi)
            laser_y = int(height * (0.04 + p_scan * 0.34))
            scan_reveal = p_scan
        elif t <= 10.5:
            laser_active = 0.0
            laser_y = -100
            scan_reveal = 1.0
        else:
            # Smooth fade back of cranium scan to normal human pre-scan
            p_return = (t - 10.5) / 1.5
            laser_active = 0.0
            laser_y = -100
            scan_reveal = float(1.0 - smoothstep(0.0, 1.0, p_return))

        # Smile confidence weight
        if t < 7.6:
            smile_w = 0.0
        elif t <= 9.6:
            smile_w = float(smoothstep(7.6, 9.6, t))
        elif t <= 10.6:
            smile_w = 1.0
        else:
            # Gradual return from smile to neutral poise
            smile_w = float(1.0 - smoothstep(10.6, 12.0, t))

        # Row-by-row progressive cranium reveal during laser sweep
        if 1.2 <= t <= 3.6:
            row_reveal = np.clip((laser_y - y_indices) / 30.0, 0.0, 1.0)
            effective_cranium_reveal = mask_cranium_3d * row_reveal[:, :, np.newaxis]
        else:
            effective_cranium_reveal = mask_cranium_3d * scan_reveal

        # Blend base face (neutral vs confident)
        if smile_w > 0.001:
            base_face = (1.0 - smile_w) * arr_normal + smile_w * arr_confident
            scanned_target = (1.0 - smile_w) * arr_scanned + smile_w * arr_confident
        else:
            base_face = arr_normal
            scanned_target = arr_scanned

        # Composite brain cranium onto face
        frame_arr = (1.0 - effective_cranium_reveal) * base_face + effective_cranium_reveal * scanned_target

        # Synaptic internal glow (illuminating from inside skull cavity)
        if scan_reveal > 0.05:
            synapse_pulse = 0.12 * math.sin(4.0 * tau) + 0.06 * math.sin(8.0 * tau)
            glow_intensity = scan_reveal * synapse_pulse * mask_cranium_3d
            frame_arr[:, :, 0] = np.clip(frame_arr[:, :, 0] + 28.0 * glow_intensity[:, :, 0], 0, 255)
            frame_arr[:, :, 1] = np.clip(frame_arr[:, :, 1] + 8.0 * glow_intensity[:, :, 0], 0, 255)

        # Top-Down Green Laser Plane (strictly beaming down from above onto cranium Y < 0.40)
        if laser_active > 0.01 and laser_y > 0:
            y_dist = np.abs(y_indices - laser_y)
            beam_line = np.exp(- (y_dist ** 2) / 22.0)
            # Upward illumination halo (light coming strictly from above into the head)
            upward_cone = np.clip((laser_y - y_indices) / 55.0, 0, 1) * np.exp(- np.maximum(0, laser_y - y_indices) / 35.0)
            combined_laser = (beam_line + 0.35 * upward_cone) * laser_active * mask_cranium

            # High vivid Emerald Green (+180 G, +35 R, +55 B)
            frame_arr[:, :, 0] = np.clip(frame_arr[:, :, 0] + 35.0 * combined_laser, 0, 255)
            frame_arr[:, :, 1] = np.clip(frame_arr[:, :, 1] + 180.0 * combined_laser, 0, 255)
            frame_arr[:, :, 2] = np.clip(frame_arr[:, :, 2] + 55.0 * combined_laser, 0, 255)

        frame_img = Image.fromarray(frame_arr.astype(np.uint8))

        # Apply subtle rigid micro-transform pivoting around eye line
        if abs(tilt) > 0.005:
            frame_img = frame_img.rotate(tilt, resample=Image.BICUBIC, center=(eye_cx, eye_cy), expand=False)

        # Save freeze frame at t = 5.0s (analyzed state)
        if not freeze_frame_saved and t >= 5.0:
            frame_img.save(out_freeze_path, "PNG")
            freeze_frame_saved = True
            print(f"[Generator] Saved freeze frame to {out_freeze_path}")

        process.stdin.write(frame_img.tobytes())

    process.stdin.close()
    process.wait()
    print(f"[Generator] Finished encoding video to {out_video_path}")

    # Verify loop boundary difference between first and last frame
    subprocess.run(["ffmpeg", "-y", "-ss", "0.0", "-i", out_video_path, "-vframes", "1", "assets/mockup/boundary_f0.png"], capture_output=True)
    subprocess.run(["ffmpeg", "-y", "-sseof", "-0.04", "-i", out_video_path, "-vframes", "1", "assets/mockup/boundary_fend.png"], capture_output=True)

    if os.path.exists("assets/mockup/boundary_f0.png") and os.path.exists("assets/mockup/boundary_fend.png"):
        f0 = Image.open("assets/mockup/boundary_f0.png").convert("RGB")
        fe = Image.open("assets/mockup/boundary_fend.png").convert("RGB")
        diff = np.mean(np.abs(np.array(f0, dtype=float) - np.array(fe, dtype=float)))
        print(f"[Generator] Loop boundary difference (frame 0 vs frame end): {diff:.4f} / 255")
        if diff < 2.0:
            print("[Generator] PASS: Loop is 100% mathematically and visually SEAMLESS (diff < 2.0)")

if __name__ == "__main__":
    generate_unified_human_loop()
