import random
NODE_TYPE = 0
FIREWALL_TYPE = 1
IDS_TYPE = 2
ROUTER_TYPE = 3
ATTACKER_TYPE = 4
DEFENDER_TYPE = 5
BROAD_CAST = 255
WORK_RANGE_AT_TIME = 2
MALICIOUS_EXTERNAL_AGENT_CODE = 1
BENIGN_EXTERNAL_AGENT_CODE = 0
NETWORK_BOX = [200,200]
NUM_NETWORK_MANAGER = 1
NUM_ENTERTAINMENT_PLACE = 3
NUM_OUTSIDE_PLACE = 6
NUM_VULNERABILITIES_PER_DAY = 3
NUM_PATCH_PER_DAY = 2
DECREASE_SKILL_EACH_DAY = .05
INCREASE_SKILL_CONFERENCE = 5*DECREASE_SKILL_EACH_DAY/float(3)
OUTSIDE_WORLD_PERIOD = 2
PUNISHMENT_AMOUNT = 800
vulnerability_id = 0
FILE_NAME = 'Risk_Day_Index_8'
MAX_RISK_RADIUS = 25.0
COUNTERMEASURE_POWER_REDUCTION = 10.0
INTERNAL_AGENT_CONFIDENTIALITY = 50
INTERNAL_AGENT_EXTROVERT = 40
EXTERNAL_AGENT_CONFIDENTIALITY = 70
EXTERNAL_AGENT_EXTROVERT = 30

def map_asset_id_to_asset_object_id(asset_list,asset_to_asset_object_mapping):
    start_index = 0
    for asset_type in range(len(asset_list)-1,-1,-1):
        asset_to_asset_object_mapping[asset_type] = {}
        for asset in range(len(asset_list[asset_type])):
            asset_to_asset_object_mapping[asset_type][asset] = start_index
            start_index += 1

    print ("Asset Mapping : ",asset_to_asset_object_mapping)

def generate_vulnerability(network_manager_list,asset_object_list):
    global vulnerability_id
    for i in range(NUM_VULNERABILITIES_PER_DAY):
        distribute_vulnerability(vulnerability_id + i,asset_object_list)

    vulnerability_id += NUM_VULNERABILITIES_PER_DAY
    start_patch_index = 0
    while start_patch_index < NUM_PATCH_PER_DAY:
        patch_id = random.randint(0,vulnerability_id-1)
        if patch_id not in network_manager_list[0].patch_up_vulnerability:
            # patch_up_vul.append(patch_id)
            network_manager_list[0].patch_up_vulnerability.append(patch_id)
            start_patch_index += 1



def distribute_vulnerability(vul_id,asset_object_list):
    num_asset = len(asset_object_list)
    num_asset_infected = random.randint(num_asset/2,num_asset-1)
    num_asset_infected_list = []
    start_number = 0
    while start_number < num_asset_infected:
        asset_id = random.randint(0,num_asset-1)
        if asset_id not in num_asset_infected_list:
            num_asset_infected_list.append(asset_id)
            asset_object_list[asset_id].vulnerabilities.append(vul_id)
            start_number += 1

    ################################### Test ###################################################
    # for asset in asset_object_list:
    #     print asset.primary_id," --> ",asset.vulnerabilities
    ################################### End Test ###############################################

def decrease_skill_all_agents(internal_agents_list):
    for agent in internal_agents_list:
        agent.decrease_skill()

def print_agents_skill(internal_agents_list):
    for i in range(len(internal_agents_list)):
        print ("Agent : ",i," Skill --> ",internal_agents_list[i].skill)

def increase_conference_agents_skill_all(internal_agents_skill):
    for agents in internal_agents_skill:
        agents.skill += INCREASE_SKILL_CONFERENCE
        if agents.skill > 1:
            agents.skill = 1.0


def increase_conference_agents_skill_specific(agents):
    # print "Prev Skill ",agents.skill
    agents.skill += INCREASE_SKILL_CONFERENCE
    if agents.skill > 1:
        agents.skill = 1.0
    # print "After Skill ", agents.skill


def return_price_asset(asset_id,asset_type,asset_object_list,asset_to_asset_object_mapping):
    # print "Asset Id : ",asset_id," Type : ",asset_type," ",asset_to_asset_object_mapping[asset_type][asset_id]," ",asset_object_list[asset_to_asset_object_mapping[asset_type][asset_id]].asset_value
    return asset_object_list[asset_to_asset_object_mapping[asset_type][asset_id]].asset_value

def bfs_exploitable_assets(malicious_agent,knowledge_parent_node,first_generation_asset_list,topology_traversal_specific_agent_node,asset_object_list):
    print ("Asset List ",first_generation_asset_list)
    total_risk = 0.0
    bfs_queue = []
    risk_agent = {}
    start_index = 0
    for i in first_generation_asset_list:
        topology_traversal_specific_agent_node.append(i)
        bfs_queue.append(i)
        risk_agent[i] = float(knowledge_parent_node[start_index])
        total_risk += risk_agent[i] * asset_object_list[i].asset_value
        asset_object_list[i].imposed_risk += risk_agent[i] * asset_object_list[i].asset_value
        start_index += 1

    for asset in bfs_queue:
        for neighbour in asset_object_list[asset].edge:
            if neighbour not in topology_traversal_specific_agent_node:
                if asset_object_list[neighbour].asset_type == IDS_TYPE or asset_object_list[neighbour].asset_type == FIREWALL_TYPE:
                    bfs_queue.append(neighbour)
                    risk_agent[neighbour] = risk_agent[asset] * malicious_agent.skill/float(COUNTERMEASURE_POWER_REDUCTION)
                    topology_traversal_specific_agent_node.append(neighbour)
                elif len(asset_object_list[neighbour].vulnerabilities) > 0:
                    bfs_queue.append(neighbour)
                    topology_traversal_specific_agent_node.append(neighbour)
                    risk_agent[neighbour] = risk_agent[asset] * malicious_agent.skill
                    total_risk += risk_agent[neighbour]*asset_object_list[neighbour].asset_value
                    asset_object_list[neighbour].imposed_risk += risk_agent[neighbour]*asset_object_list[neighbour].asset_value

    return total_risk

def init_asset_impact(asset_object_list):
    for asset in asset_object_list:
        asset.imposed_risk = 0

def show_risk_assets(asset_object_list):
    for asset in asset_object_list:
        print ("Asset Value : ",asset.asset_value)
        print ("Risk Asset : ",asset.imposed_risk)

def total_asset_value(asset_object_list):
    asset_value_global = 0
    for asset in asset_object_list:
        print (asset.primary_id," --> ",asset.imposed_risk," ",asset.asset_type)
        asset_value_global += asset.asset_value
    return asset_value_global

def check_confidentiality(agent_list):
    for agent in range(len(agent_list)):
        print ("Agent : ",agent," ",agent_list[agent].confidentiality)


def draw_red_lines(asset_obeject_list,designer_turtle):
    max_risk = 0
    for asset in asset_obeject_list:
        if asset.imposed_risk > max_risk:
            max_risk = asset.imposed_risk

    if max_risk > 0:
        for asset in asset_obeject_list:
            if asset.imposed_risk <= 0:
                continue
            designer_turtle.penup()
            designer_turtle.goto(asset.co_ordinate[0],asset.co_ordinate[1])
            designer_turtle.pendown()
            dot_size = asset.imposed_risk * MAX_RISK_RADIUS/float(max_risk)
            designer_turtle.dot(dot_size,'darkred')
        return 1
    else:
        return 0


