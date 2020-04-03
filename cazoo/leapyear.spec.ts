/* 
Write a function that returns true or false depending on whether its input integer is a leap year or not.

A leap year is defined as one that is divisible by 4, but is not otherwise divisible by 100 unless it is 
also divisible by 400.

For example:

2001 is a typical common year

1996 is a typical leap year

1900 is an atypical common year

2000 is an atypical leap year.
*/

const isTypicalLeapYear = (year) => {
    return year % 4 === 0;
}
const isAtypicalLeapYear = (year) => {
    return year % 400 === 0;
}

const isAtypicalCommonYear = (year) => {
    return year % 100 === 0;
}

const isLeapYear = (year) => {
    if(isAtypicalLeapYear(year)) return true
    if(isAtypicalCommonYear(year)) return false;
    if(isTypicalLeapYear(year)) return true;
    return false;
}

describe("Leapyear", () => {
    describe("typical common years", () => {
        it("should return false when year is 2001", () => {
            expect(isLeapYear(2001)).toBe(false);
        });
        it("should return false when year is 1999", () => {
            expect(isLeapYear(1999)).toBe(false);
        });
    })

    describe("atypical common year", () => {
        it("should return false when year is 1900", () =>{
            expect(isLeapYear(1900)).toBe(false);
        })
        it("should return false when year is 1700", () =>{
            expect(isLeapYear(1700)).toBe(false);
        })

        it("should return false when year is 1500", () => {
            expect(isLeapYear(1500)).toBe(false);
        });
    })

    describe("typical leap year", () => {
        it("should return true when year is 1996", () => {
            expect(isLeapYear(1996)).toBe(true);
        })
        it("should return true when year is 1992", () => {
            expect(isLeapYear(1992)).toBe(true);
        })
        it("should return true when year is 1988", () => {
            expect(isLeapYear(1988)).toBe(true);
        })
    })

    describe("atypical leap year", () => {
        it("should return true when year is 2000", () => {
            expect(isLeapYear(2000)).toBe(true);
        })

        it("should return true when year is 1600", () => {
            expect(isLeapYear(1600)).toBe(true);
        })

        it("should return true when year is 2400", () => {
            expect(isLeapYear(2400)).toBe(true);
        })
    })

});