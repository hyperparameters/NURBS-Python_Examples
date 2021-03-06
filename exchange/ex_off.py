#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2018
"""
from geomdl.shapes import surface
from geomdl import exchange

cylinder = surface.cylinder(radius=5.0, height=22.5)
cylinder.delta = 0.01

# Export the surface as a .off file
exchange.export_off(cylinder, "cylindrical_surface.off")

# Good to have something here to put a breakpoint
pass
