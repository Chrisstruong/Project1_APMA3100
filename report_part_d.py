import pandas as pd
from fractions import Fraction
import matplotlib.pyplot as plt

# Download matplotlib instruction by command lines
# python -m pip install -U pip
# python -m pip install -U matplotlib

# Write you part D here
class ReportPartD:
    def __init__(self):
        self.pmf = Fraction(1, 100)
        self.expected_value = 0
        self.my_expected_value_list = []
        self.N_value = list(range(1,101))

    def print_out_PMF_table(self):
        data = {
            'k': list(range(1, 101)) + ["Otherwise"],  # k = 1..99, else 0
            'P(X=k)': [self.pmf] * 100 + [0]
        }
        df = pd.DataFrame(data)
        # index = False to hide the index column
        print(df.to_string(index=False))

    def calculate_expected_jumps(self):
        for k in range(1, 101):
            self.expected_value += k * self.pmf
            self.my_expected_value_list.append(self.expected_value)
        # print(len(self.my_expected_value_list))
        # print(len(self.N_value))
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


