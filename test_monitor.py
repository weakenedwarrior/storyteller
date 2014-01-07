from unittest import TestCase

from monitor import Monitor

SERIAL_LINE = '0:10,1:12,2:9,3:10,4:1'
POS_LIST = [10,12,9,10,1]

class test_monitor(TestCase):
    
    def setUp(self):
        self.mon = Monitor()
        self.mon.setSerial(MockSerial)
        
    def test_get_serial_data(self):
        self.assertEqual(self.mon.getPosList(),POS_LIST)



    
class MockSerial(object):
    
    def readline(self):
        return SERIAL_LINE