from ultralytics import YOLO
import pandas as pd

# 1. Load YOLO model
model = YOLO("yolov8m.pt")

# 2. Run detection + tracking on video
results = model.track(
    source="test_video_1.mp4",   # change if filename is different
    tracker="bytetrack.yaml",
    persist=True,
    stream=True,
    
)

# 3. Storage for extracted features
data = []

frame_number = 0

# 4. Iterate through video frames
for result in results:
    frame_number += 1

    if result.boxes is None:
        continue

    for box in result.boxes:
        # Tracking ID
        track_id = int(box.id[0]) if box.id is not None else -1

        # Class info
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        # Confidence
        confidence = float(box.conf[0])

        # Bounding box
        x1, y1, x2, y2 = box.xyxy[0].tolist()

        # Save row
        data.append([
            frame_number,
            track_id,
            class_name,
            confidence,
            x1, y1, x2, y2
        ])

df = pd.DataFrame(
    data,
    columns=[
        "frame",
        "track_id",
        "class",
        "confidence",
        "x1", "y1", "x2", "y2"
    ]
)


df.to_csv("tracking_output.csv", index=False)

print("✅ CSV created: tracking_output.csv")
    