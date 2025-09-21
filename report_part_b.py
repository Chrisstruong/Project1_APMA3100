import pandas as pd
from fractions import Fraction

# To import pandas, run the following command lines:
# 1) python3 -m venv env
# 2) source env/bin/activate
# 3) pip3 install pandas
# 4) python3 report_part_b.py to execute the table (This is not part of import pandas)

class ReportPartB:
    def __init__(self):
        self.pmf = Fraction(1, 8)

    def print_out_PMF_table(self):
        data = {
            'k': [1, 2, 3, 4, 5, 6, 7, 8, "Otherwise"],  # k = 0..8
            'P(X=k)': [self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, self.pmf, 0]
        }
        df = pd.DataFrame(data)
        print(df.to_string(index=False))   # index = False to hide the index column

# part_b = ReportPartB()
# part_b.print_out_PMF_table()


