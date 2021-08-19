import unittest
import Group2_ASP_project as prog

class TestMyProgram(unittest.TestCase):
    def test_Total(self):
        self.assertEqual(prog.totalDFs,15993497)
    def test_Mean(self):
        self.assertEqual(prog.meanDF,5331165.67)
