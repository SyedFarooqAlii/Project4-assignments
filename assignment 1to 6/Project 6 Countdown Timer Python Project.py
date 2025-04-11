import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    
    print("00:00")
    print("Time's up!")

def main():
    seconds = int(input("Enter the time in seconds for countdown: "))
    countdown_timer(seconds)

if __name__ == "__main__":
    main()
