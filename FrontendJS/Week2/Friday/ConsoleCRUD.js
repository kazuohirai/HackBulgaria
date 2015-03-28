var people = [];


function display (people) {
    for (var person in people) {
        console.log(people[person]);
    }
}


function addObject (object, people) {
    people.push(object);
}

function checkID (id, people) {
    var hasValue = false;
    for (var index in people) {
        if (people[index]['ID'] === id) {
            hasValue = people[index];
        }
    }
    return hasValue;
}


function getByID (id, people) {
    var get = checkID(id, people);
    if (get !== false) {
        console.log(get);
    } else {
        console.log('No such ID found.');
    }
}


function removeID (id, people) {
    var del = checkID(id, people);
    if (del !== false) {
        people.splice(people.indexOf(del), 1)
    } else {
        console.log('No such ID found.'); 
    }
}


function updateField (id, people, key, value) {
    var upd = checkID(id, people);
    if (upd !== false) {
        var ind = people.indexOf(upd);
        people[ind][key] = value;
    } else {
        console.log('No such ID found.'); 
    }
}


function saveToJSON (data, filename) {
    var jf = require('jsonfile')
    jf.writeFileSync(filename, data)
}


function loadFromJSON (filename) {
    var jf = require('jsonfile')
    var util = require('util')
    return jf.readFileSync(filename);
}

function keywordSearch (keyword) {
    display = false;
    for (var person in people) {
        for (var item in people[person]) {
            if (people[person][item].indexOf(keyword) !== -1 ){
                display = true;
            }
        }
        if (display === true) {
            console.log(people[person]);
        }
        display = false;
    }
} 


function menu () {
    var command = require('prompt');
    command.start();
    command.get(['command'], function (err, result) {
        var user_command = result.command;
    switch(user_command) {
        case 'list':
            display(people);
            menu();
            break;
        case 'add':
            var add = require('prompt');
            add.start();
            add.get(['ID', 'Name', 'Email'], function (err, result) {
                addObject({"ID": result.ID,
                     "Name": result.Name,
                     "Email": result.Email},people);
                console.log('Information successfully added.');
                menu()
            });
            break;
        case 'get':
            var id = require('prompt');
            id.start();
            id.get(['ID'], function (err, result) {
                getByID(result.ID, people);
                menu();
            });
            break;
        case 'remove':
            var id = require('prompt');
            id.start();
            id.get(['ID'], function (err, result) {
                removeID(result.ID, people);
                menu();
            });
            break;
        case 'update':
            var id = require('prompt');
            id.start();
            id.get(['ID'], function (err, result) {
                var update = require('prompt');
                update.start();
                update.get(['Key', 'Value'], function (err, res) {
                    updateField(result.ID, people, res.Key, res.Value);
                    menu();
                });
            });
            break;
        case 'save':
            var filename = require('prompt');
            filename.start();
            filename.get(['file'], function (err, result) {
                saveToJSON(people, result.file);
                people = [];    
                menu();
            });
            break;
        case 'load':
            var filename = require('prompt');
            filename.start();
            filename.get(['file'], function (err, result) {
                contents = loadFromJSON(result.file);
                people = contents
                menu();
            });
            break;
        case 'search':
            var searchword = require('prompt');
            searchword.start();
            searchword.get(['keyword'], function (err, result) {
                keywordSearch(result.keyword);
                menu();
            });
            break;
        case 'quit':
            console.log('Goodbye!')
            break;
        default:
            console.log('Please enter valid command!');
            menu();
    } 
  });
}

menu();
