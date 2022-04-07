"""LESS - Linear Equation System Solver"""
import numpy as np

# User interaction 
number_of_variables = int(input("[INPUT] How many variables? "))
print(f"[INFO] {number_of_variables} equations are expected.")
data = []

for i in range(number_of_variables):
    data.append(input(f"[INPUT] Equation number {i + 1} : "))

alphabet = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"

# Identifying variables 
variables = [i for k in data for i in k if i in alphabet]
variables = list(dict.fromkeys(variables))


def find_right_side(equation):
    right_side_equation = clean_equation(equation)[1]
    right_side_equation.remove("") if "" in right_side_equation else right_side_equation
    right_side_equation = [eval(term) for term in right_side_equation]
    return sum(right_side_equation)


def clean_equation(equation):
    equation_right_side = equation.split("=")[1].replace("+", "&+")
    equation_right_side = equation_right_side.replace("-", "&-").split("&")

    equation_left_side = equation.split("=")[0].replace("+", "&+")
    equation_left_side = equation_left_side.replace("-", "&-").split("&")

    for term in equation_right_side:
        for variable in variables:
            if variable in term:
                coefficient = term.replace(variable, "")

                # Adds a 1 if single + or - 
                if coefficient == "+" or coefficient == "-":
                    coefficient = coefficient + "1"

                equation_left_side.append(str(-1 * eval(coefficient)) + variable)
                equation_right_side.remove(term)

    for term in equation_left_side:
        for index0, variable in enumerate(variables):
            if variable in term:
                break
            elif variable not in term and index0 == len(variables) - 1:
                equation_right_side.append(f"{-1 * eval(term)}")
                equation_left_side.remove(term)

    return equation_left_side, equation_right_side


def find_coefficients(equation):
    dict_coefficient = dict([(variable, 0) for variable in variables])
    equation = clean_equation(equation)[0]

    for term in equation:
        for variable in variables:
            if variable in term:
                coefficient = term.replace(variable, "")

                # Adds a 1 if single + or - 
                if coefficient == "+" or coefficient == "-":
                    coefficient = coefficient + "1"

                dict_coefficient[variable] += eval(coefficient) if coefficient != "" else 1

    coefficient_list = list(dict_coefficient.values())
    return coefficient_list


equation_system_matrix = np.array([find_coefficients(data[i]) for i in range(0, len(data))])
right_side_matrix = np.array([find_right_side(data[k]) for k in range(0, len(data))])
result_matrix = np.dot(np.linalg.inv(equation_system_matrix), right_side_matrix)

for index, result in enumerate(result_matrix):
    print(f"[Result] {variables[index]} = {result_matrix[index]}")

