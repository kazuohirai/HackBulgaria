function checkInput (number) {
    trash = number.toString();
    if (trash.length != 4) {
        return false;
    }

    if(isNaN(parseInt(number))) { 
        return false;
    }

    for (var i = 0; i <= trash.length; i++) {
        for (var j = i+1; j < trash.length; j++) {
            if (trash[j] === trash[i]) {
                return false;
            }
        }
    }
    return true;
}


function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}


function getRandFourDigit() {
    generated = "";
    while (generated.length < 4) {
        var randInt = getRandomInt(1, 9).toString();
        if (generated.indexOf(randInt) >= 0) {
            continue;
        } else {
            generated += randInt;
        }
    }
    return generated;
} 


function checkBulls(guess, actual) {
    guessStr = guess.toString();
    actualStr = actual.toString();
    var bulls = 0;
    for (var i = 0; i < guessStr.length; i++) {
        if (guessStr[i] === actualStr[i]) {
            bulls++;
        }
    }
    return bulls;
}


function checkCows(guess, actual) {
    guessStr = guess.toString();
    actualStr = actual.toString();
    var cows = 0;
    for (var i = 0; i < actualStr.length; i++) {
        for (var j = 0; j < guessStr.length; j++) {
            if (actualStr[i] === guessStr[j]) {
                cows++;
            }
        }
    }
    return cows;
}


function checkNumber(guess, actual) {
    var bulls = checkBulls(guess, actual);
    var cows = checkCows(guess, actual) - bulls;
    if (cows < 0) {
        cows = 0;
    }
    console.log('Cows: ' + cows + '  Bulls: ' + bulls);
}


var answer = getRandFourDigit();
console.log(answer);

function game(guess) {
    var user_guess = require('prompt');
    user_guess.start();
    var guess = ""
    user_guess.get(['Guess'], function (err, result) {
        guess = result.Guess;
        if (checkInput(guess)) {
            if (guess === answer) {
                console.log('Congratulations');
            } else {
                checkNumber(guess, answer);
                game(guess);
            }
        } else {
            game(guess);
        }
    });
}


game(answer);