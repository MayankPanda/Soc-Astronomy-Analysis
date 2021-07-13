# Soc-Astronomy-Analysis
<b>SOC: ASTRONOMICAL DATA MODELLING AND INTERPRETATION</b>

<b> INTRODUCTION: </b>

The Summer of Code project "Astronomical Data Modelling and Interpretation" provides insight into the application of Data Analysis and Image Processing in the understanding of Astronomical phenomenon and the ideas of dealing with large datasets and the special methods employed in handling them along with the basic principles of Image Processing and the aspects of Image Processing used in the field of Astronomical study formed the crux of the project. 

The Resources used were:
<ul>
  <li>
    https://www.tutorialspoint.com/python3/index.htm
  </li>
  <li>
    https://github.com/krittikaiitb/tutorials
  </li>
  <li>
    https://datatofish.com/plot-histogram-python/
  </li>
  <li>
    https://www.coursera.org/learn/data-driven-astronomy
  </li>
  <li>
    https://courses.planetary.org/p/imageclass
  </li>
  <li>
    https://astrobites.org/
  </li>
 </ul>
  
  
  



<i>WEEKWISE PROGRESS:</i>

<b>Week 0</b>:
Preliminaries of Python
Week 0 involved getting acquainted with the basics of Python in terms of data types, loops, lists etc. It also involved learning about Git and its basic functions and commands.

<b>Week 1</b>:
Basic Assignments
The assignment given in week 1 consisted of three problems namely:
<ol>
<li>
Histogram Making on rolling of two dice
</li>
<li>
Methodology of Data Analysis (Theoretical Question)
</li>
<li>
String Sorting on the basis of length
</li>
</ol>

<b>Learning Experiences:</b>
<ul>
<li>
The Histogram plotting function along with the attributes
</li>
<li>
Random number generation for probability distribution
</li>
<li>
Sorting Algorithm
</li>
</ul>

<b>Difficulties Faced:</b>

Combining two random numbers into a single unit and plotting a histogram out of this entity.
Getting acquainted with the basic nested loops without using braces as in C++ and using indentation to distinguish between inner and outer loops for string sorting program.

<b>Solutions:</b>

To generate a single unit I tried various approaches like combining two numbers into a list and using it and using double dimensional arrays but there were syntactical issues so I finally resorted to generate a string using the two numbers and then plotting histogram using strings
For the nested loops, due to improper indentation I was getting infinite loops so to tackle it I used print statements and comments at the loop area to figure out the issues and fixing bugs one by one, I made the correction in the loops.

<b>Week 2-6: Learning About Astronomy and Data Analysis</b>

Guided by the mentor to the Coursera course titled “Data Driven Astronomy”, I started learning about the underlying principles of Astronomy and how Data Analysis and proper handling of enormous amounts of data is crucial to get proper observations and get to the right conclusions.

<i>Course Week 1:</i>

Week 1 of the course involved description of a Pulsar- A neutron star which rotates at a fixed frequency releasing energy in the form of radio waves. The week also involved the concept of Image stacking wherein we learn how to get clear information from an image by increasing the Signal/Noise ratio.

Week 1 involved both mean and median stacking and we were also taught about the high storage requirements for Median Stacking and using histogram to implement median stacking without storing all Data at once.

<i>Course Week 2:</i>

Week 2 of the course revolved around the principles and the implementation of Cross Matching.Say, we use Optical Survey and Radio Survey then in Optical Survey we detect light coming from far off objects and in Radio Survey we detect radio waves. Using Cross Matching we define Radio Waves and Light waves property for each galaxy/object and learn more about the object.

We implement Cross Matching using various algorithms. If we use the naive algorithm then we get O(nm) time complexity which can take days for a large enough data set. To improve this if we impose certain conditions on the algorithm then we can do the work in half the time but this algorithm is still slow as it takes several days.

To handle large data sets we can use the astropy module and implement its cross matching function. For a data set which takes 10 days for the improved Cross Match algorithm the cross matching can be done in 20-30 seconds using this function.

This function is relatively much faster as it uses a data structure known as K-d tree.

<i>Course Week 3:</i>

