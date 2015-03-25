wordlist = ['Harman Kardon', 'Grandmother', 'Manufacturing', 'Independent', 'Iron Maiden', 'Fedde Le Grand'];


function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function pickRandomWord(words) {
    return words[getRandomInt(0, words.length)].toUpperCase();
}

function checkInput(input) {
    if ((typeof input == 'string' || input instanceof String) && input.length === 1) {
        return true;
    }
    return false;
}

function checkOccurrence(letter, word) {
    var occurrences = [];
    for (var i = 0; i < word.length; i++) {
        if (word[i] === letter) {
            occurrences.push(i);
        }
    }
    return occurrences;
}

function checkMask(mask) {
    if (mask.indexOf('_') < 0) {
        return true;
    }
    return false;
}

function maskWord(word) {
    var mask = [];
    for (var i = 0; i < word.length; i++) {
        if (word[i] === ' ') {
            mask.push(' ');
        } else {
            mask.push('_');
        }
    }
    return mask;
}

function displayWord (word) {
    console.log(word.join('|'));
}

function updateMask (masked_word, occurrences, letter) {
    for (var i = 0; i < occurrences.length; i++) {
        masked_word[occurrences[i]] = letter;
    }
}


var answer = pickRandomWord(wordlist);
var mask = maskWord(answer)

function game(guess) {
    console.log(answer);
    displayWord(mask);
    var user_guess = require('prompt');
    user_guess.start();
    var guess = ""
    user_guess.get(['Guess'], function (err, result) {
        guess = result.Guess.toUpperCase();
        if (checkInput(guess)) {
            var places = checkOccurrence(guess, answer);
            console.log(places);
            updateMask(mask, places, guess);
            if (checkMask(mask)) {
                console.log("You guessed the word. It is '" + answer + "'");
            } else {
                game(guess);
            }
        } else {
            game(guess);
        }
    });
}

game(answer);