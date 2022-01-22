import os
import webbrowser
import alsaaudio
import time


def avada_kedavra(skill_instance):
    """
    shutdown computer when avada kedavra is called.

    Parameters
    ----------
    skill_instance
        instance of MycroftSkill for performing .speak or .ask_yesno functions
        of mycroft
    """
    answer = skill_instance.ask_yesno(
        prompt="Are you sure to shutdown your computer?")
    skill_instance.log.info(answer)
    if answer == "yes":
        skill_instance.speak("Goodbye")
        time.sleep(5)
        os.system("poweroff")
    else:
        skill_instance.speak("Okay, I will not shutdown your computer")


def expecto_patronum():
    """
    open stackoverflow
    """
    webbrowser.open("https://stackoverflow.com")


def reducto():
    pass


def obliviate():
    pass


def quietus():
    """
    reduce audio volume -10%
    """
    m = alsaaudio.Mixer()
    vol = m.getvolume()
    vol = int(vol[0])
    new_vol = vol - 10
    m.setvolume(new_vol)


def salvio_hexia():
    pass
