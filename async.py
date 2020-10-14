import time


class EventLoopCommand:

    def __await__(self):
        return (yield self)


class Sleep(EventLoopCommand):

    def __init__(self, seconds):
        self.seconds = seconds


async def do_ticking(amount_of_ticks=5):
    for _ in range(amount_of_ticks):
        print("tick")
        await Sleep(1)


ticking = do_ticking()

while True:
    try:
        sleep_command = ticking.send(None)
        seconds_to_sleep = sleep_command.seconds
        time.sleep(seconds_to_sleep)
    except StopIteration:
        break  # корутина истощилась, прерываем event loop

print("BOOM!")