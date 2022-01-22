import os
import yaml
from pathlib import Path
from shutil import copy2


class Generator:
    def __init__(self):
        self.target_path = "/opt/mycroft/skills/wizard-spell-skill"
        self.intent_path = self.target_path + "/locale/en-us"
        self.registry_data = self.read_registry()

    def load_spell_skill(self):
        if not self.does_skilldir_exists():
            self.create_skill_dirs()
        self.copy_spell_script()
        self.overwrite_intent_files()
        self.copy_manifest()
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
        for key, value in self.registry_data.items():
            self.create_intent_file(filename=key, intent=value["intent"])

    def overwrite_init(self):
        """
        overwrite (or create) __init__.py in generated skill based on
        registry.yml data and use init_template as template
        """
        with open("init_template.py", "r") as template:
            init_code = template.read()

        code_split = init_code.split("# insert")
        code_before_insert = code_split[0]
        code_after_insert = code_split[1].strip("\n")

        intent_handler_code = self.generate_intent_handling_code()

        generated_code = code_before_insert + intent_handler_code + \
                         "\n" + code_after_insert + "\n"

        with open(f"{self.target_path}/__init__.py", "w+") as generated_file:
            generated_file.write(generated_code)

    def copy_manifest(self):
        """
        create manifest.yml for generated skill based on dependencies in
        spell.py
        """
        copy2("manifest.yml", self.target_path)

    def generate_intent_handling_code(self):
        """
        generating @intent_handler code

        Returns
        -------
        code : str
            correct formatted, generated code
        """
        code = ""
        for key, value in self.registry_data.items():
            intent_file = f"{key}.intent"
            pyfunction = value["pyfunction"]

            code += f"    @intent_handler('{intent_file}')\n" \
                    f"    def handle_{key}(self):\n" \
                    f"        spells.{pyfunction}()\n\n"
        return code

    def create_intent_file(self, filename, intent):
        """
        create an .intent file in locale/en-us dir

        Parameters
        ----------
        filename
            filename of the .intent file
        intent
            intent (content) of the file
        """
        with open(f"{self.intent_path}/{filename}.intent", "w+") as file:
            file.write(intent)

    @staticmethod
    def read_registry():
        """
        read out data from registry.yml

        Returns
        -------
        data : dict
            dictionary which contains function as key and details as dict, e.g.
            {'avada_kedavra': {'pyfunction': 'avada_kedavra',
             'intent': 'avada kedavra'}, 'reducto': {...}, ..}
        """
        with open("registry.yml", "r") as registry:
            data_loaded = yaml.safe_load(registry)
        return data_loaded
