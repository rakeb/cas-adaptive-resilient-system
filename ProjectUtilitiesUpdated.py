# from physicalturtle import Turtle
from turtle import Turtle

import CustomUtilities
from Assets import Assets

object_pen_size = 1.5
start_x = 1
start_y = 1
len_rec = 50
height_rec = 30
len_ids = 40
height_ids = 30
len_fw = 60
height_fw = 45
inter_distance = 150
countermeasure_distance = 50
len_entertainment = 25
height_entertainment = 16
len_conf_table = 40
height_conf_table = 50
len_house = 65
height_house = 70

ROUTER_FLAG = 0
FIREWALL_FLAG = 1
IDS_FLAG = 2

node_color = (102/255.0, 178/255.0, 255/255.0)
# node_color = 'indigo'
edge_color = (.25, .25, .7)

node_asset_id = 0


def BuildNetwork(node_list, router_list, firewall_list, ids_list, attacker_list, defender_list, asset_object_list, turtle_speed):
    designer_turtle = Turtle()
    designer_turtle.speed(10)
    primary_asset_id = 0
    init_start_x = start_x
    init_start_y = start_y
    # print "Initialized : ", init_start_x, " ", init_start_y
    designer_turtle.penup()
    # designer_turtle.pencolor('blue')
    # designer_turtle.dot(25,'blue')

    # routher 1
    router_list.append([init_start_x, init_start_y, 0])
    asset_object_list.append(Assets(primary_asset_id, CustomUtilities.ROUTER_TYPE, [init_start_x, init_start_y, 0]))
    DrawRectangle(asset_object_list[primary_asset_id].co_ordinate[0],
                  asset_object_list[primary_asset_id].co_ordinate[1], designer_turtle)
    primary_asset_id += 1

    # routher 2
    router_list.append([init_start_x, init_start_y + inter_distance, 2])
    asset_object_list.append(
        Assets(primary_asset_id, CustomUtilities.ROUTER_TYPE, [init_start_x, init_start_y + inter_distance, 2]))
    DrawRectangle(asset_object_list[primary_asset_id].co_ordinate[0],
                  asset_object_list[primary_asset_id].co_ordinate[1], designer_turtle)
    primary_asset_id += 1

    # routher 3
    router_list.append([init_start_x, init_start_y - inter_distance, 10])
    asset_object_list.append(
        Assets(primary_asset_id, CustomUtilities.ROUTER_TYPE, [init_start_x, init_start_y - inter_distance, 10]))
    DrawRectangle(asset_object_list[primary_asset_id].co_ordinate[0],
                  asset_object_list[primary_asset_id].co_ordinate[1], designer_turtle)
    primary_asset_id += 1

    # routher 4
    router_list.append([init_start_x - inter_distance, init_start_y, 4])
    asset_object_list.append(
        Assets(primary_asset_id, CustomUtilities.ROUTER_TYPE, [init_start_x - inter_distance, init_start_y, 4]))
    DrawRectangle(asset_object_list[primary_asset_id].co_ordinate[0],
                  asset_object_list[primary_asset_id].co_ordinate[1], designer_turtle)
    primary_asset_id += 1

    # routher 5
    router_list.append([init_start_x + inter_distance, init_start_y, 5])
    asset_object_list.append(
        Assets(primary_asset_id, CustomUtilities.ROUTER_TYPE, [init_start_x + inter_distance, init_start_y, 5]))
    DrawRectangle(asset_object_list[primary_asset_id].co_ordinate[0],
                  asset_object_list[primary_asset_id].co_ordinate[1], designer_turtle)
    primary_asset_id += 1

    # routher 6
    router_list.append([init_start_x - inter_distance - inter_distance, init_start_y, 13])
    asset_object_list.append(
        Assets(primary_asset_id, CustomUtilities.ROUTER_TYPE,
               [init_start_x - inter_distance - inter_distance, init_start_y, 13]))
    DrawRectangle(asset_object_list[primary_asset_id].co_ordinate[0],
                  asset_object_list[primary_asset_id].co_ordinate[1], designer_turtle)
    primary_asset_id += 1

    ################################## Draw the line among the routers ###############################################################
    asset_object_list[0].add_connection(1)
    asset_object_list[1].add_connection(0)
    DrawLineVertical(asset_object_list[0].co_ordinate[0],
                     (asset_object_list[0].co_ordinate[1] + (float(height_rec) / 2)),
                     asset_object_list[1].co_ordinate[0],
                     (asset_object_list[1].co_ordinate[1] - (float(height_rec) / 2)), designer_turtle)

    asset_object_list[0].add_connection(2)
    asset_object_list[2].add_connection(0)
    DrawLineVertical(asset_object_list[2].co_ordinate[0],
                     (asset_object_list[2].co_ordinate[1] + (float(height_rec) / 2)),
                     asset_object_list[0].co_ordinate[0],
                     (asset_object_list[0].co_ordinate[1] - (float(height_rec) / 2)), designer_turtle)

    asset_object_list[0].add_connection(3)
    asset_object_list[3].add_connection(0)
    DrawLineVertical(asset_object_list[3].co_ordinate[0] + (float(len_rec) / 2),
                     (asset_object_list[3].co_ordinate[1]),
                     asset_object_list[0].co_ordinate[0] - (float(len_rec) / 2),
                     (asset_object_list[0].co_ordinate[1]), designer_turtle)

    asset_object_list[0].add_connection(4)
    asset_object_list[4].add_connection(0)
    DrawLineVertical(asset_object_list[0].co_ordinate[0] + (float(len_rec) / 2),
                     (asset_object_list[0].co_ordinate[1]),
                     asset_object_list[4].co_ordinate[0] - (float(len_rec) / 2),
                     (asset_object_list[4].co_ordinate[1]), designer_turtle)

    asset_object_list[3].add_connection(5)
    asset_object_list[5].add_connection(3)
    DrawLineVertical(asset_object_list[5].co_ordinate[0] + (float(len_rec) / 2),
                     (asset_object_list[5].co_ordinate[1]),
                     asset_object_list[3].co_ordinate[0] - (float(len_rec) / 2),
                     (asset_object_list[3].co_ordinate[1]), designer_turtle)

    # designer_turtle.hideturtle()
    ########################################### draw IDS ##############################################################################
    ids_list.append([init_start_x - inter_distance, init_start_y + inter_distance, 9])
    asset_object_list.append(Assets(primary_asset_id, CustomUtilities.IDS_TYPE,
                                    [init_start_x - inter_distance, init_start_y + inter_distance, 9]))
    DrawIDS(asset_object_list[primary_asset_id].co_ordinate[0], asset_object_list[primary_asset_id].co_ordinate[1],
            designer_turtle)
    primary_asset_id += 1

    ids_list.append([init_start_x, init_start_y + inter_distance + height_rec + countermeasure_distance, 11])
    asset_object_list.append(Assets(primary_asset_id, CustomUtilities.IDS_TYPE,
                                    [init_start_x, init_start_y + inter_distance + height_rec + countermeasure_distance,
                                     11]))
    DrawIDS(asset_object_list[primary_asset_id].co_ordinate[0], asset_object_list[primary_asset_id].co_ordinate[1],
            designer_turtle)
    primary_asset_id += 1

    ids_list.append([init_start_x, init_start_y - inter_distance - height_rec - countermeasure_distance, 14])
    asset_object_list.append(Assets(primary_asset_id, CustomUtilities.IDS_TYPE,
                                    [init_start_x, init_start_y - inter_distance - height_rec - countermeasure_distance,
                                     14]))
    DrawIDS(asset_object_list[primary_asset_id].co_ordinate[0], asset_object_list[primary_asset_id].co_ordinate[1],
            designer_turtle)
    primary_asset_id += 1

    ############################################ Connect the IDS ######################################################################
    ids_start = len(router_list)
    asset_object_list[3].add_connection(ids_start)
    asset_object_list[ids_start].add_connection(3)
    DrawLineVertical(asset_object_list[3].co_ordinate[0],
                     (asset_object_list[3].co_ordinate[1] + float(height_rec) / 2),
                     asset_object_list[ids_start].co_ordinate[0],
                     (asset_object_list[ids_start].co_ordinate[1] - (float(height_ids) / 2)), designer_turtle)

    asset_object_list[1].add_connection(ids_start)
    asset_object_list[ids_start].add_connection(1)
    DrawLineVertical(asset_object_list[1].co_ordinate[0] - len_rec / float(2),
                     (asset_object_list[1].co_ordinate[1]),
                     asset_object_list[ids_start].co_ordinate[0] + len_ids / float(2),
                     (asset_object_list[ids_start].co_ordinate[1]), designer_turtle)

    ids_start = ids_start + 1
    asset_object_list[ids_start].add_connection(1)
    asset_object_list[1].add_connection(ids_start)
    DrawLineHorizontal(asset_object_list[ids_start].co_ordinate[0],
                       (asset_object_list[ids_start].co_ordinate[1] - height_ids / float(2)),
                       asset_object_list[1].co_ordinate[0],
                       (asset_object_list[1].co_ordinate[1] + height_rec / float(2)), designer_turtle)

    ids_start = ids_start + 1
    asset_object_list[2].add_connection(ids_start)
    asset_object_list[ids_start].add_connection(2)
    DrawLineVertical(asset_object_list[ids_start].co_ordinate[0],
                     (asset_object_list[ids_start].co_ordinate[1] + height_ids / float(2)),
                     asset_object_list[2].co_ordinate[0],
                     (asset_object_list[2].co_ordinate[1] - height_rec / float(2)), designer_turtle)

    ####################################################### Draw the firewall ############################################################
    firewall_list.append(
        [(init_start_x + inter_distance + (len_rec / float(2)) + countermeasure_distance + (len_fw / float(2))),
         init_start_y, 7])
    asset_object_list.append(Assets(primary_asset_id, CustomUtilities.FIREWALL_TYPE, [
        (init_start_x + inter_distance + (len_rec / float(2)) + countermeasure_distance + (len_fw / float(2))),
        init_start_y, 7]))
    DrawFirewall(asset_object_list[primary_asset_id].co_ordinate[0], asset_object_list[primary_asset_id].co_ordinate[1],
                 designer_turtle)
    primary_asset_id += 1

    ###################################################### Connect the firewall ###########################################################
    fw_start = primary_asset_id - 1
    asset_object_list[4].add_connection(fw_start)
    asset_object_list[fw_start].add_connection(4)
    DrawLineHorizontal(asset_object_list[4].co_ordinate[0] + len_rec / float(2),
                       (asset_object_list[4].co_ordinate[1]),
                       asset_object_list[fw_start].co_ordinate[0] - len_fw / float(2),
                       (asset_object_list[fw_start].co_ordinate[1]), designer_turtle)

    # attacker box
    attacker_list.append([init_start_x - 2 * inter_distance, init_start_y + 2 * inter_distance, 0])
    asset_object_list.append(Assets(primary_asset_id, CustomUtilities.ATTACKER_TYPE,
                                    [init_start_x - 2 * inter_distance, init_start_y + 2 * inter_distance, 0]))
    DrawRectangle(asset_object_list[primary_asset_id].co_ordinate[0],
                  asset_object_list[primary_asset_id].co_ordinate[1], designer_turtle)
    primary_asset_id += 1
    # defender box
    defender_list.append([init_start_x - 2 * inter_distance, init_start_y + 200, 0])
    asset_object_list.append(Assets(primary_asset_id, CustomUtilities.DEFENDER_TYPE,
                                    [init_start_x - 2 * inter_distance, init_start_y + 200, 0]))
    DrawRectangle(asset_object_list[primary_asset_id].co_ordinate[0],
                  asset_object_list[primary_asset_id].co_ordinate[1], designer_turtle)
    primary_asset_id += 1
    #
    # # DrawNodeConnection(ids_list[0][0],ids_list[0][1],15,IDS_FLAG,designer_turtle)
    # ##################################################### Draw Nodes with Connection #####################################################
    DrawNodeWithConnection(primary_asset_id, node_list, router_list, firewall_list, ids_list, designer_turtle,
                           asset_object_list)

    ################################################## Draw Entertainment Box ###########################################################
    # internal_entertainment_place.append([(router_list[0][0] + ids_list[0][0]) / float(2), (router_list[0][1] + ids_list[0][1]) / float(2)])
    # DrawEntertainmentPlace((router_list[0][0] + ids_list[0][0]) / float(2), (router_list[0][1] + ids_list[0][1]) / float(2), designer_turtle)
    # internal_entertainment_place.append(
    #     [(router_list[4][0] + router_list[1][0]) / float(2), (router_list[4][1] + router_list[1][1]) / float(2)])
    # DrawEntertainmentPlace((router_list[4][0] + router_list[1][0]) / float(2),
    #                        (router_list[4][1] + router_list[1][1]) / float(2), designer_turtle)
    # internal_entertainment_place.append(
    #     [(router_list[4][0] + router_list[2][0]) / float(2), (router_list[4][1] + router_list[2][1]) / float(2)])
    # DrawEntertainmentPlace((router_list[4][0] + router_list[2][0]) / float(2),
    #                        (router_list[4][1] + router_list[2][1]) / float(2), designer_turtle)

    ################################################# Draw Meeting Place #################################################################
    # internal_conference_place.append([float(router_list[3][0]+router_list[2][0])/2,float(router_list[3][1]+router_list[2][1])/2])
    # DrawMeetingPlace(float(router_list[3][0]+router_list[2][0])/2,float(router_list[3][1]+router_list[2][1])/2,designer_turtle)

    ################################################### Draw Outside Places ###############################################################
    # DrawAllHouses(1, 1, -400, -150, outside_list, designer_turtle)

    ################################################### Draw Network Box Manager ###########################################################
    # DrawNetworkBox(CustomUtilities.NETWORK_BOX[0], CustomUtilities.NETWORK_BOX[1], designer_turtle)

    ################################ Hide the Turtle ####################################################################################
    designer_turtle.hideturtle()


