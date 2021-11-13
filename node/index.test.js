const index = require('./fib');

test('First fibonacci is 1', () => {
    expect(index.incrementFib(1)).toBe(1);
});

test('Second fibonacci is 2', () => {
    expect(index.incrementFib(1)).toBe(2);
});