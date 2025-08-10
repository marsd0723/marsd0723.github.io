from flask import Flask, request
import v1_52

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! This is a GET request response."

@app.route('/reset')
def reset():
    v1_52.board_ = [row[:] for row in v1_52.board0]
    v1_52.count = 0
    return "reset successfully"

@app.route('/connect4get')
def connect4get():
    move = int(request.args.get('move', '')) # Get 'name' query parameter, default to 'Guest'
    v1_52.drop(v1_52.board_, move, 1)
    v1_52.printBoard(v1_52.board_)

    v1_52.count += 2
    r, st = v1_52.aiPlayer(v1_52.board_, 8, 2)
    print(r, st)
    status = "-99" if v1_52.isWin(v1_52.board_, 1) else\
    "-101" if v1_52.isWin(v1_52.board_, 2) else\
    "-100" if v1_52.isDraw(v1_52.board_) else "0"

    return (r+','+status+","+st) 


if __name__ == '__main__':
    app.run(debug=True, port=5100)

