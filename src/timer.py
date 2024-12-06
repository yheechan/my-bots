import time
import signal

from lib.argument_parser import TimerParser
from lib.slack import Slack
import lib.global_var as gv


class Timer:
  def __init__(self, time, label, comment, slack):
    self.time = time
    self.durated_time = 0.0
    self.label = label
    self.comment = comment
    self.channel_name = slack
    self.interrupted = False

    self.slack = Slack(channel_name=self.channel_name, bot_name="Timer Bot")

  def start_timer(self):

    self.slack.send_message(f"[TIMER START] {self.label}: {self.time} minutes.")

    try:
      for i in range(int(self.time * 60)):
        time.sleep(1)
        self.durated_time += 1.0
        print(f"\r[TIMER] {self.label} - {time.strftime('%H:%M:%S', time.gmtime(i))}", end="")
      print()
    except KeyboardInterrupt:
      self.interrupted = True
      self.time = self.durated_time / 60
      self.comment += " [INTERRUPTED]"
      print("\n[TIMER INTERRUPTED] Timer was stopped manually.")

    self.slack.send_message(f"[TIMER END] {self.label}: {self.time} minutes.")
  
  def log_time(self):
    timer_log_file = gv.LOG_DIR / "timer_log.csv"
    if not timer_log_file.exists():
      with open(timer_log_file, "w") as f:
        f.write("idx,label,date,time,durated_time,comment\n")
    
    idx = self.get_idx()
    with open(timer_log_file, "a") as f:
      f.write(f"{idx},{self.label},{time.strftime('%Y-%m-%d %H:%M:%S')},{self.time},{self.durated_time},{self.comment}\n")
  
  def get_idx(self):
    timer_log_file = gv.LOG_DIR / "timer_log.csv"
    idx = 0
    with open(timer_log_file, "r") as f:
      for line in f:
        idx += 1
    return idx


def main():
  parser = TimerParser()
  args = parser.parse()

  timer = Timer(
    args.time,
    args.label,
    args.comment,
    args.slack
  )

  try:
    timer.start_timer()
  except KeyboardInterrupt:
    timer.interrupted = True
  finally:
    timer.log_time()
    if timer.interrupted:
      print("[TIMER END] Timer log recorded after interruption.")
    else:
      print("[TIMER END] Timer completed and logged successfully.")


if __name__ == "__main__":
  main()
