import unittest
import configparser

# Read configuration
config = configparser.ConfigParser()
config.read('unittest.cfg')

# Get configuration values
start_directory = config['unittest']['start-directory']
pattern = config['unittest']['pattern']

# Discover and run tests
loader = unittest.TestLoader()
suite = loader.discover(start_directory, pattern=pattern)

runner = unittest.TextTestRunner()
runner.run(suite)