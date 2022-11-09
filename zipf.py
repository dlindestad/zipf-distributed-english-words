# Implement Jason Crease fast zipf functions in python
# Original: https://jasoncrease.medium.com/zipf-54912d5651cc


def zipf_cdf_approx(k, s, n):
    if k > n or k < 1:
        raise Exception("k must be between 1 and n")

    a = (
        ((k ** (1 - s)) - 1) / (1 - s)
        + 0.5
        + (k ** (-s)) / 2
        + s / 12
        - (k ** (-1 - s)) * s / 12
    )
    b = (
        ((n ** (1 - s)) - 1) / (1 - s)
        + 0.5
        + (n ** (-s)) / 2
        + s / 12
        - (n ** (-1 - s)) * s / 12
    )
    return a / b


def inverse_cdf_fast(p, s, n):
    if p > 1 or p < 0:
        raise Exception("p must be between 0 and 1")

    tolerance = 0.001
    x = n / 2

    pD = p * (
        12 * (n ** (-s + 1) - 1) / (1 - s) + 6 + 6 * n ** (-s) + s - s * n ** (-s - 1)
    )

    while True:
        m = x ** (-s - 2)  # x ^ ( -s - 2)
        mx = m * x  # x ^ ( -s - 1)
        mxx = mx * x  # x ^ ( -s)
        mxxx = mxx * x  # x ^ ( -s + 1)

        a = 12 * (mxxx - 1) / (1 - s) + 6 + 6 * mxx + s - (s * mx) - pD
        b = 12 * mxx - (6 * s * mx) + (m * s * (s + 1))
        newx = max(1, x - a / b)
        if abs(newx - x) <= tolerance:
            return round(newx)
        x = newx
