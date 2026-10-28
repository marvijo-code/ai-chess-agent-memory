import json, sys, chess
p = json.load(sys.stdin)
b = chess.Board()
seen = {}
for u in p["moves"]:
    key = b.board_fen() + (" w" if b.turn == chess.WHITE else " b")
    seen[key] = seen.get(key, 0) + 1
    try:
        b.push(chess.Move.from_uci(u))
    except Exception as e:
        print(f"bad move {u}: {e}")
        break
key = b.board_fen() + (" w" if b.turn == chess.WHITE else " b")
seen[key] = seen.get(key, 0) + 1
hits = sorted(((v, k) for k, v in seen.items() if v >= 2), reverse=True)
if not hits:
    print("no position repeats yet")
else:
    for v, k in hits[:5]:
        print(f"seen {v}x: {k}")
    top = hits[0][0]
    if top >= 2:
        print(f"PLAY: returning to the most-seen position = draw after occurrence 3 (currently {top}x)")
print(f"halfmove clock (50-move rule): {b.halfmove_clock}/100 since last capture or pawn move")
