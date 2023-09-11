import os
import threading
import multiprocessing
import time
import requests

# CPU-bound task (heavy computation)
def encrypt_file(path: str):
    print(f"Processing file {path} in process {os.getpid()}")
    # Simulate heavy computation by sleeping for a while
    _ = [i for i in range(100_000_000)]

# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(f"Downloading image from {image_url} in thread {threading.current_thread().name}")
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)
        
try:
    if __name__ == "__main__":
        start_time = time.perf_counter()

        encryption_process = multiprocessing.Process(target=encrypt_file, args=("rockyou.txt",))
        encryption_process.start()

        image_download_thread = threading.Thread(target=download_image, args=("https://picsum.photos/1000/1000",))
        image_download_thread.start()

        encryption_process.join()
        image_download_thread.join()

        end_time = time.perf_counter()
        total_time = end_time - start_time

        print(f"Time taken for encryption task: {encryption_process.exitcode} seconds")
        print(f"Time taken for I/O-bound task: {total_time} seconds")
    
except Exception as e:
    print(f"Error occurred: {e}")