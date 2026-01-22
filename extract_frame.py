import cv2
import os

# Video path
video_path = "test_video_1.mp4"

# Output folder
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

# Open video
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
print("Video FPS:", fps)

frame_count = 0
saved_count = 0

# Save 1 frame per second
while True:
    ret, frame = cap.read()
    if not ret:
        break

    if int(frame_count % fps) == 0:
        filename = f"img_{saved_count:04d}.jpg"
        cv2.imwrite(os.path.join(output_dir, filename), frame)
        saved_count += 1

    frame_count += 1

cap.release()
print(f"✅ Extracted {saved_count} frames into '{output_dir}' folder")

