# 🚗 Traffic Vehicle Detection & Tracking System

A deep learning-based vehicle detection and tracking system built with **YOLOv8** trained on a **custom dataset** for traffic analysis. This project implements real-time multi-object tracking using **ByteTrack** to detect, track, and analyze vehicle movement from video footage.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Custom_Trained-00FFFF.svg)
![Deep Learning](https://img.shields.io/badge/Deep_Learning-PyTorch-EE4C2C.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🎯 Project Highlights

- **Custom-Trained Model**: YOLOv8 fine-tuned on a curated traffic dataset for improved accuracy on road vehicles
- **5 Vehicle Classes**: Specialized detection for cars, trucks, buses, motorbikes, and bicycles
- **Real-Time Tracking**: ByteTrack algorithm ensures persistent object tracking across video frames
- **Traffic Analytics**: Automated statistics generation with vehicle counts, class distribution, and temporal analysis
- **Data Export**: Comprehensive CSV output for further analysis and integration

---

## 🏷️ Custom Model Classes

The model was trained to detect the following vehicle categories:

| Class ID | Class Name | Description |
|----------|------------|-------------|
| 0 | 🚗 Car | Sedans, hatchbacks, SUVs, and similar passenger vehicles |
| 1 | 🚛 Truck | Commercial trucks, pickups, and heavy goods vehicles |
| 2 | 🚌 Bus | Public transport buses and coaches |
| 3 | 🏍️ Motorbike | Motorcycles and scooters |
| 4 | 🚲 Bicycle | Bicycles and e-bikes |

---

## 📁 Project Structure

```
YOLO/
├── 📄 extract_tracking_to_csv.py   # Main script - video processing & tracking
├── 📄 analyze_tracking.py          # Analytics - statistics & visualizations
├── 📄 extract_frame.py             # Utility - frame extraction from video
├── 📄 README.md                    # Project documentation
├── 📄 .gitignore                   # Git ignore rules
│
├── 📁 runs/                        # Training outputs & model weights [gitignored]
│   └── detect/
│       └── train3/
│           └── weights/
│               └── best.pt         # ⭐ Custom trained model weights
│
├── 📁 dataset/                     # Custom training dataset [gitignored]
│   ├── data.yaml                   # Dataset configuration
│   └── images/
│       ├── train/                  # Training images
│       ├── val/                    # Validation images
│       └── test/                   # Test images
│
├── 📁 frames/                      # Extracted video frames [gitignored]
├── 📄 tracking_output.csv          # Generated tracking data [gitignored]
└── 📁 venv/                        # Python virtual environment [gitignored]
```

> **Note:** Files marked with `[gitignored]` are excluded from version control due to their large size. See [Model Weights](#-model-weights) section for obtaining the trained model.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- CUDA-compatible GPU (recommended for training/fast inference)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/YOLO-Traffic-Analysis.git
   cd YOLO-Traffic-Analysis
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install ultralytics pandas matplotlib
   ```

4. **Download/Add the trained model weights**
   
   Place the custom trained model at:
   ```
   runs/detect/train3/weights/best.pt
   ```

---

## 🧠 Model Training

### Dataset Configuration

The model was trained using a custom dataset configured in `dataset/data.yaml`:

```yaml
train: images/train
val: images/val
test: images/test

names:
  0: car
  1: truck
  2: bus
  3: motorbike
  4: bicycle
```

### Training Command

To train your own model with a custom dataset:

```bash
yolo detect train data=dataset/data.yaml model=yolov8m.pt epochs=100 imgsz=640
```

### Training Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| Base Model | YOLOv8m | Medium-sized model for balanced speed/accuracy |
| Image Size | 640×640 | Standard YOLO input resolution |
| Classes | 5 | Traffic-specific vehicle categories |

---

## 📖 Usage

### 1. Run Vehicle Detection & Tracking

Process a video file to detect and track vehicles:

```bash
python extract_tracking_to_csv.py
```

**What this does:**
- Loads the custom-trained YOLOv8 model (`runs/detect/train3/weights/best.pt`)
- Processes each frame of the input video
- Applies ByteTrack for multi-object tracking
- Extracts: frame number, track ID, vehicle class, confidence, bounding box
- Exports results to `tracking_output.csv`

### 2. Analyze Traffic Data

Generate statistics and visualizations from the tracking data:

```bash
python analyze_tracking.py
```

**What this does:**
- Loads the CSV tracking data
- Calculates unique vehicle counts per class
- Groups data by time intervals (per minute)
- Generates a bar chart visualization

---

## 📊 Output Data Format

The `tracking_output.csv` contains the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `frame` | int | Frame number in the video |
| `track_id` | int | Unique tracking ID for each vehicle |
| `class` | str | Vehicle class (car, truck, bus, motorbike, bicycle) |
| `confidence` | float | Detection confidence score (0.0 - 1.0) |
| `x1`, `y1` | float | Top-left corner of bounding box |
| `x2`, `y2` | float | Bottom-right corner of bounding box |

### Sample Output

```csv
frame,track_id,class,confidence,x1,y1,x2,y2
1,1,car,0.92,120.5,200.3,280.1,350.7
1,2,truck,0.88,450.2,180.6,620.4,380.2
2,1,car,0.91,125.3,198.7,285.0,348.9
...
```

---

## 📈 Sample Analytics

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

### Changing the Input Video

In `extract_tracking_to_csv.py`, modify the `source` parameter:

```python
results = model.track(
    source="your_video.mp4",  # Change to your video file
    tracker="bytetrack.yaml",
    persist=True,
    stream=True,
)
```

### Using a Different Model

To use a different model (e.g., after retraining):

```python
model = YOLO("runs/detect/train5/weights/best.pt")  # Update path
```

---

## 🎥 Supported Video Formats

The system supports common video formats:
- `.mp4` (recommended)
- `.avi`
- `.mov`
- `.mkv`
- `.webm`

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: ultralytics` | Run `pip install ultralytics` |
| Model file not found | Ensure `best.pt` is in `runs/detect/train3/weights/` |
| Slow inference | Use GPU with CUDA support |
| Out of memory | Reduce video resolution or batch size |
| No detections | Check if video contains target vehicle classes |

---

## 📚 Tech Stack

| Technology | Purpose |
|------------|---------|
| [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) | Object detection framework |
| [ByteTrack](https://github.com/ifzhang/ByteTrack) | Multi-object tracking algorithm |
| [PyTorch](https://pytorch.org/) | Deep learning backend |
| [Pandas](https://pandas.pydata.org/) | Data manipulation & analysis |
| [Matplotlib](https://matplotlib.org/) | Data visualization |

---

## 🔮 Future Improvements

- [ ] Add speed estimation for vehicles
- [ ] Implement vehicle counting zones
- [ ] Real-time video streaming support
- [ ] Web dashboard for analytics visualization
- [ ] License plate recognition integration

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest new features
- 🔧 Submit pull requests

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for the YOLOv8 framework
- [ByteTrack](https://github.com/ifzhang/ByteTrack) for the multi-object tracking algorithm
- Open-source traffic datasets for training data inspiration

---

<p align="center">
  <strong>Built with 🚀 YOLOv8 | Custom Trained for Traffic Analysis</strong>
</p>
