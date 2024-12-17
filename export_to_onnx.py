from ultralytics import YOLO

model = YOLO(model="runs\\segment\\train3\\weights\\best.pt")

print(model.names)

model.export(format="onnx", imgsz=512, data="config.yaml")

print("Zakończono eksport modelu do ONNX")