import pandas as pd
from fractions import Fraction

# Write you part c here


class ReportPartC:
    def __init__(self):
        self.pmf = Fraction(1, 20)
        self.expected_value = 0

    def print_out_PMF_table(self):
        data = {
            # k = 0..8
            'k': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, "Otherwise"],
            'P(X=k)': [self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf,self.pmf,self.pmf,self.pmf,self.pmf,self.pmf,0]
        }
        df = pd.DataFrame(data)
        # index = False to hide the index column
        print(df.to_string(index=False))

    def calculate_expected_jumps(self):
        for k in range(1,21):
            self.expected_value += k * self.pmf
        return self.expected_value


part_c = ReportPartC()
print(part_c.calculate_expected_jumps())
