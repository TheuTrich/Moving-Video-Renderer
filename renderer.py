import os
import urllib.request
from enum import Enum
import hashlib
import cv2
import numpy as np

input_video = "bad.mkv"

video = cv2.VideoCapture(input_video)

if video.isOpened():
    print('Video opened!\n')
else:
    print('Video closed!\n')

frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (frame_width, frame_height)
video_size = (int(frame_width), int(frame_height))
fps = video.get(cv2.CAP_PROP_FPS)
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

video_name, video_ext = os.path.splitext(input_video)
new_videoname = video_name + "_redered" + video_ext

try:
    os.remove(new_filename)
except:
    pass

new_video = cv2.VideoWriter(
    filename=new_videoname,
    fourcc=cv2.VideoWriter_fourcc(*'mp4v'),
    fps=fps,
    frameSize=video_size
)

windowName = 'Bad Apple'
cv2.namedWindow(windowName)

ret, frame1 = video.read()
prev_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
prev_final_frame = np.zeros_like(frame1)
hsv = np.zeros_like(frame1)
hsv[..., 1] = 255

frame_count = 1
while True:
    ret, frame2 = video.read()
    if not ret:
         print("Video render completed")   
         cv2.destroyWindow(windowName)
         video.release()
         break
    
    frame_count += 1
    
    print("Frame {}/{}".format(frame_count, total_frames))
    
    next_frame = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    flow = cv2.Canny(image=next_frame, threshold1=100, threshold2=200)
    flow_frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    motion_frame_bg = cv2.addWeighted(prev_final_frame, 0.8, np.zeros_like(prev_final_frame), 0.2, 0.0)
    motion_frame = np.clip(np.maximum(motion_frame_bg, flow_frame), 0, 256).astype(np.uint8)
    
    next_frame_bgr = cv2.cvtColor(next_frame, cv2.COLOR_GRAY2BGR)
    final_frame = np.clip(np.add(motion_frame, next_frame_bgr), 0, 256).astype(np.uint8)
    
    cv2.imshow(windowName, final_frame)
    
    final_video_frame = cv2.resize(final_frame, video_size, 0, 0, interpolation = cv2.INTER_NEAREST)
    
    new_video.write(final_video_frame)
    
    prev_final_frame = final_frame
    
    
    stop_playing = False
    waitKey = (cv2.waitKey(1) & 0xFF)
    if waitKey == ord('q'):
        stop_playing = True
    
    if stop_playing:
        print("Closed!")
        cv2.destroyWindow(windowName)
        video.release()
        break

#Save Video
new_video.release()
