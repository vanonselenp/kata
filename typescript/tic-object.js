const Players = {
    X: 'X',
    O: 'O',
    None: ""
}

const Positions = {
    TopLeft: 0,
    TopCenter: 1,
    TopRight: 2,
    MiddleLeft: 3,
    MiddleCenter: 4,
    MiddleRight: 5,
    BottomLeft: 6,
    BottomCenter: 7,
    BottomRight: 8,
}

const WinningConditions = {
    TopRow: [Positions.TopLeft, Positions.TopCenter, Positions.TopRight],
    MiddleRow: [Positions.MiddleLeft, Positions.MiddleCenter, Positions.MiddleRight],
    BottomRow: [Positions.BottomLeft, Positions.BottomCenter, Positions.BottomRight]
}

class TicTacToe {
    constructor(){
        this.currentPlayer = Players.X;
        this.board = new Board();
    } 

    getCurrentPlayer() {
        return this.currentPlayer;
    }

    getBoard() {
        return this.board.toString();
    }

    switchPlayer() {
        if ( this.currentPlayer === Players.X) {
            this.currentPlayer = Players.O;
            return;
        }
        
        this.currentPlayer = Players.X;
    }

    checkForWinner() {
        return this.board.checkForWinner();
    }

    playTurn(position) {
        if(this.board.positionIsAvailable(position)) {
            this.board.setPosition(position,this.currentPlayer);
            this.switchPlayer();
        }
    }
}

class DetermineWinner{
    constructor() {
        this.winningConditions = [
            WinningConditions.TopRow,
            WinningConditions.MiddleRow,
            WinningConditions.BottomRow
        ];
    }

    getWinner(board){
        for (const rule of this.winningConditions) {
            if(board.areSame(rule) && board.playerAt(rule[0]) != Players.None) {
                return board.playerAt(rule[0]);
            }
        }
        return Players.None;
    }
}

class Board {
    constructor () {
        this.board = ["", "", "", "", "", "", "", "", ""];
        this.winningConditions = new DetermineWinner();
    }

    areSame(rule) {
        if (this.board[rule[0]] === this.board[rule[1]] &&
            this.board[rule[0]] === this.board[rule[2]])
            return true;
        return false;
    }

    playerAt (postion) {
        return this.board[postion];
    }

    toString() {
        return this.board.toString();
    }

    setPosition(position, currentPlayer) {
        this.board[position] = currentPlayer;
    }

    positionIsAvailable(position) {
        return (this.board[position] === '')
    }

    checkForWinner() {
        return this.winningConditions.getWinner(this);
    }
}

module.exports = { TicTacToe, Players, Positions }
