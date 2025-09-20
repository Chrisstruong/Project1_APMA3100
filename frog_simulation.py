import random

class FrogSimulation:
    def __init__(self, N_value):
        self.remaining_distance = N_value 
        self.total_hops = 0 # total number of jumps that the frog took
        self.current_pad = 0 # current position of the frog (start = 0, end = N)

    def calculate_total_hops(self, N_value):
        print("\n*****The Frog Simulation Starts****")
        print("____________________________")

        # The frog continues until it reaches to the other side of the pond (remaining distance = 0)
        while (self.remaining_distance > 0):
            self.total_hops += 1 # keep track the total number of jumps, starting at 1
            print("Remaining distance to get to the other side of a pond is", self.remaining_distance)
            next_hop = random.randint(1, self.remaining_distance) # The frog picks randomly between 1-remaining_distance
            self.current_pad += next_hop # keep track current position of the frog
            print(f"Next hop (pick 1-{self.remaining_distance}):", next_hop)
            self.remaining_distance -= next_hop # calculate the remaining distance

            if(self.remaining_distance != 0):
                print("The frog is currently on lily pad number", self.current_pad)
            else: 
                print("The frog lands on the solid ground")
                
            print("____________________________")

        print("********Simulation Ends****\n")
        return self.total_hops











# remaining_distance = int(input("Enter the N value : "))
# total_hops = 0
# current_pad = 0

# print("\n*****The Frog Simulation Starts****")
# print("____________________________")

# # The frog continues until it reaches to the other side of the pond (remaining distance = 0)
# while (remaining_distance > 0):
#     total_hops += 1 # keep track the total number of jumps, starting at 1
#     print("Remaining distance to get to the other side of a pond", remaining_distance, "lily pads")
#     next_hop = random.randint(1, remaining_distance) # The frog picks randomly between 1-remaining_distance
#     current_pad += next_hop # keep track current position of the frog
#     print(f"Next hop (pick 1-{remaining_distance}):", next_hop)
#     remaining_distance -= next_hop # calculate the remaining distance
#     print("The frog is currently on lily pad number", current_pad)
#     print("____________________________")

# print("********Simulation Ends****\n")
# print("In this outcome, the frog took",total_hops,"total hops to complete the journey")

