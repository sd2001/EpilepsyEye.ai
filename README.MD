

<div align="center"> 
  <p align='center'> 
   <img src="https://img.shields.io/badge/Name%20-%20Epilepsy_Eye.ai-darkgreen?style=for-the-badge"/>
   <img src="https://forthebadge.com/images/badges/built-with-love.svg" />
   <img src="https://img.shields.io/badge/By-Team_Return_False-blue?style=for-the-badge" /><br>
   <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" />
	<br>
</div>
	


## Detect seizure inducing videos using Tensorflow - Background
<hr>

Earlier in March 2017, there was a lot of [news coverage](https://www.nytimes.com/2017/03/17/technology/social-media-attack-that-set-off-a-seizure-leads-to-an-arrest.html) about an incident in the social media. Journalist Kurt Eichenwald received a tweet that stated `"YOU DESERVE A SEIZURE FOR YOUR POSTS"`. The Journalist who suffered from epilepsy, got a seizure by looking at the image.

This incident has shown how social media could potentially be used as a terror weapon to inflict immediate physical pain and suffering to unsuspecting victims. Email, websites with user generated content are equally vulnerable to such attacks. In  2008 a hacker [defaced the website of the Epilepsy Foundation](http://www.cbsnews.com/news/epilepsy-site-hacked-with-seizure-images/) and inserted flashing images which caused multiple health incidents to unsuspecting victims.

It is important for sites with user generated content to acknowledge this and take preventive action. Machine Learning can be applied to automatically detect images causing strobe behavior and block them.
<br><br>
<div align="center">
  </p>
  <p>
  <img src="https://img.shields.io/badge/Vision%20%7C%20No one deserves a seizure from social media.-lavenderblush?logo=Product%20Hunt&style=for-the-badge" height="35"/>
  <br><br>
  <img src="media/product_vision.png" />
  </p>
  <br>
 </div>
 
<div align="center"> 
  <img src="https://img.shields.io/badge/Why%20%7C%20What%20it%20does-darkslategrey?logo=Windows%20Terminal&style=for-the-badge" height="40"/> 
  <br><br>
  <img src="media/objective.png" />

</div>

 <div align="center">
 <p>
 <br>
   <img src="https://img.shields.io/badge/License-MIT-yellow.svg?logo=Microsoft%20Word&style=for-the-badge" height="40"/><br>
   <br><strong>EpilepsyEye.ai</strong> is available under MIT License, read the LICENSE file for more info
  <p>
 </div>
 <br>

<div align="center"> 
  <img src="https://img.shields.io/badge/Product%20Images-mediumseagreen?logo=Pinterest&style=for-the-badge" height="40"/> 
</div>
  <br>
 
  
<div align="center"> 
  <img src="https://img.shields.io/badge/Prerequisites-teal?logo=Pinboard&style=for-the-badge" height="40"/> 
</div>
  <br>

  ```
  Python 3.7 and above

  Get it from: <https://www.python.org/downloads/>
  ```
<br>
  
<div align="center"> 
  <img src="https://img.shields.io/badge/Setting%20up%20locally-purple?logo=visual-studio-code&style=for-the-badge" height="40"/> 
</div><br>

   ```
   git clone https://github.com/<your-username>/EpilepsyEye.ai.git   
   ```   

   ```
   cd EpilepsyEye.ai
   ```

   ```
   pip install virtualenv
   python -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

   ```
   bash run.sh
   ```
  
<div align="center"> 
  <img src="https://img.shields.io/badge/Tech%20Stack%20Used-chocolate?logo=Tesla&style=for-the-badge" height="40"/> 
</div>
  <br>

  ```
  Python

   - OpenCV
   - Tensorflow
   - youtube_dl
   - Streamlit
  ```

  ```
  Technical Details
--
TensorFlow is a an open source library for building machine learning models. In our case we will use an existing model and retrain it to detect seizure inducing images.This is called transfer learning. The popular Inception v3 model trained on [ImageNet](http://image-net.org/) is used as the base model.

1. TensorFlow is installed on docker. the image used is gcr.io/tensorflow/tensorflow:latest-devel
2. Use [Fatkun Batch Image downloader](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en) for chrome to search and download images of flashing strobe lighting.
3. Follow the instructions in [Google Code Labs](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets) to retrain your model.
  * With 500 Iterations, Final test accuracy was 86.8%
  * With 4000 Iterations, Final test accuracy improved to 91.5% and that is the model uploaded here as [retrained_graph.pb](https://github.com/asasidh/Seizure-Detection-Tensor-Flow/blob/master/retrained_graph.pb)
4. Download test images to validate the trained model. Since I used google images to batch download training images, I decided to use bing image search for the test images. Couple of test images are uploaded under the `test_images` folder.

  ```
  
  <div align="center"> 
  <img src="https://img.shields.io/badge/Contributors-black?logo=Github&style=for-the-badge" height="40"/> 
</div>
  <br>

    
<div align="center"> 
  <table>
<tr align="center">

<td>

Swarnabha Das

<p align="center">
<img src = "https://avatars.githubusercontent.com/sd2001"  height="120" alt="Swarnabha Das">
</p>
<p align="center">
<a href = "https://github.com/sd2001"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/swarnabha-das-2001official/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
</table>
</tr>
</div>


  
  
<div align="center">
  <img src="https://img.shields.io/badge/Please%20star%20if%20you%20like%20it-lightcoral?logo=Starship&style=for-the-badge" width="300" height="35"/>
 </div>



Technical Details
--
TensorFlow is a an open source library for building machine learning models. In our case we will use an existing model and retrain it to detect seizure inducing images.This is called transfer learning. The popular Inception v3 model trained on [ImageNet](http://image-net.org/) is used as the base model.

1. TensorFlow is installed on docker. the image used is gcr.io/tensorflow/tensorflow:latest-devel
2. Use [Fatkun Batch Image downloader](https://chrome.google.com/webstore/detail/fatkun-batch-download-ima/nnjjahlikiabnchcpehcpkdeckfgnohf?hl=en) for chrome to search and download images of flashing strobe lighting.
3. Follow the instructions in [Google Code Labs](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets) to retrain your model.
  * With 500 Iterations, Final test accuracy was 86.8%
  * With 4000 Iterations, Final test accuracy improved to 91.5% and that is the model uploaded here as [retrained_graph.pb](https://github.com/asasidh/Seizure-Detection-Tensor-Flow/blob/master/retrained_graph.pb)
4. Download test images to validate the trained model. Since I used google images to batch download training images, I decided to use bing image search for the test images. Couple of test images are uploaded under the `test_images` folder.


Notes
----
The animated gif needs to be converted to a jpg image for the  model to work on it. This can be easily accomplished in the command line using [ImageMagick](https://www.imagemagick.org/script/index.php).


Credits
-------
* [Google Code Labs - TensorFlow for Poets](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets)
* [Build a TensorFlow Image Classifier in 5 Min](https://youtu.be/QfNvhPx5Px8)
* [Smashing Security Podcast coverage of tweet incident](http://smashingsecurity.libsyn.com/013-assault-with-a-deadly-tweet)
