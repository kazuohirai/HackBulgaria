String.prototype.capitalize = function() {
    return this.charAt(0).toUpperCase() + this.slice(1);
}

String.prototype.isBlank = function() {
    return (this.length === 0 || !this.trim());
}

String.prototype.words = function() {
    if (!this.isBlank()) {
        return this.replace(/\s{2,}/g, ' ').trim().split(' ');
    } else {
        return [];
    }
}



Array.prototype.head = function() {
    return this[0];
}

Array.prototype.last = function() {
    return this[this.length-1];
}

Array.prototype.tail = function() {
    return this.slice(1);
}

Array.prototype.range = function(start, end) {
    var result = [];
    for (var i = start; i <= end; i++) {
        result.push(i);
    }
    return result;
}

Array.prototype.sum = function() {
    var sum = 0;
    for (var i = 0; i < this.length; i++) {
        sum += this[i];
    }
    return sum;
}

Array.prototype.product = function() {
    var prod = 1;
    for (var i = 0; i < this.length; i++) {
        prod *= this[i];
    }
    return prod;
}

Array.prototype.compact = function() {
    var comp = [];
    for (var i = 0;i < this.length; i++) {
        if (this[i]) {
            comp.push(this[i]);
        }
    }
    return comp;
}

Array.prototype.take = function(elements) {
    if (elements > this.length) {
        return [];
    } else {
        return this.slice(0, elements)
    }
}

Array.prototype.drop = function(elements) {
    if (elements > this.length) {
        return [];
    } else {
        return this.slice(elements, this.last())
    }
}

Array.prototype.dedup = function() {
    var unique = [];
    for (var i = 0; i < this.length;i++){
        if (unique.indexOf(this[i]) === -1){
            unique.push(this[i]);
        }
    }
    return unique;
}

Array.prototype.sample = function() {
    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min)) + min;
    }
    return this[getRandomInt(0, this.length)];
}