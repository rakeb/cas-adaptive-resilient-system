class Attributes:
    def __init__(self, id):
        self.id = id
        self.asset_index = None
        self.variance = None
        self.defender = None

    def setAssetIndex(self, asset_index):
        self.asset_index = asset_index

    def setVariance(self, variance):
        self.variance = variance

    def setDefender(self, defender):
        self.defender = defender

    def checkEquality(self, attribute):
        if self.variance != attribute.variance:
            # do something
            return False
        return True
