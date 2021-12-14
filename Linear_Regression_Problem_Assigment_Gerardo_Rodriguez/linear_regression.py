import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt

def cost_funtion_lambdas (X, y):
    return lambda thetas: sum ((thetas[0] + thetas[1] *X - y)**2)/len(X)

def derivative_theta0 (X, y):
    return lambda theta0, theta1: 2*sum(theta0 + theta1 * X - y) / len(X)

def derivative_theta1 (X, y):
    return lambda theta0, theta1: 2*sum((theta0 + theta1 * X - y) * X) / len(X)

def gradient_descent (theta0, theta1):
    f_dic = {}
    f_dic['theta0'] = theta0 - alpha*J_prime_0(theta0, theta1)
    f_dic['theta1'] = theta1 - alpha*J_prime_1(theta0, theta1)
    f_dic['cost'] = J([theta0,theta1])
    return (f_dic)


# Main Script structure
if __name__ == "__main__":
    # Generating working data (X and y)
    theta0 = 2
    theta1 = 5
    X = (np.random.randn(100) + 1) * 50
    jitter = 75 * np.random.randn(100)
    y = theta0 + theta1 * X + jitter

    # Setting working variables:
    nmax = 10
    alpha = 0.0001
    eps = 0.1
    cost_before = 0

    # Initializing empty lists
    theta0_list = []
    theta1_list = []
    cost_list = []

    theta0, theta1 = [-10,20]
    J = cost_funtion_lambdas (X,y)
    J_prime_0 = derivative_theta0(X,y)
    J_prime_1 = derivative_theta1(X,y)

    for i in range (0,nmax):
        gradient_descent_dic = gradient_descent (theta0, theta1)
        theta0 = gradient_descent_dic['theta0']
        theta1 = gradient_descent_dic['theta1']
        cost = gradient_descent_dic['cost']
        theta0_list.append(gradient_descent_dic['theta0'])
        theta1_list.append(gradient_descent_dic['theta1'])
        cost_list.append(gradient_descent_dic['cost'])
    
        convergense = np.abs(cost - cost_before) < eps
        cost_before = cost
    
        if convergense == True:
            print ("Convergence FOUND!")
            print ("Iteration Number: {} | theta0: {} | theta1: {} | Cost: {}".format(i, theta0_list[i], theta1_list[i], cost_list[i]))
            break