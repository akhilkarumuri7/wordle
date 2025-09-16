from typing import List
from letter_state import LetterState
from wordle import Wordle
import random
import tkinter as tk
from tkinter import messagebox


def getGuess():
  global wordle
  global wordInput
  
  if wordle.can_attempt:
    x = wordInput.get()

    if len(x) != wordle.WORD_LENGTH:
      messagebox.showerror("5 Character words only", "Please enter a word with 5 characters")
    else:
      wordle.attempt(x)
      display_results(wordle)
      if wordle.is_solved:
        messagebox.showerror("WINNER", "You Solved The Puzzle!")
      if wordle.remaining_attempts == 0 and not wordle.is_solved:
        messagebox.showerror("LOSER", f"You Lose! The word was {wordle.secret}")


  

def display_results(wordle: Wordle):
    print("\nYour results so far...")
    print(f"You have {wordle.remaining_attempts} attempts remaining.\n")

    lines = []
    guessNum=1
    for word in wordle.attempts:
        result = wordle.guess(word)
        for i, letter in enumerate(result):
          label= tk.Label(root, text=letter.character)
          label.grid(row=guessNum, column=i, padx=10, pady=10)

          if result[i].is_in_position:
            label.config(bg="green", fg="white")
          elif result[i].is_in_word:
            label.config(bg="#b5b51f", fg="white")
          else:
            label.config(bg="black", fg="white")

          
        guessNum += 1




def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as f:
        for line in f.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set




word_set = load_word_set("words.txt")
secret = random.choice(list(word_set))
wordle = Wordle(secret)
root = tk.Tk()
root.title("WORDLE")
root.geometry("300x300")
wordInput = tk.Entry(root)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)
guessButton = tk.Button(root, text="Guess", command=getGuess)
guessButton.grid(row=999, column=3, columnspan=2)
root.mainloop()