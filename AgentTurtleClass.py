import random

# from physicalturtle import Turtle
from turtle import Turtle


class AgentTurtle(Turtle):
    def __init__(self, id, start_position, agent_type, turtle_speed):
        self.id = id
        self.main_position = start_position
        self.agent_type = agent_type
        self.agent_attribute = None  # means attack-defence variance
        self.turtle = Turtle(visible=False)
        self.turtle.shape("turtle")
        self.turtle.resizemode("user")
        self.turtle.shapesize(1.5, 1, 2.4)
        self.turtle.speed(turtle_speed)
        self.current_position = 0
        self.asset_knowledge = []
        self.responsible_asset = {}
        self.entertainment_position = -1
        self.confidentiality = 0
        self.extrovert = 0
        self.skill = 1.0
        self.adaptavility = random.randint(80, 99) / float(100)
        # self.turtle.color('red')
        self.number_responsible_asset = 0
        self.color_name = None

    def setColor(self, colorName):
        self.color_name = colorName
        self.turtle.color(colorName)

    def setTurtleSize(self, x, y, z):
        self.turtle.shapesize(x, y, z)

    def set_agent_attribute(self, agent_attribute):
        self.agent_attribute = agent_attribute

    def make_turtle_visible(self):
        self.turtle.showturtle()

    def move_turtle(self, x, y):
        self.turtle.goto(x, y)
