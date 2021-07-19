# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 06:54:30 2021

@author: Lucian
"""

import tellurium as te
import roadrunner

r = te.loads("https://www.ebi.ac.uk/biomodels/model/download/BIOMD0000000206.2?filename=BIOMD0000000206_url.xml")

r.simulate(0,1,500)
r.plot()
