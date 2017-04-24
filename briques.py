# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:57:49 2017

@author: 3305496
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math
import toolbox

def goToBall(m):
    return m.aller(m.ball_position())
    
def goToBallPredict(m):
    return m.aller(m.ballPredict(3))
    
def intercepter(m,d):
    if m.can_shoot():
        return shootToGoal(m)
    return m.aller((m.ball_position()-m.my_but).normalize()*d+m.my_but)
    
def saligner(m,d):
    if m.can_shoot():
        return shootToGoal(m)
    return m.aller((m.ball_position()-m.adv_but).normalize()*d+m.adv_but)

def shootEnA(m):
    if (m.ball_position().y<=settings.GAME_HEIGHT/2):
        return m.shoot(m.posA-Vector2D(0,settings.GAME_HEIGHT/4))
    if (m.ball_position().y>=settings.GAME_HEIGHT/2):
        return m.shoot(m.posA+Vector2D(0,settings.GAME_HEIGHT/4))
  
def allerEnA(m):
    if (m.ball_position().y<settings.GAME_HEIGHT/2):
        return m.aller(m.posA-Vector2D(0,settings.GAME_HEIGHT/4))
    if (m.ball_position().y>settings.GAME_HEIGHT/2):
        return m.aller(m.posA+Vector2D(0,settings.GAME_HEIGHT/4))

def goToBallAmeliore(m,k):
    return m.aller(m.ball_position(),k*m.distanceToBall(m.my_position()))
 
def shootToGoal(m,k=4.8):
    return m.shoot(m.adv_but,k)

def TirerEn(m,p,k=4.8):
    return m.shoot(p,k)

def degager(m):
    if m.can_shoot():
        return shootEnA(m)
    return goToBallPredict(m)

def tirer(m,k=4.8):
    if m.can_shoot():
        return shootToGoal(m,k)
    return goToBallPredict(m)

def dribblerVersCage(m):
    if m.can_shoot():
        return shootToGoal(m,0.5)
    return goToBall(m) 

def dribbler(m):
    if m.can_shoot():
        return m.shoot(m.my_position()+m.myVitesse(),1)
    return goToBall(m) 

def allerGauche(m):
    return m.aller(m.my_position()+Vector2D(-1,0))
    
def allerDroite(m):
    return m.aller(m.my_position()+Vector2D(1,0))
    
def allerBas(m):
    return m.aller(m.my_position()+Vector2D(0,-1))
    
def allerHaut(m):
    return m.aller(m.my_position()+Vector2D(0,1))
    