def DrawAllHouses(start_x, start_y, del_x, del_y, outside_list, designer_turtle):
    first_house_x = start_x + del_x
    first_house_y = start_y + del_y

    DrawHouse(first_house_x, first_house_y, designer_turtle)
    outside_list.append([first_house_x, first_house_y])

    DrawHouse(first_house_x, first_house_y + 300, designer_turtle)
    outside_list.append([first_house_x, first_house_y + 300])

    right_house_x = start_x - del_x
    right_house_y = start_y + del_y

    DrawHouse(right_house_x, right_house_y, designer_turtle)
    outside_list.append([right_house_x, right_house_y])

    DrawHouse(right_house_x, right_house_y + 300, designer_turtle)
    outside_list.append([right_house_x, right_house_y + 300])

    DrawHouse(float(right_house_x + first_house_x) / 2, start_y + 400, designer_turtle)
    outside_list.append([float(right_house_x + first_house_x) / 2, start_y + 400])

    DrawHouse(float(right_house_x + first_house_x) / 2, start_y - 400, designer_turtle)
    outside_list.append([float(right_house_x + first_house_x) / 2, start_y - 400])


def DrawNodeWithConnection(asset_id, node_list, router_list, firewall_list, ids_list, designer_turtle,
                           asset_object_list):
    global node_asset_id
    node_asset_id = asset_id
    num_router = len(router_list)
    for router in range(num_router):
        # print router
        DrawNodeConnection(node_list, router, asset_object_list[router].co_ordinate[0],
                           asset_object_list[router].co_ordinate[1], asset_object_list[router].co_ordinate[2],
                           ROUTER_FLAG, designer_turtle, asset_object_list)

    num_ids = len(ids_list)
    for ids in range(num_ids):
        # print ids
        DrawNodeConnection(node_list, ids + num_router, asset_object_list[ids + num_router].co_ordinate[0],
                           asset_object_list[ids + num_router].co_ordinate[1],
                           asset_object_list[ids + num_router].co_ordinate[2], IDS_FLAG, designer_turtle,
                           asset_object_list)

    num_fw = len(firewall_list)
    for firewall in range(num_fw):
        # print firewall
        DrawNodeConnection(node_list, firewall + num_router + num_ids,
                           asset_object_list[firewall + num_router + num_ids].co_ordinate[0],
                           asset_object_list[firewall + num_router + num_ids].co_ordinate[1],
                           asset_object_list[firewall + num_router + num_ids].co_ordinate[2], FIREWALL_FLAG,
                           designer_turtle, asset_object_list, {1: 'dark blue'})


