import numpy as np

from constraint import Constraint
from optimization_config import OptimizationConfig
from design_variables import DesignVariables
from objective import Objective
from typing import List


class OptimizationTask:
    def __init__(self, config: OptimizationConfig = None,
                 cae_model = None, ojective: Objective = None, constraint: List[Constraint] = None,
                 design_variables: DesignVariables = None,
                 solver_path = None, solver_script = None):
        self.config = config
        self.cae_model = cae_model
        self.objective = ojective
        self.constraint = constraint
        self.design_variables = design_variables
        self.solver_path = solver_path
        self.sover_script = solver_script