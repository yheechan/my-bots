import argparse

class Parser:
    """
    Super class for the argument parser
    """
    def __init__(self, description):
        self.description = description
        self.parser = argparse.ArgumentParser(description=self.description)
        self.parser.add_argument("-sc", "--slack-channel", type=str, help="Slack channel name to send the message", required=False)
    
    def parse(self):
        return self.parser.parse_args()



class TimerParser(Parser):
    """
    Argument parser for the timer
    """
    def __init__(self):
        super().__init__("Timer Bot")
        self.parser.add_argument("-gt", "--goal-time", type=float, help="Time in minutes (float type) for the timer", required=True)
        self.parser.add_argument("-l", "--label", type=str, help="Label for the timer", required=True)
        self.parser.add_argument("-c", "--comment", type=str, help="Comment for the timer", default="No-Comment")

