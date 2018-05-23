"""
Module tests for the water-regulation module
"""

import unittest
from unittest.mock import MagicMock

from pump.pump import Pump
from sensor.sensor import Sensor

from waterregulation.controller import Controller
from waterregulation.decider import Decider


class ModuleTests(unittest.TestCase):
    """
    Module tests for the water-regulation module
    """

    def test_integration_happy_path(self):
        decider = Decider(target_height=3000, margin=500)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)

        pump.set_state = MagicMock(return_value = True) 
        pump.get_state = MagicMock(return_value = Pump.PUMP_OFF)

        sensor.measure = MagicMock (return_value = 3500)
        controller = Controller(sensor, pump, decider)

        result = controller.tick()
        self.assertEqual(result, True)

    def test_integration_set_pump_state_fail(self):
        decider = Decider(target_height=3000, margin=500)
        pump = Pump('127.0.0.1', 8000)
        sensor = Sensor('127.0.0.1', 8000)

        pump.set_state = MagicMock(return_value = False) 
        pump.get_state = MagicMock(return_value = Pump.PUMP_OFF)

        sensor.measure = MagicMock (return_value = 3500)
        controller = Controller(sensor, pump, decider)

        result = controller.tick()
        self.assertEqual(result, False)

       