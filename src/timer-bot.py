
from lib.argument_parser import TimerParser
from lib.timer import Timer


def main():
  parser = TimerParser()
  args = parser.parse()

  timer = Timer(
    args.goal_time,
    args.label,
    args.comment,
    args.slack_channel
  )

  timer.start_timer()


if __name__ == "__main__":
  main()
