from unittest import TestCase
from splitter import Splitter
class SplitterTest(TestCase):
    def setUp(self):
        self.s = Splitter()

    def test_returns_none_when_loot_is_undivisible_by_number_of_pirates(self):
        self.assertEqual(None,self.s.split([2,3],2))
        
    def test_returns_none_when_there_are_not_enough_gems(self):
        self.assertEqual(None,self.s.split([4,2],3))
        
    def test_everybody_gets_the_same_kind_of_bucket_when_we_have_only_one_type_of_gem(self):
        self.assertEqual([[2],[2]],self.s.split([2,2],2))
        self.assertEqual([[2],[2],[2]],self.s.split([2,2,2],3))
        self.assertEqual([[2,2],[2,2]],self.s.split([2,2,2,2],2))
        
    def test_everybody_gets_the_same_kind_of_bucket_when_we_have_an_even_kind_gem(self):
        self.assertEqual([[3,2],[3,2]],self.s.split([3,2,3,2],2))
    