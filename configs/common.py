from os.path import dirname, abspath
BASE_DIR = dirname(dirname(abspath(__file__)))


import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the minimum logging level
    format="%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()]  # Output to console
)

if __name__ == '__main__':
    print("BASE_DIR:", BASE_DIR)