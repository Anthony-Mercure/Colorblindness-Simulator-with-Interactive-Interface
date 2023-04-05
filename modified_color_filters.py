# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:18:37 2023

@author: shane
"""

import numpy as np

rgb_to_lms = np.array([[0.3811, 0.5783, 0.0402],
                       [0.1967, 0.7244, 0.0782],
                       [0.0241, 0.1288, 0.8444]])

normal = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]])

lms_protanomaly = np.array([[0.85616793, 0.18283919, -0.03800712],
                            [0.02934201, 0.95764199, 0.012015],
                            [0, 0, 1]]) # Modified

lms_deuteranomaly = np.array([[0.735, 0.265, 0],
                              [0.115, 0.885, 0],
                              [0, 0.028, 0.972]]) # Modified

lms_tritanomaly = np.array([[0.967, 0.033, 0],
                            [0, 0.733, 0.267],
                            [0, 0.183, 0.817]])

lms_protanopia = np.array([[0, 1.05118294, -0.05116099],
                       [0, 0.9513092, 0.04866992],
                       [0, 0, 1]])

lms_deuteranopia = np.array([[0.625, 0.375, 0],
                             [0.70, 0.30, 0],
                             [0, 0.30, 0.70]]) # Modified

"""lms_tritanopia = np.array([[1, 0, 0],
                           [0.095, 0.627, 0.278], 
                           [0, 0.075, 0.925]])""" # Modified

lms_tritanopia = np.array([[1, 0, 0],
                           [0.095, 0.627, 0.278], 
                           [0, 0.075, 0.925]]) # Modified

lms_achromatopsia = np.array([[0.299, 0.587, 0.114],
                              [0.299, 0.587, 0.114],
                              [0.299, 0.587, 0.114]])

filter_options = {
    "Normal": normal,
    "Protanopia": lms_protanopia,
    "Deuteranopia": lms_deuteranopia,
    "Tritanopia": lms_tritanopia,
    "Achromatopsia": lms_achromatopsia,
    "Protanomaly": lms_protanomaly,
    "Deuteranomaly": lms_deuteranomaly,
    "Tritanomaly": lms_tritanomaly
}