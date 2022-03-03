import cv2
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def run():
    vidcap = cv2.VideoCapture('misc/test/test.mp4')

    count = 0
    success = True
    
    # Define the location for saving the preprocessed video
    new_vid = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('misc/test/new video.avi', new_vid, 20.0, (640,480))

    with tf.io.gfile.GFile("./weights/retrained_graph.pb", 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        while success:
            success,frame = vidcap.read()
            byte_im = cv2.imencode('.jpg', frame)[1].tobytes()
            label_lines = [line.rstrip() for line 
                    in tf.io.gfile.GFile("./misc/retrained_labels.txt")]

            # Processes on frames after every 0.2 seconds
            if count%5 == 0:
                predictions = sess.run(softmax_tensor, \
                        {'DecodeJpeg/contents:0': byte_im})
                
                # Sort to show labels of first prediction in order of confidence
                top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
                
                for node_id in top_k:
                    human_string = label_lines[node_id]
                    if human_string == "strobe":
                        score = predictions[0][node_id]
                        #print('%s (score = %.5f)' % (human_string, score))
                
            if score>0.85:

                # Convert the epileptic frames to gray-scale
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            count+=1
        
            # Display the video
            cv2.imshow("Live", frame)

            # Save as a new video
            out.write(frame)
        
            # Exit the loop
            key = cv2.waitKey(1)
            if key == ord("q"):
                break
            
    # Close all windows
    cv2.destroyAllWindows()
    out.release()
    vidcap.release()
