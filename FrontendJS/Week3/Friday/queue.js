var Queue = function() {
        var items = [];
        return {'push': function(obj){
                console.log(items);
                items.push(obj);
            }, 'pop': function(){
                items.shift();
                console.log(items);
            }, 'isEmpty': function() {
                if (items.length === 0) {
                    return true;
                } else {
                    return false;
                }
            }
        }
    }
