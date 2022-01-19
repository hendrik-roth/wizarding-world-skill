

class Generator:
    def __init__(self):
        self.target_path = ""

    def load_spell_skill(self):
        if not self.does_skillstructure_exists():
            self.create_skill_structure()
        self.copy_spell_script()
        self.overwrite_intent_files()
        self.overwrite_init()
        pass

    def does_skillstructure_exists(self):
        pass

    def create_skill_structure(self):
        pass

    def copy_spell_script(self):
        pass

    def overwrite_intent_files(self):
        pass

    def overwrite_init(self):
        pass
