import numpy as np


def calculate(list):
    if len(list) == 9:
        mat33 = np.array(list).reshape(3, 3)
        list_mean = [mat33.mean(axis=0).tolist(), mat33.mean(axis=1).tolist(), mat33.flatten().mean()]
        list_var = [mat33.var(axis=0).tolist(), mat33.var(axis=1).tolist(), mat33.flatten().var()]
        list_std = [mat33.std(axis=0).tolist(), mat33.std(axis=1).tolist(), mat33.flatten().std()]
        list_max = [mat33.max(axis=0).tolist(), mat33.max(axis=1).tolist(), mat33.flatten().max()]
        list_min = [mat33.min(axis=0).tolist(), mat33.min(axis=1).tolist(), mat33.flatten().min()]
        list_sum = [mat33.sum(axis=0).tolist(), mat33.sum(axis=1).tolist(), mat33.flatten().sum()]

    else:
        raise ValueError("List must contain nine numbers.")

    calculations = {
        'mean': list_mean,
        'variance': list_var,
        'standard deviation': list_std,
        'max': list_max,
        'min': list_min,
        'sum': list_sum
    }

    return calculations