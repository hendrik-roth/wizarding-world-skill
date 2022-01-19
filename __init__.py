from mycroft import MycroftSkill, intent_handler

from .generator import Generator


class WizardingWorld(MycroftSkill):
    def __init__(self):
        super().__init__()
        self.skill_generator = Generator()
        self.skill_generator.load_spell_skill()

    @intent_handler('world.wizarding.intent')
    def handle_world_wizarding(self, message):
        self.speak_dialog('world.wizarding')
        self.skill_generator.load_spell_skill()


def create_skill():
    return WizardingWorld()
