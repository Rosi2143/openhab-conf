'''
----------------------------------------------------------------------------------------------------
hue_switch_bedroom.py - Dimmer Switch Bedroom Buttons handling rule.
----------------------------------------------------------------------------------------------------
Changelog:
20200116 v01    Created initial script.
----------------------------------------------------------------------------------------------------
'''

from core.rules import rule
from core.triggers import when
from core.log import logging, LOG_PREFIX
import configuration
reload(configuration)
from configuration import LOG_PREFIX
# from core.utils import postUpdateCheckFirst #,postUpdateIfDifferent


#===================================================================================================
@rule("HueSwBed1000", description="Hue bedroom dimmer Key 1 (ON) Initial Press", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 1000.0")
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 1000.0")
def hueBedroomSwitch1000(event):
    switch = str(event.channel).split(":")[3].split("_")[1]
    hueBedroomSwitch1000.log.info("Switch detected [{}]".format(switch))


#===================================================================================================
@rule("HueSwBed1001", description="Hue bedroom dimmer Key 1 (ON) Hold", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 1001.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 1001.0")
def hueBedroomSwitch1001(event):
    # hueBedroomSwitch1001.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3]
    hueBedroomSwitch1001.log.info("Switch detected [{}]".format(switch))
    if ir.getItem("Light_Dim_BedroomLeft").state == 0 or ir.getItem("Light_Dim_BedroomLeft").state == ir.getItem("Bedroom_Brightness_READ").state:
        hueBedroomSwitch1001.log.info("Turn on left bedroom light to EVENING scene")
        events.sendCommand("Light_Dim_BedroomLeft", str(items["Bedroom_Brightness_EVENING"]))
        events.sendCommand("Light_ColorTemp_BedroomLeft", str(items["Bedroom_ColorTemp_EVENING"]))
    elif ir.getItem("Light_Dim_BedroomLeft").state == ir.getItem("Bedroom_Brightness_EVENING").state:
        hueBedroomSwitch1001.log.info("Turn on left bedroom light to READ scene")
        events.sendCommand("Light_Dim_BedroomLeft", str(items["Bedroom_Brightness_READ"]))
        events.sendCommand("Light_ColorTemp_BedroomLeft", str(items["Bedroom_ColorTemp_READ"]))
    elif ir.getItem("Light_Dim_BedroomLeft").state == ir.getItem("Bedroom_Brightness_READ").state:
        hueBedroomSwitch1001.log.info("Turn left bedroom light back to EVENING scene")
        events.sendCommand("Light_Dim_BedroomLeft", str(items["Bedroom_Brightness_EVENING"]))
        events.sendCommand("Light_ColorTemp_BedroomLeft", str(items["Bedroom_ColorTemp_EVENING"]))


#===================================================================================================
@rule("HueSwBed1002", description="Hue bedroom dimmer Key 1 (ON) Short Release", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 1002.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 1002.0")
def hueBedroomSwitch1002(event):
    # hueBedroomSwitch1002.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3]
    hueBedroomSwitch1002.log.info("Switch detected [{}]".format(switch))
    if str(ir.getItem("Light_Scene_Bedroom").state) == "OFF":
        hueBedroomSwitch1002.log.info("First Button 1 (ON) Short Release - Set bedroom Scene to EVENING")
        events.sendCommand("Light_Scene_Bedroom", "EVENING")
    elif str(ir.getItem("Light_Scene_Bedroom").state) == "EVENING":
        hueBedroomSwitch1002.log.info("Second Button 1 (ON) Short Release - Set bedroom Scene to READ")
        events.sendCommand("Light_Scene_Bedroom", "READ")
    elif str(ir.getItem("Light_Scene_Bedroom").state) == "READ":
        hueBedroomSwitch1002.log.info("Third Button 1 (ON) Short Release - Set bedroom Scene to COSY")
        events.sendCommand("Light_Scene_Bedroom", "COSY")
    else:
        hueBedroomSwitch1002.log.info("Fourth Button 1 (ON) Short Release state - reset to EVENING scene")
        events.sendCommand("Light_Scene_Bedroom", "EVENING")


#===================================================================================================
@rule("HueSwBed1003", description="Hue bedroom dimmer Key 1 (ON) Long Release", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 1003.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 1003.0")
def hueBedroomSwitch1003(event):
    # hueBedroomSwitch1003.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3].split("_")[1]
    hueBedroomSwitch1003.log.info("Switch detected [{}]".format(switch))


#===================================================================================================
@rule("HueSwBed2000", description="Hue bedroom dimmer Key 2 (INCREASE) Initial Press", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 2000.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 2000.0")
def hueBedroomSwitch2000(event):
    # hueBedroomSwitch2000.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3].split("_")[1]
    hueBedroomSwitch2000.log.info("Switch detected [{}]".format(switch))


#===================================================================================================
@rule("HueSwBed20012", description="Hue bedroom dimmer Key 2 (INCREASE)", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 2001.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 2001.0")
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 2002.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 2002.0")
def hueBedroomSwitch20012(event):
    # hueBedroomSwitch20012.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3]
    hueBedroomSwitch20012.log.info("Switch detected [{}]".format(switch))
    if ir.getItem("Light_Dim_BedroomLeft").state != 0:
        events.sendCommand("Light_Dim_BedroomLeft", "INCREASE")
    if ir.getItem("Light_Dim_BedroomRight").state != 0:
        events.sendCommand("Light_Dim_BedroomRight", "INCREASE")


#===================================================================================================
@rule("HueSwBed2003", description="Hue bedroom dimmer Key 2 (INCREASE) Long Release", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 2003.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 2003.0")
def hueBedroomSwitch2003(event):
    # hueBedroomSwitch2003.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3].split("_")[1]
    hueBedroomSwitch2003.log.info("Switch detected [{}]".format(switch))


#===================================================================================================
@rule("HueSwBed3000", description="Hue bedroom dimmer Key 3 (DECREASE) Initial Press", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 3000.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 3000.0")
def hueBedroomSwitch3000(event):
    # hueBedroomSwitch3000.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3].split("_")[1]
    hueBedroomSwitch3000.log.info("Switch detected [{}]".format(switch))


#===================================================================================================
@rule("HueSwBed30012", description="Hue bedroom dimmer Key 3 (DECREASE)", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 3001.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 3001.0")
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 3002.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 3002.0")
def hueBedroomSwitch30012(event):
    # hueBedroomSwitch30012.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3]
    hueBedroomSwitch30012.log.info("Switch detected [{}]".format(switch))
    if ir.getItem("Light_Dim_BedroomLeft").state != 0:
        events.sendCommand("Light_Dim_BedroomLeft", "DECREASE")
    if ir.getItem("Light_Dim_BedroomRight").state != 0:
        events.sendCommand("Light_Dim_BedroomRight", "DECREASE")


#===================================================================================================
@rule("HueSwBed3003", description="Hue bedroom dimmer Key 3 (DECREASE) Long Release", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 3003.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 3003.0")
def hueBedroomSwitch3003(event):
    # hueBedroomSwitch3003.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3].split("_")[1]
    hueBedroomSwitch3003.log.info("Switch detected [{}]".format(switch))


#===================================================================================================
@rule("HueSwBed4000", description="Hue bedroom dimmer Key 4 (OFF) Initial Press", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 4000.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 4000.0")
def hueBedroomSwitch4000(event):
    # hueBedroomSwitch4000.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3].split("_")[1]
    hueBedroomSwitch4000.log.info("Switch detected [{}]".format(switch))


#===================================================================================================
@rule("HueSwBed4001", description="Hue bedroom dimmer Key 4 (OFF) Hold", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 4001.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 4001.0")
def hueBedroomSwitch4001(event):
    # hueBedroomSwitch4001.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3]
    hueBedroomSwitch4001.log.info("Switch detected [{}]".format(switch))
    events.sendCommand("Light_Scene_Bedroom", "OFF")


#===================================================================================================
@rule("HueSwBed4002", description="Hue bedroom dimmer Key 4 (OFF) Short Release", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 4002.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 4002.0")
def hueBedroomSwitch4002(event):
    # hueBedroomSwitch4002.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3]
    hueBedroomSwitch4002.log.info("Switch detected [{}]".format(switch))
    if str(ir.getItem("Light_Scene_Bedroom").state) != "OFF":
        events.sendCommand("Light_Scene_Bedroom", "OFF")


#===================================================================================================
@rule("HueSwBed4003", description="Hue bedroom dimmer Key 4 (OFF) Long Release", tags=["lights"])
@when("Channel hue:0820:0017882ec5b3:dim_rbed:dimmer_switch_event triggered 4003.0")
@when("Channel hue:0820:0017882ec5b3:dim_lbed:dimmer_switch_event triggered 4003.0")
def hueBedroomSwitch4003(event):
    # hueBedroomSwitch4003.log.info("Event [{}] received".format(event.event))
    switch = str(event.channel).split(":")[3]
    hueBedroomSwitch4003.log.info("Switch detected [{}]".format(switch))
    events.sendCommand("Light_Scene_Bedroom", "OFF")
    events.sendCommand("Light_Scene_Livingroom", "OFF")
    events.sendCommand("Light_Scene_Dining", "OFF")
    events.sendCommand("Alarm_Status", "ARMED_HOME")