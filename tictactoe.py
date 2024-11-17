import streamlit as st
import numpy as np

def print_board(board):
    st.write("```")
    for row in range(3):
        st.write("|".join(board[row]))
        if row != 2:
            st.write("-----")
    st.write("```")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
            return True
    return False

def check_draw(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                return False
    return True

def evaluate(board):
    """Evaluates the current board state.
    Returns:
        1: Player X wins
        -1: Player O wins
        0: Draw
    """
    # Check rows, columns, and diagonals for a win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'X':
                return 1
            elif board[row][0] == 'O':
                return -1
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'X':
                return 1
            elif board[0][col] == 'O':
                return -1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
                return 1
            elif board[0][0] == 'O':
                return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 1
        elif board[0][2] == 'O':
            return -1
    # Check for a draw
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                return 0
    return 0

def minimax(board, depth, is_max):
    score = evaluate(board)
    if score != 0:
        return score

    if depth == 0:
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth - 1, not is_max))
                    board[i][j] = '-'
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth - 1, not is_max))
                    board[i][j] = '-'
        return best

def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                moveVal = minimax(board, 0, False)
                board[i][j] = '-'

                if moveVal > bestVal:
                    bestVal = moveVal
                    bestMove = (i, j)

    return bestMove

def main():
    st.title("Tic-Tac-Toe")
    board = np.array([['-' for _ in range(3)] for _ in range(3)])
    player = 'X'

    while True:
        print_board(board)

        if player == 'X':
            row, col = findBestMove(board)
            board[row][col] = player
            st.write(f"AI's turn: {row}, {col}")
        else:
            row = st.number_input("Enter row (0, 1, or 2): ", min_value=0, max_value=2, key="row_input")
            col = st.number_input("Enter column (0, 1, or 2): ", min_value=0, max_value=2, key="col_input")
            if board[row][col] == '-':
                board[row][col] = player
            else:
                st.write("Invalid move. Try again.")

        if check_win(board, player):
            print_board(board)
            st.write(f"{player} wins!")
            break
        elif check_draw(board):
            print_board(board)
            st.write("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

if __name__ == "__main__":
    main()
