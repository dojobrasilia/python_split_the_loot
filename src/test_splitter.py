from unittest import TestCase
from splitter import Splitter
class SplitterTest(TestCase):
    def setUp(self):
        self.s = Splitter()

    def test_returns_none_when_loot_is_undivisible_by_number_of_pirates(self):
        self.assertEqual(None,self.s.split([2,3],2))
        
    def test_returns_none_when_there_are_not_enough_gems(self):
        self.assertEqual(None,self.s.split([4,2],3))
        
    def test_should_split_for_trivial_case(self):
        self.assertEqual([[2],[2]],self.s.split([2,2],2))
        self.assertEqual([[2],[2],[2]],self.s.split([2,2,2],3))
        self.assertEqual([[2,2],[2,2]],self.s.split([2,2,2,2],2))
        
    