# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 06:54:30 2021

@author: Lucian
"""

import tellurium as te
import roadrunner

r = te.loada("""
// Created by libAntimony v2.12.0.3
model *Wolf2000_Glycolytic_Oscillations()

  // Reactions:
  v1: s1 + 2 atp -> s2 + 2 adp + 2 $pIn; k1*s1*atp/(1 + (atp/ki)^n);
  v2: s2 -> 2 s3; k2*s2;
  v3: s3 + NADH + adp + $pIn -> s4 + atp + NAD; ((k31*k32*s3*NADH*adp - k33*k34*s4*atp*NAD)/(k33*NAD + k32*adp));
  v4: s4 + adp + $pIn -> s5 + atp; k4*s4*adp;
  v5: s5 -> s6; k5*s5;
  v7: atp -> adp + $pIn; k7*atp;
  v8: s3 + NAD -> NADH; k8*s3*NAD;
  v9: s6o -> ; k9*s6o;
  v10: s6 -> 0.1 s6o; k10*(s6 - s6o);
  v6: s6 + NAD -> NADH; k6*s6*NAD;
  v0:  -> s1; k0;

  // Species initializations:
  s1 = 1;
  atp = 2;
  adp = atot - atp
  pIn = 1000
  s2 = 5;
  s3 = 0.6;
  NADH = 0.6;
  NAD = ntot - NADH
  s4 = 0.7;
  s5 = 8;
  s6 = 0.08;
  s6o = 0.02;

  // Variable initializations:
  k0 = 50;
  k1 = 550;
  k2 = 9.8;
  k31 = 323.8;
  k33 = 57823.1;
  k32 = 76411.1;
  k34 = 23.7;
  k4 = 77.77;
  k5 = 9.7;
  k6 = 2140;
  k7 = 31.17;
  k8 = 85.7;
  k9 = 180;
  k10 = 375;
  atot = 4;
  ntot = 1;
  n = 4;
  ki = 1;

  // Display names:
  substance is "milli mole";
  time_unit is "min";
  s1 is "Glucose";
  atp is "ATP";
  s2 is "F16P";
  s3 is "Triose_Gly3Phos_DHAP";
  NADH is "NADH";
  s4 is "3PG";
  s5 is "Pyruvate";
  s6 is "Acetaldehyde";
  s6o is "extracellular acetaldehyde";

end

""")    
r.simulate(0,1,500)
r.plot()
