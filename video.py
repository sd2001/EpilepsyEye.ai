import cv2

vidcap = cv2.VideoCapture('test_video/AbstractRotating.mov')
fps = vidcap.get(cv2.CAP_PROP_FPS)
print(fps)
success,image = vidcap.read()
count = 0
success = True

while success:
    success,frame = vidcap.read()
    count+=1
    print("time stamp current frame:",count/fps)