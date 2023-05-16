import cv2

# Open the video file
video = cv2.VideoCapture('opencv_video.mp4')

# Get video properties
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object
output_filename = 'reversed_video.mp4'
codec = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(output_filename, codec, fps, (int(video.get(3)), int(video.get(4))))

# Read and write video frames in reverse order
for frame_number in range(total_frames - 1, -1, -1):
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = video.read()
    if ret:
        output.write(frame)
    else:
        break

# Release the video objects
video.release()
output.release()

# Display the output filename
print("Reversed video saved as:", output_filename)
