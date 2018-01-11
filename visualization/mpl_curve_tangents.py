# -*- coding: utf-8 -*-

"""
    Visualization Examples for the NURBS-Python Package
    Released under The MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""
from geomdl import BSpline
from geomdl import utilities

import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

#
# Curve Evaluation
#

# Create a BSpline curve instance
curve = BSpline.Curve2D()

# Set evaluation delta
curve.delta = 0.01

# Set up the NURBS curve
curve.read_ctrlpts_from_txt("../curve2d/ex_curve03.cpt")
curve.degree = 3

# Auto-generate knot vector
curve.knotvector = utilities.generate_knot_vector(curve.degree, len(curve.ctrlpts))

# Evaulate curve
curve.evaluate()

#
# Tangent Vector Evaluation
#

# Store tangent vectors in a list for plotting
curvetan = []

# Evaluate curve tangent at u = 0.0
ct1 = curve.tangent(0.0, normalize=True)
curvetan.append(ct1)

# Evaluate curve tangent at u = 0.2
ct2 = curve.tangent(0.2, normalize=True)
curvetan.append(ct2)

# Evaluate curve tangent at u = 0.5
ct3 = curve.tangent(0.5, normalize=True)
curvetan.append(ct3)

# Evaluate curve tangent at u = 0.6
ct4 = curve.tangent(0.6, normalize=True)
curvetan.append(ct4)

# Evaluate curve tangent at u = 0.8
ct5 = curve.tangent(0.8, normalize=True)
curvetan.append(ct5)

# Evaluate curve tangent at u = 1.0
ct6 = curve.tangent(1.0, normalize=True)
curvetan.append(ct6)

#
# Control Points, Curve and Tangent Vector Plotting
#

# Arrange control points and evaluated curve points for plotting
ctrlpts = np.array(curve.ctrlpts)
curvepts = np.array(curve.curvepts)

# Convert tangent list into a NumPy array
ctarr = np.array(curvetan)

# Plot using Matplotlib
plt.figure(figsize=(10.67, 8), dpi=96)
yaxis = plt.plot((-1, 25), (0, 0), "k-")  # y-axis line
cppolygon, = plt.plot(ctrlpts[:, 0], ctrlpts[:, 1], "k-.")  # control points polygon
curveplt, = plt.plot(curvepts[:, 0], curvepts[:, 1], "g-")  # evaluated curve points
tanline = plt.quiver(ctarr[:, 0, 0], ctarr[:, 0, 1], ctarr[:, 1, 0], ctarr[:, 1, 1], color="blue", angles='xy', scale_units='xy', scale=1, width=0.003)  # tangents
tanlinekey = plt.quiverkey(tanline, 23.75, -14.5, 35, "Tangent Vectors", coordinates='data', labelpos='W')
plt.legend([cppolygon, curveplt], ["Control Points", "Evaluated Curve"])
plt.axis([-1, 25, -15, 15])
plt.show()