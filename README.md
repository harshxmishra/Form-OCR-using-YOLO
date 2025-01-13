# Form-OCR-using-YOLO

This project implements a Form Optical Character Recognition (OCR) system using YOLOv8 for detecting signatures and handwritten text on forms.

## Overview

The project consists of several Python scripts that handle data generation, model training, and prediction:

- **`config.yaml`**: Configuration file for the YOLOv8 model, specifying the paths to training and validation data and the class names ("sign" and "handwritten").
- **`dataset_gen.py`**: This script generates augmented training data by applying various transformations to existing images. These transformations include flipping, adjusting brightness and opacity, rotating, and shearing. It reads images from a "New Folder" directory and saves the augmented images to an "augment" directory.
- **`photograph.py`**: This script creates synthetic form data by overlaying signature images onto form images. It uses OpenCV to remove backgrounds from signatures, resize them, and then place them on the form images.
- **`predict.py`**: This script loads a trained YOLOv8 model and performs inference on a directory of images. It saves the bounding box coordinates to text files and visualizes the predictions by saving the images with bounding boxes in a "resultview" directory.
- **`yolo.py`**: This script is used to train the YOLOv8 model. It loads a pretrained model and fine-tunes it using the dataset specified in `config.yaml`.

## Usage

1. **Prepare the Dataset**:
   - Place original form images in a directory named "with_photos".
   - Place signature images in a directory named "signatures".
   - Run `photograph.py` to generate synthetic training data with overlaid signatures in a "new_folder" directory.
   - Run `dataset_gen.py` to augment the images in the "new_folder" directory and save them to an "augment" directory.
   - Organize the augmented images into `images/train` and `images/val` directories as specified in `config.yaml`, along with their corresponding labels.

2. **Train the Model**:
   - Modify the `config.yaml` file with the correct paths to your training and validation data.
   - Run `yolo.py` to train the YOLOv8 model. The trained weights will be saved in the `runs/train/weights` directory.

3. **Run Predictions**:
   - Modify the `predict.py` script to point to the desired trained model weights and the directory of images you want to run predictions on.
   - Run `predict.py`. The prediction results, including bounding box coordinates, will be saved in the specified directories.

## Dependencies

- `ultralytics`
- `opencv-python`
- `matplotlib`
- `numpy`

## Directory Structure

```
Form-OCR-using-YOLO-main/
├── config.yaml
├── dataset_gen.py
├── photograph.py
├── predict.py
├── README.md
├── yolo.py
├── yolov8n.pt
├── images/
│   ├── train/
│   └── val/
├── runs/
│   └── train/
│       └── weights/
├── augment/
├── new_folder/
├── with_photos/
└── signatures/
```

**Note:** You may need to create the `images/train`, `images/val`, `runs`, `augment`, `new_folder`, `with_photos`, and `signatures` directories.

## Classes

- **0**: sign
- **1**: handwritten
