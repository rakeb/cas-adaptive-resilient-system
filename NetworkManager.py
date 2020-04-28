import CustomUtilities
# from physicalturtle import Turtle,done
from turtle import Turtle,done
import random

class NetworkManager(Turtle):
    def __init__(self,asset_list):
        self.current_position = 0
        self.turtle = Turtle()
        self.turtle.resizemode("user")
        self.turtle.shapesize(2, 2, 3.4)
        self.entertainment_position = -1
        self.co_ordinate = 0
        self.asset_knowledge = []
        self.confidentiality = 0
        self.extrovert = 0
        self.issue_queue = []
        self.patch_up_vulnerability = []
        self.skill = 1.0
        self.adaptavility = 1.0
        for asset_type in asset_list:
            asset_type_knowledge = []
            for i in range(len(asset_type)):
                asset_type_knowledge.append(float(1))
            self.asset_knowledge.append(asset_type_knowledge)

    def start_manager(self,position):
        self.turtle.color('blue')
        self.turtle.penup()
        self.turtle.goto(position[0]+10,position[1])
        self.co_ordinate = [position[0]+10,position[1]]
        self.setConfidentiality(1.0)
        self.setExtrovert(1.0)

    def setConfidentiality(self, conf):
        self.confidentiality = conf

    def setExtrovert(self, extro):
        self.extrovert = extro

    def roam_around_the_responsible_asset(self):
        self.turtle.penup()
        self.turtle.goto(self.co_ordinate[0], self.co_ordinate[1])
        self.current_position = 0

    def roam_internal_entertainment(self, internal_entertainment_place):
        # print internal_entertainment_place
        entertain_place = random.randint(0, len(internal_entertainment_place) - 1)
        self.turtle.goto(internal_entertainment_place[entertain_place][0],
                         internal_entertainment_place[entertain_place][1])
        self.current_position = entertain_place + 1
        self.entertainment_position = entertain_place

    def roam_conference(self, internal_conference_place):
        confer_place = random.randint(0, len(internal_conference_place) - 1)
        self.turtle.goto(internal_conference_place[confer_place][0],
                         internal_conference_place[confer_place][1])
        self.current_position =  confer_place + 1

    def roam_around_outside_place(self, outside_place_list):
        while (True):
            outside_place = random.randint(0, len(outside_place_list) - 1)
            if (outside_place + 2) != self.current_position:
                self.turtle.penup()
                self.turtle.goto(outside_place_list[outside_place][0], outside_place_list[outside_place][1])
                self.current_position = outside_place + 2
                self.entertainment_position = outside_place + CustomUtilities.NUM_ENTERTAINMENT_PLACE
                break

    def request_service(self,asset_object_id):
        if asset_object_id in self.issue_queue:
            return
        # print "Now Inserting Service Queue : ---> ",asset_object_id
        self.issue_queue.append(asset_object_id)

    def serve_request(self,asset_object_list):
        if len(self.issue_queue)==0:
            print ("No Service for network manager")
            return
        asset_id = self.issue_queue.pop(0)
        # print "Asset Id :",asset_id," Vul ",asset_object_list[asset_id].vulnerabilities
        # print "After Poping ",asset_id," Now Status ",self.issue_queue
        self.turtle.penup()
        # print "Co-Ordination : ",asset_object_list[asset_id].co_ordinate[0]," ",asset_object_list[asset_id].co_ordinate[1]
        self.turtle.goto(asset_object_list[asset_id].co_ordinate[0],asset_object_list[asset_id].co_ordinate[1])
        remove_list = []
        for vul in asset_object_list[asset_id].vulnerabilities:
            if vul in self.patch_up_vulnerability:
                remove_list.append(vul)

        for vul in remove_list:
            asset_object_list[asset_id].vulnerabilities.remove(vul)

        # print "After Service ", asset_object_list[asset_id].vulnerabilities