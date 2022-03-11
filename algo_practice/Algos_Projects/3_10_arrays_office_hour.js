// Given a positive integer representing a number of American cents, return an object of the most efficent way to create change
// 90
//{
    // "quarters":3,
    // "dimes": 1,
    // "nickels": 1,
//}

//1 Get Quarters
//1a Modulus 25 as var remainder
//1b Subtract remainder from change
//1c Divide change / 25 = var num_of_quarters
//2 Get Dimes
//2a Modulus 10 as var remainder
//2b Subtract remainder from change
//2c Divide change / 10 = var num_of_dimes
//3 Get Nickels
//3a Modulus 05 as var remainder
//3b Subtract remainder from change
//3c Divide change / 05 = var num_of_nickets
//4 Get Pennies
//4a var num_of_pennies = remainder
//5 Populate object


function get_change(change){    //90
    var modulus_change = change%25  // remainder_change = 15
    var num_of_quarters = (change-modulus_change)/25  
    remainder_change = modulus_change%10
    var num_of_dimes = (modulus_change-remainder_change)/10
    modulus_change = remainder_change%5
    var num_of_nickels = (remainder_change-modulus_change)/5
    var num_of_pennies = modulus_change
    var coins = {
        'quarters': num_of_quarters,
        'dimes' : num_of_dimes,
        'nickels' : num_of_nickels,
        'pennies' : num_of_pennies
    }
    return coins
}
console.log(get_change(90))
console.log(get_change(94))
console.log(get_change(20))
