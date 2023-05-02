def _deurlize_FEN(raw_urlized_fen: str) -> str:
    return raw_urlized_fen.replace("_", " ").replace("~", "/")

def _deurlize_board(raw_urlized_board: str) -> list[str]:
    return raw_urlized_board.split(",")