import argparse

class TimerParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Timer')
        self.parser.add_argument("-t", "--time", type=float, help="Time in minutes (float type) for the timer", required=True)
        self.parser.add_argument("-l", "--label", type=str, help="Label for the timer", required=True)
        self.parser.add_argument("-c", "--comment", type=str, help="Comment for the timer", default="No-Comment")

        self.parser.add_argument("-s", "--slack", type=str, help="Slack channel name to send the message", required=False)

    def parse(self):
        return self.parser.parse_args()
