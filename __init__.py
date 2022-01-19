from mycroft import MycroftSkill, intent_file_handler


class WizardingWorld(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('world.wizarding.intent')
    def handle_world_wizarding(self, message):
        self.speak_dialog('world.wizarding')


def create_skill():
    return WizardingWorld()

