from unittest import TestCase

from monitor import Monitor, SerialNotYetPolledError

SERIAL_LINE = '0:10,1:12,2:9,3:0,4:1'
POS_LIST = [10,12,9,0,1]
THRESHOLD = 10
CLOSED_SENSORS = [0,2,4]
OPEN_SENSORS = [1,3]

class test_monitor(TestCase):
    
    def setUp(self):
        self.mon = Monitor()
        self.mon.setSerial(MockSerial)
        self.mon.setThreshold(THRESHOLD)
        
    def test_get_serial_data(self):
        self.assertEqual(self.mon.getPosList(),POS_LIST)
        
    def test_list_closed_sensors(self):
        self.assertEqual(self.mon.getClosedSensors(),CLOSED_SENSORS)
        
    def test_list_open_sensors(self):
        self.assertEqual(self.mon.getOpenSensors(),OPEN_SENSORS)
            
    def test_sensor_count_too_early_raises_exception(self):
        self.assertRaises(SerialNotYetPolledError, self.mon.sensorCount)
        
    def test_list_sensor_count(self):
        self.mon.readline()
        self.assertEqual(len(POS_LIST), self.mon.sensorCount()) 
        
    def test_only_lists_one_triggered_sensor(self):
        self.mon.readline()
        self.assertEqual(self.mon.getTriggeredSensor(),CLOSED_SENSORS[0])
        
        

    

    
class MockSerial(object):
    
    def readline(self):
        return SERIAL_LINE