from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load an official model
model = YOLO("C:/Users/ADITYA/Desktop/Form OCR/runs/detect/train2/weights/best.pt")

source = "C:/Users/ADITYA/Desktop/Form OCR/augment7"

results = model(source, save_txt=True)
count = 0
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB output
    result.save(filename= "C:/Users/ADITYA/Desktop/Form OCR/resultview/"+ str(count) + ".jpg")
    count += 1