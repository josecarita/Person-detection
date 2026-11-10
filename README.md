# 🛗 Elevator Person Detection

> Detects whether there is at least one person inside an elevator and sets a Raspberry Pi GPIO output, so the elevator controller can act on it.

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-HOG%20%2B%20SVM-5C3EE8?logo=opencv&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?logo=raspberrypi&logoColor=white)

## Use case

An elevator needs a simple condition: **is someone inside or not?** For example, to avoid sending an empty car, to turn lights/ventilation off, or to confirm the car is empty before a maintenance action. A camera plus a Raspberry Pi provides that signal without extra sensors.

## How it works

1. The camera frame is processed with OpenCV's **HOG descriptor + pre-trained SVM people detector**.
2. Each detected person is drawn with a bounding box.
3. If at least one person is detected, **GPIO pin 7 (BOARD) goes HIGH**; otherwise it stays LOW. This pin can drive a relay or an input of the elevator controller.

```
Camera ─► HOG + SVM ─► person? ─► GPIO 7 HIGH / LOW ─► elevator controller
```

## Run

```bash
pip install opencv-python numpy RPi.GPIO
python detectperson2.py   # press q to quit
```

## Next steps

- [ ] Replace HOG with a lightweight deep model (e.g. MediaPipe or TFLite SSD MobileNet) for better accuracy with occlusions and crowded cars.
- [ ] Count people (occupancy) instead of a yes/no signal.
- [ ] Add a short time filter so one missed frame does not toggle the output.