def DrawLineVertical(first_x, first_y, second_x, second_y, turtleDesigner):
    turtleDesigner.penup()
    turtleDesigner.pensize(3)
    turtleDesigner.pencolor((.25, .25, .7))
    # first_y += float(height_rec)/2
    # second_y -= float(height_rec)/2
    turtleDesigner.goto(first_x, first_y)
    turtleDesigner.pendown()
    turtleDesigner.goto(second_x, second_y)


def DrawLineHorizontal(first_x, first_y, second_x, second_y, turtleDesigner):
    turtleDesigner.penup()
    turtleDesigner.pensize(3)
    turtleDesigner.pencolor((.25, .25, .7))
    # first_x += float(len_rec)/2
    # second_x -= float(len_rec)/2
    turtleDesigner.goto(first_x, first_y)
    turtleDesigner.pendown()
    turtleDesigner.goto(second_x, second_y)


def DrawRectangle(x_ordinate, y_ordinate, turtleDesigner):
    turtleDesigner.penup()
    start_ordinate_x = x_ordinate - (len_rec / float(2))
    start_ordinate_y = y_ordinate + (height_rec / float(2))
    turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
    turtleDesigner.pendown()
    turtleDesigner.pensize(object_pen_size)
    turtleDesigner.pencolor('black')
    flag_x = 1
    flag_y = -1
    for i in range(4):
        if (i % 2) == 0:
            start_ordinate_x += (len_rec * flag_x)
            flag_x *= (-1)
        else:
            start_ordinate_y += (height_rec * flag_y)
            flag_y *= (-1)
        turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
    delta_y = height_rec / float(10)
    y_current_coordinate = start_ordinate_y
    for i in range(9):
        y_current_coordinate -= delta_y
        turtleDesigner.penup()
        turtleDesigner.goto(start_ordinate_x, y_current_coordinate)
        turtleDesigner.pendown()
        turtleDesigner.goto(start_ordinate_x + len_rec, y_current_coordinate)


