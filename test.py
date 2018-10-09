import unittest, gc
from demo import WorldData

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.worldlData = WorldData('happy') 

    def tearDown(self):
         self.worldlData = None
         del self.worldlData
         gc.collect()

    def test_result_method(self):
         self.assertEqual(self.worldlData.write_result(),'happy')

if __name__ == '__main__':
    unittest.main()





