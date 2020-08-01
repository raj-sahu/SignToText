# Hack the Hourglass 2020
For the "Hack the Hourglass" hackathon

# SigntoText - HealthCare and AI Project

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

### Built With
* Machine Learning: This application is built with opencv. It segments the hand from the frame using masking techniques. The translation of the sign is done using a 
  deep neural network that uses a CNN which recognizes the features of the image. These features are then fed into an RNN which checks the differences between high level frames.
