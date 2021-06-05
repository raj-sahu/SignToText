# Hack the Hourglass 2020
For the "Hack the Hourglass" hackathon

# SignToText - HealthCare and AI Project

![](https://img.shields.io/badge/DL-Deep%20Learning-black)
![](https://img.shields.io/badge/Rnn-Recurrent%20Neural%20Network-yellow)
![](https://img.shields.io/badge/Cnn-Convolutional%20Neural%20Network-lightgrey)
![](https://img.shields.io/badge/Communication-Sign%20Language%20Translator-blue)


## Table of Contents


* [About the Project](#about-the-project)
  * [What it Does](#what-it-does)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

## About The Project
Today, around million people use Sign Language as their main way to communicate. But, at the same time there are many people who don't know the sign language.So, it becomes very 
hard for people to interact among themselves. We have created an application that will help bridge the gap for those who have impaired hearing and who do not know sign language. 
Using this app, communication will be easier for both parties and people who have their voices drowned out will have a way to speak up.

### What it Does
SigntoText allows users to sign a word (full gesture) which is then translated into text. This allows people to communicate without having to fully learn sign language.

![Demo](./demo)

### Built With
* Machine Learning: This application is built with opencv. It segments the hand from the frame using masking techniques. The translation of the sign is done using a 
  deep neural network that uses a CNN which recognizes the features of the image. These features are then fed into an RNN which checks the differences between high level frames.

### Dataset Used :
The sign [database](http://facundoq.github.io/unlp/lsa64/) was created with the goal of producing a dictionary for LSA and training an automatic sign recognizer, includes 3200 videos where 10 non-expert subjects executed 5 repetitions of 64 different types of signs. Signs were selected among the most commonly used ones in the LSA lexicon, including both verbs and nouns.

## Built With (Tech Stack)

* [Keras](https://keras.io/) - The Machine Learning Api framework used for Training.

* [MediaPipe](https://google.github.io/mediapipe/) - Used To  Extract Landmark Points 
  and Features for tracking Hands.

* [Google Collab](https://colab.research.google.com/) -  Provided Us A Platform to train Our Model .

* [Python](https://www.python.org/) - The Programing Language Used to Drive various components of Our Project.

* [OpenCV](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html) - The Library used for Image-Processing . 
