# Assessment 1

## Important Grading Information
* TODO PUT RUBRIC HERE
* This assessment is worth 15% of your final grade. You need to get a 75% or better to pass.
* If you fail the assessment, you will have one week to retake it for a 10% penalty. We will not regrade passing assessments.

## Rules / Process
* This test is fully open notes and open Google, but is not to be completed with other students
* Do not open a pull request against this repository. We will evaluate your code individually with you.

# Part 1: Algorithms
You are writing a computer program for an electronic vending machine to give you the optimal change for an item's cost. Write a method called `optimal_change` that takes in two arguments: `item_cost` and `amount_paid`. The method will `print` a string with optimal change which follows the following convention:

```
optimal_change(62.13, 100)
> "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies."

optimal_change(31.51, 50)
> "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies."
```

Don't forget to account for plural denominations (i.e., quarters, dimes, pennies, bills) and punctuation (i.e., commas and the period at the end of a sentence) to delineate between different denominations. Some other things to note:
- This is **optimal** change. Obviously, you can give the change in pennies, but we're looking for the most optimal (least amount of) change possible.
- Fully understand the data types of your input and output
- Write at least 3-4 unit tests. Feel free to start with the two examples above
