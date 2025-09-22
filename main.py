from frog_simulation import FrogSimulation
from report_part_a import ReportPartA
from report_part_b import ReportPartB
from report_part_c import ReportPartC
from report_part_d import ReportPartD


'''
Here is the full command line to activate the python virtual environment to run pandas and matplot. Please these command lines and you should be fine. Keep in mind that those command lines are for Mac:
1) python3 -m venv env
2) source env/bin/activate
3) pip3 install pandas
4) python -m pip install -U pip 
5) python -m pip install -U matplotlib
6) python main.py

'''

# Frog Simulation run by frog_simulation.py
N_value = int(input("Enter the N value: "))
frog = FrogSimulation(N_value)
total_hops = frog.calculate_total_hops(N_value)
print("In this outcome, the frog took",total_hops,"total hops to complete the journey\n")

# Part a
print("a) When N=10, what is the probability that it takes exactly three jumps?")
part_a = ReportPartA(1/10, 3)
print("The probability that it takes three jumps (k = 3) is", round(part_a.calculate_geometric_PMF(), 3))

# Part b
print("\nb) When N=8, estimate the full PMF of the number X of jumps. In other words, what are all the possible values of X, and what are all the corresponding probabilities?")
part_b = ReportPartB()
part_b.print_out_PMF_table()

# Part c
print("\nc) When N=20, what is the expected number of jumps?")
part_c = ReportPartC()
print("When N=20, what the expected number of jumps is", part_c.calculate_expected_jumps())

# Part d
print("\nd) How does the expected value change as N increases?")
part_d = ReportPartD()
print("Table of values for estimates for E[X] for N=1,2,3,...,100")
part_d.print_out_PMF_table()
print("\nPlot of these results")
part_d.plot_expected_value()