def DrawIDS(start_x, start_y, turtleDesigner):
    turtleDesigner.penup()
    turtleDesigner.pencolor((.5, .5, .5))
    turtleDesigner.pensize(object_pen_size)
    start_ordinate_x = start_x - len_ids / float(2)
    start_ordinate_y = start_y + height_ids / float(2)
    turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
    turtleDesigner.pendown()
    flag_x = 1
    flag_y = -1
    for i in range(4):
        if (i % 2) == 0:
            start_ordinate_x += (len_ids * flag_x)
            flag_x *= (-1)
        else:
            start_ordinate_y += (height_ids * flag_y)
            flag_y *= (-1)
        turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
    delta_x = len_ids / float(10)
    x_current_coordinate = start_ordinate_x
    for i in range(9):
        x_current_coordinate += delta_x
        turtleDesigner.penup()
        turtleDesigner.goto(x_current_coordinate, start_ordinate_y)
        turtleDesigner.pendown()
        turtleDesigner.goto(x_current_coordinate, start_ordinate_y - height_ids)


def DrawFirewall(start_x, start_y, turtleDesigner):
    turtleDesigner.penup()
    # turtleDesigner.pencolor((1, .25, 0))
    turtleDesigner.pencolor('blue')
    turtleDesigner.pensize(object_pen_size)
    start_ordinate_x = start_x - len_fw / float(2)
    start_ordinate_y = start_y + height_fw / float(2)
    turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
    turtleDesigner.pendown()
    flag_x = 1
    flag_y = -1
    for i in range(4):
        if (i % 2) == 0:
            start_ordinate_x += (len_fw * flag_x)
            flag_x *= (-1)
        else:
            start_ordinate_y += (height_fw * flag_y)
            flag_y *= (-1)
        turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
    delta_x = len_fw / float(10)
    x_current_coordinate = start_ordinate_x
    for i in range(9):
        x_current_coordinate += delta_x
        turtleDesigner.penup()
        turtleDesigner.goto(x_current_coordinate, start_ordinate_y)
        turtleDesigner.pendown()
        turtleDesigner.goto(x_current_coordinate, start_ordinate_y - height_fw)

    delta_y = height_fw / float(4)
    y_current_coordinate = start_ordinate_y
    for i in range(3):
        y_current_coordinate -= delta_y
        turtleDesigner.penup()
        turtleDesigner.goto(start_ordinate_x, y_current_coordinate)
        turtleDesigner.pendown()
        turtleDesigner.goto(start_ordinate_x + len_fw, y_current_coordinate)


