# � Traffic Analysis using YOLOv8 (Custom Training + Tracking + Analytics)

## 📌 Overview

This project is an end-to-end computer vision pipeline built as a learning-focused implementation of object detection, tracking, data extraction, and analytics using YOLOv8.

The goal was not just to detect objects, but to understand the full lifecycle of a real-world ML system:

- detection → tracking → structured data → analysis
- dataset creation → labeling → training → evaluation
- debugging real issues instead of relying on prebuilt demos

---

## 🎯 What This Project Does

- Detects vehicles in traffic videos using YOLOv8
- Tracks vehicles across frames using ByteTrack
- Assigns unique tracking IDs
- Extracts tracking data into a CSV file
- Performs traffic analytics using Python
- Trains a custom YOLOv8 model using a self-labeled dataset
- Reuses the same tracking + analytics pipeline with the custom model

---

## 🧠 Key Learnings

- How YOLO assigns detection confidence and bounding boxes
- How tracking IDs work and why they may change
- Why data quality matters more than model size
- How dataset structure and `data.yaml` affect training
- How to debug real-world ML pipeline issues
- How to design a modular and reusable ML system

---

## �️ Tech Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- ByteTrack
- Pandas
- Matplotlib
- Roboflow (dataset labeling & export)

---

## � Project Structure

```
YOLO/
├── dataset/
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   ├── labels/
│   │   ├── train/
│   │   ├── val/
│   │   └── test/
│   └── data.yaml
├── frames/                       # Extracted frames from video
├── runs/                         # YOLO training outputs
├── venv/                         # Virtual environment
├── extract_frames.py             # Frame extraction from video
├── extract_tracking_to_csv.py    # Detection + tracking → CSV
├── analyze_tracking.py           # Traffic analytics
├── yolov8n.pt
├── yolov8m.pt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install ultralytics opencv-python pandas matplotlib
```

---

## 🚗 Run Object Detection & Tracking

**Using pretrained YOLO:**

```bash
yolo predict model=yolov8n.pt source=test_video_1.mp4 show=True
```

**Using custom trained model:**

```bash
yolo predict model=runs/detect/train3/weights/best.pt source=test_video_1.mp4 show=True
```

---

## � Extract Tracking Data to CSV

```bash
python extract_tracking_to_csv.py
```

**Output:**
- `tracking_output.csv`

**Contains:**
- frame number
- track ID
- class label
- confidence
- bounding box coordinates

---

## 📈 Traffic Analytics

```bash
python analyze_tracking.py
```

**Analytics include:**
- unique vehicle count
- vehicle distribution
- vehicles per minute
- visual traffic flow graphs

---

## 🧪 Custom Dataset & Training

### Dataset Creation

- Frames extracted from traffic video
- Labeled using Roboflow
- Vehicle-only classes (car, truck, etc.)

### Training Command

```bash
yolo train model=yolov8n.pt data=dataset/data.yaml epochs=30 imgsz=640
```

**Trained model saved at:**
```
runs/detect/train3/weights/best.pt
```

---

## 📌 Results (Learning Phase)

- High recall on vehicle detection
- Clean tracking output
- End-to-end pipeline successfully validated

> **Note:** Dataset is intentionally small (learning-focused), so metrics are optimistic.
> The project emphasizes understanding and system design, not production accuracy.

---

## � Future Improvements

- [ ] Increase dataset size and diversity
- [ ] Add data augmentation
- [ ] Speed and lane-wise traffic analysis
- [ ] Multi-video aggregation
- [ ] Deployment using Flask / Streamlit
- [ ] Model export (ONNX / TensorRT)

---

## 📖 Motivation

This project was built as a **learning journey**, not just a demo.

The focus was on:
- understanding how things work internally
- fixing real errors
- building confidence in ML system design

---

## � Author

**Niranjan T**  
B.Tech AI & Data Science Student  
Interested in Computer Vision, Machine Learning & Real-world AI Systems

🔗 GitHub: [github.com/Niranjan070](https://github.com/Niranjan070)  
🔗 LinkedIn: [linkedin.com/in/your-profile]([https://linkedin.com/in/your-profile](https://www.linkedin.com/in/niranjan-t-79a6b7320/))
