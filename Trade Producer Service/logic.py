import time
import schedule

def send_trade_data():
    # Placeholder function to send trade data
    print("Sending trade data...")

# Schedule to send trade data every 10 seconds
schedule.every(10).seconds.do(send_trade_data)

# Run scheduler indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)
