# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes: notes/ruy-lopez-black.md - Ruy Lopez Closed as Black (setup, plans, ...Nxb2 trap); notes/ruy-lopez-white.md - Ruy Lopez Closed as White (Chigorin; 15...Nb4 / c2 trap).

## Time discipline (game 1: lost on time; game 2: blundered despite long thinks)
- TC 600+10. Opening/theory <=10s; most moves <=20-25s; only 2-3 real decisions 40-60s; check the clock every 5 moves; keep >=3 min at move 25.
- Spend seconds on a CCT scan of the opponent (checks, captures, threats) before any pawn move that attacks a piece, any recapture, any king-area move.
- Dead-lost positions: move in <=5-10s (game 2 wasted ~4 min on moves 17-23 for nothing).
- Verify piece + exact square before submitting; illegal attempts burn 30-100s (game 1).

## Move-safety checklist
- Poisoned recapture: after ...Nxc2 I played Qxc2 and Black recaptured ...Qxc2; c2 was undefended -> lost queen for knight (game 2). Before any recapture: can the piece I capture with be captured next move (open file, undefended square)?
- Kicking a knight with a pawn (16.a3 vs the b4-knight): first list every jump; it took c2 with a fork of both rooks.
- Pawn moves drop old guards: a2-a3 left Nb3 loose; ...Qxb3 won it next move (game 2).
- Open file + enemy queen = entry-square danger (c2). Cover c2 with a rook (Rac1) before pushing pawns.
- Never take a defended piece with a rook, or a piece for a pawn, without a forcing reason (game 1: ...Nxb2, ...Rxd2).

## Ruy Lopez as White (game 2) - Chigorin main line
- 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.Nb3 a5 15.d5 Nb4 = critical.
- 16.a3?? loses to 16...Nxc2 17.Qxc2 Qxc2. Instead move the bishop (Bb1) or cover c2 (16.Rac1), then handle the knight.

## Ruy Lopez as Black
- ...a6, ...Nf6, ...Be7, ...b5, ...d6, ...O-O; then Chigorin (...Na5, ...c5) or Breyer; theory <=5s. Details: notes/ruy-lopez-black.md.
- Keep f7 covered; ...Nxb2 only if a rook already controls b2.

## Opponents
- Sonnet 5.5 (Claude): fast, sound theory, calm conversion; priority = stay ahead on time.
- GPT-6.1 Sol: fast standard theory, slows (~40s) at critical decisions; spots forks/hanging pieces instantly, converts material flawlessly. Keep every piece defended against it.

## Principles
- Piece for a pawn is a blunder without concrete compensation.
- Scan knight-fork squares in my camp (c2, d3, b4) whenever an enemy knight approaches.
- When worse: trade pieces, seek activity; when dead-lost: play fast, protect the clock.
