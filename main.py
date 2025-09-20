from frog_simulation import FrogSimulation

# Frog Simulation run by frog_simulation.py
N_value = int(input("Enter the N value: "))
frog = FrogSimulation(N_value)
total_hops = frog.calculate_total_hops(N_value)
print("In this outcome, the frog took",total_hops,"total hops to complete the journey")

#
