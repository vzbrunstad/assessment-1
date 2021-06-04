def optimal_change(owed,paid): # Define the change function that returns a string with the correct change
    

    us_currency = {# Declare a directory of us currency.

    '$100 bill': 100,
    '$50 bill' : 50,
    '$20 bill': 20,
    '$10 bill': 10,
    '$5 bill': 5,
    '$1 bill': 1,
    'quarter': .25,
    'dime': .10,
    'nickle': .05,
    'penny': .01,

    } 

    
    optimal_change_dir = {# Declare an optimal_change_dir to add the number of each bill/coin

    '$100 bill': 0,
    '$50 bill' : 0,
    '$20 bill': 0,
    '$10 bill': 0,
    '$5 bill': 0,
    '$1 bill': 0,
    'quarter': 0,
    'dime': 0,
    'nickle': 0,
    'penny': 0,

    } 
    

    change = paid- owed # Calculate Change 
    if change < 0:  # Test if enough money way paid
        return  f"Insufficient funds, please pay an additional ${round(change * -1, 3)}."
    elif change == 0: # Test for exact change
        return "Exact change paid, have a nice day." 
    
    
    for x in us_currency: # step through each key in the us_currency directory
        
        while (change>=us_currency[x]): # adds current bill/coin to optimal_change_dir and removes from change   
            optimal_change_dir[x] +=+1 
            change -= us_currency [x]
            change =  round(change,4)
            if optimal_change_dir[x]!=0:# checks the position of last non-zero value in optimal_change_dir
                optimal_change_last_value = x
  
  
    optimal_change_str = f"The optimal change for an item that costs ${owed} with an amount paid of ${paid} is"
    i = 0
    for y in optimal_change_dir: # Add # of each bill in optimal_change_dir to the optimal_change_string
        
        if y == 'penny' and optimal_change_dir[y]!=0: # check for the pennies condition
            optimal_change_str += f"{', and'if y==optimal_change_last_value and i!=0 else ''}"
            optimal_change_str += f" {optimal_change_dir[y]} "
            optimal_change_str += f"{y if optimal_change_dir[y] == 1 else 'pennies'}"

        elif optimal_change_dir[y]!=0: # handle all other non zero bills/coins
            optimal_change_str += f"{''if i == 0 else ','}"
            optimal_change_str += f"{' and'if y==optimal_change_last_value and i!=0 else ''}"
            optimal_change_str += f" {optimal_change_dir[y]} {y}"
            optimal_change_str += f"{''if optimal_change_dir[y] == 1 else 's'}" 
            i+=1

    optimal_change_str+='.' # Add a period to the end of each output

    return optimal_change_str #returns the correct change as a string     

