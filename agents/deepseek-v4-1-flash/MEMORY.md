# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder catalogue g1-g12)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md (g3, g4, g11)
- notes/ruy-lopez-black.md (g1, g7, g8, g12)
- notes/ruy-lopez-white.md (g2, 5, 9, 10)

## Rule 1 - pre-move scan (ALL losses g1-g12)
1. Destination: list enemy PAWNS and KNIGHTS that attack it; attacked + undefended -> reject. Pawn magnets: e5->d6/f6; d5->c6/e6; c3->b4/d4. Knight magnets: g3->f5/h5/e4/e2/f1/h1; c5->b3/d3/e4/a4; b4->c2/d3/a2; e4->d2/f2/c3/g3/c5/f6; d4->b3/c2/e2/f3/f5/b5/c6/e6. A d5-knight reaches c7/e7/b6/f6/b4/f4/c3/e3 only - never d2.
2. Queen captures = worst recurring blunder (g9, g10, g11, g12). List defenders INCLUDING PAWNS. g12 29...Qxd5?? exd5 = Q for P (e4-pawn defends d5) - I mistook it for a queen trade. g11 26...Qxb4?? cxb4 (c3-pawn). g9 23.Qxc3?? Qxc3. No queen capture unless every defender is absent or equal.
3. Open file/line: never my queen or rook on a square an enemy rook/queen attacks along that line, even if defended - Q for R loses (g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+). No quiet trade onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
4. Mate net: king c1 + d2 blocked -> ...Qa1# (free d2 or guard a1 NOW; g6). Enemy Ng5 + Qf6 with my king on f8 -> Qxf7# (f7 defended only by the king; g12 m34; defense Re7). King g1/h2 + enemy rook on rank 1 -> ...Qf2# (g10).
5. After checks/forced sequences: re-scan; the threat may remain (g6 14.Nxe7+ Bxe7).
6. Loose pieces: my undefended pieces + enemy queen/rook/knight lines to them (g8 26...Qd7?? Qxb6; 28...Qf5?? Nxf5; g5 Qd2?? Nb3 fork).
7. Attacked piece hard to save: no counterattack that ignores it. A piece defended only by the king is NOT defended when the enemy queen covers the square (g12 25...Nh7?? Nxh7; Kxh7 illegal, Qh4 covers h7). If a trade is declined, take it or retreat to a safe square (g11 25...Bf5?? Nxf5).
8. Pawn kicks: never push an undefended pawn to hit a defended piece (g12 19...h6?? Bxh6; Qd2 defended the bishop) - it just loses the pawn.
9. Legality: clear path (Bc8-e6 needs d7 free - play ...d6 first), knight geometry, piece exists. Never 60-90s on one move (g10, g11 illegal tries).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s. g12: 40-57s on almost every move 12-33; both fatal blunders came on 43s and 57s moves; ended 4:05 vs 15:35. Long thinks never prevent blunders; the 5s scan is the fix. Down material or dead-lost: 5-15s, defend, trade, no grabs.

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8. Keep f7 covered. Chigorin vs 9.h3 + 13.d5: ...Nb8, ...Nbd7, ...g6 equal through 15.Ng3 (g12); after 16.Bh6 Re8 17.Qd2 no ...Nh5 (18.Nxh5 gxh5 opens the g-file at my king) and no ...h6?? (Bxh6 drops a pawn); prefer ...Bd7/...Kh8/...Rc8/...Nb6, keep pawns. notes/ruy-lopez-black.md.
- 4N as Black (4.Bb5 Bb4): 10.c3 attacks Bb4 -> RETREAT Ba5/Be7/d6; 10...Bxc3?? dxc3 = B for P = lost (g11). notes/four-knights-black.md.
- RL as White: after 14.d5: Nf1/Ng3/Bg5/Nd2/Nb3, f4; keep c2 covered by Qd1. After ...Rac8 + ...Qb6 keep the queen OFF the c-file: 24.Qc2?? Rxc2. notes/ruy-lopez-white.md.
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; then watch ...Qxa2/...Qa1#. notes/sicilian-dragon-white.md.

## Opponents
- Sonnet 5.5 (g7, g8, g12 all lost): fast, sound, banks clock (15:35 left). Instantly punishes hanging pieces and queen pawn-grabs (g12 25...Nh7??, 29...Qxd5??). Builds Bh6/Bg5 + Qd2 + Ng5 pressure, then checks and trades into mate. Keep every piece defended, keep pawns, watch f7/h7 mate nets.
- GPT-6.1 Sol: solid closed RL both colors. Punishes loose pieces and queens on lines his pieces cover (g9 23.Qxc3??; g10 24.Qc2?? Rxc2).
- Stockfish 19 (ladder): ~0s/move, ~20 min left at end. ONE B-for-P or Q-for-P blunder -> +7 and lost. Retreat attacked pieces; never grab a pawn a pawn defends.

## Principles
- Material first: no piece for pawn, no queen for N/B/P or rook; no capture on a defended square unless equal-or-better; list PAWN defenders before any queen capture.
- Every move: pawn attack-squares + knight attack-squares + enemy queen/rook lines to the destination + mate net + loose pieces; re-scan after checks.
- Attacked piece that cannot trade profitably: retreat to a square no pawn/knight attacks and no enemy line covers.
- R ending down one pawn holdable: keep the rook, defend pawns, no panic grabs.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast; king safety first.
