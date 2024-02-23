# Face Detection using OpenCV

This is a Python script for real-time face detection using OpenCV library. It utilizes a pre-trained model named "haarcascade_frontalface_default.xml" for detecting faces in a live video stream from a webcam.

## Prerequisites

Before running the script, ensure you have the following installed:
- Python (3.x recommended)
- OpenCV library (`opencv-python`)

You can install the necessary libraries using pip:

```
pip install opencv-python
```

## Usage

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using the following command:

```
python Face_Detection.py
```

4. The script will open a window displaying the live video feed from your webcam.
5. Faces detected in the video stream will be highlighted with circles drawn around them.
6. Press the 'Esc' key to exit the program.

## Explanation

- The script begins by importing necessary libraries including `cv2` for OpenCV and `math`.
- It initializes the webcam capture using `cv2.VideoCapture(0)`.
- The script checks if the webcam is opened correctly. If not, it raises an error.
- Inside the main loop, it reads each frame from the webcam.
- Converts the frame to grayscale using `cv2.cvtColor()` since the face detection algorithm works on grayscale images.
- Utilizes the pre-trained Haar Cascade classifier for face detection. The classifier is loaded using `cv2.CascadeClassifier()`.
- `haar_cascade.detectMultiScale()` detects faces in the grayscale frame. It returns a list of rectangles representing the faces' positions.
- The script iterates through the list of faces detected and draws circles around them using `cv2.circle()`.
- The radius of each circle is calculated as half of the maximum dimension (width or height) of the detected face rectangle.
- Displays the processed frame with face detection rectangles in a window named "Camera" using `cv2.imshow()`.
- Waits for a key press using `cv2.waitKey(1)`. If the pressed key is 'Esc' (ASCII code 27), the loop breaks, and the program exits.
- After exiting the loop, it releases the webcam using `cap.release()` and closes all OpenCV windows using `cv2.destroyAllWindows()`.

## Files

- `Face_Detection.py`: The Python script for real-time face detection.
- `haarcascade_frontalface_default.xml`: Pre-trained Haar Cascade classifier file for face detection.

## Notes

- Ensure that you have proper lighting conditions for better face detection results.
- You may need to adjust the parameters in `haar_cascade.detectMultiScale()` for optimal performance depending on your environment and camera setup.

