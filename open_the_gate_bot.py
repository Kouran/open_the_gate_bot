#!/usr/bin/env python
import telepot
from telepot.loop import MessageLoop
import time
import subprocess
import shlex


bot = telepot.Bot('')
my_id=
open_command="systemctl start openvpn@server.service"
close_command="systemctl stop openvpn@server.service"


def startup():
        print(bot.getMe())

        
def handle(msg):
        sender_id = msg["from"]["id"]
        chat_id = msg['chat']['id']
        command = msg['text']
        if sender_id==my_id:
                if command == "/open".encode("utf-8"):
                        command=open_command
                elif command == "/close".encode("utf-8"):
                        command=close_command
                else:
                        return
                args = shlex.split(command)
                proc = subprocess.Popen(args)
                response = proc.wait()
                if response == 0:
                        bot.sendMessage(chat_id, "Done!")
                else:
                        bot.sendMessage(chat_id, "Command failed")


def main():
        startup()
        MessageLoop(bot, handle).run_as_thread()
        while 1:
                print('I am listening...')
                time.sleep(10)


if __name__ == "__main__":
        main()
