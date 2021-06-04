import unittest
from optimal_change import optimal_change

class armstrong_test(unittest.TestCase):
    
    '''Tests the correct output if insufficient funds are paid'''
    def test_returns_insufficient_funds(self):
        self.assertEqual(optimal_change(62.13, 60), "Insufficient funds, please pay an additional $2.13.")
    
    '''Tests the correct output if exaxct change is paid'''
    def test_returns_exact_change(self):
        self.assertEqual(optimal_change(20, 20), "Exact change paid, have a nice day.")

    '''Tests the correct output if only change is one denomination'''
    def test_returns_one_denomination(self):
        self.assertEqual(optimal_change(20, 40), "The optimal change for an item that costs $20 with an amount paid of $40 is 1 $20 bill.")

    '''Tests when there is only 1 penny change'''
    def test_returns_one_penny(self):
        self.assertEqual(optimal_change(20, 20.01), "The optimal change for an item that costs $20 with an amount paid of $20.01 is 1 penny.")

    '''Tests when there are two pennies change'''
    def test_returns_one_penny(self):
        self.assertEqual(optimal_change(20, 20.02), "The optimal change for an item that costs $20 with an amount paid of $20.02 is 2 pennies.")

    '''Tests when there are no pennies with larger change'''
    def test_returns_3(self):
        self.assertEqual(optimal_change(20,1500), "The optimal change for an item that costs $20 with an amount paid of $1500 is 14 $100 bills, 1 $50 bill, 1 $20 bill, and 1 $10 bill.")

    '''Test that the output string matches the expected string output with the correct number of bills, punctuation and plurals'''

    def test_returns_1(self):
        self.assertEqual(optimal_change(62.13, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
    def test_returns_2(self):
        self.assertEqual(optimal_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

if __name__ == '__main__':
    unittest.main()