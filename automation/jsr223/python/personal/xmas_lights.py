'''
----------------------------------------------------------------------------------------------------
xmas_lights.py - Handle Christmas lighting.
----------------------------------------------------------------------------------------------------
Changelog:
20201223 v01    Created initial script.
----------------------------------------------------------------------------------------------------
'''

from core.rules import rule
from core.triggers import when
import configuration
reload(configuration)
from core.actions import NotificationAction

#===================================================================================================
@rule("Xmas Scene Switch", description="Turn Xmas lights on and off based on the Day Mode", tags=["xmas"])
@when("Item Day_Mode changed")
def xmasSceneSwitch(event):
    if isinstance(event.oldItemState, UnDefType) or event.oldItemState is None:
        return
    xmasSceneSwitch.log.info("{name} changed to {newState} from {oldState}".format(name=event.itemName, newState=event.itemState, oldState=event.oldItemState))
    # Determine the Scene to select
    command = "OFF" if str(ir.getItem("Day_Mode").state) == "DAY" else "ON"
    xmasSceneSwitch.log.info("Send command [{}] to Xmas lights".format(command))
    events.sendCommand("ShellyXmas1_Relay", command)
    msg = "Day mode change: Xmas lights switched to Scene " + command
    NotificationAction.sendBroadcastNotification(msg)

#===================================================================================================
@rule("Xmas Livingroom Switch", description="Turn Xmas lights in the livingroom on and off", tags=["xmas"])
@when("Item Light_Scene_Livingroom changed")
def xmasLivingRoomSwitch(event):
    if isinstance(event.oldItemState, UnDefType) or event.oldItemState is None:
        return
    xmasLivingRoomSwitch.log.info("{name} changed to {newState} from {oldState}".format(name=event.itemName, newState=event.itemState, oldState=event.oldItemState))
    # Determine the Scene to select
    command = "OFF" if str(ir.getItem("Light_Scene_Livingroom").state) == "OFF" else "ON"
    xmasSceneSwitch.log.info("Send command [{}] to Xmas livingroom lights".format(command))
    events.sendCommand("ShellyplugS9a3f4e_Relay", command)
    msg = "Livingroom lights change: Xmas lights switched to Scene " + command
    NotificationAction.sendBroadcastNotification(msg)
