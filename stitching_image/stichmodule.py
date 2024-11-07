from PIL import Image 
import cv2 
import os

def get_user_input():
    return input("Enter the path to the input video file: "), input("Enter the path to the output directory: ")

def stitch_images(image_paths):
    images = [Image.open(image_path) for image_path in image_paths]
    total_width = sum(img.width for img in images)
    max_height = max(img.height for img in images)
    stitched_image = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for img in images:
        stitched_image.paste(img, (x_offset, 0))
        x_offset += img.width
    return stitched_image