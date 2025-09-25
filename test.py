import asyncio

from src.check_qq_update import qqnt_version_monitor

if __name__ == '__main__':

    import time

    while True:
        print(asyncio.run(qqnt_version_monitor.get_new_version()))
        time.sleep(5)