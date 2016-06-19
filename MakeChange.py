from types import IntType
import argparse
			
"""
Technical test question 1
"""

def MakeChange(money):
    """
    Function that returns the minimum amount of bills given a given amount of money
    :param money: The amount of money to be changes
    :return: The total count of the bills
    """
    denominations=[100, 50, 20, 10, 5, 1] # Denominations (bill types) of the currency
    bills_returned={} # Dictionary {denomination(bill type):amount}
    
    # Check if input is valid
    if (type(money) is not IntType):
        raise ValueError("Expected integer. Input can not be of {0}: {1}".format(type(money),money))
    if (money<0):
        raise ValueError("Input can not a negative number: {0}".format(money))
    
    original_amount=money #save the original amount for assertion
    
    # For each denomination the amount of bills to return equals to the integer part of the division of the money
    # Example : 226/100=2 with 26 as remainder. Then since 26 < 50 , continue to the next type. 26/20=1 with 6 as remainder.
    # Continue for 10. 6/5=1 and 1 remains 1/1=1 and finish. The resulting dict would be {100:2, 20:1,5:1,1:1}
    for den in denominations:
        if (money<den):
            continue
        else:
            div=money/den
            bills_returned[den]=div
            money-=div*den
            
    # Assert that the original amount equals to the amount after summing all the bills     
    assert original_amount==sum(k*v for k,v in bills_returned.iteritems()) , "Error creating change from input {0}".format(original_amount) 
    
    # Return the sum of the count of the bills
    return sum(bills_returned.values())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Make change")
    parser.add_argument("money", nargs=1, help = "Input money (integer) to make change")
    args = parser.parse_args()

    print MakeChange((int)(args.money[0]))