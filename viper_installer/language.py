from json import loads
from rich.prompt import Prompt
from . import logo, console, bilgi

def importlang ():
    console.clear()
    logo()
    bilgi("\n\[1] Tukey\n\[2] Azərbaycanca\n\[3] English\n\[4] O'zbek")
    Dil = Prompt.ask("[bold yellow]language is must / Please select a language[/]", choices=["1", "2", "3", "4"], default="1")

    if Dil == "1":
        COUNTRY = "Turkey"
        LANGUAGE = "TR"
        TZ = "Europe/Istanbul"
    elif Dil == "2":
        COUNTRY = "Azerbaijan"
        LANGUAGE = "AZ"
        TZ = "Asia/Baku"
    elif Dil == "3":
        COUNTRY = "United Kingdom"
        LANGUAGE = "EN"
        TZ = "Asia/Kolkata"
    elif Dil == "4":
        COUNTRY = "Uzbekistan"
        LANGUAGE = "UZ"
        TZ = "Asia/Kolkata"

    return COUNTRY, LANGUAGE, TZ

COUNTRY, LANGUAGE, TZ = importlang()
LANG = loads(open(f"./viper_installer/language/{LANGUAGE}.viperjson", "r").read())["STRINGS"]
