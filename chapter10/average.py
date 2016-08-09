def average(values):
    """calculate aveerage from numeric list

    >>> print(average([20, 30, 70]))
    40.0
    """

    return sum(values) / len(values)

import doctest
doctest.testmod()