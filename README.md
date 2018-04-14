# ProductRecommendation
<b>MACHINE LEARNING</b>

It is one of the applications of machine learning.it Recommends the similar products based on users choice that he enters.<br>
This aplication is based on the electronics based products and to build this dataset i have made a dummy dataset of my own.This datasets does not belongs to any e-commerce websites.

<h2> CONTENTS </h2>

    1.Introduction.
    2.Requirements and Dependencies.
    4.How to run.
    5.Snapshots.
    6.Outputs
    7.References.
<h3> INTRODUCTION </h3>

![alt_tag](https://github.com/vshantam/ProductRecommendation/blob/master/screenshots/prs1.png)

This system allows us to recommend the similar kind of products which the user might be interested in , The recommendation is based on the type of products and its specifications is been provided by the user itself.<br>
The <b>algorithm </b> we used in this application is </b>Nearest Neighbors</b>.It  provides functionality for unsupervised and supervised neighbors-based learning methods. Unsupervised nearest neighbors is the foundation of many other learning methods, notably manifold learning and spectral clustering. Supervised neighbors-based learning comes in two flavors: classification for data with discrete labels, and regression for data with continuous labels.<br>

More Details can be found here :- http://scikit-learn.org/stable/modules/neighbors.html

<h3> REQUIREMENTS/DEPENDENCIES </h3>

            numpy >= 1.14.1
            pandas >= 0.22.0
            scikit-learn >= 0.19.1
            pyfiglet >= 0.7.5
            termcolor >= 0.0
            colorama >= 0.3.9

   To install the dependencies you can use pip/pip3 commands to install :
   
        pip install numpy #for python2
        pip3 install numpy #for python3
        
  Or you can use below command to install all dependencies automatically:
  
        apt-get update && dist-getupgrade; # to update the system.
        pip3 install -r req.txt
        
<h3> HOW TO INSTALL </h3>
To run this system please follow the below steps one by one :

<b> step 1: </b>
Clone this repository using the command:

        git clone https://github.com/vshantam/ProductRecommendation.git
Screenshot:
![alt_tag](https://github.com/vshantam/ProductRecommendation/blob/master/screenshots/output1.png)
        
 <b>step 2: </b>
 Change the directory to project repository .
    
        cd ProductRecommendation/
  Screenshot:
  ![alt_tag](https://github.com/vshantam/ProductRecommendation/blob/master/screenshots/output2.png)
  
  <b>step 3: </b>
  use python commands to run the scripts, i am using ipython version 3 that is why i will run the python scripts using ipython3 interpreter.
  
  commands:
  
            ipython3 recom.py # It will build the classifier.
            ipython3 main.py # main python script.
            
  screenshot:
  
  ![alt_tag](https://github.com/vshantam/ProductRecommendation/blob/master/screenshots/output3.png)
  
  ![alt_tag](https://github.com/vshantam/ProductRecommendation/blob/master/screenshots/output4.png)
  
<h3>OUTPUT</h3>
Dataset :

![alt_tag](https://github.com/vshantam/ProductRecommendation/blob/master/screenshots/dataset.png)

Final output:

![alt_tag](https://github.com/vshantam/ProductRecommendation/blob/master/screenshots/output5.png)

![alt_tag](https://github.com/vshantam/ProductRecommendation/blob/master/screenshots/output6.png)

<b><h2>REFERENCES</h2></b>

        [1] https://en.wikipedia.org/wiki/Recommender_system
        [2] https://en.wikipedia.org/wiki/Knowledge-based_recommender_system
        [3] https://cambridgespark.com/content/tutorials/implementing-your-own-recommender-systems-in-Python/index.html
       

<b><h4>NOTE:</h4></b> Make sure you type the product details correctly(spelling) and the specifications which are present in the dataset.

This application is built on Linux based system, it will be best to run on the same but it may run on windows also(not tested yet,soon will be updated.)
