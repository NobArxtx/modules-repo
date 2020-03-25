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
    country_lol = "**Country** %s\n\n"%country_name
    confirmed_lol = "**Confirmed**:%s\n"%confirmed_info
    Active_lol = "**Active**:%s\n"%Active_info
    Deaths_lol = "**Deaths**:%s\n"%deaths_info
    recovered_lol = "**Recovered**:%s"%recovered_info
    country_lol += confirmed_lol
    country_lol += Active_lol
    country_lol += Deaths_lol
    country_lol += recovered_lol
    await event.edit(country_lol)
def get_country_data(country, world):
    for country_data in world:
        if country_data["country"] == country:
            return country_data
    return {"**Status**": "No information yet about this country!"}
