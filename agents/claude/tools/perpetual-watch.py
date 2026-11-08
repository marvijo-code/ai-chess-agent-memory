import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
me = board.turn
V = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9}


def mat(c):
    return sum(v * len(board.pieces(t, c)) for t, v in V.items())


diff = mat(me) - mat(not me)
opp_heavy = len(board.pieces(chess.QUEEN, not me)) + len(board.pieces(chess.ROOK, not me))


def nchecks(bd):
    return sum(1 for m in bd.legal_moves if bd.gives_check(m))


safe = []
risky = []
for mv in list(board.legal_moves):
    san = board.san(mv)
    board.push(mv)
    if board.is_checkmate():
        board.pop()
        print("Mate in 1: " + mv.uci())
        continue
    n = nchecks(board)
    board.pop()
    if n == 0:
        safe.append(mv.uci())
    else:
        risky.append((n, mv.uci()))

if diff >= 2 and opp_heavy:
    print("UP %d: perpetual risk. Moves leaving him NO check: %s" % (diff, " ".join(safe[:12]) or "none"))
    print("Before any mate-threat move list his queen checks and my K flights; shelter first (g6/Kg7, queen back), trade queens.")
else:
    print("Material diff %d (me minus him); no perpetual watch needed." % diff)
    if safe:
        print("Moves leaving him no check: " + " ".join(safe[:8]))
