from models.objective_type import ObjectiveType
from models.optimization_task import *
from utils.optimizer import Optimizer
from models.constraint import Constraint
from models.optimization_config import OptimizationConfig
from models.design_variables import DesignVariables
from models.objective import Objective
from typing import List


my_task = OptimizationTask()
my_task.cae_model = "K:\\edu\\opti\\opt\\script.txt"
my_task.config = OptimizationConfig(10, 0.5, 0.5, 20, 0.01)
my_task.objective = Objective('mass', ObjectiveType.MIN, [])
my_task.constraint.append(Constraint(220e6, None, 'stress', []))
my_task.design_variables.append(DesignVariables('radius_a', 0.9, 0.1, 0.1, []))
my_task.design_variables.append(DesignVariables('radius_b', 0.9, 0.1, 0.1, []))

# optimizer = Optimizer()
# optimizer.optimize(my_task)