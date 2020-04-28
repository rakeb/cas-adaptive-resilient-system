import CustomUtilities
from physicalturtle import Turtle,done
import random
class ExternalAgent(Turtle):
    def __init__(self,asset_list):
        self.current_position = -1
        self.turtle = Turtle()
        self.turtle.resizemode("user")
        self.turtle.shapesize(1.5, 1, 2.4)
        self.entertainment_position = -1
        self.asset_knowledge = []
        self.confidentiality = 0
        self.extrovert = 0
        self.skill = random.randint(60,99)/float(100)
        self.crime_intention = random.randint(50,99)/float(100)
        for asset_type in asset_list:
            asset_type_knowledge = []
            for i in range(len(asset_type)):
                asset_type_knowledge.append(float(0))
            self.asset_knowledge.append(asset_type_knowledge)

    def setConfidentiality(self, conf):
        self.confidentiality = conf

    def setExtrovert(self, extro):
        self.extrovert = extro

    def setColor(self,colorname):
        self.turtle.color(colorname)

    def type_based_color(self,agent_type):
        if CustomUtilities.MALICIOUS_EXTERNAL_AGENT_CODE == agent_type:
            self.turtle.color('red')
            self.turtle.penup()
            self.turtle.goto(-400, -400)

        elif CustomUtilities.BENIGN_EXTERNAL_AGENT_CODE == agent_type:
            self.turtle.color('green')
            self.turtle.penup()
            self.turtle.goto(400, -400)

    def roam_around_outside_place(self, outside_place_list):
        while (True):
            outside_place = random.randint(0, len(outside_place_list) - 1)
            if outside_place != self.current_position:
                self.turtle.penup()
                self.turtle.goto(outside_place_list[outside_place][0], outside_place_list[outside_place][1])
                self.current_position = outside_place
                self.entertainment_position = outside_place
                break

    def get_punishment_risk(self):
        return float(CustomUtilities.PUNISHMENT_AMOUNT)/self.crime_intention