Week 3 of the course took up the example of discovering Exoplanets by using the transit method. Due to low probability of a proper transit alignment, a large number of stars are observed.

Major analysis of this data about Exoplanets is done using DBMS like SQL which can filter data out by implementing Queries. We can also improve our analysis by using two or more tables and using the Join Command of SQL to combine them into one entity using a common attribute and studying them.

<i>Course Week 4:</i>

Week 4 of the course explores various ways of storing and retrieving Data in terms of using flat files or Relational Databases or Non-Relational Databases. The platform used depends upon the scale of Data and the usage.

When we use Databases, we do not implement or care about the storage of data or the type of Data Structure used or how the algorithms behind implementing the queries. This is a very common aspect of many software applications known as Abstraction wherein inner functional details are hidden from the user.

One common Astronomical Analysis is of the Star Clusters using Hertzsprung-Russell diagrams which involve plotting Luminosity vs Temperature of stars and classifying them. 

<i>Course Week 5:</i>

Week 5 delves into the aspect of measurement of stellar distances and how even parallax doesn't work here so we use red shift of a star reaching the telescope to find its distance. We use Supervised learning to calculate redshift using redshift-distance datasets.

<i>Course Week 6:</i>

The content of Week 6 covers the classification of galaxies. Galaxies can be classified using various parameters depending on the underlying aim of the classification and the factors normally used are shape, colour, merging factor etc. The act of classification of galaxies is automated using a random forest classifier from the scikit-learn library of Python based on certain features of the galaxy found out using various measurement methods.

Using K-folds validation, we obtain the accuracy of the classifier.  

Further using a confusion matrix, we check the overall accuracy, precision and recall of the model.


<b>Week 6: Image Processing</b>

After the Coursera course on Data Driven Astronomy, out of various further options
given by my mentor I decided to  go forward with Image Processing. The resource given to me was the Image Processing Course on Planetary Courses website.

As a part of introduction to Image Processing, I learnt how images are not merely snapshots but are made up of millions of pixels each having a pixel value which leads to even the simplest of images being a collection of many data points and analyzing this data is the crux of Image Processing.

<i>Course Lecture 1</i>

In the first lecture and demonstration using GIMP, I learnt how we can generate Images by assigning colour to pixel values and further analyse the image. The first lecture dealt with assigning grayscale to images thereby generating black and white or monochrome images from Pixel Values.

<i>Course Lecture 2</i>

The second lecture demonstrates how computers store images in terms of greyscale and the more bits we allow for each pixel, more grey levels we have to generate a better representation of the image although for human eye grey levels differentiated in 8 bits are the maximum we can differentiate between. For any image we can also generate a histogram of pixel values which will depend on the colours in the image itself and we can also manipulate the histogram to change properties of image

<i>Course Lecture 3</i>

The third lecture explains various practices acceptable and commonly used in Scientific Image Processing like Multiplying or Adding a Constant to Pixel values, cropping ,blurring, sharpening, downsampling and removing geometric distortions. Practices like adding or removing elements from images are not acceptable as a part of Scientific Image Processing.

<i>Course Lecture 4</i>

Fourth Lecture explains Light Levels and Exposure and how variation in these two parameters changes the image we get. The Space Cameras have a factor known as aperture which determines the light levels that can be captured. The Exposure time is generally varied depending on the surface reflection from the object being captured.

<i>Course Lecture 5</i>

Fifth Lecture delves into the various Image Formats used and Lossless and Lossy formats depending on the preservation of pixel values on repeated saves and openings. The Lecture also discusses image compression details

<i>Course Lecture 6</i>

Sixth lecture explains Resolution and its various interpretations and it also shows Upsampling and Downsampling of images to change it.

<i>Course Lecture 7</i>

Seventh lecture shows the different kinds of Datasets which contain images. There are mainly three types of sets: Captioned Images, Raw Images and Archival Images. Captioned images are generally seen in press releases wherein the image which is processed for the general public and having a caption is contained. The Raw images are the ones which are sent by the spacecraft or slightly processed versions of those stored and published as JPEG, PNG files meant for enthusiasts. Archival Data contains the original images with appropriate metadata and a lot of other relevant information from various space missions.



