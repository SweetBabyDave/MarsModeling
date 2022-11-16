from matplotlib import pyplot as plt
import numpy as np
import math

NUM_VARS = 13
VAR_DICT = {0 : "N Demand (N\u2080)", 1 : "Reactor Volume (V)", 2 : "Fixation Rate (r)", 
3 : "Bioreactor Harvest Index (TODO)", 4 : "Crop Harvest Index (TODO)", 5 : "Fertilization Efficiency",
6 : "Digester (AE) Efficiency (TODO)", 7 : "Digester (AN) Efficiency (TODO)", 8 : "Urine Recyclability (TODO)",
9 : "Fraction Biomass to AE (TODO)", 10 : "Fraction Feces to AE (TODO)", 11 : "Fecal Fraction of Waster (TODO)",
12 : "Crew Members"}
DEFAULT_VAR = [14, 800, 13, 0.8, 0.5, 1, 0.75, 0.5, 1, 0.8, 0.5, 0.2, 10]

def graph(variables):
    x = np.linspace(0, 365, 365)
    y = np.linspace(-40, 40, 5)
    Z = 1
    
    # The 1 to start in N_in might be incorrect
    # Need to finish up coding the math for this part. It's super confusing, but I might be able to make it more readable.
    N_in = (1)*(variables[2])*(variables[1])*(variables[3])*(n_x(variables[9], variables))**(Z)
    N_out = ((variables[0])/((variables[5])*(variables[4]))) + ((Z)*((variables[0])*(variables[8])*(1-(variables[11])*n_x(variables[10], variables))))
    N_rec = variables[0]*((n_x(variables[9], variables))*((1/variables[4])-1)+(variables[11]*(n_x(variables[10], variables)))+(variables[8]*(1-variables[11])))
    N_change = variables[12] * x * (N_in + N_rec - N_out)
    print(N_change)
    print("im here")
    plt.plot(x, N_change)
    plt.title("Nitrogen Management Regiment Comparisons")
    plt.yticks(y)
    plt.show()

def n_x(x, variables):
    return (((variables[6])*(x))+((variables[7])*(1-(x))))

def compute_var():
    variables = []
    for current_var in range(NUM_VARS):
        variables.append(input(f"Currently choosing value for {VAR_DICT[current_var]}.\n Enter 'd' for default value or the desired number you would like for this value:\n"))
        if variables[current_var] == 'd':
            # Need to add a way to get default values into the array
            variables[current_var] = DEFAULT_VAR[current_var]
    return variables

if __name__ == '__main__':
    default = input("Enter 'd' for for default values or anything else for non-default values:\n").lower()
    if default == 'd':
        graph(DEFAULT_VAR)
    else:
        variables = compute_var()
        graph(variables)

