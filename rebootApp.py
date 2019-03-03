from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.storage.jsonstore import JsonStore
from pexpect import pxssh
import os


store = JsonStore('test.json')
HOST = 'your ip'
LOGIN = 'yout login'
PASSWORD = 'your password'

if not os.path.isfile('./test.json'):
    store.put('rankName', text="Your Rank: Pidor")
    store.put('reboots', txt="Reboots: 0", savedClikcs=0)

clicks = store.get('reboots')['savedClikcs']


class rebootApp(App):
    def build(self):

        rebootButtonAnch = AnchorLayout(anchor_x='center', anchor_y='bottom')
        rebootButtonBox = BoxLayout(orientation='vertical',
                                    size_hint=[.8, .25],
                                    padding=[50])

        rebooterRank = Label(text=store.get('rankName')['text'],
                             font_size='15sp')
        textReboots = Label(text=store.get('reboots')['txt'],
                            font_size='60sp')
        buttonReboot = Button(text="REBOOT ROUTER", size_hint=[1, 1])

        rebootButtonAnch.add_widget(textReboots)
        rebootButtonBox.add_widget(rebooterRank)
        rebootButtonBox.add_widget(buttonReboot)
        rebootButtonAnch.add_widget(rebootButtonBox)

        def sshReboot():
            router = pxssh.pxssh()
            if not router.login(HOST, LOGIN, PASSWORD):
                # do something
                pass
            else:
                # print something
                router.sendline('reboot')
                router.prompt()
                router.logout()
                # print something

        def on_click(self):
            sshReboot()
            global clicks
            clicks += 1
            store.put('reboots', txt="Reboots: " + str(clicks),
                      savedClikcs=clicks)
            clicksText = "Reboots: " + str(clicks)
            textReboots.text = clicksText
            if (clicks > 5 and clicks < 10):
                rebooterRank.text = "WoW, now you are: Gondon!"
                store.put('rankName', text="WoW, now you are: Gondon!")
            elif (clicks > 10 and clicks < 20):
                rebooterRank.text = "Wait, you are just fucking Gleb"
                store.put('rankName', text="Wait, you are just fucking Gleb")
            elif clicks > 20:
                rebooterRank.text = "Look at him, he is REBOOT GOD!"
                store.put('rankName', text="Look at him, he is REBOOT GOD!")

        buttonReboot.bind(on_press=on_click)
        return rebootButtonAnch


if __name__ == "__main__":
    rebootApp().run()
