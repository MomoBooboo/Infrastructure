import time

def send_trade_data():
    # Logic to generate trade data and send it to the Leaderboard Service
    print("Sending trade data...")
    # Placeholder code for sending data
    time.sleep(1)  # Simulate delay
    print("Trade data sent successfully.")

def main():
    # Periodically send trade data
    while True:
        send_trade_data()
        time.sleep(10)  # Send data every 10 seconds

if __name__ == "__main__":
    main()
