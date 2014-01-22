from unittest import TestCase

from monitor import Monitor, SerialNotYetPolledError

SERIAL_LINE = ['0:10,1:12,2:9,3:5,4:1, ',
               '0:20,1:20,2:20,3:20,4:20, ',
               '0:20,1:5,2:20,3:20,4:20, ',
               '0:5,1:5,2:5,3:20,4:20, ',
               '0:0,1:0,2:0,3:5,4:0, ',
               '0:0,1:0,2:0,3:9,4:0, ',
               '0:0,1:0,2:0,3:0,4:0, ',
               '0:0,1:0,2:0,3:0,4:0, ',
               '0:0,1:0,2:0,3:0,4:5, ']

POS_LIST = [[10,12,9,5,1],
            [20,20,20,20,20],
            [20,5,20,20,20],
            [5,5,5,20,20],
            [0,0,0,5,0],
            [0,0,0,9,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,5]]

CLOSED_SENSORS = [[0,2,3,4],
                  [],
                  [1],
                  [0,1,2],
                  [3],
                  [],
                  [],
                  [],
                  [4]]

OPEN_SENSORS = [[1],
                [0,1,2,3,4],
                [0,2,3,4],
                [3,4],
                [0,1,2,4],
                [0,1,2,3,4],
                [0,1,2,3,4],
                [0,1,2,3,4],
                [0,1,2,3]]

CURRENT_SENSOR = [0,
                  None,
                  1,
                  1,
                  3,
                  None,
                  None,
                  None,
                  4]

DEFAULT_THRESHOLD = 10
INDIVIDUAL_THRESHOLDS = {3:6}

class test_monitor(TestCase):
    
    def setUp(self):
        self.cases = range(len(SERIAL_LINE))
        self.mon = Monitor()
        self.mon.setSerial(MockSerial, None, None)
        self.mon.setThresholds(DEFAULT_THRESHOLD,INDIVIDUAL_THRESHOLDS)
        
    def test_get_serial_data(self):
        for i in self.cases:
            self.assertEqual(self.mon.getDistances(),POS_LIST[i])
        
    def test_list_closed_sensors(self):
        for i in self.cases:
            self.assertEqual(self.mon.getClosedSensors(),CLOSED_SENSORS[i])
        
    def test_list_open_sensors(self):
        for i in self.cases:
            self.assertEqual(self.mon.getOpenSensors(),OPEN_SENSORS[i])
            
    def test_sensor_count_too_early_raises_exception(self):
        self.assertRaises(SerialNotYetPolledError, self.mon.sensorCount)
        
    def test_list_sensor_count(self):
        self.mon.readline()
        self.assertEqual(len(POS_LIST[0]), self.mon.sensorCount()) 
        
    def test_only_lists_one_triggered_sensor(self):
        for i in self.cases: 
            self.assertIn(self.mon.getCurrentSensor(),[None]+self.cases)
        
    def test_when_no_sensors_are_closed_return_none(self):
        self.mon.readline()
        self.assertEqual(self.mon.getCurrentSensor(),None)
        
    def test_once_a_sensor_is_current_it_remains(self):
        for i in self.cases:
            self.assertEqual(self.mon.getCurrentSensor(),CURRENT_SENSOR[i])
            
    def test_getNextSensor_blocks_until_a_sensor_closes(self):
        self.readMany(5)
        self.assertEqual(self.mon.getNextSensor(),CURRENT_SENSOR[8])

    def test_flush_occurs_on_first_readline(self):
        self.readMany(5)
        self.mon.flush()
        self.assertEqual(self.mon.getDistances(),POS_LIST[0])

    def readMany(self, readlines):
        for i in range(readlines):
            self.mon.readline()
            
    

class MockSerial(object):
    
    def __init__(self, device, baud):
        self.lineno = -1
    
    def readline(self):
        self.lineno = (self.lineno + 1) % len(SERIAL_LINE)
        return SERIAL_LINE[self.lineno]
    
    def flushInput(self):
        self.lineno = -1