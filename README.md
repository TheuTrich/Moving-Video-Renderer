# Moving-Video-Renderer
make your video with moving effect
## Required
1. Install required libraries
2. VERY IMPORTANT. Make sure you have **enough space** on your drive, other than it will **crash**. The 3 minutes 27 MB video can be rendered to 2GB. But don't worry much it has an ***acceptable render speed***.

## Input
1. Change the 'bad.mkv' to your video path(with extension)
2. At Ln: 66 Col: 56 ```motion_frame_bg = cv2.addWeighted(prev_final_frame, 0.8, np.zeros_like(prev_final_frame), 0.2, 0.0)``` you can see **0.8** number in the code, change it can make the effect faster or slower.
* 0: is not change(same as input)
* (>0) - (<1): bigger number makes it move slower
* 1: *Bad apple but if you pause you can't see*
* (>1): just don't.


The code looks bad I don't know to optimize it.