def DrawNodeConnection(node_list, asset_index, start_x, start_y, edge_list, object_type, turtleDesigner,
                       asset_object_list, special_color=None):
    edge_length = 40
    node_diameter = 25
    len_obj = len_rec
    height_obj = height_rec
    dot_x = 0
    dot_y = 0
    if object_type == IDS_FLAG:
        len_obj = len_ids
        height_obj = height_ids
    elif object_type == FIREWALL_FLAG:
        len_obj = len_fw
        height_obj = height_fw

    turtleDesigner.penup()

    i = 1
    flag_sign = 1
    for loop_index in range(4):
        if loop_index == 2:
            flag_sign *= -1
        if (edge_list & i):
            i = i << 1
        else:
            i = i << 1
            continue

        init_x = start_x
        init_y = start_y
        end_x = init_x
        end_y = init_y

        if ((loop_index % 2) == 0):
            init_y += flag_sign * (height_obj / float(2))
            end_y = init_y + flag_sign * edge_length
            dot_x = end_x
            dot_y = end_y + flag_sign * node_diameter / float(2)
        else:
            init_x += flag_sign * (len_obj / float(2))
            end_x = init_x + flag_sign * edge_length
            dot_x = end_x + flag_sign * node_diameter / float(2)
            dot_y = end_y

        # print init_x,",",init_y,",",end_x,",",end_y,",",dot_x,",",dot_y," ",loop_index
        turtleDesigner.penup()
        turtleDesigner.goto(init_x, init_y)
        turtleDesigner.pendown()
        turtleDesigner.pencolor(edge_color)
        turtleDesigner.goto(end_x, end_y)
        turtleDesigner.goto(dot_x, dot_y)

        colored = 0
        if special_color is not None:
            for key in special_color.keys():
                if key == loop_index:
                    asset_object_list[asset_index].internet_connection = 1
                    turtleDesigner.dot(node_diameter, special_color[key])
                    colored = 1
                    # node_list.append([dot_x, dot_y, 1])
                    break
            if colored: continue
        global node_asset_id
        node_list.append([dot_x, dot_y, 0])
        asset_object_list.append(Assets(node_asset_id, CustomUtilities.NODE_TYPE, [dot_x, dot_y, 0]))
        asset_object_list[asset_index].add_connection(node_asset_id)
        asset_object_list[node_asset_id].add_connection(asset_index)
        node_asset_id += 1
        turtleDesigner.dot(node_diameter, node_color)


