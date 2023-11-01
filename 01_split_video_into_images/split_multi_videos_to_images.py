import os

import cv2

# Directory containing videos
videos_dir = "./videos"
output_dir = "./output"

# Set the desired interval in seconds here (3, 5, or 10)
desired_interval = 5  # Change this value to the desired interval in seconds

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

video_files = [
    f for f in os.listdir(videos_dir) if os.path.isfile(os.path.join(videos_dir, f))
]


# Function to extract frames at a specific time interval
def extract_frames(input_video, output_folder, video_name, interval_seconds=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    vidcap = cv2.VideoCapture(input_video)
    frame_rate = int(vidcap.get(cv2.CAP_PROP_FPS))
    total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / frame_rate

    frame_count = 0
    success, image = vidcap.read()

    while success:
        frame_count += 1
        elapsed_time = frame_count / frame_rate
        if elapsed_time % interval_seconds == 0:
            frame_path = os.path.join(
                output_folder, f"{video_name}_frame_{frame_count}.jpg"
            )
            print(f"Writing frame {frame_count} to {frame_path}")
            cv2.imwrite(frame_path, image)
        success, image = vidcap.read()

    vidcap.release()


if __name__ == "__main__":
    for video_file in video_files:
        video_name = os.path.splitext(video_file)[0]
        video_path = os.path.join(videos_dir, video_file)
        output_video_dir = os.path.join(output_dir, video_name)

        extract_frames(video_path, output_video_dir, video_name, desired_interval)

    print("Frames extraction completed.")
