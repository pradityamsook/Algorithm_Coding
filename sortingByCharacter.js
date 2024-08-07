
var objs = [
    {
        first_nom: '5.1.Laszlo', last_nom: [{ first_nom: '5.1.Laszlo', last_nom: 'Jamf' },
        { first_nom: '5.3Pig', last_nom: 'Bodine' },
        { first_nom: 'Pirate', last_nom: 'Prentice' },
        { first_nom: '5.2 Pirate', last_nom: 'Prentice' },
        { first_nom: 'สัญญาจ้าง', last_nom: 'Prentice' }]
    },
    {
        first_nom: '5.3Pig', last_nom: [{ first_nom: '5.1.Laszlo', last_nom: 'Jamf' },
        { first_nom: '5.3Pig', last_nom: 'Bodine' },
        { first_nom: 'Pirate', last_nom: 'Prentice' },
        { first_nom: '5.2 Pirate', last_nom: 'Prentice' },
        { first_nom: 'สัญญาจ้าง', last_nom: 'Prentice' }]
    },
    {
        first_nom: 'Pirate', last_nom: [{ first_nom: '5.1.Laszlo', last_nom: 'Jamf' },
        { first_nom: '5.3Pig', last_nom: 'Bodine' },
        { first_nom: 'Pirate', last_nom: 'Prentice' },
        { first_nom: '5.2 Pirate', last_nom: 'Prentice' },
        { first_nom: 'สัญญาจ้าง', last_nom: 'Prentice' }]
    },
    {
        first_nom: '5.2 Pirate', last_nom: [{ first_nom: '5.1.Laszlo', last_nom: 'Jamf' },
        { first_nom: '5.3Pig', last_nom: 'Bodine' },
        { first_nom: 'Pirate', last_nom: 'Prentice' },
        { first_nom: '5.2 Pirate', last_nom: 'Prentice' },
        { first_nom: 'สัญญาจ้าง', last_nom: 'Prentice' }]
    },
    {
        first_nom: 'สัญญาจ้าง', last_nom: [{ first_nom: '5.1.Laszlo', last_nom: 'Jamf' },
        { first_nom: '5.3Pig', last_nom: 'Bodine' },
        { first_nom: 'Pirate', last_nom: 'Prentice' },
        { first_nom: '5.2 Pirate', last_nom: 'Prentice' },
        { first_nom: 'สัญญาจ้าง', last_nom: 'Prentice' }]
    }
];

let main = {
    a: 20,
    objs: objs
}

function compare(a, b) {
    if (a.first_nom < b.first_nom) {
        return -1;
    }
    if (a.first_nom > b.first_nom) {
        return 1;
    }
    return 0;
}
main.objs.forEach((value) => {
    return value.last_nom.sort(compare)
})

console.log(JSON.stringify(main, null, 1));
