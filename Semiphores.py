import threading
import time

class Semaphore:
    def __init__(self, initial_val, name= 'Semaphore'):
        # Conditional variable for Lock and Set
        self.lock = threading.Condition(threading.Lock())

        self.name = 'Semaphore'
        # current semaphore value
        self.value = initial_val
        # Log to show start time
        print(f"[{time.strftime('%H:%M:%S')}] {self.name} initialized with value {self.value}")

    def P(self):
        """
        Decrease Semaphore Value
        Implement wait operation with blocking when resources are unavailable
        """
        # get the current thread name fo rlogging
        thread_id = threading.current_thread().name

        # enter cond var to acquire lock
        with self.lock:
            #check if resources are available
            if self.value <= 0:
                print(f"[{time.strftime('%H:%M:%S')}] {self.name} value is {self.value}, Thread {thread_id} BLOCKED")


            # Handle wakeups
            while self.value <= 0:
                self.lock.wait()
                print(f"[{time.strftime('%H:%M:%S')}] {self.name} value is {self.value}, Thread {thread_id} woke up, value is now {self.value}")

            # Decrease semaphore value
            self.value = self.value - 1

            # log sucessful acquisition with new value
            print(f"[{time.strftime('%H:%M:%S')}] Thread {thread_id} acquired {self.name}, value is decreased to {self.value}")


    def V(self):
        """
            Increase Semaphore Value
            Implement signal operation for waiting threads
        """

        # get current thread
        thread_id = threading.current_thread().name

        #Show attempts to release
        print(f"[{time.strftime('%H:%M:%S')}] thread {thread_id} releasing {self.name}")

        #cond variable lock
        with self.lock:
            #increse resource count (release)
            self.value += 1
            print(f"[{time.strftime('%H:%M:%S')}] {self.name} value increased to {self.value}")


            #wake waiting threads
            self.lock.notify()

            print(f"[{time.strftime('%H:%M:%S')}] Thread {thread_id} was notified of available resources")