def DrawEntertainmentPlace(start_x, start_y, turtleDesigner):
    turtleDesigner.penup()
    turtleDesigner.pencolor('darkmagenta')
    turtleDesigner.pensize(object_pen_size)
    local_len_entertainment = len_entertainment
    local_height_entertainment = height_entertainment
    increased_size = 2

    for outer_loop in range(4, -1, -1):
        local_len_entertainment = len_entertainment + increased_size * outer_loop
        local_height_entertainment = height_entertainment + increased_size * outer_loop
        start_ordinate_x = start_x - local_len_entertainment / float(2)
        start_ordinate_y = start_y + local_height_entertainment / float(2)
        turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
        turtleDesigner.pendown()
        flag_x = 1
        flag_y = -1
        for i in range(4):
            if (i % 2) == 0:
                start_ordinate_x += (local_len_entertainment * flag_x)
                flag_x *= (-1)
            else:
                start_ordinate_y += (local_height_entertainment * flag_y)
                flag_y *= (-1)
            turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
        turtleDesigner.penup()
    end_ordinate_x = start_x + (len_entertainment + 8) / float(2)
    end_ordinate_y = start_y + 8
    stick_size = 26
    # end_top_ordinate_x = end_ordinate_x
    end_top_ordinate_y = end_ordinate_y + stick_size
    for i in range(4):
        turtleDesigner.goto(end_ordinate_x, end_ordinate_y)
        turtleDesigner.pendown()
        turtleDesigner.goto(end_ordinate_x + 9, end_top_ordinate_y)
        turtleDesigner.penup()
        end_ordinate_x -= 2


def DrawMeetingPlace(start_x, start_y, turtleDesigner):
    turtleDesigner.penup()
    turtleDesigner.pencolor('darkgreen')
    turtleDesigner.pensize(1)
    cap_size = len_conf_table + 24
    high_point = start_y + height_conf_table / float(2)
    low_point = start_y - height_conf_table / float(2)
    turtleDesigner.penup()
    draw_x = start_x + 3
    for i in range(4):
        turtleDesigner.goto(draw_x, high_point)
        turtleDesigner.pendown()
        turtleDesigner.goto(draw_x, low_point)
        turtleDesigner.penup()
        draw_x -= 2

    far_negative_point_high = start_x - cap_size / float(2)
    far_positive_point_high = start_x + cap_size / float(2)
    draw_y = high_point
    for i in range(4):
        turtleDesigner.goto(far_negative_point_high, draw_y)
        turtleDesigner.pendown()
        turtleDesigner.goto(far_positive_point_high, draw_y)
        draw_y += 2
        turtleDesigner.penup()

    far_negative_point_low = start_x - len_conf_table / float(2)
    far_positive_point_low = start_x + len_conf_table / float(2)
    draw_y = low_point
    for i in range(4):
        turtleDesigner.goto(far_negative_point_low, draw_y)
        turtleDesigner.pendown()
        turtleDesigner.goto(far_positive_point_low, draw_y)
        draw_y -= 2
        turtleDesigner.penup()

    draw_x = far_negative_point_low + 8
    for i in range(4):
        turtleDesigner.goto(draw_x, low_point)
        turtleDesigner.pendown()
        turtleDesigner.goto(draw_x - 6, high_point)
        draw_x -= 2
        turtleDesigner.penup()

    draw_x = far_positive_point_low - 8
    for i in range(4):
        turtleDesigner.goto(draw_x, low_point)
        turtleDesigner.pendown()
        turtleDesigner.goto(draw_x + 6, high_point)
        draw_x += 2
        turtleDesigner.penup()


