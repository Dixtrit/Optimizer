import numpy as np

from models.constraint import Constraint
from models.optimization_config import OptimizationConfig
from models.design_variables import DesignVariables
from models.objective import Objective
from typing import List


class OptimizationTask:
    def __init__(self, config: OptimizationConfig = None,
                 cae_model = None, ojective: Objective = None, constraint: List[Constraint] = [],
                 design_variables: List[DesignVariables] = [],
                 solver_path = None, solver_script = None):
        self.config = config
        self.cae_model = cae_model
        self.objective = ojective
        self.constraint = constraint
        self.design_variables = design_variables
        self.solver_path = solver_path
        self.sover_script = solver_script
