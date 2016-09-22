# boggle-solver-flask
boggle solver built on Flask, Angular JS, Bootstrap

# Summary:
I wrote a boggle solver in Python and wanted to see how easily I could build a web app using Flask, Angular JS and Bootstrap.
The Flask backend acts as REST endpoints to get random boards and solutions to the board while the frontend uses Angular to make requests to the backend.

# Boggle Solution:
Found a scrabble dictionary online and used it to build a Trie. Recursively explores paths on boggle board to find words using the Trie to return on paths that do not lead to valid words. 

Solution currently builds the trie and stores as a global Flask object. Requests to solve api will use the global Trie object to find words.

# Functionality:
- User can choose the size of the boggle board from 4x4 to 7x7 which will generate a random boggle board of that size
- User can click the random button to generate new random board of currently selected size
- User can click the solve button to display a list of words found on the board

# Improvements:
- Consider using Redis to store the trie
- Allow user to enter boards
- Include more stats to user ex: amount of points on the board and how much points each word is worth
