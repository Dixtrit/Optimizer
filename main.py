from models.objective_type import ObjectiveType
from models.optimization_task import *
from utils.optimizer import Optimizer


my_task = OptimizationTask()
my_task.config = (10, 0.5, 0.5, 20, 0.001)
my_task.objective = Objective('mass', ObjectiveType.MAX)
my_task.constraint.append(Constraint('stress', upper_bound=200e6, lower_bound=None, vallues=[]))
my_task.design_variables.append(DesignVariables('radius_a', 0.1, 0.9, 0.1))
my_task.design_variables.append(DesignVariables('radius_b', 0.1, 0.9, 0.1))


optimizer = Optimizer()
optimizer.optimize(my_task)