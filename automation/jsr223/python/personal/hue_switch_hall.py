'''
----------------------------------------------------------------------------------------------------
hue_switch_hall.py - Dimmer Switch Hall Buttons handling rule.
----------------------------------------------------------------------------------------------------
Changelog:
20200115 v01    Created initial script.
----------------------------------------------------------------------------------------------------
'''

from core.rules import rule
from core.triggers import when
# from core.log import logging, LOG_PREFIX
# import configuration
# reload(configuration)
# from configuration import LOG_PREFIX

#===================================================================================================
# @rule("HueSwBath1000", description="Hue Hallway dimmer Key 1 (ON) Initial Press - ignored", tags=["lights"])
# @when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 1000.0")
# def hue_hall_switch1000(event):
#     log.info("Event [{}] received".format(event.event))
#     switch = str(event.channel).split(":")[3].split("_")[1]
#     log.info("Switch detected [{}]".format(switch))

#===================================================================================================
@rule("HueSwBath1001", description="Hue Hallway dimmer Key 1 (ON) Hold - turn on all groundfloor lights", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 1001.0")
def hueHallSwitch1001(event):
    hueHallSwitch1001.log.info("Event [{}] received".format(event.event))
    # switch = str(event.channel).split(":")[3]
    events.sendCommand("Light_Scene_Hall", "EVENING")
    events.sendCommand("Light_Scene_Kitchen", "EVENING")
    events.sendCommand("Light_Scene_Dining", "EVENING")
    events.sendCommand("Light_Scene_Livingroom", "EVENING")

#===================================================================================================
@rule("HueSwBath1002", description="Hue Hallway dimmer Key 1 (ON) Short release - turn off hall/kitchen light", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 1002.0")
def hueHallSwitch1002(event):
    hueHallSwitch1002.log.info("Event [{}] received".format(event.event))
    # switch = str(event.channel).split(":")[3]
    if str(ir.getItem("Light_Scene_Hall").state) == "OFF" and str(ir.getItem("Light_Scene_Kitchen").state) == "OFF":
        events.sendCommand("Light_Scene_Hall", "EVENING")
        events.sendCommand("Light_Scene_Kitchen", "EVENING")
    elif str(ir.getItem("Light_Scene_Hall").state) == "EVENING" and str(ir.getItem("Light_Scene_HallCeiling").state) == "OFF":
        events.sendCommand("Light_Scene_HallCeiling", "EVENING")
    elif str(ir.getItem("Light_Scene_Hall").state) == "EVENING" and str(ir.getItem("Light_Scene_HallCeiling").state) == "EVENING":
        events.sendCommand("Light_Scene_HallCeiling", "READ")
        events.sendCommand("Light_Scene_Hall", "READ")
    elif str(ir.getItem("Light_Scene_HallCeiling").state) == "READ" and str(ir.getItem("Light_Scene_Hall").state) == "READ":
        events.sendCommand("Light_Scene_HallCeiling", "OFF")
        events.sendCommand("Light_Scene_Hall", "EVENING")
    else:
        events.sendCommand("Light_Scene_HallCeiling", "EVENING")
        events.sendCommand("Light_Scene_Hall", "EVENING")

#===================================================================================================
# @rule("HueSwBath1003", description="Hue Hallway dimmer Key 1 (ON) Long release - ignored", tags=["lights"])
# @when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 1003.0")
# def hue_hall_switch1003(event):
#     log.info("Event [{}] received".format(event.event))
#     switch = str(event.channel).split(":")[3].split("_")[1]
#     log.info("Switch detected [{}]".format(switch))

#===================================================================================================
# @rule("HueSwBath2000", description="Hue Hallway dimmer Key 2 (INCREASE) Initial Press - ignored", tags=["lights"])
# @when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 2000.0")
# def hue_hall_switch2000(event):
#     log.info("Event [{}] received".format(event.event))
#     switch = str(event.channel).split(":")[3].split("_")[1]
#     log.info("Switch detected [{}]".format(switch))

#===================================================================================================
@rule("HueSwBath20012", description="Hue Hallway dimmer Key 2 (INCREASE) - increase brightness", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 2001.0")
@when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 2002.0")
def hueHallSwitch20012(event):
    hueHallSwitch20012.log.info("Event [{}] received".format(event.event))
    # switch = str(event.channel).split(":")[3]
    if str(ir.getItem("Light_Scene_Hall").state) != "OFF":
        events.sendCommand("gLight_Brightness_Hall", "INCREASE")
    if str(ir.getItem("Light_Scene_HallCeiling").state) != "OFF":
        events.sendCommand("gLight_Brightness_HallCeiling", "INCREASE")

#===================================================================================================
# @rule("HueSwBath2003", description="Hue Hallway dimmer Key 2 (INCREASE) Long Release - ignored", tags=["lights"])
# @when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 2003.0")
# def hue_hall_switch2003(event):
#     log.info("Event [{}] received".format(event.event))
#     switch = str(event.channel).split(":")[3].split("_")[1]
#     log.info("Switch detected [{}]".format(switch))

#===================================================================================================
# @rule("HueSwBath3000", description="Hue Hallway dimmer Key 3 (DECREASE) Initial Pressed - ignored", tags=["lights"])
# @when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 3000.0")
# def hue_hall_switch3000(event):
#     log.info("Event [{}] received".format(event.event))
#     switch = str(event.channel).split(":")[3].split("_")[1]
#     log.info("Switch detected [{}]".format(switch))

#===================================================================================================
@rule("HueSwBath30012", description="Hue Hallway dimmer Key 3 (DECREASE) - decrease brightness", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 3001.0")
@when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 3002.0")
def hueHallSwitch30012(event):
    hueHallSwitch30012.log.info("Event [{}] received".format(event.event))
    # switch = str(event.channel).split(":")[3]
    if str(ir.getItem("Light_Scene_Hall").state) != "OFF":
        events.sendCommand("gLight_Brightness_Hall", "DECREASE")
    if str(ir.getItem("Light_Scene_HallCeiling").state) != "OFF":
        events.sendCommand("gLight_Brightness_HallCeiling", "DECREASE")

#===================================================================================================
# @rule("HueSwBath3003", description="Hue Hallway dimmer Key 3 (DECREASE) Long Release - ignored", tags=["lights"])
# @when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 3003.0")
# def hue_hall_switch3003(event):
#     log.info("Event [{}] received".format(event.event))
#     switch = str(event.channel).split(":")[3].split("_")[1]
#     log.info("Switch detected [{}]".format(switch))

#===================================================================================================
# @rule("HueSwBath4000", description="Hue Hallway dimmer Key 4 (OFF) Initial Pressed - ignored", tags=["lights"])
# @when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 4000.0")
# def hue_hall_switch4000(event):
#     log.info("Event [{}] received".format(event.event))
#     switch = str(event.channel).split(":")[3].split("_")[1]
#     log.info("Switch detected [{}]".format(switch))

#===================================================================================================
@rule("HueSwBath4001", description="Hue Hallway dimmer Key 4 (OFF) Hold - Turn of groundfloor lighting", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 4001.0")
def hueHallSwitch4001(event):
    hueHallSwitch4001.log.info("Event [{}] received".format(event.event))
    # switch = str(event.channel).split(":")[3]
    if str(ir.getItem("Light_Scene_Livingroom").state) != "OFF":
        events.sendCommand("Light_Scene_Livingroom", "OFF")
    elif str(ir.getItem("Light_Scene_Dining").state) != "OFF":
        events.sendCommand("Light_Scene_Dining", "OFF")
    elif str(ir.getItem("Light_Scene_Kitchen").state) != "OFF":
        events.sendCommand("Light_Scene_Kitchen", "OFF")
    else:
        events.sendCommand("Light_Scene_HallCeiling", "OFF")
        events.sendCommand("Light_Scene_Hall", "OFF")

#===================================================================================================
@rule("HueSwBath4002", description="Hue Hallway dimmer Key 4 (OFF) Short Release - Turn of hallway lighting", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 4002.0")
def hueHallSwitch4002(event):
    hueHallSwitch4002.log.info("Event [{}] received".format(event.event))
    # switch = str(event.channel).split(":")[3]
    if str(ir.getItem("Light_Scene_HallCeiling").state) != "OFF":
        events.sendCommand("Light_Scene_HallCeiling", "OFF")
    if str(ir.getItem("Light_Scene_Hall").state) == "READ":
        events.sendCommand("Light_Scene_Hall", "EVENING")
    elif str(ir.getItem("Light_Scene_Hall").state) == "EVENING":
        events.sendCommand("Light_Scene_Hall", "OFF")
        events.sendCommand("Light_Scene_Kitchen", "OFF")

#===================================================================================================
@rule("HueSwBath4003", description="Hue Hallway dimmer Key 4 (OFF) Long Release - Turn of all groundfloor lights", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_hall:dimmer_switch_event triggered 4003.0")
def hueHallSwitch4003(event):
    hueHallSwitch4003.log.info("Event [{}] received".format(event.event))
    # switch = str(event.channel).split(":")[3]
    events.sendCommand("Light_Scene_Livingroom", "OFF")
    events.sendCommand("Light_Scene_Dining", "OFF")
    events.sendCommand("Light_Scene_Kitchen", "OFF")
    events.sendCommand("Light_Scene_HallCeiling", "OFF")
    events.sendCommand("Light_Scene_Hall", "OFF")