# -*- coding: utf-8 -*-
#!/usr/bin/env python

# define dictionary
english_german={}
english_german['Date']='Datum'
english_german['Home Usage (kWh)']='Eigenverbrauch (kWh)'
english_german['Grid Imported (kWh)']='Netzimport (kWh)'
english_german['Grid to Home (kWh)']='Netzstrom zu Haushalt (kWh)'
english_german['Grid to Storage (kWh)']='Netzstrom zu Speicher (kWh)'
english_german['Total Solar Generation (kWh)']='Gesamte Solarstromerzeugung (kWh)'
english_german['Solar to Home (kWh)']='Solarstrom zu Haushalt (kWh)'
english_german['Solar to Storage (kWh)']='Solarstrom zu Speicher (kWh)'
english_german['Solar to Grid (kWh)']='Solarstrom-Einspeisung (kWh)'
english_german['Storage Discharged Energy (kWh)']='Speicherentladung (kWh)'
english_german['Storage to Home (kWh)']='Speicher zu Haushalt (kWh)'
english_german['Storage to Grid (kWh)']='Speicher-Einspeisung (kWh)'
english_german['PV1 Generation (kWh)']='PV1-Erzeugung (kWh)'
english_german['PV2 Generation (kWh)']='PV2-Erzeugung (kWh)'
english_german['PV3 Generation (kWh)']='PV3-Erzeugung (kWh)'
english_german['PV4 Generation (kWh)']='PV4-Erzeugung (kWh)'
english_german['Storage Charged Energy (kWh)']='Speicherladung (kWh)'
english_german['Total Generation (kWh)']='Gesamterzeugung (kWh)'
english_german['Third-Party Solar (kWh)']='Drittanbieter-Solar (kWh)'
english_german['Third-Party PV To Home (kWh)']='Drittanbieter-Haushalt (kWh)'
english_german['Third-Party PV To Battery (kWh)']='Drittanbieter-Speicher (kWh)'
english_german['Third-Party PV To Grid (kWh)']='Drittanbieter-Einspeisung (kWh)'
english_german['Smart Plug Energy (kWh)']='Verbrauch über Smart Plug (kWh)'
english_german['Charging Pile Energy (kWh)']='Ladesäulen-Verbrauch (kWh)'
english_german['Carbon Reduction (kgCO2/kWh)']='CO₂-Reduktion (kgCO₂/kWh)'
english_german['Free Electricity (Off-Grid) (kWh)']='Freie Energie (Off-Grid) (kWh)'
english_german['Other Loads Energy (kWh)']='Andere Lasten (kWh)'
english_german['Built-in PV Generation (kWh)']='eigene Solarstromerzeugung (kWh)'
english_german['PV To Home (kWh)']='Solarstrom zu Haushalt (kWh)'
english_german['PV To Battery (kWh)']='Solarstrom zu Speicher (kWh)'
english_german['PV To Grid (kWh)']='Solarstrom-Einspeisung (kWh)'


def translateThis(tT:str):
    """searches for key in dict.keys returns translated or tT
    :param tT: like key
    :return: translated str

    """
    for ind in english_german:
        if tT.lower() in ind.lower():
            return english_german[ind]
    return tT
