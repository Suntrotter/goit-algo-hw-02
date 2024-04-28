from queue import Queue
import time
import random

queue = Queue()

def generate_request():
    request_id = random.randint(1, 1000)
    request = f"Request {request_id}"
    queue.put(request)
    print(f"Generated request: {request}")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"Processing request: {request}")
        
        time.sleep(random.uniform(0.5, 2))
        print(f"Completed processing: {request}")
    else:
        print("Queue is empty. No requests to process.")

def main():    
    while True:
        exit_program = input("Press 'q' to quit, or any other key to continue: ")
        if exit_program.lower() == 'q':
            print("Exiting the program....")
            break
        else:
            if queue.empty():    
                generate_request()    
                time.sleep(1)        
                process_request()    
                time.sleep(2)        
        

if __name__ == "__main__":
    main()


