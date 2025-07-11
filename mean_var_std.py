import numpy as np
import pprint

def calculate(list):
    
    calculations = {}

    # To make sure we get a 3x3 array
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(list, dtype=float).reshape(3, 3)
    
    # The following functions calculate different relevant statistical tools in columns, rows and the whole matrix
    # Finds the mean
    calculations['mean'] = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()]
    # Finds the variance
    calculations['variance'] = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()]
    # Finds the std
    calculations['standard deviation'] = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()]
    # Finds the max value
    calculations['max'] = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()]
    # Finds the min value
    calculations['min'] = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()]
    # Finds the sum of all values
    calculations['sum'] = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]

    return calculations

# Example usage
pprint.pprint(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
