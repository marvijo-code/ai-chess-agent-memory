import json, sys

payload = json.load(sys.stdin)
mine = int(payload.get("clocks", {}).get("you_ms", 0) or 0)
opp = int(payload.get("clocks", {}).get("opponent_ms", 0) or 0)
moves = payload.get("moves", []) or []
n = len(moves)

def fmt(ms):
    s = max(0, ms) // 1000
    return f"{s // 60}:{s % 60:02d}"

print(f"clock check: {n} moves played, mine {fmt(mine)}, opponent {fmt(opp)}")

cap = 20
if n >= 40:
    cap = 8
elif n >= 30:
    cap = 10
elif n >= 25:
    cap = 12

if mine < 60_000:
    cap = 3
    print("DANGER: under 1 minute - only 2-3 s moves, play a known defended move")
elif mine < 120_000:
    cap = min(cap, 5)
    print("DANGER: under 2 minutes - 3-5 s moves, no checks left unexplored")
elif mine < 300_000:
    cap = min(cap, 8)
    print("LOW: under 5 minutes - hard cap 8 s")
elif mine < 600_000:
    cap = min(cap, 10)
    print("under 10 minutes - hard cap 10 s")

print(f"SUGGESTED MAX THINK: {cap} s")
print("Reminder: level or worse after move 25 = cap 15 s, pick ONE fortress plan and repeat it; count minutes left vs moves left.")

if opp > 0 and mine > 0 and opp > 3 * mine and n >= 20:
    print("Opponent has over 3x my clock: simplify, avoid long thinks, force repetitions or trades.")
