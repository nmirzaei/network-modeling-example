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
  v1: s1 + 2 atp -> s2; k1*s1*atp/(1 + (atp/ki)^n);
  v2: s2 -> 2 s3; k2*s2;
  v3: s3 + nad -> s4 + atp; ((k31*k32*s3*nad*(atot - atp) - k33*k34*s4*atp*(ntot - nad))/(k33*(ntot - nad) + k32*(atot - atp)));
  v4: s4 -> s5 + atp; k4*s4*(atot - atp);
  v5: s5 -> s6; k5*s5;
  v7: atp -> ; k7*atp;
  v8: s3 -> nad; k8*s3*(ntot - nad);
  v9: s6o -> ; k9*s6o;
  v10: s6 -> 0.1 s6o; k10*(s6 - s6o);
  v6: s6 -> nad; k6*s6*(ntot - nad);
  v0:  -> s1; k0;

  // Species initializations:
  s1 = 1;
  atp = 2;
  s2 = 5;
  s3 = 0.6;
  nad = 0.6;
  s4 = 0.7;
  s5 = 8;
  s6 = 0.08;
  s6o = 0.02;

  // Variable initializations:
  k0 = 4.82;
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

  // Display nadmes:
  substance is "milli mole";
  time_unit is "min";
  s1 is "Glucose";
  atp is "ATP";
  s2 is "F16P";
  s3 is "Triose_Gly3Phos_DHAP";
  nad is "NAD";
  s4 is "3PG";
  s5 is "Pyruvate";
  s6 is "Acetaldehyde";
  s6o is "extracellular acetaldehyde";

end

""")    
r.simulate(0,1,500)
r.plot()
