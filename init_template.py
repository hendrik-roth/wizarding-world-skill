from mycroft import MycroftSkill, intent_handler
import spells


class WizardingWorldSpells(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__()


# insert


def create_skill():
    return WizardingWorldSpells()
