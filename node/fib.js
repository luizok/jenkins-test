let fibNumber = 0;

let incrementFib = n => {

    fibNumber += n;

    return fibNumber;
}

module.exports = { incrementFib }