#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:14:15 2019

@author: jiaruijiang
"""

#hw7_1

import numpy as np
import sympy as sp

#sp.init_printing(use_latex='mathjax')
#from IPython.display import display

def normalcurve(a,b): #a as lower bound, b as upper
    x = sp.symbols('x')
    f = (sp.exp(-(x**2)/2))/sp.sqrt(2*sp.pi) #std distribution prob function
    base = sp.integrate(f,(x,-sp.oo,sp.oo)) #check integration be 1
    #print base
    sub = sp.integrate(f,(x,a,b))
    numerical_result = float(sub/base)
    
    return (sub, numerical_result)

#print normalcurve(0,1)

#hw7_2
from numpy import linalg
import re
from sympy.parsing.sympy_parser import parse_expr
import sympy as sp

def form_mx(s):
    # seperate chemical equation into left and right
    lhs = re.split("=", s)[0]
    rhs = re.split("=", s)[1]

    # seperate compounds for both sides
    left_compounds = re.split('\s*\+\s*', lhs)
    right_compounds = re.split('\s*\+\s*', rhs)

    chem_num = len(left_compounds) + len(right_compounds)
    
    elements = []
    left_list = []
    right_list = []

    for l_ele in left_compounds:
        # a list of tuples with forms (element, number) for each compound in the left hand side
        temp_list = re.findall(r'([A-Z][a-z]{0,1})(\d*)', l_ele)
        left_list.append(temp_list)
        for ele in temp_list:
            if ele[0] not in elements:
                elements.append(ele[0])

    for r_ele in right_compounds:
        # a list of tuples with forms (element, number) for each compound in the right hand side
        temp_list = re.findall(r'([A-Z][a-z]{0,1})(\d*)', r_ele)
        right_list.append(temp_list)

    ele_num = len(elements)

    # create a matrix with 0
    Matrix = sp.zeros(ele_num, chem_num + 1)
    
    k = 0

    for l_item in left_list:
        for l_tuple in l_item:
            if l_tuple[1] == '':
                a = 1
            else:
                a = int(l_tuple[1])
            row_m = elements.index(l_tuple[0])
            Matrix[row_m, k] = Matrix[row_m, k] + a
        k += 1

    for r_item in right_list:
        for r_tuple in r_item:
            if r_tuple[1] == '':
                a = 1
            else:
                a = int(r_tuple[1])
            row_m = elements.index(r_tuple[0])
            Matrix[row_m, k] = Matrix[row_m, k] - a
        k += 1

    return Matrix

# the function to balance the chemical equation
def balance(eq):
    M = form_mx(eq)
    lhs = re.split("=", eq)[0]
    rhs = re.split("=", eq)[1]

    left_compounds = re.split('\s*\+\s*', lhs)
    right_compounds = re.split('\s*\+\s*', rhs)

    elements = []

    for left_ele in left_compounds:
        help_list = re.findall(r'([A-Z][a-z]{0,1})(\d*)', left_ele)
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
    result_str = ""
    for i in range(len(left_compounds)):
        if new_dict[x[i]] == 1:
            result_str += left_compounds[i]
        else:
            result_str += str(new_dict[x[i]]) + left_compounds[i]
        if i != (len(left_compounds) - 1):
            result_str += '+'

    result_str += '='

    for i in range(len(right_compounds)):
        temp = len(left_compounds)
        if new_dict[x[i+temp]] == 1:
            result_str += right_compounds[i]
        else:
            result_str += str(new_dict[x[i+temp]]) + right_compounds[i]
        if i != (len(right_compounds) - 1):
            result_str += '+'

    return result_str

#print balance("PhCH3+KMnO4+H2SO4=PhCOOH+K2SO4+MnSO4+H2O")
