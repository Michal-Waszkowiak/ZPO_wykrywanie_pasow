from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt')

model.train(data='config.yaml', epochs=100, imgsz=512)

print("Zakończono trening modelu.") 