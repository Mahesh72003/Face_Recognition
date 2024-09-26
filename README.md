

# Face Recognition using OpenCV and Deep Learning

This repository contains an implementation of a **Face Recognition System** using **OpenCV** and deep learning models. The system can detect and recognize faces from live video feeds or static images.

## Features
- **Face Detection**: Uses a pre-trained deep learning model to detect faces in images or video frames.
- **Face Recognition**: Identifies faces by comparing them with known face encodings.
- **Image and Video Support**: The system works with both image files and live video streams.
- **Model Training**: Supports adding new faces to the system by training on labeled images.

## Technologies Used
- **OpenCV**: For capturing video, image processing, and face detection.
- **Dlib**: For face recognition and facial landmark detection.
- **Deep Learning Models**: Pre-trained models are used for high accuracy face recognition.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mahesh72003/Face_Recognition.git
   cd Face_Recognition
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Install **Dlib** and **OpenCV**:
   ```bash
   pip install dlib
   pip install opencv-python
   ```

## Usage

1. **Face Detection**:
   Run the script to detect faces in real-time using your webcam:
   ```bash
   python face_detection.py
   ```

2. **Face Recognition**:
   Add known faces to the system and recognize faces from video streams:
   ```bash
   python face_recognition.py
   ```

3. **Training New Faces**:
   Place the images of new faces in the `known_faces` folder, labeled with the person's name. The system will automatically encode these faces.

## Folder Structure
- `known_faces/`: Directory for storing labeled images of known individuals.
- `face_detection.py`: Script for detecting faces in real-time.
- `face_recognition.py`: Script for recognizing faces from a video feed.
- `requirements.txt`: Contains all the dependencies needed to run the project.

## Dependencies
- Python 3.6+
- OpenCV
- Dlib
- face_recognition
- NumPy
