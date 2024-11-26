# Okabe-Ito color palette
# For details, see https://jfly.uni-koeln.de/colorset/

from enum import StrEnum

class OIColor(StrEnum):
    red = "#FF4B00"
    yellow = "#FFF100"
    green = "#03AF7A"
    blue = "#005AFF"
    skyblue = "#4DC4FF"
    pink = "#FF8082"
    orange = "#F6AA00"
    purple = "#990099"
    brown = "#804000"

class OIBaseColor(StrEnum):
    pink = "#FFCABF"
    cream = "#FFFF80"
    ygreen = "#D8F255"
    skyblue = "#BFE4FF"
    beige = "#FFCA80"
    green = "#77D9A8"
    purple = "#C9ACE6"

class  OIAchromaticColor(StrEnum):
    white = "#FFFFFF"
    rightgray = "#C8C8CB"
    gray = "#84919E"
    black = "#000000"