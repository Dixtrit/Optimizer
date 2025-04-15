import numpy as np
from models.optimization_task import OptimizationTask
import utils.ansys as ansys

class Optimizer:
    def init(self):
        pass

    def optimize(self, ot: OptimizationTask):
        population = self.generate_initial_population(ot)
        for i in range(ot.config.max_iter):
            self.crossbending(population, ot)
            self.mutation(ot)
            self.selection(ot)
            self.check_convergence(ot)
            self.plot_results(ot)

    def generate_initial_population(self, ot: OptimizationTask):
        num_pars = len(ot.design_variables)
        indivuduals = np.random.rand(num_pars, ot.config.popuation_size)
        pass

    def crossbending(self, ot: OptimizationTask):
        pass

    def mutation(ot: OptimizationTask):
        pass

    def selection(ot: OptimizationTask):
        pass

    def check_convergence(ot: OptimizationTask):
        pass

    def plot_results(ot: OptimizationTask):
        pass

    def change_input(self, individual, ot: OptimizationTask):
        with open(ot.cae_model) as f:
            lines = f.readlines()
        lines[0] = 'a' + str(individual[0]) + '\n'
        lines[1] = 'b' + str(individual[1]) + '\n'
        with open(ot.cae_model, 'w') as f:
            f.writelines(lines)

    def calculate_dresps(self, ot: OptimizationTask, population):
        for individual in population:
            change_input(individual, ot)
            ansys.run()


