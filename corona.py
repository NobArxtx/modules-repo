"""CoronaVirus LookUp
Syntax: .corona <country>"""
from covid import Covid
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="corona (.*)"))
async def _(event):
    covid = Covid()
    data = covid.get_data()
    country = event.pattern_match.group(1)
    country_data = get_country_data(country, data)
    confirmed_info = country_data["confirmed"]
    Active_info = country_data["active"]
    deaths_info = country_data["deaths"]
    recovered_info = country_data["recovered"]
    country_name = country_data["country"]
    await event.edit("**Country**","**"+country_name+"**","\n**Confirmed**:",confirmed_info,"\n**Active**:",Active_info,"\n**Deaths**:",deaths_info,"\n**Recovered**:",recovered_info)
def get_country_data(country, world):
    for country_data in world:
        if country_data["country"] == country:
            return country_data
    return {"**Status**": "No information yet about this country!"}
