/* 
Write a function that takes numbers from 1 to 100 and outputs them as a
string, but for multiples of three returns Fizz instead of the number and for
the multiples of five returns Buzz. For numbers which are multiples of both
three and five returns FizzBuzz. 
*/

const isDivisibleBy3 = (num) => {
    return num % 3 === 0
}

const isDivisibleBy5 = (num) => {
    return num % 5 === 0
}

const isNotAValidInput = (num) => {
    return num > 100 || num < 1
}

const fizzBuzz = (num) => {
    if(isNotAValidInput(num)) return 'Panic!!'
    let result = '';
    if (isDivisibleBy3(num)) result += "Fizz";
    if (isDivisibleBy5(num)) result += "Buzz";
    
    return result ? result : `${num}`;
}


describe("FizzBuzz", () => {
    describe("for multiples of 3", () => {
        it("should return Fizz when given 3", () => {
            expect(fizzBuzz(3)).toEqual("Fizz");
        });
    
        it("should return Fizz when given 6", () => {
            expect(fizzBuzz(6)).toEqual("Fizz");
        });
    
        it("should return Fizz when given 9", () => {
            expect(fizzBuzz(9)).toEqual("Fizz");
        });
    });

    describe("for multiples of 5", () => {
        it("should return Buzz when given 5", () => {
            expect(fizzBuzz(5)).toEqual("Buzz");
        });

        it("should return Buzz when given 10", () => {
            expect(fizzBuzz(10)).toEqual("Buzz");
        });
    });

    describe("for multiples of 3 and 5", () => {
        it("should return FizzBuzz when given 15", () => {
            expect(fizzBuzz(15)).toEqual("FizzBuzz");
        });

        it("should return FizzBuzz when given 30", () => {
            expect(fizzBuzz(30)).toEqual("FizzBuzz");
        });
    });

    describe("for numbers outside of 1 and 100", () => {
        it('should return Panic!! when given 101', () => {
            expect(fizzBuzz(101)).toEqual("Panic!!");
        });
        it('should return Panic!! when given 0', () => {
            expect(fizzBuzz(0)).toEqual("Panic!!");
        });
        it('should return Panic!! when given -1', () => {
            expect(fizzBuzz(-1)).toEqual("Panic!!");
        });
    });
    
    describe("for other numbers", () => {
        it("should return a string of 1 when given 1", () => {
            expect(fizzBuzz(1)).toEqual("1");
        });
    
        it("should return a string of 2 when given 2", () => {
            expect(fizzBuzz(2)).toEqual("2");
        });
    
        it("should return a string of 4 when given 4", () => {
            expect(fizzBuzz(4)).toEqual("4");
        });    
    });

});