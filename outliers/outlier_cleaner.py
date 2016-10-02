#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    zipped = zip(predictions, ages, net_worths)
    result = list(map(lambda t: (t[1], t[2], t[0] - t[2]), zipped))
    result.sort(key=lambda t: abs(t[2]))

    return result[:len(result) * 9 / 10]

