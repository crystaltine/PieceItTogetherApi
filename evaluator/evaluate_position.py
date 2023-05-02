from stockfish import Stockfish

stockfish = Stockfish(path="C:/Stockfish/stockfish-windows-2022-x86-64-avx2.exe")
def get_eval(fen: str) -> int:
    stockfish.set_fen_position(fen)
    stockfish._go_time(1000)

    evaluation = stockfish.get_evaluation()
    
    if evaluation['type'] == 'cp':
        # regular eval
        return evaluation['value']/100
    # mate
    return 10000 + evaluation['value'] if evaluation['value'] > 0 else -10000 + evaluation['value']