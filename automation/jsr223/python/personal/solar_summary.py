'''
----------------------------------------------------------------------------------------------------
solar_summary.py - Calculate the solarpanel production price and totals summary.
----------------------------------------------------------------------------------------------------
Changelog:
20200116 v01    Created initial script.
----------------------------------------------------------------------------------------------------
'''

from core.rules import rule
from core.triggers import when
import configuration
reload(configuration)
from configuration import powerPriceDict

#===================================================================================================
@rule("Calculate Solar Summary", description="Calculate the solarpanel production prices and totals", tags=["energy","solar"])
@when("Item Solar_Prod_Day changed")
@when("Item Solar_Prod_Month changed")
@when("Item Solar_Prod_Year changed")
def solarSummary(event):
    if event.oldItemState is None:
        return
    price = powerPriceDict.get("T"+str(items["Power_Tariff"])).get("return_price")
    cost = float(event.itemState.toString()) * float(price)
    summary = "{} kWh, EUR {}".format(float(str(event.itemState))/1000, cost/100)
    costItem = ir.getItem(event.itemName + "_Cost")
    events.postUpdate(costItem, str(cost))
    summaryItem = ir.getItem(event.itemName + "_Summary")
    events.postUpdate(summaryItem.name, summary)