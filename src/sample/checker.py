from src.sample.environment import Environment


class Checker:
    def __init__(self):
        self.environment = Environment()

    def remainder(self):
        time = self.environment.getTime()
        if 17 < time:
            return self.environment.wavWasPlayed()
        else:
            return self.environment.resetWav()
