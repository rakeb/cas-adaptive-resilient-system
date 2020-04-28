import CustomUtilities
# from physicalturtle import Turtle,done
from turtle import Turtle,done
import random

class InternalAgent(Turtle):
    def __init__(self,start_position,responsibility_type,asset_list):
        self.main_position = start_position
        self.responsibility_type = responsibility_type
        self.turtle = Turtle()
        self.turtle.resizemode("user")
        self.turtle.shapesize(1.5,1,2.4)
        self.current_position = 0
        self.asset_knowledge = []
        self.responsible_asset = {}
        self.entertainment_position = -1
        self.confidentiality = 0
        self.extrovert = 0
        self.skill = 1.0
        self.adaptavility = random.randint(80,99)/float(100)
        # self.turtle.color('red')
        self.number_responsible_asset = 0
        for asset in asset_list:
            asset_type_knowledge = []
            for i in range(len(asset)):
                asset_type_knowledge.append(float(0))
            self.asset_knowledge.append(asset_type_knowledge)

        # print self.asset_knowledge
    def setColor(self,colorName):
        self.turtle.color(colorName)

    def setConfidentiality(self,conf):
        self.confidentiality = conf

    def setExtrovert(self,extro):
        self.extrovert = extro

    def knowledge_other_asset(self,responsible_list):
        for asset_type in responsible_list.keys():
            if asset_type not in self.responsible_asset.keys():
                self.responsible_asset[asset_type] = []
            get_asset_knowledge = responsible_list[asset_type]
            # print asset_type, " :::: ", get_asset_knowledge
            if get_asset_knowledge == CustomUtilities.BROAD_CAST:
                # print asset_type, " :::: ", get_asset_knowledge
                get_asset_knowledge = self.asset_knowledge[asset_type]


                for asset in range(len(get_asset_knowledge)):
                    self.asset_knowledge[asset_type][asset] = float(1)
                    self.responsible_asset[asset_type].append(asset)
                    self.number_responsible_asset += 1
                continue
            for asset in get_asset_knowledge:
                self.asset_knowledge[asset_type][asset] = float(1)
                self.responsible_asset[asset_type].append(asset)
                self.number_responsible_asset += 1

    def roam_around_the_responsible_asset(self,asset_list):
        if self.number_responsible_asset == 1:
            if self.current_position != 0:
                self.turtle.goto(asset_list[self.responsibility_type][self.responsible_asset[self.responsibility_type][0]][0],
                                 asset_list[self.responsibility_type][self.responsible_asset[self.responsibility_type][0]][1])
                self.current_position = 0
            return
        asset_responsible = self.responsible_asset[self.responsibility_type]
        while(True):
            new_position = random.randint(0,self.number_responsible_asset-1)
            if self.current_position != new_position:
                self.current_position = new_position
                self.turtle.penup()
                # print asset_list
                # print self.responsibility_type," ",new_position
                self.turtle.goto(asset_list[self.responsibility_type][self.responsible_asset[self.responsibility_type][new_position]][0],
                                 asset_list[self.responsibility_type][self.responsible_asset[self.responsibility_type][new_position]][1])

                break

    def roam_internal_entertainment(self,internal_entertainment_place):
        # print internal_entertainment_place
        entertain_place = random.randint(0,len(internal_entertainment_place)-1)
        self.turtle.goto(internal_entertainment_place[entertain_place][0],internal_entertainment_place[entertain_place][1])
        self.current_position = self.number_responsible_asset + entertain_place
        self.entertainment_position = entertain_place

    def roam_conference(self,internal_conference_place):
        confer_place = random.randint(0, len(internal_conference_place) - 1)
        self.turtle.goto(internal_conference_place[confer_place][0],
                         internal_conference_place[confer_place][1])
        self.current_position = self.number_responsible_asset + confer_place
        CustomUtilities.increase_conference_agents_skill_specific(self)

    def roam_around_outside_place(self,outside_place_list):
        while(True):
            outside_place = random.randint(0, len(outside_place_list) - 1)
            if outside_place != (-self.current_position):
                self.turtle.penup()
                self.turtle.goto(outside_place_list[outside_place][0],outside_place_list[outside_place][1])
                self.current_position = (-1) * outside_place
                self.entertainment_position = CustomUtilities.NUM_ENTERTAINMENT_PLACE + outside_place
                break

    def check_vulnerability(self,asset_to_asset_object_mapping,asset_object_list,network_manager_list):
        # print "Agent Skill : ",self.skill
        if self.skill > 0.8:
            for asset_type in self.responsible_asset.keys():
                for asset in self.responsible_asset[asset_type]:
                    if len(asset_object_list[asset_to_asset_object_mapping[asset_type][asset]].vulnerabilities) > 0:
                        network_manager_list[0].request_service(asset_to_asset_object_mapping[asset_type][asset])

    def decrease_skill(self):
        self.skill -= CustomUtilities.DECREASE_SKILL_EACH_DAY

    def move_next_position(self):
        pass