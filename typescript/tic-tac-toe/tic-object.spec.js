
const { TicTacToe, Players, Positions } = require('./tic-object');


describe("tic tac toe game with added calisthenics", () => {
    let ticTacToe;

    beforeEach(() => {
        ticTacToe = new TicTacToe();
    });

    it("First player should be X", () => {
        const currentPlayer = ticTacToe.getCurrentPlayer();
        expect(currentPlayer).toEqual(Players.X);
    });

    it("After X has played the next player is O", () => {
        ticTacToe.playTurn(Positions.TopLeft);
        const currentPlayer = ticTacToe.getCurrentPlayer();
        expect(currentPlayer).toEqual(Players.O);
    });

    it("After O has played the next player is X", () => {
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.TopCenter);
        const currentPlayer = ticTacToe.getCurrentPlayer();
        expect(currentPlayer).toEqual(Players.X);
    });

    it("X plays Top left corner and it is in the board", () => {
        ticTacToe.playTurn(Positions.TopLeft);

        expect(ticTacToe.getBoard()).toEqual("X,,,,,,,,")
    });

    it("O plays Top Center corner and it is in the board", () => {
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.TopCenter);

        expect(ticTacToe.getBoard()).toEqual("X,O,,,,,,,")
    });

    it("X plays Top left corner and O is prevented playing Top left", () => {
        ticTacToe.playTurn(Positions.TopLeft);

        ticTacToe.playTurn(Positions.TopLeft);

        expect(ticTacToe.getBoard()).toEqual("X,,,,,,,,");
        expect(ticTacToe.getCurrentPlayer()).toEqual(Players.O);
    });

    it("Top Row horizonal win for player X", () => {
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.MiddleLeft);
        ticTacToe.playTurn(Positions.TopCenter);
        ticTacToe.playTurn(Positions.MiddleCenter);
        ticTacToe.playTurn(Positions.TopRight);

        expect(ticTacToe.checkForWinner()).toEqual(Players.X);
    });

    it("Top Row horizonal win for player O", () => {
        ticTacToe.playTurn(Positions.BottomRight);
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.MiddleLeft);
        ticTacToe.playTurn(Positions.TopCenter);
        ticTacToe.playTurn(Positions.MiddleCenter);
        ticTacToe.playTurn(Positions.TopRight);

        expect(ticTacToe.checkForWinner()).toEqual(Players.O);
    });

    it("Middle Row horizonal win for player X", () => {
        ticTacToe.playTurn(Positions.MiddleLeft);
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.MiddleCenter);
        ticTacToe.playTurn(Positions.TopCenter);
        ticTacToe.playTurn(Positions.MiddleRight);

        expect(ticTacToe.checkForWinner()).toEqual(Players.X);
    });

    it("Middle Row horizonal win for player O", () => {
        ticTacToe.playTurn(Positions.BottomRight);
        ticTacToe.playTurn(Positions.MiddleLeft);
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.MiddleCenter);
        ticTacToe.playTurn(Positions.TopCenter);
        ticTacToe.playTurn(Positions.MiddleRight);

        expect(ticTacToe.checkForWinner()).toEqual(Players.O);
    });

    it("After X has played once then there is no winner", () => {
        ticTacToe.playTurn(Positions.TopLeft);
        const currentPlayer = ticTacToe.getCurrentPlayer();
        expect(ticTacToe.checkForWinner()).toEqual(Players.None);
    });

    it("Bottom Row horizonal win for player X", () => {
        ticTacToe.playTurn(Positions.BottomLeft);
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.BottomCenter);
        ticTacToe.playTurn(Positions.TopCenter);
        ticTacToe.playTurn(Positions.BottomRight);

        expect(ticTacToe.checkForWinner()).toEqual(Players.X);
    });

    it("left vertical win for player x", () => {
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.TopCenter);
        ticTacToe.playTurn(Positions.MiddleLeft);
        ticTacToe.playTurn(Positions.MiddleCenter);
        ticTacToe.playTurn(Positions.BottomLeft);

        expect(ticTacToe.checkForWinner()).toEqual(Players.X);
    });

    it("center vertial win for player x", () => {
        ticTacToe.playTurn(Positions.TopCenter);
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.MiddleCenter);
        ticTacToe.playTurn(Positions.MiddleLeft);
        ticTacToe.playTurn(Positions.BottomCenter);

        expect(ticTacToe.checkForWinner()).toEqual(Players.X);
    });

    it("right vertial win for player x", () => {
        ticTacToe.playTurn(Positions.TopRight);
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.MiddleRight);
        ticTacToe.playTurn(Positions.MiddleLeft);
        ticTacToe.playTurn(Positions.BottomRight);

        expect(ticTacToe.checkForWinner()).toEqual(Players.X);
    });

    it("left diagonal win for player x", () => {
        ticTacToe.playTurn(Positions.TopLeft);
        ticTacToe.playTurn(Positions.MiddleRight);
        ticTacToe.playTurn(Positions.MiddleCenter);
        ticTacToe.playTurn(Positions.MiddleLeft);
        ticTacToe.playTurn(Positions.BottomRight);

        expect(ticTacToe.checkForWinner()).toEqual(Players.X);
    });

    it("right diagonal win for player x", () => {
        ticTacToe.playTurn(Positions.TopRight);
        ticTacToe.playTurn(Positions.MiddleRight);
        ticTacToe.playTurn(Positions.MiddleCenter);
        ticTacToe.playTurn(Positions.MiddleLeft);
        ticTacToe.playTurn(Positions.BottomLeft);

        expect(ticTacToe.checkForWinner()).toEqual(Players.X);
    });
});