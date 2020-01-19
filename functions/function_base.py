from abc import ABC, abstractmethod
from typing import Optional

from numpy import ndarray, array


class FunctionBase(ABC):
    """
    Base class for function classes.
    """

    def __init__(self, num_inputs: Optional[int] = None, num_outputs: Optional[int] = None):
        self.num_inputs: Optional[int] = num_inputs
        self.num_outputs: Optional[int] = num_outputs

    def get_num_inputs(self) -> Optional[int]:
        return self.num_inputs

    def get_num_outputs(self) -> Optional[int]:
        return self.num_outputs

    def check_x_array_dimension(self, x_array_2d: ndarray) -> None:
        if self.get_num_inputs() is not None:
            assert x_array_2d.shape[1] == self.get_num_inputs()

    def check_y_array_dimension(self, y_array_2d: ndarray) -> None:
        if self.get_num_outputs() is not None:
            assert y_array_2d.shape[1] == self.get_num_outputs()

    def get_y_values_1d(self, x_array_1d: ndarray) -> ndarray:
        x_array_2d: ndarray = array([x_array_1d]).T
        y_array_2d: ndarray = self.get_y_values_2d(x_array_2d)
        return y_array_2d.ravel()

    @abstractmethod
    def get_y_values_2d(self, x_array_2d: ndarray) -> ndarray:
        """
        Returns y values for given x values.

        Parameters
        ----------
        x_array_2d:
          N-by-n array representing x.

        Returns
        -------
        y_array_2d:
          N-by-m array representing y.
        """
        pass
