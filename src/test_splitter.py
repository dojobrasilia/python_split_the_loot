from unittest import TestCase
from splitter import Splitter
class SplitterTest(TestCase):
    
    def test_spliting_for_a_single_pirate_is_trivial(self):
        s = Splitter()
        self.assertEqual(s.split([2,2,3],1), [[2,2,3]], "Should be trivial")
        self.assertEqual(s.split([1,3],1), [[1,3]], "Should be trivial")
        pass
    
    def test_spliting_an_homogeneous_array_leads_to_an_homogeneous_answer(self):
        s = Splitter()
        self.assertEqual(s.split([2,2],2), [[2],[2]], "Should be trivial")
        pass