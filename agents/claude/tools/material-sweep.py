import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
me = board.turn
V = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9, 6: 100}
VAL = {1: 1, 2: 3, 3: 3, 4: 5, 5: 9}


def count(b, color):
    return sum(VAL[p.piece_type] for p in b.piece_map().values()
               if p.color == color and p.piece_type in VAL)


def hanging(b, color):
    res = {}
    for sq, p in b.piece_map().items():
        if p.color != color or p.piece_type in (1, 6):
            continue
        att = b.attackers(not color, sq)
        if not att:
            continue
        amin = min(V[b.piece_type_at(a)] for a in att)
        dfn = b.attackers(color, sq)
        if amin < V[p.piece_type] or not dfn:
            res[sq] = V[p.piece_type]
    return res


def loose_pawns(b, color):
    out = []
    for sq, p in b.piece_map().items():
        if p.color == color and p.piece_type == 1:
            if b.attackers(not color, sq) and not b.attackers(color, sq):
                out.append(chess.square_name(sq))
    return out


w = count(board, chess.WHITE)
bl = count(board, chess.BLACK)
mine = w if me == chess.WHITE else bl
theirs = bl if me == chess.WHITE else w
print(f"MATERIAL (pawn units, no kings): me {mine} / him {theirs} / diff {mine - theirs:+d}. Trust this, not comments.")
lp = loose_pawns(board, me)
if lp:
    print("My attacked and unguarded pawns now: " + " ".join(lp))
now = hanging(board, me)
if now:
    print("My pieces en prise now: " + " ".join(chess.square_name(s) for s in now))

bad = []
before = set(now.keys())
for move in list(board.legal_moves):
    gain = 0
    if board.is_capture(move):
        if board.is_en_passant(move):
            gain = 1
        else:
            cp = board.piece_at(move.to_square)
            gain = VAL.get(cp.piece_type, 0) if cp else 0
    san = board.san(move)
    gives_check = board.gives_check(move)
    board.push(move)
    if board.is_checkmate():
        board.pop()
        continue
    after = hanging(board, me)
    new = {s: v for s, v in after.items() if s not in before}
    board.pop()
    if new and not gives_check:
        loss = max(new.values())
        if loss > gain:
            sq = max(new, key=lambda s: new[s])
            bad.append(move.uci())
            if len(bad) <= 4:
                print(f"{san} leaves my piece on {chess.square_name(sq)} en prise (value {loss}, I gain {gain}).")
if bad:
    print("AVOID: " + " ".join(bad))
else:
    print("No move leaves a piece newly en prise (pieces only; pins and pawn forks not checked).")
