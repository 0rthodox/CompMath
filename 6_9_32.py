from collections import namedtuple


def Thomas(alpha, beta, gamma, delta):
    m = len(delta)
    Race = namedtuple('Race', 'P Q')
    coeffs = [Race(gamma[0] / beta[0], -delta[0] / beta[0]),]
    for i in range(1, m - 1):
        p = gamma[i] / (beta[i] - alpha[i] * (coeffs[i - 1]).P)
        q = (alpha[i] * coeffs[i - 1].Q - delta[i]) / (beta[i] - alpha[i] * (coeffs[i - 1]).P)
        coeffs.append(Race(p, q))
    result = [(alpha[-1] * coeffs[-1].Q - delta[-1]) / (beta[-1] - alpha[-1] * coeffs[-1].P), ]
    for i in range(2, m):
        result.append(coeffs[-i].P * result[i - 2] + coeffs[-i].Q)
    return list(reversed(result))


def finiteDifference(data, delta):
    return [(data[i + 1] - data[i]) / delta for i in range(len(data) - 1)]

data = list()
for line in open("6_9_32_data"):
    data.append([int(val.replace(' ', '')) for val in line.split('-')][1])

N = len(data) - 1
delta = 10

finiteDiffs = finiteDifference(data, delta)
#calculating rvals

rvals = finiteDifference(finiteDiffs, delta)

alpha = [0.] + (N - 2) * [0.5]
beta = (N - 1) * [2.]
gamma = (N - 2) * [0.5] + [0.]
c = [0] + Thomas(alpha, beta, gamma, rvals) + [0]
b = [0] + [c[i] * delta / 3 + c[i - 1] * delta / 6 + finiteDiffs[i - 1] for i in range(N)]
d = [0.] + [(c[i] - c[i - 1]) / delta for i in range(1, N)]
a = [0, data[0] + d[1] * delta ** 3 / 6 - c[1] * delta ** 2 / 2 + b[1] * delta] + data[1:]
print(a, b, c, d, sep='\n')



