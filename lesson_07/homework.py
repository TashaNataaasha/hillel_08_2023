import time
import logging

class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        logging.info(f"Execution time: {elapsed_time:.4f} seconds")

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


with TimerContext():
    time.sleep(2)
    
with TimerContext():
    for _ in range(100):
        pass
    
with TimerContext():
    for _ in range(10000):
        pass