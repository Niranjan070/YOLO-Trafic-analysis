# 🚗 Vehicle Tracking & Analytics System

A Python-based vehicle detection and tracking system using **YOLOv8** object detection and **ByteTrack** multi-object tracking. This project processes video footage to detect, track, and analyze vehicle movement in real-time.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## ✨ Features

- **Real-time Object Detection**: Uses YOLOv8 for accurate vehicle and pedestrian detection
- **Multi-Object Tracking**: ByteTrack algorithm for persistent object tracking across frames
- **Comprehensive Data Export**: Exports tracking data to CSV for further analysis
- **Traffic Analytics**: Generates vehicle count statistics by class and time intervals
- **Visualization**: Creates bar charts showing vehicles per minute

---

## 📁 Project Structure

```
YOLO/
├── extract_tracking_to_csv.py   # Main tracking script - processes video and exports data
├── analyze_tracking.py          # Analytics script - generates statistics and visualizations
├── tracking_output.csv          # Generated tracking data (output)
├── test_video_1.mp4             # Sample video file for testing
├── yolov8m.pt                   # YOLOv8 Medium model weights
├── yolov8n.pt                   # YOLOv8 Nano model weights
├── runs/                        # YOLO output directory
└── venv/                        # Python virtual environment
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone/Download the project**

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**:
   ```bash
   pip install ultralytics pandas matplotlib
   ```

---

## 📖 Usage

### 1. Extract Tracking Data from Video

Run the extraction script to process your video file and generate tracking data:

```bash
python extract_tracking_to_csv.py
```

**What it does:**
- Loads the YOLOv8 model (`yolov8m.pt`)
- Processes each frame of `test_video_1.mp4`
- Applies ByteTrack for object tracking
- Extracts features: frame number, track ID, class, confidence, bounding box coordinates
- Saves results to `tracking_output.csv`

### 2. Analyze Tracking Data

After extraction, run the analysis script:

```bash
python analyze_tracking.py
```

**What it does:**
- Loads the CSV tracking data
- Filters for vehicle classes (car, truck, bus, motorbike, bicycle)
- Calculates unique vehicle counts
- Groups data by class and time intervals
- Generates a bar chart visualization of vehicles per minute

---

## 📊 Output Data Format

The `tracking_output.csv` contains the following columns:

| Column | Description |
|--------|-------------|
| `frame` | Frame number in the video |
| `track_id` | Unique tracking ID for each object |
| `class` | Detected object class (car, person, truck, etc.) |
| `confidence` | Detection confidence score (0-1) |
| `x1`, `y1` | Top-left corner of bounding box |
| `x2`, `y2` | Bottom-right corner of bounding box |

---

## 📈 Sample Analytics Output

```
Total rows: 6685
Unique vehicles: 15

Vehicles by Class:
class
car          8
truck        3
bus          2
motorbike    2

Vehicles per Minute:
minute
0    5
1    7
2    3
```

---

## ⚙️ Configuration

### Changing the Video Source

In `extract_tracking_to_csv.py`, modify the `source` parameter:

```python
results = model.track(
    source="your_video.mp4",  # Change to your video file
    tracker="bytetrack.yaml",
    persist=True,
    stream=True,
)
```

### Using Different YOLO Models

| Model | Size | Speed | Accuracy |
|-------|------|-------|----------|
| `yolov8n.pt` | Nano | Fastest | Lower |
| `yolov8s.pt` | Small | Fast | Good |
| `yolov8m.pt` | Medium | Balanced | Better |
| `yolov8l.pt` | Large | Slower | High |
| `yolov8x.pt` | XLarge | Slowest | Highest |

To change the model, modify:
```python
model = YOLO("yolov8n.pt")  # Use nano for faster processing
```

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'ultralytics'` | Run `pip install ultralytics` |
| Slow processing | Use `yolov8n.pt` instead of `yolov8m.pt` |
| Out of memory | Reduce video resolution or use smaller model |
| No detections | Check video path and ensure good lighting conditions |

---

## 📚 Dependencies

- **[Ultralytics](https://github.com/ultralytics/ultralytics)** - YOLOv8 implementation
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis
- **[Matplotlib](https://matplotlib.org/)** - Data visualization

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for the amazing YOLOv8 implementation
- [ByteTrack](https://github.com/ifzhang/ByteTrack) for the multi-object tracking algorithm

---

<p align="center">Made with ❤️ using YOLOv8</p>
