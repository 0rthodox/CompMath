from collections import namedtuple


def Thomas(alpha, beta, gamma, delta):
    m = len(delta)
    Race = namedtuple('Race', 'P Q')
    coeffs = [Race(gamma[0] / beta[0], -delta[0] / beta[0]),]
    for i in range(1, m - 1):
        p = gamma[i] / (beta[i] - alpha[i] * (coeffs[i - 1]).P)
        q = (alpha[i] * coeffs[i - 1].Q - delta[i]) / (beta[i] - alpha[i] * (coeffs[i - 1]).P)
        coeffs.append(Race(p, q))
    result = [(alpha[-1] * coeffs[-1].Q - delta[-1]) / (beta[-1] - alpha[-1] * coeffs[-1].P[-1]),]
    for i in range(2, m + 1):
        result.append(coeffs[-i].P * result[-i] + coeffs[-i].Q)
    return reversed(result)


def finiteDifference(u1, u0, h):
    return (u1 - u0) / h


data = list()
for line in open("6_9_32_data"):
    data.append([int(val.replace(' ', '')) for val in line.split('-')][1])

N = len(data) - 1
delta = 10
#calculating rvals

rvals = list()
for i in range(N - 1):
    rvals.append(
        6 * finiteDifference(
            finiteDifference(data[i + 2], data[i + 1], delta),
            finiteDifference(data[i + 1], data[i], delta),
            delta)
    )
alpha = [0.] + (N - 2) * [0.5]
beta = (N - 1) * [2.]
gamma = (N - 2) * [0.5] + [0.]
c = Thomas(alpha, beta, gamma, rvals)


