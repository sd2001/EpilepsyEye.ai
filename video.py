import cv2
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

vidcap = cv2.VideoCapture('test_video/AbstractRotating.mov')
fps = vidcap.get(cv2.CAP_PROP_FPS)
print(fps)
success,image = vidcap.read()
count = 0
success = True

# Unpersists graph from file
with tf.io.gfile.GFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')
    
max_strobe = 0
min_strobe = 100
time_process = {"0"}
strobe_threshold = 90

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    while success:
        success,frame = vidcap.read()
        if success:
            byte_im = cv2.imencode('.jpg', frame)[1].tobytes()
            label_lines = [line.rstrip() for line 
                    in tf.io.gfile.GFile("retrained_labels.txt")]

            if count%(0.4 * fps) == 0:  # processes on frames after every 0.4 seconds
                predictions = sess.run(softmax_tensor, \
                        {'DecodeJpeg/contents:0': byte_im})
                
                # Sort to show labels of first prediction in order of confidence
                top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                
                for node_id in top_k:
                    human_string = label_lines[node_id]
                    if human_string == "strobe":
                        score = predictions[0][node_id]
                        if score > max_strobe:
                            max_strobe = score
                        if score < min_strobe:
                            min_strobe = score
                            
                        if score < 80:
                            cv2.imshow('Frame', frame)
                        else:
                            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
                            cv2.imshow('Frame', frame)
                            
                        print('%s (score = %.5f)' % (human_string, score))

            count+=1
            print("time stamp current frame:",count/fps)
            
print(max_strobe, min_strobe)