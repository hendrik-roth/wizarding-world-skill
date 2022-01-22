import os
import webbrowser
import alsaaudio

from . import WizardingWorld


def avada_kedavra():
    answer = WizardingWorld.ask_yesno(
        prompt="Are you sure to shutdown your computer?")
    if answer == "yes":
        os.system("shutdown /s /t 1")
    else:
        WizardingWorld.speak("Okay, I will not shutdown your computer")


def expecto_patronum():
    webbrowser.open("https://stackoverflow.com")


def reducto():
    pass


def obliviate():
    pass


def quietus():
    m = alsaaudio.Mixer()
    vol = m.getvolume()
    vol = int(vol[0])
    new_vol = vol - 10
    m.setvolume(new_vol)


def salvio_hexia():
    pass
