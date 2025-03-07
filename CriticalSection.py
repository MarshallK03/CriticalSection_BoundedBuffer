import time
import threading
import random
from tkinter.font import names

from Semiphores import Semaphore

class CriticalSection:
    def  __init__(self):
        # Create a binary semaphore
        self.semaphore = Semaphore(1, "CS_mutex")

        #log the initialization
        print(f"[{time.strftime('%H:%M:%S')}] critical section initialized")

    def critical_section(self, p):
        """
        1. Entry Section: request access to CS
        2. Critical Section itself
        3. Exit section
        """

        # get the current thread
        thread_id = threading.current_thread().name

        # Entry
        print(f"[{time.strftime('%H:%M:%S')}] Thread {thread_id} ATTEMPTING CS")
        self.semaphore.P() # Semaphore acquire operation (decrease value)

        # critical section
        print(f"[{time.strftime('%H:%M:%S')}] Thread {thread_id} RUNNING CS")
        # simulate cs
        cpu_time = random.uniform(1,3)
        print(f"[{time.strftime('%H:%M:%S')}] Thread {thread_id} RUNNING CS for {cpu_time} second")
        time.sleep(cpu_time)


        # exit section
        print(f"[{time.strftime('%H:%M:%S')}] Thread {thread_id} EXITING CS")
        self.semaphore.V() #release the resource (increase value)

        # remainder
        print(f"[{time.strftime('%H:%M:%S')}] Thread {thread_id} LEFT THE CS")


