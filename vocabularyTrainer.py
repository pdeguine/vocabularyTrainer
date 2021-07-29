import pandas as p
import random as r


class VocabularyTrainer:
    def __init__(self):
        self.dataframe = p.pandas.read_csv("dataset.csv", delimiter=';')
        self.voc_dict = {}
        self.load()
        self.current_index = 0
        self.total_entries = len(self.dataframe) - 1
        self.correct_answers = 0

    def load(self):
        for i in range(0, len(self.dataframe)):
            self.voc_dict = {index: {'Nederlands': row.Nederlands,
                                     'Deutsch': row.Deutsch,
                                     'Type': row.Type,
                                     'Comment': row.Comment} for (index, row) in self.dataframe.iterrows()}

    def next(self):
        self.current_index = r.randint(0, self.total_entries)
        return self.voc_dict[self.current_index]["Deutsch"]

    def reveal(self):
        return [self.voc_dict[self.current_index]["Nederlands"], self.voc_dict[self.current_index]["Comment"]]
