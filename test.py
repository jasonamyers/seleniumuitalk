import unittest
from driverspike import webdriver_setup, main

class TestUIFunctions(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver_setup()


    def tearDown(self):
        self.driver.close()


    def test_spike_main(self):
        main()
