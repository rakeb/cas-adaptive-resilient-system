import csv
import random
import time

# from physicalturtle import done, mainloop
from turtle import Turtle,done, mainloop
import CustomUtilities
import ProjectUtilitiesUpdated
from AgentAttributesClass import Attributes
from AgentTurtleClass import AgentTurtle

YES = True
NO = False

############## customize here: STARTS ##############
# fastest: 0
# fast: 10
# normal: 6
# slow: 3
# slowest: 1
turtle_speed = "normal"
# turtle_speed = 8
adaptive_window = 100  # how many simulation

number_of_defense_agent = 5  # how many defender agent
can_new_defender_added = YES
can_defense_variance_will_increase = YES
new_defense_agent_adding_chance = .8
new_defense_agent_scale = 1

can_defend_through_node = YES
can_defender_learn_network_component = YES

defense_variance = 50  # number of strategy defender can have
defender_adaptation_by = .5

attack_variance = 5  # number of strategy attacker can have
can_attacker_adapt = YES
can_attacker_try_previous_technique = YES
attacker_adaptation_rate = .2
attacker_adaptation_by = .5

can_attack_node = YES

# if can_defender_learn_network_component = NO
probability_of_asset_selection = .1
############## customize here: ENDS ##############


AGENT_ATTACKER = 0
AGENT_DEFENDER = 1
already_attacked_variance = []
attacker_turtle = None
defender_agent_list = []
attacker_knowledge = []
defender_knowledge = []
attack_defense_knowledge = {}

router_list = []
attacker_box_list = []
defender_box_list = []
firewall_list = []
node_list = []
ids_list = []
internal_agents = []
internal_entertainment_place = []
internal_conference_place = []
asset_list = []
responsible_asset_agent = []
outside_place_list = []
benign_agent_list = []
malicious_agent_list = []
network_manager_list = []
asset_object_list = []
internal_entertainment_place_agents = []
outside_place_agents = []
day_index = 8
each_work_day_index = 0
conference_gap_period = 2
network_manager_service_per_period = 1
asset_to_asset_object_mapping = {}
risk_by_days = []
risk_file = 0

# color_code = {0: "#CCFFCC", 1: "#99FF99", 2: "#66FF66", 3: "#33FF33", 4: "#00FF00", 5: "#00CC00", 6: "#009900",
#               7: "#006600", 8: "#003300"}
color_code = {0: "#33FF33", 1: "#00FF00", 2: "#00CC00", 3: "#009900",
              4: "#006600", 5: "#003300"}


def decision(probability):
    return random.random() < probability


def create_attacker_turtle():
    global attacker_turtle
    print("Attacker Agent Created")
    for attacker_box in attacker_box_list:
        attacker_turtle = AgentTurtle(0, attacker_box, AGENT_ATTACKER, turtle_speed)
        attacker_turtle.turtle.penup()

        attacker_turtle.move_turtle(500, 250)
        attacker_turtle.make_turtle_visible()

        attacker_turtle.setColor('red')
        attacker_turtle.turtle.goto(attacker_box[0], attacker_box[1])
        attacker_turtle.setTurtleSize(1.8, 1.3, 2.7)


def create_defender_turtle(position):
    global color_code
    global defender_agent_list
    for i in range(number_of_defense_agent):
        print("Creating Defender Agent %s" % i)
        defender_agent_list.append(AgentTurtle(i, position, AGENT_DEFENDER, turtle_speed))
        defender_agent_list[i].turtle.penup()

        defender_agent_list[i].move_turtle(500, 250)
        defender_agent_list[i].make_turtle_visible()

        defender_agent_list[i].setColor(color_code[0])

        defender_agent_list[i].turtle.goto(position[0], position[1])


def create_new_defender_turtle(position):
    global defender_agent_list
    global color_code
    current_number_of_defender = len(defender_agent_list)
    for i in range(new_defense_agent_scale):
        id = current_number_of_defender + i
        defender_agent_list.append(AgentTurtle(id, position, AGENT_DEFENDER, turtle_speed))
        defender_agent_list[id].turtle.penup()

        defender_agent_list[id].move_turtle(500, 250)
        defender_agent_list[id].make_turtle_visible()

        defender_agent_list[id].setColor(color_code[0])
        defender_agent_list[id].turtle.goto(position[0], position[1])


