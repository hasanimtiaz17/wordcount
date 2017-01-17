# Wordcount Program Challenge


There has been several iteration of the base wordcount.py program. Here are the descriptions as follows

## Phase 1

**wordcount_1.py:**This is the first quick code up to with many assumptions in place. This does not take account for punctuation marks, capitalization and other features.This inputs the alice.txt directly from the url
  <br />**wordcount_2.py:**This part only adds a sys input method so the text can be piped through to the program from the local directory.
 <br />**wordcount_3.py:** This part changes all text to lowercase and removes punctuation marks
  <br />**wordcount_4.py:** This part add another layer to ensure all punctuation marks are removed
  
**Map Reduce Implementation** In this part a mapper and reducer was created. In the implementations before this, it was assumed that the program will be stored in system memory. Using a map reduce framework allows the program to be run on a hadoop or Spark environment.

**Output and Documentation** Please refer to the several output files for each run. Output includes the output run from each wordcount version as well as the map reduce version.

## Phase 2

**wordcount_5.py:** For this implementation, user is asked two prompts 1) Define Prefix, 2) Enter text URL. The program then collects the text, processes it and stores it in a pandas dataframe. If any of the words starts with the Prefix defined, then the words and count is printed on the screen,seperated by a comma


## Phase 3

This is the last part of the challenge. To deploy the program on a webserver, flask and heroku was used. AWS was also implemented but heroku proved to be a cost-effective implementation. The server was also connected with HTML and Javascript in the front-end. The link to the program is https://wordcount-challenge.herokuapp.com 



## Contact

For any questions, contact me at hasanimtiaz17@gmail.com or call me at 713-412-9382
