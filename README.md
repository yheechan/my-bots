# hcy-python-bot
Attempt to use [Slackbot](https://slack.com/intl/ko-kr/help/articles/202026038-Slackbot-%EC%86%8C%EA%B0%9C) and practice coding with OOP (modules). **Mostly waste time...**

## Setting ``SLACK_TOKEN`` to environmental variable
User should set their own [slack token](https://api.slack.com/tutorials/tracks/getting-a-token) to environmental variable, ``SLACK_TOKEN``, to enable connection with user's own **slack channel**.
  * reference cite: [link](https://www.datacamp.com/tutorial/how-to-send-slack-messages-with-python)

## 1. timer-bot
Timer-bot **registers** a timer and and automatically **alerts** user through slack channel and **logs** the information to a file.
  * motivation:
    1. Form some kind of drive to stay focused on one task.
    2. Enable easy automated way of logging work status.

### Functionalities
1. Starts and ends a timer based on user input, ``-t <goal-time>`` (metric: minutes, type: float).
2. Alerts start and end time to user through slack channel, ``-sc <slack-channel>`` (optional).
3. Logs the timer information to ``results/logs/timer_logs.csv`` file.

Example File: [timer_logs_example.csv](./results/logs/timer_logs_example.csv)

Example Log:
idx | label | comment | date | goal_time(min) | start_time | end_time | durated_time (min)
--- | --- | --- | --- | --- | --- | --- | ---
1 | read-book | The-Bible | \<year-month-date\> | \<min-in-float\> | \<hour:min:sec\> | \<hour:min:sec\> | \<min-in-float\>
2 | read-book | 길갈 [INTERRUPTED] | 2024-12-06 | 30.0 | 17:37:18 | 17:37:23 | 0.06666666666666667

### Usage
```
usage: timer-bot.py [-h] [-sc SLACK_CHANNEL] -gt GOAL_TIME -l LABEL [-c COMMENT]

Timer Bot

options:
  -h, --help            show this help message and exit
  -sc SLACK_CHANNEL, --slack-channel SLACK_CHANNEL
                        Slack channel name to send the message
  -gt GOAL_TIME, --goal-time GOAL_TIME
                        Time in minutes (float type) for the timer
  -l LABEL, --label LABEL
                        Label for the timer
  -c COMMENT, --comment COMMENT
                        Comment for the timer
```

A user can register a timer with following input arguments:
  * ``-sc <slack-channel>`` (optional): name of the slack channel.
  * ``-t <goal-time>`` (required): goal time in minutes (float type).
  * ``-l <str>`` (required): basic label for what your timer is for.
  * ``-c <str>`` (optional): basic commentary about the timer.

Example Execution Command:
```
$ python3 timer-bot.py -sc <slack-channel> -gt 30.0 -l read-book -c The-Bible
```
* User can press ``<ctrl+c>`` key to terminate timer (logs the timer before termination).

last updated Dec 06, 2024
