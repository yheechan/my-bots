import time

from lib.slack import Slack
import lib.global_vars as gv

class Timer:
  def __init__(self, goal_time, label, comment, slack_channel):
    self.goal_time = goal_time

    self.date = time.strftime("%Y-%m-%d", time.localtime())
    self.end_time = None
    self.durated_time = 0.0

    self.label = label
    self.comment = comment
    self.channel_name = slack_channel

    self.interrupted = False

    self.slack = Slack(channel_name=self.channel_name, bot_name="Timer Bot")

  def start_timer(self):
    """
    Start the timer and log the information.
    """
    self.slack.send_message(f"[TIMER START] {self.label}: {self.goal_time} minutes.")

    try:
      self.start_time = time.strftime("%H:%M:%S", time.localtime())
      for i in range(int(self.goal_time * 60)):
        time.sleep(1)
        self.durated_time += 1.0
        print(f"\r[TIMER] {self.label} - {time.strftime('%H:%M:%S', time.gmtime(i))}", end="")
      print()
      self.log_time()
    except KeyboardInterrupt:
      self.interrupted = True
      self.time = self.durated_time / 60
      self.comment += " [INTERRUPTED]"
      print("\n[TIMER INTERRUPTED] Timer was stopped manually.")
      self.log_time()

    self.slack.send_message(f"[TIMER END] {self.label}: {self.goal_time} minutes.")
  
  def log_time(self):
    """
    Log the timer information to the timer log file.
    """
    timer_log_file = gv.LOG_DIR / "timer_logs.csv"
    if not timer_log_file.exists():
      with open(timer_log_file, "w") as f:
        f.write("idx,label,comment,date,goal_time(min),start_time,end_time,durated_time(min)\n")
    
    idx = self.get_idx()
    self.end_time = time.strftime("%H:%M:%S", time.localtime())
    with open(timer_log_file, "a") as f:
      f.write(f"{idx},{self.label},{self.comment},{self.date},{self.goal_time},{self.start_time},{self.end_time},{self.durated_time/60}\n")

  
  def get_idx(self):
    """
    Get the index of the timer log file.
    """
    timer_log_file = gv.LOG_DIR / "timer_logs.csv"
    idx = 0
    with open(timer_log_file, "r") as f:
      for line in f:
        idx += 1
    return idx
