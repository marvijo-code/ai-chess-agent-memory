import json, sys, chess

payload = json.load(sys.stdin)
clocks = payload.get("clocks") or {}
me = int(clocks.get("you_ms") or 0)
op = int(clocks.get("opponent_ms") or 0)
moves = payload.get("moves") or []
ply = len(moves)
move_no = ply // 2 + 1


def fmt(ms):
    s = max(0, ms // 1000)
    return "%d:%02d" % (s // 60, s % 60)


print("move %d (%d plies): you %s vs opp %s" % (move_no, ply, fmt(me), fmt(op)))

if me and me < 600000:
    per = max(3, int(me / 1000 / max(8, 45 - move_no)))
    print("CLOCK LOW: %s left. Budget ~%ds/move, HARD CAP 20s. Play the first sound move; the destination sweep is the spend." % (fmt(me), per))
elif me and op and me < op - 300000:
    print("CLOCK BEHIND by %s: 5-10s moves, no long think on a quiet move." % fmt(op - me))
elif move_no > 20:
    print("past move 20: NO move over 30s. Quiet/consolidating 5-10s; only a capture or check that changes guards gets 20-30s.")
else:
    print("clock fine: book 5-10s, routine 10-15s, hard cap 30s.")
