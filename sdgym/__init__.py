"""SDGym - Synthetic data Gym.

SDGym is a framework to benchmark the performance of synthetic data generators for
non-temporal tabular data.
"""

__author__ = 'MIT Data To AI Lab'
__copyright__ = 'Copyright (c) 2018, MIT Data To AI Lab'
__email__ = 'dailabmit@gmail.com'
__license__ = 'MIT'
__version__ = '0.1.0-dev'

from sdgym.benchmark import benchmark
from sdgym.data import load_dataset

__all__ = [
    'benchmark',
    'load_dataset'
]
