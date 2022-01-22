from mycroft import MycroftSkill, intent_handler
from .spells import *


class WizardingWorldSpells(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__()


# insert


def create_skill():
    return WizardingWorldSpells()
