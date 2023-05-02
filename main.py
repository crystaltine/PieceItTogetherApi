from flask import *
import json
from flask_cors import CORS, cross_origin
from math import sqrt
from deurlizer import _deurlize_FEN, _deurlize_board

from evaluator.evaluate_position import get_eval
from generator.generate_position import generate_random_pos
from generator.fetch_random_position import get_random_puzzle_fen
from highlighter.highlight_submission import highlight_submission

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/geteval/<urlizedfen>', methods=['GET'])
def fetch_eval(urlizedfen: str):
    
    fenstr = _deurlize_FEN(urlizedfen)
    
    # print("geteval rq received w/fenstr=" + fenstr)
    evaluation = get_eval(fenstr)
    json_dump = json.dumps({'evaluation': evaluation})
    
    return json_dump

@app.route('/getrandompos', methods=['GET'])
def fetch_random_puzzle_and_eval():
    
    fenstr = get_random_puzzle_fen()
    
    # print("random puzzle rq received; fenstr=" + fenstr)
    evaluation = get_eval(fenstr)
    json_dump = json.dumps({'evaluation': evaluation, 'fen': fenstr})
    
    return json_dump

@app.route('/highlightsubm/<subm>/<ans>', methods=['GET'])
def highlight(subm: str, ans: str):
    highlighted_grid = highlight_submission(_deurlize_board(subm), _deurlize_board(ans))
    
    # print("highlight rq received w/subm=" + subm + " and ans=" + ans)
    json_dump = json.dumps({'highlighted': highlighted_grid})
    
    return json_dump

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)