# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/quidditch.svg" card_color="#8CE0FE" width="50" height="50" style="vertical-align:bottom"/> Wizarding World

Use harry potter spells on your computer

> **_NOTE:_**  currently under development. Hence the skill is not working properly.
>

## About

Use spells of the wizarding world universe for some operations on your
computer.

You'll be able to change functions of pre-defined spell functions or expand
easily the spells with custom functions/add custom spells.

This skill will generate the actual skill based on the registry.yml. With the
reload intent you'll be able to reload the actual skill with new defined
functions of your registry.yml

## registry.yml

In this section you will learn how to edit the registry.yml for adding your
custom functions.

The registry.yml is structured as follows:

```
handle_function_name:
  pyfunction: function_name_in_spells_py
  intent: "This is what the user has to say that the function is triggered"
  prompts: True or False
```

The name of the top-level (```handle_function_name```) in the registry.yml is
not really relevant at all for the user, it's just the name of function of
the ```@intent_handler``` inside of the generated ```__init__.py``` and
identifier/key for the custom configuration aspects of it - which function
should be called, which intents are there for this identifier, should mycroft
respond something in the called function?

```pyfunction``` should have the name of the python function in ```spells.py```
as value which should be called as intent handling. Make sure that you copy the
exact name (with underscores, etc.)

```intent``` takes a list with intents as strings. If there is only one intent,
write just one String inside the list else add more elements
like ```["This is intent1", "This is intent2"]```

```prompts``` takes either ```True``` or ```False```. If your python function in spells.py
contains prompts as described
in [mycroft prompts docs](https://mycroft-ai.gitbook.io/docs/skill-development/user-interaction/prompts)
then you have to write ```True```. The difference is that the code generator
generates the function call of ```pyfunction``` with "self" as parameter
e.g. ```example_function(self)``` in the init.py
if prompts value is True. This makes it possible that you can define your
custom function in spells.py like

```
def example_function(skill_instance):
    skill_instance.speak("This phrase will mycroft speak")
```

If you don't have prompts in your custom function, you can
set ```prompts: false``` and don't have to use a param like```skill_instance```
in your function because in the function call in init.py won't be a parameter.

<br>
To put it all together, here is an example how your registry.yml should look:

```
---
avada_kedavra:
  pyfunction: avada_kedavra
  intent: ["avada kedavra"]
  prompts: True

expecto_patronum:
  pyfunction: expecto_patronum
  intent: ["expecto patronum"]
  prompts: False

obliviate:
  pyfunction: obliviate
  intent: ["obliviate"]
  prompts: False
```

There is no limit how many handle_functions can be added, all of them will be
generated

## Examples

* "avada kedavra" (shutdown your computer)
* "expecto patronum" (will open stackoverflow)
* "Reload my spells" (reload generated spells)

## Credits

Hendrik Roth (@hendrik-roth)

## Category

**Entertainment**
Configuration

## Tags

# Harry potter

# Spells

# Wizarding world

