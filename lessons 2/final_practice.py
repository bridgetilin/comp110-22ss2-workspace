class ChristmasTreeFarm:
    plots: list[int]
    def __init__(self, plots: int, initial_planting: int):
        self.plots = []
        i: int = 0 
        while i < initial_planting:
            self.plots.append(1)
            i += 1
        while i < plots:
            self.plots.append(0)
            i += 1
    
    def plant(self, plot_index: int) -> None:
        self.plots[plot_index] = 1

    def growth(self) -> None:
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] != 0:
                self.plots[i] += 1
            i += 1
    
    def harvest(self, replant: bool) -> int:
        successes: int = 0
        i: int = 0
        while i < len(self.plots):
            if self.plots[i] >= 5:
                successes += 1
                if replant: 
                    self.plots[i] = 1 
                else:
                    self.plots[i] = 0
            i += 1
        return successes

# recursive calls try again



