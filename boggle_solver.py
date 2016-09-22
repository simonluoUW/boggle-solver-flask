import Trie
import string
import random
from flask import Flask, render_template, jsonify, request

'''
Input parameters:
    board - lists of lists representing boggle board
    visited - representing which cells on board are visited during recursion
        visited[row][col] = 1 if cell visited else  visited[row][col] = 0
    result - set of words found on the board
    row - row currently visiting
    col - column currently visiting
    trie_node - trie node of current recursion

Explores neighboring cells for words
Returns if out of bounds of board, already visited cell, letter not in trie_node children
'''
def explore(board,visited,result,row,col,trie_node):
    if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0 or visited[row][col] == 1:
        return

    if board[row][col] == 'QU':
        if 'Q' in trie_node.children and 'U' in trie_node.children['Q'].children:
            cur_node = trie_node.children['Q'].children['U']
        else:
            return
    elif board[row][col] not in trie_node.children:
        return
    else:
        cur_node = trie_node.children[board[row][col]]

    if cur_node.word is not None:
        result.add(cur_node.word)

    visited[row][col] = 1
    for x in range(-1, 2):
        for y in range(-1, 2):
            explore(board, visited, result, row+x, col+y, cur_node)

    visited[row][col] = 0


'''
Input:
    board - list of lists of letters
-given boggle board explore all words starting at each cell on the board
-Uses Trie of boggle dictionary to return on paths not leading to actual words

Returns set of words found on the board
'''
def boggle_solver(board):
    root = trie.root
    word_list = set()
    visited = [[0 for x in range(len(board))] for x in range(len(board[0]))]
    for row in range(len(board)):
        for col in range(len(board[0])):
            explore(board, visited, word_list, row, col, root)

    return word_list

# build the trie
trie = Trie.build_trie()

app = Flask(__name__)

# serve main page
@app.route('/', methods=['GET'])
def main_app():
    return render_template('index.html')

# endpoint returns a random boggle board size nxn
# given size parameter n
@app.route('/api/random_board', methods=['POST'])
def random_board():
    data = request.get_json()
    size = int(data['size'])
    board_input = []

    for x in range(size):
        row = []
        for y in range(size):
            letter = random.choice(string.ascii_uppercase)
            if letter == 'Q':
                letter = 'QU'
            row.append(letter)
        board_input.append(row)

    return jsonify(board_input)


# endpoint returns list of found words
# given a boggle board (list of lists of letters)
@app.route('/api/solve', methods=['POST'])
def solve_boggle():
    data = request.get_json()
    board = data['board']
    word_list = boggle_solver(board)
    return jsonify(sorted(list(word_list)))

