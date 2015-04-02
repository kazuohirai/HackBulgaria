function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}

function Panda(name, sex) {
    if (!(this instanceof Panda)) {
        return new Panda(name, sex);
    }
    if (['male', 'female'].indexOf(sex) === -1) {
        sex = 'female';
    }
    this.name = name;
    this.sex = sex;
    this.weight = 20;
}

Panda.prototype.toString = function () {
    return this.name + " is a " + this.sex + " panda which weighs " + this.weight + " kg.";
}

Panda.prototype.isMale = function () {
    return this.sex === 'male';
}

Panda.prototype.isFemale = function () {
    return this.sex === 'female';
}

Panda.prototype.eat = function (bamboo) {
    this.weight += bamboo / 2;
    var isLazy = this.weight >= 80;
    if (this.weight > 80 && !isLazy) {
        this.name = 'Lazy Panda ' + this.name;
    }
}

Panda.prototype.mate = function (anotherPanda) {
    if (this.sex === anotherPanda.sex) {
        throw new Error("CannotMatePandas");
    }
    fatherName = "";
    motherName = "";
    if (this.sex === 'male' && anotherPanda.sex === 'female') {
        fatherName = this.name;
        motherName = anotherPanda.name;
    } else if (this.sex === 'female' && anotherPanda.sex === 'male') {
        fatherName = anotherPanda.name;
        motherName = this.name;
    } else {
        //
    }
    babySex = ['female', 'male'][getRandomInt(0, 2)];
    babyName = {'female':motherName + " " + fatherName,
                'male': fatherName + " " + motherName}[babySex];
    return new Panda(babyName, babySex);
}
