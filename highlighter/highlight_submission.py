from deurlizer import _deurlize_board


def highlight_submission(subm: list[str], ans: list[str]) -> list[str]:
    """
    Inputs: ["", "", "", "P", "R", ... etc] and ["", "", "R", "P", "k", ... etc]
    Outputs: ["", "", "", "square-highlight-gre", "square-highlight-yel", ... etc]
    """

    piece_frequencies = {
        "P": 0, "N": 0, "B": 0, "R": 0, "Q": 0, "K": 0,
        "p": 0, "n": 0, "b": 0, "r": 0, "q": 0, "k": 0,
    }
    
    
    # Note: a square/highlighted_grid[i] will be subscripted with [-1]
    # because sometimes they take on values like "square-highlight-gre K" and "square-highlight-yel p"
    
    hinted_indicies = set()
    for square in ans:
        if not square == "":
            piece_frequencies[square[-1]] += 1
            
    for i in range(len(subm)):
        if subm[i][0:20] == "square-highlight-blu": hinted_indicies.add(i)
    
    highlighted_grid = ["" for i in range(len(subm))]

    for i in range(len(subm)):
        if i in hinted_indicies:
            highlighted_grid[i] = "square-highlight-blu " + subm[i][-1]
            piece_frequencies[subm[i][-1]] -= 1
        elif subm[i] != "" and subm[i][-1] == ans[i]: # Correct place
            highlighted_grid[i] = "square-highlight-gre " + subm[i][-1]
            piece_frequencies[subm[i][-1]] -= 1
    for i in range(len(subm)):
        if subm[i] != "" and not(subm[i][-1] == ans[i]):
            if piece_frequencies[subm[i][-1]] > 0: # Piece exists elsewhere but is not in correct place
                highlighted_grid[i] = "square-highlight-yel " + subm[i][-1]
                piece_frequencies[subm[i][-1]] -= 1
            else: # Piece does not exist elsewhere in the answer
                highlighted_grid[i] = "square-highlight-gra " + subm[i][-1]
        
    return highlighted_grid