def start_attack(simulation_count):
    global attacker_turtle
    global can_attack_node
    global attacker_knowledge
    global already_attacked_variance

    attack_success = False

    while not attack_success:
        index_assets = random.randint(0, len(asset_object_list) - 1)
        asset = asset_object_list[index_assets]
        if not can_attack_node and asset.asset_type == CustomUtilities.NODE_TYPE:
            continue

        if asset.asset_type == CustomUtilities.ATTACKER_TYPE or asset.asset_type == CustomUtilities.DEFENDER_TYPE:
            continue

        variance = random.randint(0, int(attack_variance))

        if not can_attacker_try_previous_technique:
            if variance in already_attacked_variance:
                if len(already_attacked_variance) > attack_variance:
                    increase_attack_variance()
                continue

        already_attacked_variance.append(variance)

        atr_id = len(attacker_knowledge)
        attacker_attribute = Attributes(atr_id)

        attacker_attribute.setVariance(variance)
        attacker_attribute.setAssetIndex(index_assets)

        attacker_turtle.turtle.penup()
        attacker_turtle.turtle.goto(asset.co_ordinate[0], asset.co_ordinate[1])
        attacker_turtle.set_agent_attribute(attacker_attribute)

        attack_success = True
        attacker_knowledge.append(attacker_attribute)

        print("Attack started with Attack Variance: %s" % variance)


def reset_attacker():
    global attacker_turtle
    attacker_turtle.turtle.penup()
    attacker_turtle.turtle.goto(attacker_box_list[0][0], attacker_box_list[0][1])


def adapt_knowledge(attacker_turtle, defender_turtle):
    global attack_defense_knowledge

    print("Defender get adapted.")
    variance = attacker_turtle.agent_attribute.variance
    attack_defense_knowledge[variance] = defender_turtle


def check_knowledge(attacker_attribute):
    global attack_defense_knowledge
    variance = attacker_attribute.variance

    if variance in attack_defense_knowledge:
        return True, attack_defense_knowledge[variance]
    else:
        return False, None


def defense_with_knowledge(defender_turtle):
    global probability_of_asset_selection
    global can_defend_through_node

    defense_success = False
    while not defense_success:
        index_assets = random.randint(0, len(asset_object_list) - 1)
        asset = asset_object_list[index_assets]

        if not can_defend_through_node and asset.asset_type == CustomUtilities.NODE_TYPE:
            continue
        if asset.asset_type == CustomUtilities.ATTACKER_TYPE or asset.asset_type == CustomUtilities.DEFENDER_TYPE:
            continue

        defender_turtle.turtle.penup()
        defender_turtle.turtle.goto(asset.co_ordinate[0], asset.co_ordinate[1])
        # defender_turtle.set_agent_attribute(defender_attribute)

        if can_defender_learn_network_component:
            probability_of_asset_selection += .1

        if decision(probability_of_asset_selection):
            defense_success = True
            reset_attacker()
            # redefine successful agent
            color_name = defender_turtle.color_name
            color_name = get_next_color(color_name)
            defender_turtle.setColor(color_name)
            defender_turtle.setColor(color_name)
            # adapt_knowledge(attacker_turtle, defender_turtle)
            print("Defended with attack knowledge. Defender: %s" % defender_turtle.id)
        else:
            # print("Probabilistic decision: False")
            pass


def get_next_color(color):
    global color_code
    number_of_color = len(color_code)
    for key, value in color_code.items():
        if value == color:
            if key == number_of_color - 1:
                return color

            key = (key + 1) % number_of_color
            return color_code[key]


def try_adding_new_defender():
    if can_new_defender_added:
        if decision(new_defense_agent_adding_chance):
            print("Existing defense agent failed to defend. Researcher adding new defense agent...")
            create_new_defender_turtle(defender_box_list[0])


def increase_defense_variance():
    global defense_variance
    global defender_adaptation_by
    defense_variance += defender_adaptation_by
    print("Defense variance increased to: %s" % defense_variance)


def increase_attack_variance():
    global attack_variance
    global attacker_adaptation_by
    global can_attacker_adapt
    if can_attacker_adapt:
        if decision(attacker_adaptation_rate):
            attack_variance += attacker_adaptation_by
            print ("Attacker Adapted.")
            print("Attack variance: %s" % attack_variance)


