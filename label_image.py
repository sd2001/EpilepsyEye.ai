import sys
import tensorflow.compat.v1 as tf
import cv2
import os

tf.disable_v2_behavior()
image_path = "test_images/th_test.png"

## Converting Image read by OpenCV to bytes
cv2_image = im = cv2.imread(image_path)
extension = os.path. splitext(image_path)[-1]
is_success, im_buf_arr = cv2.imencode(extension, cv2_image)
byte_im = im_buf_arr.tobytes()

## Read in the image_data(Now required after the above conversion)
# image_data = tf.io.gfile.GFile(image_path, 'rb').read()
# print(type(image_data))

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.io.gfile.GFile("retrained_labels.txt")]

# Unpersists graph from file
with tf.io.gfile.GFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': byte_im})
    
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))


"""
## Sources
1. Youtube - primary key - utube url
2. Local File system - video - frame encoding

## Approach 1(avoid)
00:00 - 10:15

2:09 - 2:16
2:10 - 2:15

## Approach 2(select)
make the eplilepsy frame non epilepsy

# pipeline
- Ask user 1. Youtube video 2. Video from local system
- Based on the choice, we'll select the process
- Get frames one by one and
- We check if frames are epileptic or not (dictionary - timestamp)
- If not, then continue
- If yes, then store the timestamp in MongoDB

- While we play, use'll ensure that this timestamp is skipped(dictionary)

Processing - opencv frame by frame processing

## TODO:
0. Convert frame to cv frame(Line 7 to 10)
1. Time skip
2. Streamlit video play
3. storing epilepsy to

4. Streamlit UI - 2 option : whether from filesystem or youtube video link(side bar)




# Schema
{
	"unique_id": "",
 	if timestamp in dict_name.keys()
		"timestamp": {
			"start": "end",
			"2:10": "2:15",
			"3:10": "3:18"
		}
}

"""