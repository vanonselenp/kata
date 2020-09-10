const TicTacToe = require("./tic-tac-toe");

describe("Tic Tac Toe", () => {
    
    it("X goes first when the game starts", () => {
        const ticTacToe = new TicTacToe();
        expect(ticTacToe.whoIsCurrentPlayer()).toBe("X");
    });

    it("O plays after X starts the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        expect(ticTacToe.whoIsCurrentPlayer()).toBe("O");
    });

    it("X plays after O makes their turn", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(1);
        expect(ticTacToe.whoIsCurrentPlayer()).toBe("X");
    });

    it("should place an X on board when X plays turn", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        expect(ticTacToe.getBoard()).toEqual(["X", "", "", "", "", "", "", "", ""])
    });

    it("should place an O on board when O plays turn", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(1);
        expect(ticTacToe.getBoard()).toEqual(["X", "O", "", "", "", "", "", "", ""])
    });

    it("player should not be able to play on an already played position", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(0);
        expect(ticTacToe.getBoard()).toEqual(["X", "", "", "", "", "", "", "", ""])
    });

    it("when board is ['X', 'X', 'X', 'O', 'O', '', '', '', ''] then X wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(3);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(4);
        ticTacToe.playTurn(2);
        expect(ticTacToe.getWinner()).toEqual('X')
    });

    it("when board is ['O', 'O', 'O', 'X', 'X', '', 'X', '', ''] then O wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(3);
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(4);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(7);
        ticTacToe.playTurn(2);
        expect(ticTacToe.getWinner()).toEqual('O')
    });

    it("when board is ['O', 'O', '', 'X', 'X', 'X', '', '', ''] then X wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(3);
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(4);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(5);
        expect(ticTacToe.getWinner()).toEqual('X')
    });

    it("when board is ['O', 'O', '', '', '', '', 'X', 'X', 'X'] then X wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(6);
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(7);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(8);
        expect(ticTacToe.getWinner()).toEqual('X')
    });

    it("when board is empty then there is no winner", () => {
        const ticTacToe = new TicTacToe();

        expect(ticTacToe.getWinner()).toEqual('');
    });

    it("when board is ['X', 'O', 'X', '', '', '', '', '', ''] then no one wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(2);
        expect(ticTacToe.getWinner()).toEqual('')
    });

    it("when board is ['X', 'O', 'O', 'X', '', '', 'X', '', ''] then X wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(3);
        ticTacToe.playTurn(2);
        ticTacToe.playTurn(23);
        expect(ticTacToe.getWinner()).toEqual('X');
    });

    it("when board is ['X', 'O', 'X', 'X', 'O', '', '', 'O', ''] then X wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(2);
        ticTacToe.playTurn(4);
        ticTacToe.playTurn(3);
        ticTacToe.playTurn(7);

        expect(ticTacToe.getWinner()).toEqual('O');
    });

    it("when board is ['O', 'O', 'X', '', '', 'X', '', '', 'X'] then X wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(2);
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(5);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(8);

        expect(ticTacToe.getWinner()).toEqual('X');
    });

    it("when board is ['X', 'O', '', '', 'X', 'O', '', '', 'X'] then X wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(4);
        ticTacToe.playTurn(5);
        ticTacToe.playTurn(8);

        expect(ticTacToe.getWinner()).toEqual('X');
    });

    it("when board is ['', 'O', 'X', '', 'X', 'O', 'X', '', ''] then X wins the game", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(2);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(4);
        ticTacToe.playTurn(5);
        ticTacToe.playTurn(6);

        expect(ticTacToe.getWinner()).toEqual('X');
    });

    it("when board is ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O'] then it's a draw", () => {
        const ticTacToe = new TicTacToe();
        ticTacToe.playTurn(0);
        ticTacToe.playTurn(1);
        ticTacToe.playTurn(2);
        ticTacToe.playTurn(4);
        ticTacToe.playTurn(3);
        ticTacToe.playTurn(6);
        ticTacToe.playTurn(5);
        ticTacToe.playTurn(8);
        ticTacToe.playTurn(7);

        expect(ticTacToe.getWinner()).toEqual('draw');
    });

});