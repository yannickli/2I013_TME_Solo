# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:35:21 2017

@author: 3305496
"""

from soccersimulator import Vector2D, SoccerState, SoccerAction
from soccersimulator import Simulation, SoccerTeam, Player, show_simu
from soccersimulator import Strategy
from soccersimulator import settings
import math
import toolbox
import briques as BDB

class GolfStrategy(Strategy):
    def __init__(self):
        super(GolfStrategy,self).__init__("Golf")
    def compute_strategy(self,state,id_team,id_player):
        mystate = toolbox.MyState(state,id_team,id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return BDB.tirer(mystate,2)
            #return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                    #Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        distance = state.player_state(id_team,id_player).position.distance(zone.position+zone.l/2.)
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            if (distance>4):
                return BDB.goToBall(mystate)
            else:
                return SoccerAction()
        """ sinon """
        if mystate.can_shoot():
            if (distance<10):
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,0.1)
            elif (distance>30): 
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,3)
            else:
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,1)
        return BDB.goToBall(mystate)
        
        
class SlalomStrategy(Strategy):
    def __init__(self):
        super(SlalomStrategy,self).__init__("Slalom")
    def compute_strategy(self,state,id_team,id_player):
        mystate = toolbox.MyState(state,id_team,id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return BDB.tirer(mystate,2)
            #return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                    #Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return BDB.goToBall(mystate)
        """ sinon """
        distance = state.player_state(id_team,id_player).position.distance(zone.position+zone.l/2.)
        if mystate.can_shoot():
            if (distance<10):
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,0.5)
            elif (distance>30): 
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,3)
            else:
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,1)
        return BDB.goToBall(mystate)
        
        
class SlalomStrategyJ1(Strategy):
    def __init__(self):
        super(SlalomStrategyJ1,self).__init__("SlalomJ1")
    def compute_strategy(self,state,id_team,id_player):
        mystate = toolbox.MyState(state,id_team,id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return BDB.tirer(mystate,2)
            #return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                    #Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return BDB.goToBall(mystate)
        """ sinon """
        distance = state.player_state(id_team,id_player).position.distance(zone.position+zone.l/2.)
        if mystate.can_shoot():
            if (distance<10):
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,0.5)
            elif (distance>30): 
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,3)
            else:
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,1)
        return BDB.goToBall(mystate)
        
        
class SlalomStrategyJ2(Strategy):
    def __init__(self):
        super(SlalomStrategyJ2,self).__init__("SlalomJ2")
    def compute_strategy(self,state,id_team,id_player):
        mystate = toolbox.MyState(state,id_team,id_player)
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return BDB.tirer(mystate,2)
            #return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                    #Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return BDB.goToBall(mystate)
        """ sinon """
        distance = state.player_state(id_team,id_player).position.distance(zone.position+zone.l/2.)
        if mystate.can_shoot():
            if (distance<10):
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,0.5)
            elif (distance>30): 
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,3)
            else:
                return BDB.TirerEn(mystate,zone.position+zone.l/2.,1)
        return BDB.goToBall(mystate)
        