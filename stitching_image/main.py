import cv2
from PIL import Image
import os
from stichmodule import get_user_input
from stichmodule import stitch_images

def main():
    video_path, output_dir = get_user_input()
    
    if not os.path.isfile(video_path) or not os.path.exists(output_dir):
        print("Error: Invalid input or output directory.")
        return
    frame_count = 0
    images = []

    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        image_path = os.path.join(output_dir, f"frame_{frame_count:04d}.png")
        cv2.imwrite(image_path, frame)
        images.append(image_path)
        frame_count += 20
    cap.release()

    if images:
        stitched_image = stitch_images(images)
        if stitched_image:
            stitched_image.save(os.path.join(output_dir, 'stitched_image.jpg'))
            print("Stitched image saved successfully.")
        else:
            print("Error: Failed to stitch images.")
    else:
        print("Error: No frames were extracted from the video.")



if __name__ == "__main__":
    main()
