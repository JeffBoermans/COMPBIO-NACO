import numpy as np

from typing import List, Tuple
from statistics import NormalDist


def centered_normal_dist(range: Tuple[int, int], std_factor: float=4.0) -> NormalDist:
    """Create a normal distribution centered on the middle of the specified range.
    
    Suppose the width of the range is named x, then the standard deviation of the
    resulting normal distribution is calculated as:
        x / std_factor
    
    :param range: The range to center a normal dist on
    :param std_factor: The inverse scaling factor on the the range width to produce the std
    :return: The centered normal distribution
    """
    range_dist: int = range[1] - range[0]
    range_std: int = range_dist / std_factor
    mean: int = range[0] + range_std
    return NormalDist(mu=mean, sigma=range_std)


def logistic_growth(t: List[float], r: float, K: float):
    """A practical derivation of the Verhulst model for population growth, for use in curve fitting.
    
    The original Verhulst model is:
        dN / dt = rN (1 - N / K)
    This has been transformed into:
        N = K / ( 1 + e^(-rt) )
    This way, this function can be used to estimate the r
    and K parameters in the Verhulst model by using curve
    fitting, a specified time series t and the related
    population data N generated by the simulation.

    :param t: The time series of the simulation; i.e. The list
    of all passed time steps: [0, 1, 2, 3, ..., t] where t is
    the current time or current day
    :param r: The intrinsic growth parameter r in the Verhulst model,
    will be estimated by curve fitting
    :param K: The carry capacity parameter K in the Verhulst model,
    will be estimated by curve fitting
    """
    N = K / (1 + np.exp(-r*t))
    return N


class Logger():
    def __init__(self, file_path: str) -> None:
        # self.file = file_path
        pass

    def log(self, msg: str) -> None:
        """ Logs the message with the current date and time
        """
        # file = open(self.file, 'a')
        # file.write(f"[{datetime.now()}] : {msg}\n")
        # file.close()
        pass
    
    def setup(self, input_file: str) -> None:
        """ Sets up file with custom beautiful '='-art. 
        """
        # file = open(self.file, 'w')
        # file.write("==================================================================\n")
        # file.write(f"Log created on: {datetime.now()}\n")
        # file.write(f"Input file used: {input_file}\n")
        # file.write("IMPORTANT: Save this file externally, starting a new simulation will clear this file\n")
        # file.write("==================================================================\n")
        # file.close()
        pass

    def logNoTimestamp(self, msg: str) -> None:
        """ Prints the message without timestamp
        """
        # file = open(self.file, 'a')
        # file.write(f"{msg}\n")
        # file.close()
        pass
