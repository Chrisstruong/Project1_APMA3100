# Write you part d here
import pandas as pd
from fractions import Fraction
import matplotlib.pyplot as plt

my_expected_value_list = [0]


class ReportPartD:
    def __init__(self):
        self.pmf = Fraction(1, 100)
        self.expected_value = 0

    def print_out_PMF_table(self):
        data = {
            # k = 0..8
            'k': list(range(1, 100)) + ["Otherwise"],  # k = 1..99, else 0
            'P(X=k)': [self.pmf] * 99 + [0]
        }
        df = pd.DataFrame(data)
        # index = False to hide the index column
        print(df.to_string(index=False))

    def calculate_expected_jumps(self):
        for k in range(1, 101):
            self.expected_value += k * self.pmf
            my_expected_value_list.append(self.expected_value)
        print(my_expected_value_list)
        return self.expected_value

    def plot(self):
        x_values = [1, 2, 3, 4, 5]
        y_values = [2, 4, 6, 8, 10]
        plt.plot(x_values, y_values)
        plt.xlabel("X-axis Label")
        plt.ylabel("Y-axis Label")
        plt.title("My Simple Line Graph")


part_d = ReportPartD()
# part_d.print_out_PMF_table()
# part_d.calculate_expected_jumps()

x_values = [1, 2, 3, 4, 5]
y_values = [2, 4, 6, 8, 10]
plt.plot(x_values, y_values)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("My Simple Line Graph")
