import time
from datetime import datetime as dt

sites_to_unblock = [
    "www.facebook.com",
    "facebook.com",
    "www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com",
]


Window_host = r"C:\\Windows\\System32\\drivers\\etc\\hosts"
default_hoster = Window_host
redirect = "127.0.0.1"


def unblock_websites(start_hour, end_hour):
    while True:
            with open(default_hoster, "r+") as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_unblock):
                        hostfile.write(host)
                hostfile.truncate()
            print("Check your websites")


if __name__ == "__main__":
    unblock_websites(9, 21)