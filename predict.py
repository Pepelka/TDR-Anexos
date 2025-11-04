from ultralytics import YOLO

model = YOLO("yolov11_custom.pt")

model.predict(source = "1.jpeg", show=True, save=True, conf=0.6)