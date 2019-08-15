"""
operationpolicy.py - a module to define a class to specify the computation
backend
"""

from enum import Enum

class OperationPolicy(Enum):
    """a class to specify the computation backend
    """
    CPU = 1
    GPU = 2
    CPU_SPARSE = 3
    GPU_SPARSE = 4

    def __str__(self):
        if self.value == 1:
            return "operation_policy_cpu"
        elif self.value == 2:
            return "operation_policy_gpu"
        elif self.value == 3:
            return "operation_policy_cpu_sparse"
        else:
            return "operation_policy_gpu_sparse"


    def __repr__(self):
        return self.__str__()
