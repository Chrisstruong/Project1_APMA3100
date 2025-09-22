import pandas as pd
from fractions import Fraction
from frog_simulation import FrogSimulation
# Write you part c here
class ReportPartC:
    def __init__(self, number_trials=100000, number_pads=20):
        self.expected_value = 0
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

    def calculate_expected_jumps(self):
        for k in range(1,self.number_pads + 1):
            self.expected_value += k * self.prob_list[k-1]
        return self.expected_value

part_c = ReportPartC()
part_c.generate_prob_list()
part_c.print_out_PMF_table()
print(part_c.calculate_expected_jumps())
