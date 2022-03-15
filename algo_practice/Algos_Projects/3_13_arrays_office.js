//create a function accepts two parameters word & guess
//turn each paramter into a list and and store it in variable 
//create empty list
// iterate through guess
// nested for loop iterates word
// green check if guess[i] == word [j] append "green" to list
// yellow check if guess[i] in word append "yellow" to list
// append grey to list. 

function wordle(guess, word){
    guess = guess.split("")
    word = word.split("")
    console.log(word)
    console.log(guess)
    var answer=[]
    
    for(var i = 0; i<guess.length; i++){
        green_check = 0
        yellow_check = 0
        var color = "Grey"
        for(var j = 0; j<word.length; j++){
            if(guess[i] == word[j] && i==j){
                color = "Green"
                green_check = 1
            } 
        }
        if(word.includes(guess[i]) && green_check == 0){
            answer.push('Yellow')
            yellow_check = 1
        }
        answer.push(color)
    
    
    }
    console.log(answer)
}

wordle("cours","crack")