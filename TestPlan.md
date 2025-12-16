| **Feature** | **Expected Result** | **Actual Result** | **Pass/Fail** |
|--------------|--------------------|-------------------|---------------|
| **Homepage loads** | the homepage should load up with 2 buttons and match the colour scheme of the mockups | see figure 1 | ✅ Pass |
| **Navigate to play with freinds** |the page should load from the homepage to the play wiht freinds page and not break|see figure 2 | ✅ Pass |
| **Category page loads** | the category page should load up with no errors | see figure 3| ❌fail |
| **check if the game is compatible on phone**| the homepage should load fine in its correct dimensions on mobile layout |see figure 4| ✅ Pass|
| **check if the game is compatible on phone** | the create room/join room should be displayed correctly on phone layout|see figure 5| ❌fail|
| **check if the game is compatible on phone** |check to see if the actual hangman game loads up | see figure 6| ✅ Pass|
| **Create/Join Room buttons work** |The buttons should be usable and match with the layout |.see figure | ✅ Pass|
| **Input room code into space** | The space allows for letters for be inputted| .| ✅ Pass/❌fail|
| **create/join room matches colour scheme and buttons work** | the create/join page should be blue matching thecolour scheme as the rest of the game and the butons should work |see figure 7| ✅ Pass|
| **Game shows message when game ends** | When the game is over it will show message| See figure 8 |❌fail|
| **** |. | .| ✅ Pass/❌fail|

## Appendix for photos
**Figure 1** : <img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/76c22f4b-4487-4f7e-91d5-4e4164150d5e" />
the homepage loads successfully without any erros and the blue background is displayed correctly with the Hangman online title displyed in the middle of the screen. Both play online and play with freinds buttons are visible, aligned correctly and the layout does not crash.
<img width="294" height="59" alt="image" src="https://github.com/user-attachments/assets/75d9c435-4815-48f5-9568-ace9087cd5e0" />
this part in the pyhton code is what validates the correct rendering of the applications entry point

**Figure 2** <img width="959" height="539" alt="image" src="https://github.com/user-attachments/assets/5bc120e9-d150-4ffa-b089-29f1bcd01aac" />
The Create or Join Game screen loaded successfully after navigation from the homepage. The page displayed the expected heading along with options to create a room, join a room, and manually enter a room code. All elements were centred correctly on the screen, and no errors or layout issues were observed during loading. 

**Figure 3** <img width="959" height="538" alt="image" src="https://github.com/user-attachments/assets/0d1f014f-2346-4cb4-ac20-ecac2bc1f3f2" />
After the user creates the room their is a select category title however no options to chose from although the category file  is linked in the pyhton file. Howeber this is expected as category selection is handled on a seperate screen that will be created later. the game is being developed part by part so we are developing and testing as we go along.

**figure 4** <img width="959" height="478" alt="image" src="https://github.com/user-attachments/assets/661a859c-fab2-4a01-b59f-4b8427b3d9de" /> 
the hompeage sits perfectly o nthe iphone 14 pro max display with nothing moved around therefore this test result is successful 

**figure 5** <img width="958" height="479" alt="image" src="https://github.com/user-attachments/assets/f360ab62-5620-443d-a6c7-808ad0aa7d89" />
webpage loads however the create and join room part should not be in the corner, furthermore some styling needs to be done with the page to match the theme of the game 

**figure 6** <img width="959" height="480" alt="image" src="https://github.com/user-attachments/assets/640087ed-5e93-4511-9da1-6d2018cd8693" />
 the actual hangman game loads up onto the phone ui and the format is still the same although the size looks smaller however that may be because it is being tested on phone view on chrome on a laptop
 
**figure 7** <img width="919" height="479" alt="image" src="https://github.com/user-attachments/assets/da04f4da-0798-4bcc-8ad7-500681431009" />
the create/join page now matches the colour scheme of the game and has its buttons in the middle of the page making the layout look good on both desktop and mobile 




 ## 1st draft testing 
 **problems thoughout the python, HTML and javascript**
 1) <img width="590" height="169" alt="image" src="https://github.com/user-attachments/assets/a6357cdd-bac9-4744-9397-2e7146fe13d4" />
  the only id that is stored is current_player so the system cant tell which browser is allowed to guess

2) <img width="350" height="73" alt="image" src="https://github.com/user-attachments/assets/a389ee9d-7613-494a-b5f4-11e5d3584ad4" />
 there is no limit on how many users can join the room

3) <img width="346" height="65" alt="image" src="https://github.com/user-attachments/assets/aa30f1c1-a383-4b98-a438-01ae72c7712a" />
issues with polling

4) <img width="710" height="58" alt="image" src="https://github.com/user-attachments/assets/fcf596f7-16d9-47a3-b3d7-b7a7d0722b56" />
 the fixed width would cause trouble whoile scrolling on mobile 

 



 






