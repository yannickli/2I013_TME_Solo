# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:41:12 2017

@author: 3305496
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math
import toolbox
import sys
import briques as BDB
import messtrategies as MS
    
def get_golf_team():
    s=SoccerTeam("Y.L.")
    s.add("JoueurGolf",MS.GolfStrategy())
    return s
    
def get_slalom_team1():
    s=SoccerTeam("Y.L.")
    s.add("JoueurSlalom",MS.SlalomStrategy())
    return s
    
def get_slalom_team2():
    s=SoccerTeam("Y.L.")
    s.add("JoueurSlalom1",MS.SlalomStrategyJ1())
    s.add("JoueurSlalom2",MS.SlalomStrategyJ2())
    return s
