from tkinter import *
import pandas as p

# TODO: 1. Import CSV into Pandas dataframe and make available
# TODO: 2. Create GUI. 2 labels for NL/DE and 2 buttons for next/reveal. Drop down to select German or NL as source
# TODO: 3. Iterate over dataframe and show source language in label

# data set functionality


# Iteration


# GUI setup
window = Tk()
window.title("vocabularyTrainer")
window.minsize(height=500, width=800)

# Labels
source_lbl = Label(text="German")
source_lbl.grid(row=0, column=0)

target_lbl = Label(text="Dutch")
target_lbl.grid(row=1, column=0)

# Buttons
next_btn = Button(text="Next")
next_btn.grid(row=2, column=0)

reveal_btn = Button(text="Reveal")
reveal_btn.grid(row=3, column=0)

# Runtime
window.mainloop()

