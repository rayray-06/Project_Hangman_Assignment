# Project_Hangman_Assignment
This is a repo for our hangman project made up of a team of three. Rayyan, Maleeha and Bridget 
## Project overview
Our group has chosen to create an engaging, fun mobile version of the game Hangman. The idea is the classic game but adapted into an app with a touchscreen layout so that it can be used easily on a phone. The target audience for this application is teenagers and young adults aged 13–20, as this age group is a good fit for our game because they generally enjoy quick, casual and even competitive games anywhere, whether that be in class, on the bus or at home.
## Project specification 
The overall aim of this project is to make a simple and engaging mobile version of the classic hangman game aimed at users aged 13-20. The app will allow for players to guess letters using on screen buttons with each guess revealing the correct letters in the word, or reduce the number of attempts that remain. The multiplayer aspect of our game will let two players participate together through different devices. The first player needs to generate a room with a brief code which enables the second player to enter the room through their own device. The two devices will share the same game state through an online database system which shows letter guesses in real-time to both players. The design keeps the game basic while allowing two players to play together without sharing a single device.The app provides immediate feedback to players when they choose an incorrect answer. The game will show a basic results screen after players finish the word or use up all their attempts. The development of this application will use Python together with a mobile-friendly framework. This includes Kivy as a potential option. The project files will be stored and managed through GitHub.
## Target audience 
The project aims to serve young adults together with teenagers who fall within the age range of 13 to 20 years. A mobile Hangman game would suit this age group perfectly because they tend to enjoy quick and simple games that need no complex controls or extended instructions. Most people in this range already know how Hangman works, so the rules are very quick to understand.
## User profiles
<img width="567" height="362" alt="image" src="https://github.com/user-attachments/assets/d72b5e51-d698-4501-9d20-0f297d0b4d60" />
<img width="686" height="564" alt="image" src="https://github.com/user-attachments/assets/a8e107db-35f4-4ecd-ab16-9053390d058e" />



## Functional and nonfunctional requirements
### functional requirements 
- The system will allow for the game to start from he main menu
- The system will allow users to input thier own word to use for the other player
- The game will display blank lines taht wouold indicate the legnth of the word and everytime a letter is guessed correctly the letter would fill in the blank
- The game will reduce the number of attempts whne a player guesses wrong
- When a guess is incorrect the hangman ui will change
- The sysetm will not allow the same letter to be inputted twice
- The system should detect when all attempts have been used ad should display a you lose screen
- The system will allow one player to create an online room and another player to join using a code.
- Both players’ devices will share the same game state through an online database.
### nonfunctional requirements 
- The game should have a clear and visually apealling interface
-  All buttons and text should be formatted properly for mobile screen size
-  The system should be able to handle errors efficiently
-  The app shouldnt be too complicated so it does not use too much battery

## system requiremnets
### Hardware 
-  A mobile device that can run lightwieght mobile application, along with a touchscreen
-  The device has to be able to run python
-  The device has to have a standard screen size
-  Enough storage to install any neccesary files

### Software 
- A mobile friendly framework to run the game on
- connection to the internet to play multiplayer 

## Mock-ups (B)
...

## Basic storyboard 
<img width="1156" height="1521" alt="image" src="https://github.com/user-attachments/assets/7698678a-f3da-4896-8b82-6d41c943051d" />


## Potential risks to the project’s success: (not including time management)
1) Technical skill gaps: some users may not be familiar or have much experience with the software being used in this project which could lead to challenges while implementing certain features e.g multiplayer.
2) Multi player synchronisation issues: As the game is going to be running on different devices at the same time, there is a risk that the game states may become out of sync if the database doesn’t update correctly or quickly enough. 
3) Internet connection issues: Multiplayer mode relies on stable internet connection. if internet connection is slow or unstable for one user that could cause delays or incorrect game updates.
4) User interface challenges: If the ui is not designed clearly it users may be hard for users to navigate the game smoothly. Since the target audience is 13–20 clarity and simplicity are important.
5) Handling player disconnection: if one player leaves the game mid match the system might not be able to handle or recognize the disconnection which could distrupt the current game session.
6) Duplicate room codes: If the room code generator creates the same code twice by accident, two different games could end up sharing the same room and cause issues.
## Software development strategy
 For this project we wll be using an agile approach, this means that will be breaking down the woerkload into small steps rather than trying to finish everything at once. As a group. we will focus one part at time making sure its correct before moving onto the next part and we aim to do this throughout the project. This approach works well for our group because the project has different sections, like the UI, the game logic, and the multiplayer system. By working in short cycles, everyone can contribute to their part without waiting for someone else to finish first. It also makes it easier for us to fix problems early instead of discovering them at the end. Overall, using agile will help us stay flexible and improve the game as we develop.

## Flowchart(will complete later) (M)
...

## Game State Management(Will complete later) (R)
The multiplayer match in our game is managed via a straightforward state system. When two players enter the same room, they both attempt to guess the same word. The game begins in a waiting state until both players are connected, at which time it enters a playing state where each right guess earns the player one point. To keep both devices in sync, Firebase is used to update the shared game state, which includes disclosed letters, remaining attempts, and each player's score. The game is over and the scores are compared after the word is fully disclosed or all efforts are exhausted. If both scores are equal, the game is a draw; otherwise, the person with the greater score wins. The final state only displays the outcome to both players

## Contribution to Project
### Rayyan:
- Created the repo
- wrote up the project overview
- wrote up the project specification
- created a target audience for the game
- done functional requirements
- done non functional requirements
- done system software requirements
- done system hardware requirements
- created the structure for the readme file
- created a test plan that we can add to throughout the project
- delegating tasks to other team members and giving them deadlines to complete the work by
- Created and wrote up 6 potential risks to the projects success(not including time management)
- created and wrote up the software development strategy
- completing game state management 

### Bridget:
- Created one detailed user profile
-  Created the mockups
-  Created the basic storyboard of the game 

### maleeha:
- created one detailed  user profile 





