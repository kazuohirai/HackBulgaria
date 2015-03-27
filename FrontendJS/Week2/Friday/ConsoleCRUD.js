var people = [
    {
        'ID': '001',
        'Name': 'John',
        'Email': 'appleseed@apple.com'
    },
    {
        'ID': '002',
        'Name': 'Steven',
        'Email': 'jobs@apple.com'
    },
    {
        'ID': '003',
        'Name': 'Steve',
        'Email': 'woz@apple.com'
    }];


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
                addObject({'ID': result.ID,
                     'Name': result.Name,
                     'Email': result.email},people);
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
// update по ID
// load & save \JSONFILE\  WITH readfile/ writefile SYNC
// search keyword
