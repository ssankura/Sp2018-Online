"""
Unit tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump.pump import Pump
from sensor.sensor import Sensor

from waterregulation.controller import Controller
from waterregulation.decider import Decider


class DeciderTests(unittest.TestCase):
    """
    Unit tests for the Decider class
    """

    def test_decider_current_action_pump_off_height_less_than_target(self):
        decider = Decider(target_height=10000, margin=1000)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)
        controller = Controller(sensor, pump, decider)
        result = decider.decide(current_height = 5000, current_action = Pump.PUMP_OFF, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_IN)

    def test_decider_current_action_pumpoff_height_greater_target_and_margin(self):
        decider = Decider(target_height=1000, margin=200)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)
        controller = Controller(sensor, pump, decider)

        result = decider.decide(current_height = 1250, current_action = Pump.PUMP_OFF, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OUT)

    def test_decider_current_action_pumpoff_height_in_target_and_margin_range(self):
        decider = Decider(target_height=5000, margin=1000)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)
        controller = Controller(sensor, pump, decider)

        #equal to target + margin case
        result = decider.decide(current_height = 4000, current_action = Pump.PUMP_OFF, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OFF)

        #equal to target + margin case
        result = decider.decide(current_height = 4000, current_action = Pump.PUMP_OFF, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OFF)


        #in the range of (target - margin to target + margin)
        result = decider.decide(current_height = 5800, current_action = Pump.PUMP_OFF, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OFF)

        #in the range of (target - margin to target + margin)
        result = decider.decide(current_height = 4200, current_action = Pump.PUMP_OFF, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OFF)
    
    def test_decider_current_action_pumpin_greater_than_target(self):
        decider = Decider(target_height=3000, margin=500)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)
        controller = Controller(sensor, pump, decider)
        
        result = decider.decide(current_height = 3500, current_action = Pump.PUMP_IN, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OUT)        

        result = decider.decide(current_height = 5000, current_action = Pump.PUMP_IN, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OUT)        

    def test_decider_current_action_pumpin_less_than_target(self):
        decider = Decider(target_height=7500, margin=2500)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)
        controller = Controller(sensor, pump, decider)
        
        result = decider.decide(current_height = 2000, current_action = Pump.PUMP_IN, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_IN)        

        result = decider.decide(current_height = 7499, current_action = Pump.PUMP_IN, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_IN) 

    
    def test_decider_current_action_pumpout_less_than_target(self):
        decider = Decider(target_height=3000, margin=500)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)
        controller = Controller(sensor, pump, decider)
        
        result = decider.decide(current_height = 2550, current_action = Pump.PUMP_OUT, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OFF)        

        result = decider.decide(current_height = 1000, current_action = Pump.PUMP_OUT, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OFF)        

    def test_decider_current_action_pumpout_greater_than_target(self):
        decider = Decider(target_height=18000, margin=2000)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)
        controller = Controller(sensor, pump, decider)
        
        result = decider.decide(current_height = 19000, current_action = Pump.PUMP_OUT, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OUT)        

        result = decider.decide(current_height = 20050, current_action = Pump.PUMP_OUT, actions = controller.actions)
        self.assertEqual(result, Pump.PUMP_OUT) 


class ControllerTests(unittest.TestCase):
    """
    Unit tests for the Controller class
    """

    def test_controller_tick(self):
        decider = Decider(target_height=3000, margin=500)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)

        pump.set_state = MagicMock(return_value = True)
        pump.get_state = MagicMock(return_value = Pump.PUMP_OFF)

        sensor.measure = MagicMock (return_value = 3500)
        controller = Controller(sensor, pump, decider)

        result = controller.tick()
        self.assertEqual(result, True)

