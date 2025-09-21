# Write you part a here
# p = probability of success
class ReportPartA:
    def __init__(self, p, k):
        self.p = p # N = 10 => Probility of each pad lily is 1/10
        self.k = k # number of jumps

    def calculate_geometric_PMF(self):
        return (self.p * (1 - self.p)**(self.k-1)) # geometric_PMF
    
# report1 = ReportPartA(3)
# print(report1.calculate_geometric_PMF())