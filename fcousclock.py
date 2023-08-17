import time

def focus_timer(duration, interval):
    end_time = time.time() + duration

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes, seconds = divmod(int(remaining_time), 60)
        print(f"Remaining time: {minutes:02d}:{seconds:02d}", end='\r')
        time.sleep(interval)

    print("Focus time is over!")

if __name__ == "__main__":
    focus_duration = 25 * 60  # 25 minutes in seconds
    update_interval = 1  # Update interval in seconds

    print("Focus timer started!")
    focus_timer(focus_duration, update_interval)
