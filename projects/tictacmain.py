import tictactoe as tc

print("TIC-TAC-TOE")
print("----------------------------------")
a = int(input("Press 1 to start game"))
while a == 1:
    tc.initialize()
    flag = True
    for i in range(9):
        if i % 2 == 0:
            x, y = map(int, input("Player 1 enter position in x y form").split())
            tc.insert('X', x, y)
            tc.display()
            if tc.check('X'):
                print("--------------------------------------------")
                print("\nCongratulations!!! Player 1 wins\n")
                print("--------------------------------------------")
                flag = False
                break
        else:
            x, y = map(int, input("Player 1 enter position in x y form").split())
            tc.insert('O', x, y)
            tc.display()
            if tc.check('O'):
                print("--------------------------------------------")
                print("\nCongratulations!!! Player 2 wins\n")
                print("--------------------------------------------")
                flag = False
                break
    if flag:
        print("\nGame is draw\n")
    a = int(input("\nEnter 1 to play again\nEnter any no. to exit\n"))
