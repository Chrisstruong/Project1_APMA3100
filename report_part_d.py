import pandas as pd
from fractions import Fraction
from frog_simulation import FrogSimulation
import matplotlib.pyplot as plt

# Download matplotlib instruction by command lines
# python -m pip install -U pip
# python -m pip install -U matplotlib

# Write you part D here
class ReportPartD:
    def __init__(self, number_trials=100000, number_pads=100):
        self.expected_value = 0
        self.number_trials = number_trials
        self.number_pads = number_pads
        self.total_num_jumps_list = []
        self.prob_list = []
        self.my_expected_value_list = []
        self.N_value = list(range(1,101))
        

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
        
        for i in range(1, self.number_pads + 1):
            self.prob_list.append((self.total_num_jumps_list.count(i))/(self.number_trials))


    def calculate_expected_jumps(self):
        for k in range(1,self.number_pads + 1):
            self.expected_value += k * self.prob_list[k-1]
            self.my_expected_value_list.append(self.expected_value)
        return self.expected_value

    def plot_expected_value(self):
        # This condition is to check if the my_expected_value_list is empty
        if not self.my_expected_value_list:
            print("Expected values array is empty. Running the calculation for expected values from 1-100")
            self.calculate_expected_jumps()

        plt.plot(self.N_value, self.my_expected_value_list)
        plt.title("Expected Number of Jumps vs. Number of Lily Pads")
        plt.xlabel("N hops")
        plt.ylabel("E[X]")
        plt.grid(True)
        plt.show()

part_d = ReportPartD()
part_d.generate_prob_list()
part_d.print_out_PMF_table()
print(part_d.calculate_expected_jumps())
part_d.plot_expected_value()

