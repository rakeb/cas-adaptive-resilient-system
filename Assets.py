import random


class Assets:
    def __init__(self, asset_id, asset_type, co_ordinate):
        self.primary_id = asset_id
        self.co_ordinate = co_ordinate
        self.edge = []
        self.asset_type = asset_type
        self.internet_connection = 0
        self.vulnerabilities = []
        self.asset_value = 0
        self.set_asset_value()
        self.imposed_risk = 0

    def add_connection(self, asset_neighbour_id):
        self.edge.append(asset_neighbour_id)

    def set_asset_value(self):
        self.asset_value = float(random.randint(1500, 3000))
        # print "Asset ID : ",self.primary_id," Asset Value :",self.asset_value

    def set_attacker(self, attacker):
        self.attacker = attacker

    def set_defender(self, defender):
        self.defender = defender
