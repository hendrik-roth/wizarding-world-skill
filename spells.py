import os
import webbrowser
import alsaaudio

from mycroft import MycroftSkill


def avada_kedavra():
    answer = MycroftSkill.ask_yesno("Are you sure to shutdown your computer?")
    if answer == "yes":
        os.system("shutdown /s /t 1")
    else:
        MycroftSkill.speak("Okay, I will not shutdown your computer")


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
