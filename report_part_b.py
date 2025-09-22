import pandas as pd
from fractions import Fraction
# from report_part_a import ReportPartA
import numpy as np
from frog_simulation import FrogSimulation


# To import pandas, run the following command lines:
# 1) python3 -m venv env
# 2) source env/bin/activate
# 3) pip3 install pandas
# 4) python3 report_part_b.py to execute the table (This is not part of import pandas)


class ReportPartB:
    def __init__(self, number_trials=10, number_pads=8):
        self.number_trials = number_trials
        self.number_pads = number_pads
        self.total_num_jumps_list = []
        self.prob_list = []
        
    def print_out_PMF_table(self):
        data = []
        for k in range(1,self.number_pads + 1):
            data.append({
                "k": k,
                "P(X=k)" :self.prob_list[k-1],
            })
        data.append({
            "k": 0,
            "P(X=k)": "Otherwise"
        })
        df = pd.DataFrame(data)
        # index = False to hide the index column
        print(df.to_string(index=False))

    def generate_prob_list(self):
        for i in range(self.number_trials):
            frog = FrogSimulation(self.number_pads)
            self.total_num_jumps_list.append(frog.calculate_total_hops(self.number_pads))
        print(self.total_num_jumps_list)
        
        for i in range(1, self.number_pads + 1):
            self.prob_list.append((self.total_num_jumps_list.count(i))/(self.number_trials))

        print(self.prob_list)

part_b = ReportPartB()
part_b.generate_prob_list()
part_b.print_out_PMF_table()
