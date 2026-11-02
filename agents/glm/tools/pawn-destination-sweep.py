import json, sys, chess

p = json.load(sys.stdin)
b = chess.Board(p["fen"])
me = chess.WHITE if p["side_to_move"] == "white" else chess.BLACK
if me != b.turn:
    me = b.turn

NOTE = {chess.PAWN: "pawn", chess.KNIGHT: "knight", chess.BISHOP: "bishop",
        chess.ROOK: "rook", chess.QUEEN: "queen"}
VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9}


def has_real_defense(board, sq, color):
    for s in board.attackers(color, sq):
        pc = board.piece_at(s)
        if pc and pc.piece_type != chess.KING:
            return True
    return False

if b.is_check():
    print("IN CHECK - read the see-sweep reply list instead; this sweep is noise in check")
    sys.exit()

# my mini-pieces already attacked before my move: skip them (avoid flooding lost games)
pre = set()
for sq in chess.SQUARES:
    pc = b.piece_at(sq)
    if pc and pc.color == me and pc.piece_type != chess.KING:
        if b.attackers(not me, sq):
            pre.add(sq)

avoids = []
notes = []
for move in list(b.legal_moves):
    uci = move.uci()
    try:
        san = b.san(move)
    except Exception:
        san = uci
    b.push(move)
    worst = 0
    worst_txt = None
    for sq in chess.SQUARES:
        if sq in pre:
            continue
        pc = b.piece_at(sq)
        if not pc or pc.color != me or pc.piece_type == chess.KING:
            continue
        kinds = set()
        s_items = [b.piece_at(s) for s in b.attackers(not me, sq) if b.piece_at(s)]
        for it in s_items:
            kinds.add(it.piece_type)
        if chess.PAWN not in kinds and chess.KNIGHT not in kinds:
            continue
        if not has_real_defense(b, sq, me):
            v = VAL[pc.piece_type]
            if v > worst:
                worst = v
                worst_txt = NOTE[pc.piece_type] + " on " + chess.square_name(sq)
    b.pop()
    if worst >= 3 and worst_txt:
        avoids.append("AVOID: " + uci + " - " + san + " leaves a " + worst_txt +
                      " hit by his pawn/knight jump with no piece defence (minor+ loss)")

if avoids:
    for line in avoids[:6]:
        print(line)
    if len(avoids) > 6:
        print("AVOID: (more, " + str(len(avoids) - 6) + " further flagged moves)")
else:
    print("clean: no pawn/knight jump of his hits your piece undefended after any move")