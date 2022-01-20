# My-Portfolio--DMA


It is still a work in progress, but 650+ lines of code later I have the base for my project. The goal is to develop a program that can take two pieces of handwriting and compare them, to test if they were written by the same person. To do this I hope to use the linguistics used, the font unique to each person, the year the notes were written, and so on. Eventually, I would like to take this project to an auditory workspace, and compare recordings to test if it is the same voice based on pitch, speed, tone, vocabulary, emphasis, and so on. Of course the code I have currently can be optimized, and is incredibly messing as I am still learning and finding my way aroundd Data science and Machine learning (which I hope to incorporate a lot more in the future), but I am proud of what I have been able to learn and accomplish in these first 2 months. 


The main file, that is the most operable file is: "extractwordsdata.py"
All the other files are pieces of this main file, or slightly different versions of the code. 

The steps in my code are:
  1. input an image and turn all the letters into four points (the data). These four points represent the four corners of the letter (It's box).
  2. I put all these numbers into a dataset and then read them into lists for each letter of the word.
  3. I then run this a second time on another image, extracting like words and running the main analysis function on them. 
  4. I then compare the quantity of like values between the two words, if it meets the required quota for the person being the same to hold true it return: "It is the same person", otherwise it returns: "False".
