from unittest import TestCase
from splitter import Splitter
class SplitterTest(TestCase):
    def setUp(self):
        self.s = Splitter()

    def test_for_a_single_pirate_is_trivial(self):
        self.assertEqual(self.s.split([2,2,3],1), [[2,2,3]])
        self.assertEqual(self.s.split([1,3],1), [[1,3]])
    
    def test_an_homogeneous_loot_leads_to_an_homogeneous_answer(self):
        self.assertEqual(self.s.split([2,2],2), [[2],[2]])
        self.assertEqual(self.s.split([2,2,2,2,2,2],3), [[2,2],[2,2],[2,2]])
    
    def _test_a_loot_with_a_even_number_of_elements_an_single_kind_of_answer(self):
        self.assertEqual(self.s.split([1,2,1,2],2), [[1,2],[1,2]])
        self.assertEqual(self.s.split([1,1,2,2],2), [[1,2],[1,2]])
        self.assertEqual(self.s.split([1,3,1,2,3,3,2,1,2],3), [[1,2,3],[1,2,3],[1,2,3]])
    
    def test_a_loot_with_an_simple_eager_example(self):
        self.assertEqual(self.s.split([1,3,4],2), [[1,3],[4]])
    
    def test_a_loot_with_an_eager_example_returning_one_choice(self):
        self.assertEqual(self.s.split([2,2,1,1],2), [[1,2],[1,2]])
        