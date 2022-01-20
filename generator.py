import os
import subprocess
from pathlib import Path
from shutil import copy2


class Generator:
    def __init__(self):
        self.target_path = "/opt/mycroft/skills/wizard-spell-skill"

    def load_spell_skill(self):
        if not self.does_skilldir_exists():
            self.create_skill_dirs()
        self.copy_spell_script()
        self.overwrite_intent_files()
        self.create_manifest()
        self.overwrite_init()

    def does_skilldir_exists(self) -> bool:
        """
        check if target skill directory of new generated skill exists

        Returns
        -------
        path.exists() : bool
            true if target path to new generated skill exists, else false
        """
        path = Path(self.target_path)
        return path.exists()

    def create_skill_dirs(self):
        """
        creating directory structure of skill.
        creates the main folder in /opt/mycroft/skills/wizard-spell-skill
        and the /locale/en-us directory for intent files

        """
        os.mkdir(self.target_path)
        os.makedirs(self.target_path + "/locale/en-us")

    def copy_spell_script(self):
        """
        copy spell.py from this dir to generated dir because it's necessary to
        have this file in the new skill

        """
        copy2("spells.py", self.target_path)

    def overwrite_intent_files(self):
        """
        overwrite (or create) intent files based on registry.yml
        """
        pass

    def overwrite_init(self):
        """
        overwrite (or create) __init__.py in generated skill based on
        registry.yml
        """
        # after overwriting/creation run black for formatting
        subprocess.run(["black", f"{self.target_path}/__init__.py"])
        pass

    def create_manifest(self):
        """
        create manifest.yml for generated skill based on dependencies in
        spell.py
        """
        pass
