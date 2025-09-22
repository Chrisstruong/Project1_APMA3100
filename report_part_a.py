from frog_simulation import FrogSimulation
import random

# Write you part a here
# p = probability of success
class ReportPartA:
    def __init__(self, number_trials = 1000, number_pads = 10):
        self.number_trials = number_trials;
        self.total_num_jumps_list = [];
        self.number_pads = number_pads
    
    def cal_prob_3_jumps(self):
        count = 0

        for i in range(self.number_trials):
            frog = FrogSimulation(self.number_pads)
            self.total_num_jumps_list.append(frog.calculate_total_hops(self.number_pads))
        #print(self.total_num_jumps_list)

        for i in range(len(self.total_num_jumps_list)):
            if (self.total_num_jumps_list[i] == 3):
                count += 1
        #print(count)
        return count / self.number_trials    
    

ReportA = ReportPartA()
print(ReportA.cal_prob_3_jumps())



