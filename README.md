# Hack the Hourglass 2020
For the "Hack the Hourglass" hackathon

# SignToText - HealthCare and AI Project

![](https://img.shields.io/badge/DL-Deep%20Learning-blue)
![](https://img.shields.io/badge/CNN-Convolutional%20Neural%20Network-blue)
![](https://img.shields.io/badge/RNN-Recurrent%20Neural%20Network-blue)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1WTFBeIP7xogyvlGqog0sp3Te2xCmk1uN?usp=sharing)
![](https://img.shields.io/badge/Communication-Sign%20Language%20Translator-blue)
[![](https://img.shields.io/badge/Google%20-Drive-blue.svg)](https://drive.google.com/drive/folders/1NNaC6C3E_YpaLprPKT90RP1zo1pTcqYM?usp=sharing)
[![](https://img.shields.io/badge/Made%20with-Python-blue.svg)](https://www.python.org/)

# Table of Contents

- [Hack the Hourglass 2020](#hack-the-hourglass-2020)
- [SignToText - HealthCare and AI Project](#signtotext---healthcare-and-ai-project)
- [Table of Contents](#table-of-contents)
  - [About The Project](#about-the-project)
  - [What it Does](#what-it-does)
  - [Built With](#built-with)
  - [Dataset](#dataset)
  - [Usage](#usage)
  - [Tech Stack](#tech-stack)

## About The Project
Today, around Million of people use Sign Language as their main way to communicate. But, at the same time there are many people who don't know the Sign language. So, it becomes very hard for people to interact among themselves. We have created an application that will help Bridge the gap for those who have impaired hearing and who do not know sign language. 
Using this app, communication will be easier for both parties and people who have their voices drowned out will have a way to speak up.

## What it Does
SigntoText allows users to sign a word (full gesture) which is then translated into text. This allows people to communicate without having to fully learn sign language.

![Demo](./demo)

## Built With
  Machine Learning: This application is built with opencv,Google MediaPipe and an RNN Connected at Back of CNN . It segments the hand from the frame using masking techniques and Landmark Points are Extracted using Google Media Pipe. The Translation of the Sign is done using a Neural Network Model 
  which uses a CNN which recognizes the features of the image. These features are then fed into an RNN which checks the differences between high level frames and feeds Out the Sign being fired as Text.

## Dataset  
The sign [database](http://facundoq.github.io/unlp/lsa64/) was created with the goal of producing a dictionary for LSA and training an automatic sign recognizer, includes 3200 videos where 10 non-expert subjects executed 5 repetitions of 64 different types of signs. Signs were selected among the most commonly used ones in the LSA lexicon, including both verbs and nouns.

## Usage

1. Clone The Repo
2. Fire Up Terminal and Hit
   ```
   pip install -r requirements.txt 
   python3 predict.py
   ```
## Tech Stack

* [Keras](https://keras.io/) - The Machine Learning Api framework used for Training.

* [MediaPipe](https://google.github.io/mediapipe/) - Used To  Extract Landmark Points 
  and Features for tracking Hands.

* [Google Collab](https://colab.research.google.com/) -  Provided Us A Platform to train Our Model .

* [Python](https://www.python.org/) - The Programing Language Used to Drive various components of Our Project.

* [OpenCV](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html) - The Library used for Image-Processing .
  