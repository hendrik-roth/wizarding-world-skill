import os
import webbrowser
import alsaaudio


def avada_kedavra(skill_instance):
    answer = skill_instance.ask_yesno(
        prompt="Are you sure to shutdown your computer?")
    skill_instance.log.info(answer)
    if answer == "yes":
        skill_instance.speak("Goodbye")
        os.system("poweroff")
    else:
        skill_instance.speak("Okay, I will not shutdown your computer")


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