def start_defend():
    global defender_agent_list
    global can_defend_through_node
    global attacker_turtle
    global defender_knowledge
    global attack_defense_knowledge

    attacker_attribute = attacker_turtle.agent_attribute

    flag, defender_turtle = check_knowledge(attacker_attribute)
    defense_success = False
    if flag:
        # print("Defense with Knowledge...")
        defense_with_knowledge(defender_turtle)
        defense_success = True

    i = 0
    trial_number = 0
    while not defense_success:
        index_assets = random.randint(0, len(asset_object_list) - 1)
        asset = asset_object_list[index_assets]
        trial_number += 1
        if not can_defend_through_node and asset.asset_type == CustomUtilities.NODE_TYPE:
            continue
        if asset.asset_type == CustomUtilities.ATTACKER_TYPE or asset.asset_type == CustomUtilities.DEFENDER_TYPE:
            continue

        defender_turtle = defender_agent_list[i]
        i = (i + 1) % len(defender_agent_list)

        atr_id = len(defender_knowledge)
        defender_attribute = Attributes(atr_id)
        variance = random.randint(0, int(defense_variance))
        defender_attribute.setVariance(variance)
        defender_attribute.setAssetIndex(index_assets)

        defender_turtle.turtle.penup()
        defender_turtle.turtle.goto(asset.co_ordinate[0], asset.co_ordinate[1])
        defender_turtle.set_agent_attribute(defender_attribute)

        # print("Defense Agent %s is trying to defend with defense variance %s." % (defender_turtle.id, variance))

        if defender_attribute.checkEquality(attacker_attribute):
            defense_success = True
            reset_attacker()
            # redefine successful agent
            color_name = defender_turtle.color_name
            color_name = get_next_color(color_name)
            defender_turtle.setColor(color_name)
            print("Defended without prior attack knowledge. Defender: %s" % defender_turtle.id)

            adapt_knowledge(attacker_turtle, defender_turtle)

        else:
            # print("Defender %s is failed to defend." % defender_turtle.id)
            if trial_number > (len(asset_object_list) - 2):
                try_adding_new_defender()
                if can_defense_variance_will_increase:
                    increase_defense_variance()
                trial_number = 0


def start_simulation(i):
    start_attack(i)
    start_defend()


def create_some_turtle():
    global color_code
    for key, value in color_code.iteritems():
        t = AgentTurtle(key, None, AGENT_DEFENDER, turtle_speed)
        t.turtle.penup()

        t.move_turtle(500, 250)
        t.make_turtle_visible()
        t.setColor(value)

        t.turtle.goto((key * 20 + 300), 300)


if __name__ == "__main__":
    print ("Adaptive Cyber Defense System Against Advanced Persistent Threat Starts...")
    # init_env()
    ProjectUtilitiesUpdated.BuildNetwork(node_list, router_list, firewall_list, ids_list, attacker_box_list,
                                         defender_box_list,
                                         asset_object_list, turtle_speed)
    # check_network_connection()
    # print "Node List --> ",
    # for i in node_list:
    #     print "(", i[0], ",", i[1], ")",
    # print ""
    # print "Router List --> ",
    # for i in router_list:
    #     print "(", i[0], ",", i[1], ")",
    # print ""
    # print "Firewall List --> ",
    # for i in firewall_list:
    #     print "(", i[0], ",", i[1], ")",
    # print ""
    # print "IDS List --> ",
    # for i in ids_list:
    #     print "(", i[0], ",", i[1], ")",
    # print ""
    # create_some_turtle()
    asset_list.append(node_list)
    asset_list.append(firewall_list)
    asset_list.append(ids_list)
    asset_list.append(router_list)

    create_attacker_turtle()
    create_defender_turtle(defender_box_list[0])

    # create_some_turtle()
    for i in range(adaptive_window):
        print ("Attacker Adaptation round: %s" % i)
        start = time.time()
        start_simulation(i)
        done = time.time()
        elapsed = done - start
        print("Time: %s seconds" % elapsed)
        # print("Time to defense: %s seconds" % int(elapsed))

        # if can_new_defender_added:
        #     if decision(new_defense_agent_chance):
        #         print("Adding new defender...")
        #         create_new_defender_turtle(defender_box_list[0])
        if can_attacker_adapt:
            if decision(attacker_adaptation_rate):
                attack_variance += attacker_adaptation_by
                print ("Attacker Adapted.")
                print("Attack variance: %s" % attack_variance)

        with open('cas.csv', 'a+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow([i, elapsed])
        # time.sleep(1)
    mainloop()
    # done()
