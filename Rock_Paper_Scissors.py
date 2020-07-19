from tkinter import *
import random

root = Tk()
# set basics like title and icon
root.title('rock paper scissors')
photo = PhotoImage(file='Rock_Paper_Scissors_Image.png')
root.iconphoto(False, photo)

# creates quit button
quit_button = Button(root, text='quit game', bg='#2ec4db', padx=20, pady=20, command=root.quit)

# your results and what the cpu picked
results = Label(root)
cpu_result = Label(root)

computer_score = 0
your_score = 0

# code for rock button
def rock_input():
    global results
    global cpu_result
    global computer_score
    global your_score
    cpu_result.grid_forget()

    # how the computer randomly picks an option
    options = ['rock', 'paper', 'scissors']
    cpu = random.choice(options)
    cpu_result = Label(root, text=f'The computer chose {cpu}')
    cpu_result.config(font=('Courier', 15))

    # The labels and their configurations
    tie = Label(root, text="it's a tie")
    lose = Label(root, text='you lose')
    win = Label(root, text='you win!!!')
    cpu_score = Label(root, text=f'Computer score: {computer_score}')
    cpu_score.config(font=('Courier', 15))
    lose.config(font=('Courier', 44))
    tie.config(font=('Courier', 44))
    win.config(font=('Courier', 44))

    results.grid_forget()

    # if how the program responds to what the cpu picks
    # Decides if you win, lose, or tie.
    if cpu == 'rock':
        # Showing the necessary Labels and updating the scores if necessary.
        human_score = Label(root, text=f'your score {your_score}')
        human_score.config(font=('Courier', 15))
        human_score.grid(row=2, column=1)
        cpu_score.grid(row=3, column=1)
        cpu_result.grid(row=1, column=1)
        results = tie
        results.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)

    if cpu == 'paper':
        computer_score += 1
        cpu_score = Label(root, text=f'Computer score: {computer_score}')
        cpu_score.config(font=('Courier', 15))
        human_score = Label(root, text=f'your score {your_score}')
        human_score.config(font=('Courier', 15))
        human_score.grid(row=2, column=1)
        cpu_score.grid(row=3, column=1)
        results = lose
        cpu_result.grid(row=1, column=1)
        results.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)

    if cpu == 'scissors':
        your_score += 1
        human_score = Label(root, text=f'your score {your_score}')
        human_score.config(font=('Courier', 15))
        human_score.grid(row=2, column=1)
        cpu_score.grid(row=3, column=1)
        results = win
        cpu_result.grid(row=1, column=1)
        results.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)


# Command for paper button
def paper_input():
    global results
    global cpu_result
    global computer_score
    global your_score
    options = ['rock', 'paper', 'scissors']
    cpu = random.choice(options)
    cpu_result.grid_forget()
    cpu_result = Label(root, text=f'The computer chose {cpu}')
    cpu_result.config(font=('Courier', 15))
    tie = Label(root, text="it's a tie")
    win = Label(root, text='you win!!!')
    lose = Label(root, text='you lose')
    cpu_score = Label(root, text=f'Computer score: {computer_score}')

    cpu_score.config(font=('Courier', 15))
    lose.config(font=('Courier', 44))
    tie.config(font=('Courier', 44))
    win.config(font=('Courier', 44))
    results.grid_forget()

    if cpu == 'rock':
        your_score += 1
        win = Label(root, text='you win!!!')
        human_score = Label(root, text=f'your score {your_score}')
        win.config(font=('Courier', 44))
        human_score.config(font=('Courier', 15))
        human_score.grid(row=2, column=1)
        cpu_score.grid(row=3, column=1)
        results = win
        cpu_result.grid(row=1, column=1)
        results.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)

    if cpu == 'paper':
        human_score = Label(root, text=f'your score {your_score}')
        human_score.config(font=('Courier', 15))
        human_score.grid(row=2, column=1)
        cpu_score.grid(row=3, column=1)
        cpu_result.grid(row=1, column=1)
        results = tie
        results.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)

    if cpu == 'scissors':
        computer_score += 1
        cpu_score = Label(root, text=f'Computer score: {computer_score}')
        cpu_score.config(font=('Courier', 15))
        human_score = Label(root, text=f'your score {your_score}')
        human_score.config(font=('Courier', 15))
        human_score.grid(row=2, column=1)
        cpu_score.grid(row=3, column=1)
        results = lose
        cpu_result.grid(row=1, column=1)
        results.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)

# command for scissors button
def scissor_input():
    global cpu_result
    global results
    global computer_score
    global your_score

    options = ['rock', 'paper', 'scissors']
    cpu = random.choice(options)
    cpu_result.grid_forget()
    cpu_result = Label(root, text=f'The computer chose {cpu}')
    cpu_result.config(font=('Courier', 15))
    tie = Label(root, text="it's a tie")
    win = Label(root, text='you win!!!')
    lose = Label(root, text='you lose')
    cpu_score = Label(root, text=f'Computer score: {computer_score}')

    cpu_score.config(font=('Courier', 15))
    lose.config(font=('Courier', 44))
    tie.config(font=('Courier', 44))
    win.config(font=('Courier', 44))

    results.grid_forget()

    if cpu == 'rock':
        computer_score += 1
        cpu_score = Label(root, text=f'Computer score: {computer_score}')
        cpu_score.config(font=('Courier', 15))
        human_score = Label(root, text=f'your score {your_score}')
        human_score.config(font=('Courier', 15))
        human_score.grid(row=2, column=1)
        cpu_score.grid(row=3, column=1)
        results = lose
        cpu_result.grid(row=1, column=1)
        results.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)

    if cpu == 'paper':
        your_score += 1
        win = Label(root, text='you win!!!')
        human_score = Label(root, text=f'your score {your_score}')
        win.config(font=('Courier', 44))
        human_score.config(font=('Courier', 15))
        human_score.grid(row=2, column=1)
        cpu_score.grid(row=3, column=1)
        results = win
        cpu_result.grid(row=1, column=1)
        results.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)

    if cpu == 'scissors':
        human_score = Label(root, text=f'your score {your_score}')
        human_score.config(font=('Courier', 15))
        human_score.grid(row=2, column=1)
        cpu_score.grid(row=3, column=1)
        cpu_result.grid(row=1, column=1)
        results = tie
        results.grid(row=4, column=0)
        quit_button.grid(row=5, column=0)


# creates and grids the buttons
rock_button = Button(root, text='rock', bg='#a85032', padx=20, pady=15, command=rock_input)
paper_button = Button(root, text='paper', bg='white', padx=20, pady=15, command=paper_input)
scissors_button = Button(root, text='scissors', bg='#fc0a77', padx=20, pady=15, command=scissor_input)

rock_button.grid(row=1, column=0)
paper_button.grid(row=2, column=0)
scissors_button.grid(row=3, column=0)
quit_button.grid(row=4, column=0)

root.mainloop()
