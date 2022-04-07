from flask_meld import Component, emit
import time


class LongRunningProcess(Component):
    value = 0

    def start(self):
        self.value = 0
        sleep_time = .05
        step_size = .5
        for count in range(int(100 / step_size)):
            time.sleep(sleep_time)
            self.value += step_size
            emit("progress", progress=self.value)
        emit("progress", progress=0)
