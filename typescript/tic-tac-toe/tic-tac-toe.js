class TicTacToe {
    constructor() {
        this.currentPlayer = "X"
        this.board = ["", "", "", "", "", "", "", "", ""];
    }

    whoIsCurrentPlayer() {
        return this.currentPlayer
    }

    getBoard() {
        return this.board 
    }

    playTurn(position) {
        if (!this.board[position]) {
            this.board[position] = this.currentPlayer
            this.currentPlayer = this.currentPlayer === "X" ? "O" : "X";
        }
    }

    isWinningRow(startOfRow) {
      return (this.board[startOfRow] === this.board[startOfRow + 1] && this.board[startOfRow] === this.board[startOfRow + 2] && this.board[startOfRow] != "");
    }

    isWinningColomn(startOfColumn) {
        return (this.board[startOfColumn] === this.board[startOfColumn + 3] && this.board[startOfColumn] === this.board[startOfColumn + 6] && this.board[0] != "")
    }

    isWinningLeftDiagonal() {
        return (this.board[0] === this.board[4] && this.board[0] === this.board[8] && this.board[0] != "")
    }

    isWinningRightDiagonal() {
        return (this.board[2] === this.board[4] && this.board[2] === this.board[6] && this.board[2] != "")
    }

    isDraw(){
        return (!this.board.includes(""))
    }

    getWinner() {
        for (const startOfRow of [0, 3, 6]){
          if (this.isWinningRow(startOfRow)) {
            return this.board[startOfRow];
          }
        }

        for (const startOfColumn of [0, 1, 2]){
            if (this.isWinningColomn(startOfColumn)) {
                return this.board[startOfColumn];
            }
        }

        if (this.isWinningLeftDiagonal() || this.isWinningRightDiagonal()){
            return this.board[4];
        }
        
        if (this.isDraw()){
            return "draw";
        }

        return "";
    }



}

module.exports = TicTacToe