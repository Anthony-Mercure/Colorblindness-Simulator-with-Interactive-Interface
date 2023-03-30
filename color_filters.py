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

lms_protanomaly = np.array([[0.817, 0.183, 0],
                            [0.333, 0.667, 0],
                            [0, 0.125, 0.875]])

lms_deuteranomaly = np.array([[0.8, 0.2, 0],
                              [0.258, 0.742, 0],
                              [0, 0.142, 0.858]])

lms_tritanomaly = np.array([[0.967, 0.033, 0],
                            [0, 0.733, 0.267],
                            [0, 0.183, 0.817]])

lms_protanopia = np.array([[0, 1.05118294, -0.05116099],
                       [0, 0.9513092, 0.04866992],
                       [0, 0, 1]])

lms_deuteranopia = np.array([[0.65, 0.35, 0],
                             [0.70, 0.30, 0],
                             [0, 0.30, 0.70]])

"""lms_tritanopia = np.array([[1.00000000, 0.00000000, 0.00000000],
                           [0.00000000, 0.73334000, 0.26666000],
                           [0.00000000, 0.18334000, 0.81666000]])"""

lms_tritanopia = np.array([[1, 0, 0],
                           [0.2, 0.8, 0], 
                           [0, 0.18334, 0.81666]])

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