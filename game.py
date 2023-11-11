from typing import Literal
import random


class Board:

    def __init__(self) -> None:
        self.board = {
            'empty': 9,
            1: ' ',
            2: ' ',
            3: ' ',
            4: ' ',
            5: ' ',
            6: ' ',
            7: ' ',
            8: ' ',
            9: ' '
        }

    def clear(self) -> None:
        """Отчистка поля
        """
        self.board = {
            'empty': 9,
            1: ' ',
            2: ' ',
            3: ' ',
            4: ' ',
            5: ' ',
            6: ' ',
            7: ' ',
            8: ' ',
            9: ' '
        }

    def print(self) -> None:
        board = "\n\n\n" \
            f"{self.board[1]} | {self.board[2]} | {self.board[3]}     1 | 2 | 3\n" \
            "--+---+--     --+---+--\n" \
            f"{self.board[4]} | {self.board[5]} | {self.board[6]}     4 | 5 | 6\n" \
            "--+---+--     --+---+--\n" \
            f"{self.board[7]} | {self.board[8]} | {self.board[9]}     7 | 8 | 9"
        print(board)

    def move(self, number: int, sign: Literal['X', 'O']) -> bool:
        """Ход

        Args:
            number (int): номер поля 1-9

            sign (Literal[&#39;X&#39;, &#39;O&#39;]): знак хода X или O

        Returns:
            bool: True - ход успешно выполнен. False - позиция занята.
        """
        if self.board[number] == ' ':
            self.board[number] = sign
            self.board['empty'] -= 1
            return True
        return False

    def check_winner(self) -> bool | str:
        """Проверка на победу

        Returns:
            bool | str: 'X' or 'Y' if win else False
        """
        X = [i for i in self.board if self.board[i] == 'X']
        O = [i for i in self.board if self.board[i] == 'O']
        wins_combs = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]
        ]
        for comb in wins_combs:
            if len(set(comb) & set(X)) == 3:
                return 'X'
            elif len(set(comb) & set(O)) == 3:
                return 'O'
        return False

    def check_draw(self) -> bool:
        """Проверка на ничью

        Returns:
            bool: True если все поля заняты и нету победителя, иначе False
        """
        return self.board['empty'] == 0 and not self.check_winner()


def computer(board: Board):
    X = [i for i in board.board if board.board[i] == 'X']
    O = [i for i in board.board if board.board[i] == 'O']
    null = [i for i in board.board if board.board[i] == ' ']
    wins_combs = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    for comb in wins_combs:
        intersect = set(comb) & set(O)
        if len(intersect) == 2:
            diff = list(set(comb).difference(set(O)))[0]
            if diff in null:
                board.move(diff, sign='O')
                break
    else:
        for comb in wins_combs:
            intersect = set(comb) & set(X)
            if len(intersect) == 2:
                diff = list(set(comb).difference(set(X)))[0]
                if diff in null:
                    board.move(diff, sign='O')
                    break
        else:
            if 5 in null:
                board.move(5, sign='O')
            else:
                for comb in wins_combs:
                    intersect = set(comb) & set(O)
                    diff = list(set(comb).difference(set(O)))
                    if len(intersect) == 1 and len(set(comb).intersection(set(X))) == 0:
                        if diff[0] in null:
                            board.move(diff[0], sign='O')
                            break
                        elif diff[1] in null:
                            board.move(diff[1], sign='O')
                            break
                else:
                    choice = random.choice(null)
                    board.move(choice, sign='O')

def game():
    board = Board()
    while True:
        board.print()
        player = int(input("Введите цифру (1-9): "))
        if board.move(player, sign='X'):
            winner = board.check_winner()
            if winner:
                board.print()
                print("Вы победили!" if winner == 'X' else "Победил компьютер!")
                board.clear()
                continue
            elif board.check_draw():
                board.print()
                print("Ничья!")
                board.clear()
                continue
            else:
                computer(board=board)
                winner = board.check_winner()
                if winner:
                    board.print()
                    print("Вы победили!" if winner ==
                        'X' else "Победил компьютер!")
                    board.clear()
                    continue
                elif board.check_draw():
                    board.print()
                    print("Ничья!")
                    board.clear()
                    continue
        else:
            print("Данная позиция занята!")

if __name__ == '__main__':
    game()
