import json, sys, chess

payload = json.load(sys.stdin)
board = chess.Board(payload["fen"])
moves = payload.get("moves") or []
clocks = payload.get("clocks") or {}
you = clocks.get("you_ms", 0) or 0
opp = clocks.get("opponent_ms", 0) or 0

hist = None
try:
    b = chess.Board()
    for m in moves:
        b.push_uci(m)
    if b.board_fen() == board.board_fen() and b.turn == board.turn:
        hist = b
except Exception:
    hist = None
if hist is None:
    hist = board

ahead_clock = opp < 300000 and you > opp + 600000
third = []
second = []
for mv in list(hist.legal_moves):
    hist.push(mv)
    try:
        if hist.is_repetition(3):
            third.append(mv.uci())
        elif hist.is_repetition(2):
            second.append(mv.uci())
    except Exception:
        pass
    hist.pop()

if third:
    print("THREEFOLD DRAW if played: " + " ".join(third))
    if ahead_clock:
        print("Opponent is nearly flagging and I am far ahead on the clock: a draw throws the win away, play a NEW safe move.")
        for u in third:
            print("AVOID: " + u + " - threefold draw gives up a flag win (no material lost)")
if second:
    print("Second repetition if played (next time it is a draw): " + " ".join(second))
if not third and not second:
    print("no repetition risk")
if ahead_clock:
    print("CLOCK LEAD: change the structure each move (new piece square or a pawn step), never K back and forth.")
