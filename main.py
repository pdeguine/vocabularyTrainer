from tkinter import *
from vocabularyTrainer import *
import random as r

# TODO: 1. Import CSV into Pandas dataframe and make available
# TODO: 2. Create GUI. 2 labels for NL/DE and 2 buttons for next/reveal. Drop down to select German or NL as source
# TODO: 3. Iterate over dataframe and show source language in label

# data set functionality
voc = VocabularyTrainer()


# Iteration
def next_word():
    source_lbl.config(text=voc.next())
    target_lbl.config(text="***")
    comment_lbl.config(text="***")


def reveal():
    target_lbl.config(text=voc.reveal()[0])
    comment_lbl.config(text=voc.reveal()[1])


# GUI setup
window = Tk()
window.title("vocabularyTrainer")
window.minsize(height=200, width=200)
window.config(padx=30, pady=30)

# Labels
source_lbl = Label(text=voc.next(), width=30)
source_lbl.grid(row=0, column=0)

target_lbl = Label(text="***", width=30)
target_lbl.grid(row=0, column=1)

comment_lbl = Label(text="***")
comment_lbl.grid(row=1, column=1)

# Buttons
next_btn = Button(text="Next", command=next_word)
next_btn.grid(row=2, column=0)

reveal_btn = Button(text="Reveal", command=reveal)
reveal_btn.grid(row=3, column=0)

# Runtime
window.mainloop()

