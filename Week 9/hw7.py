#!/usr/bin/env python
# coding: utf-8

# ### Problem 1:
# Use integration in SymPy to write a function named normalcurve(a,b) that takes as input two boundaries a, b, and returns the probability that the a standard normal random variable falls in the interval between a and b. Your function should return both a precise answer and a numerical answer.

# In[10]:


import sympy as sp
def normalcurve(a, b):
    x = sp.symbols('x')
    # probability density function
    std_pdf = (1/(sp.sqrt(2*sp.pi))) * (sp.exp(-(x**2)/2))
    precise = sp.integrate(std_pdf, (x, a, b))  
    # evaluate the value of the integral
    numerical = sp.integrate(std_pdf, (x, a, b)).evalf()
    return precise, numerical

normalcurve(0,1)


# ### Problem 2:
# Write a function named balance(eq) that balances chemical equations. So, it takes as input strings of the form "H2+O2=H2O" into "2H2+O2=2H2O". This function does not need to account for the compounds with parentheses like Pb(OH)4 or Pb(SO4)2.

# In[9]:


from numpy import linalg
import re
from sympy.parsing.sympy_parser import parse_expr

def getmatrix(s):
    # seperate chemical equation into lefteq and right eq
    lefteq = re.split("=", s)[0]
    righteq = re.split("=", s)[1]

    # seperate compounds for both sides
    left_compounds = re.split('\s*\+\s*', lefteq)
    right_compounds = re.split('\s*\+\s*', righteq)

    n_chem = len(left_compounds) + len(right_compounds)

    elements = []
    l_list = []
    r_list = []

    for l_ele in left_compounds:
        # a list of tuples which are forms of (element, number) for each compound in the left hand side
        help_list = re.findall(r'([A-Z][a-z]{0,1})(\d*)', l_ele)
        l_list.append(help_list)
        for ele in help_list:
            if ele[0] not in elements:
                elements.append(ele[0])

    for r_ele in right_compounds:
        # a list of tuples which are forms of (element, number) for each compound in the right hand side
        help_list = re.findall(r'([A-Z][a-z]{0,1})(\d*)', r_ele)
        r_list.append(help_list)

    n_ele = len(elements)

    # initialize our matrix with zero
    our_matrix = sp.zeros(n_ele, n_chem + 1)
    m = 0

    for l_item in l_list:
        for l_tuple in l_item:
            if l_tuple[1] == '':
                a = 1
            else:
                a = int(l_tuple[1])
            row_m = elements.index(l_tuple[0])
            our_matrix[row_m, m] = our_matrix[row_m, m] + a
        m += 1

    for r_item in r_list:
        for r_tuple in r_item:
            if r_tuple[1] == '':
                a = 1
            else:
                a = int(r_tuple[1])
            row_m = elements.index(r_tuple[0])
            our_matrix[row_m, m] = our_matrix[row_m, m] - a
        m += 1

    return our_matrix

# the function we use to balance the chemical equation
def balance(eq):
    M = getmatrix(eq)
    lefteq = re.split("=", eq)[0]
    righteq = re.split("=", eq)[1]

    left_compounds = re.split('\s*\+\s*', lefteq)
    right_compounds = re.split('\s*\+\s*', righteq)

    elements = []

    for l_ele in left_compounds:
        help_list = re.findall(r'([A-Z][a-z]{0,1})(\d*)', l_ele)
        for ele in help_list:
            if ele[0] not in elements:
                elements.append(ele[0])

    n = len(left_compounds) + len(right_compounds)
    x = [parse_expr('x%d' % i) for i in range(n)]
    x = sp.symbols('x0:%d' % n)
    sols = sp.solve_linear_system(M, *x)
    new_dict = {}
  
    for i in x:
        new_dict[i] = 1
    # print new_dict
    for key in sols:
        if sols[key].args == ():
            new_dict[key] = 1
        else:
            new_dict[key] = (sols[key]).args[0]

    # remove fractions
    final_list = []
    for i in range(n):
        final_list.append(sp.fraction(new_dict[x[i]])[1])
    f = sp.lcm(final_list)
    for key in new_dict:
        new_dict[key] = new_dict[key]*f

    # form the final output string
    final_string = ""
    for i in range(len(left_compounds)):
        if new_dict[x[i]] == 1:
            final_string += left_compounds[i]
        else:
            final_string += str(new_dict[x[i]]) + left_compounds[i]
        if i != (len(left_compounds) - 1):
            final_string += '+'

    final_string += '='

    for i in range(len(right_compounds)):
        temp = len(left_compounds)
        if new_dict[x[i+temp]] == 1:
            final_string += right_compounds[i]
        else:
            final_string += str(new_dict[x[i+temp]]) + right_compounds[i]
        if i != (len(right_compounds) - 1):
            final_string += '+'

    return final_string

print(balance("PhCH3+KMnO4+H2SO4=PhCOOH+K2SO4+MnSO4+H2O"))


# In[ ]:




