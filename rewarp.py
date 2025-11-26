import subprocess
import os
import sys

def get_video_fps(input_file):
    cmd = [
        'ffprobe', '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream=r_frame_rate',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        input_file
    ]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, _ = process.communicate()
    fps = output.decode('utf-8').strip()
    return eval(fps)

def ffmpeg_rewarp(input_file, output_file):
    fps = get_video_fps(input_file)

    cmd = [
        'ffmpeg', '-i', input_file,
        '-c:v', 'copy',
        '-c:a', 'copy',
        '-map_metadata', '0',
        '-r', str(fps),
        output_file
    ]

    subprocess.run(cmd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 rewarp.py <input_video>")
        sys.exit(1)

    input_file = sys.argv[1]

    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    base_name = os.path.basename(input_file)
    output_file = os.path.join(output_dir, base_name)

    ffmpeg_rewarp(input_file, output_file)
    print(f"Rewrap completed → {output_file}")
