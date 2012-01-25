from unittest import TestCase
from splitter import Splitter
class SplitterTest(TestCase):
    def setUp(self):
        self.s = Splitter()

    def test_spliting_for_a_single_pirate_is_trivial(self):
        self.assertEqual(self.s.split([2,2,3],1), [[2,2,3]])
        self.assertEqual(self.s.split([1,3],1), [[1,3]])
        pass
    
    def test_spliting_an_homogeneous_array_leads_to_an_homogeneous_answer(self):
        self.assertEqual(self.s.split([2,2],2), [[2],[2]])
        self.assertEqual(self.s.split([2,2,2,2,2,2],3), [[2,2],[2,2],[2,2]])
        pass