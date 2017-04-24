# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:42:26 2017

@author: 3305496
"""

from soccersimulator import GolfState,Golf,Parcours1,Parcours2,Parcours3,Parcours4
from soccersimulator import SoccerTeam,show_simu
from soccersimulator import Strategy,SoccerAction,Vector2D,settings
import briques as BDB
import messtrategies as MS

GOLF = 0.001
SLALOM = 10.

class DemoStrategy(Strategy):
    def __init__(self):
        super(DemoStrategy,self).__init__("Demo")
    def compute_strategy(self,state,id_team,id_player):
        """ zones : liste des zones restantes a valider """
        zones = state.get_zones(id_team)
        if len(zones)==0:
            """ shooter au but """
            return SoccerAction(state.ball.position-state.player_state(id_team,id_player).position,\
                    Vector2D((2-id_team)*settings.GAME_WIDTH,settings.GAME_HEIGHT/2.)-state.ball.position)
        """ zone : carre de zone avec z.position angle bas,gauche et z.l longueur du cote
            centre du carre : zone.position+Vector2D(z.l/2.,z.l/2.)
            zone.dedans(point) : teste si le point est dans la zone
        """
        zone = zones[0]
        """ si la ball est dans une zone a valider """
        if zone.dedans(state.ball.position):
            return SoccerAction()
        """ sinon """
        #distance = state.player_state(id_team,id_player).position.distance(zone.position+zone.l/2.)
        return SoccerAction()

team0 = SoccerTeam()
team0.add("John",DemoStrategy())

team1 = SoccerTeam()
team1.add("Golf",MS.GolfStrategy())

team2 = SoccerTeam()
team2.add("Slalom",MS.SlalomStrategy())

team3 = SoccerTeam()
team3.add("SlalomJ1",MS.SlalomStrategyJ1())
team3.add("SlalomJ2",MS.SlalomStrategyJ2())
"""
simu = Parcours1(team1=team1,vitesse=GOLF)
show_simu(simu)

simu = Parcours2(team1=team1,vitesse=GOLF)
show_simu(simu)
simu = Parcours3(team1=team1,vitesse=GOLF)
show_simu(simu)
"""
simu = Parcours4(team1=team3,team2=team0,vitesse=SLALOM)
show_simu(simu)