def DrawHouse(start_x, start_y, turtleDesigner):
    top_left_x = start_x - float(len_house) / 2
    top_left_y = start_y + float(height_house) / 2
    turtleDesigner.pencolor('maroon')
    turtleDesigner.pensize(2.5)
    turtleDesigner.penup()
    turtleDesigner.goto(top_left_x, top_left_y)

    flag_x = 1
    flag_y = -1
    start_ordinate_x = top_left_x
    start_ordinate_y = top_left_y
    turtleDesigner.pendown()
    for i in range(4):
        if (i % 2) == 0:
            start_ordinate_x += (len_house * flag_x)
            flag_x *= (-1)
        else:
            start_ordinate_y += (height_house * flag_y)
            flag_y *= (-1)
        turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
    turtleDesigner.penup()

    turtleDesigner.pendown()
    turtleDesigner.goto(top_left_x + float(len_house) / 2, top_left_y + float(height_house + 15) / 2)
    turtleDesigner.goto(top_left_x + len_house, top_left_y)

    turtleDesigner.penup()
    turtleDesigner.goto(top_left_x, top_left_y)
    turtleDesigner.pendown()
    turtleDesigner.goto(top_left_x - 7, top_left_y - 10)
    turtleDesigner.penup()
    turtleDesigner.goto(top_left_x + len_house, top_left_y)
    turtleDesigner.pendown()
    turtleDesigner.goto(top_left_x + len_house + 9.8, top_left_y - 14)
    turtleDesigner.penup()

    len_door = float(len_house) / 3
    height_door = float(height_house) / 2

    top_door_x = start_x - float(len_door) / 2
    top_door_y = top_left_y - height_house + height_door
    turtleDesigner.goto(top_door_x, top_door_y)
    flag_x = 1
    flag_y = -1
    start_ordinate_x = top_door_x
    start_ordinate_y = top_door_y
    turtleDesigner.pendown()
    for i in range(4):
        if (i % 2) == 0:
            start_ordinate_x += (len_door * flag_x)
            flag_x *= (-1)
        else:
            start_ordinate_y += (height_door * flag_y)
            flag_y *= (-1)
        turtleDesigner.goto(start_ordinate_x, start_ordinate_y)
    turtleDesigner.penup()


def DrawNetworkBox(start_x, start_y, turtleDesigner):
    radius = 20
    line_length = 30
    turtleDesigner.pencolor('black')
    custom_pen_size = 9
    # turtleDesigner.pensize(1.5)
    turtleDesigner.penup()
    turtleDesigner.goto(start_x, start_y - radius)
    turtleDesigner.pendown()
    turtleDesigner.pensize(custom_pen_size)
    turtleDesigner.circle(radius)

    turtleDesigner.penup()
    turtleDesigner.goto(start_x, start_y + radius)
    turtleDesigner.pendown()
    turtleDesigner.goto(start_x, start_y + radius + line_length)

    turtleDesigner.penup()
    turtleDesigner.goto(start_x, start_y - radius)
    turtleDesigner.pendown()
    turtleDesigner.goto(start_x, start_y - radius - line_length)

    turtleDesigner.penup()
    turtleDesigner.goto(start_x + radius, start_y)
    turtleDesigner.pendown()
    turtleDesigner.goto(start_x + radius + line_length, start_y)

    turtleDesigner.penup()
    turtleDesigner.goto(start_x - radius, start_y)
    turtleDesigner.pendown()
    turtleDesigner.goto(start_x - radius - line_length, start_y)

    turtleDesigner.penup()
