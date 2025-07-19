Objective 
1. Convert a video into frames (images). 
2. Use YOLOv8 to detect objects in each image. 
3. Save the detected images. 

Step 1: Install Required Libraries (Shell 1) 

pip install ultralytics opencv-python numpy pillow 

Step 2: Convert Video to Frames (Shell 2) 

import cv2 
import os 
# Set paths 
video_path = "input_video.mp4"  # Change to your video file 
output_folder = "output_frames" 
# Create output directory 
os.makedirs(output_folder, exist_ok=True) 
# Open video file 
cap = cv2.VideoCapture(video_path) 
frame_count = 0 
while cap.isOpened(): 
ret, frame = cap.read() 
if not ret: 
break  # End of video 
# Save frame as image 
frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg") 
cv2.imwrite(frame_path, frame) 
frame_count += 1 
cap.release() 
cv2.destroyAllWindows() 
print(f"Frames extracted: {frame_count}") 
This will save all video frames in output_frames/ folder. 

Step 3: Object Detection Using YOLOv8 (Shell 3) 

import os 
from ultralytics import YOLO 
# Load YOLOv8 model 
model = YOLO("yolov8n.pt")  # Ensure model file exists 
input_folder = "output_frames"  # Folder containing images 
output_folder = "detected_frames"  # Folder to save results 
# Create output directory 
os.makedirs(output_folder, exist_ok=True) 
# Process each image in the folder 
image_files = sorted([f for f in os.listdir(input_folder) if f.endswith((".jpg", ".png"))]) 
for i, img_file in enumerate(image_files): 
image_path = os.path.join(input_folder, img_file) 
if not os.path.exists(image_path): 
print(f"Skipping missing file: {image_path}") 
continue 
# Run YOLO detection 
results = model(image_path) 
# Save detected objects 
output_path = os.path.join(output_folder, f"detected_{i}.jpg") 
results[0].save(output_path) 
print("Object detection complete. Check the 'detected_frames/' folder.") 


This will detect objects in images and save the results in detected_frames/.
