from typing import Optional, Dict
from logging import Logger, getLogger

from numpy import ndarray

from basic_modueles.class_base import OptMLStatClassBase
from opt.optimization_problem import OptimizationProblem
from opt.opt_alg.optimization_algorithm_base import OptimizationAlgorithmBase
from opt.iteration import Iteration
from opt.opt_iterate import OptimizationIterate
from opt.opt_prob_evaluation import OptimizationProblemEvaluation

logger: Logger = getLogger()


class OptimizationResult(OptMLStatClassBase):
    """
    Stores optimization history and final results.
    """

    def __init__(self, opt_prob: OptimizationProblem, opt_alg: OptimizationAlgorithmBase) -> None:
        self.opt_prob: OptimizationProblem = opt_prob
        self.opt_alg: OptimizationAlgorithmBase = opt_alg
        self.iter_iterate_dict: Dict[Iteration, OptimizationIterate] = dict()

    def register_solution(
        self,
        iteration: Iteration,
        x_array_2d: Optional[ndarray] = None,
        primal_prob_evaluation: Optional[OptimizationProblemEvaluation] = None,
        lambda_array_2d: Optional[ndarray] = None,
        nu_array_2d: Optional[ndarray] = None,
        dual_prob_evaluation: Optional[OptimizationProblemEvaluation] = None,
    ) -> None:
        assert iteration not in self.iter_iterate_dict

        self.iter_iterate_dict[iteration] = OptimizationIterate(
            x_array_2d, primal_prob_evaluation, lambda_array_2d, nu_array_2d, dual_prob_evaluation
        )

    @property
    def final_iterate(self) -> OptimizationIterate:
        return sorted(self.iter_iterate_dict.items(), key=lambda x: x[0])[-1][1]
