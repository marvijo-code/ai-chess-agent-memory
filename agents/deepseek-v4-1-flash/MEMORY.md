# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder catalogue g1-g13)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md (g3, g4, g11)
- notes/ruy-lopez-black.md (g1, g7, g8, g12)
- notes/ruy-lopez-white.md (g2, 5, 9, 10, 13)

## Rule 1 - pre-move scan (ALL losses g1-g13)
1. Destination: list enemy PAWNS, KNIGHTS and the KING (adjacent squares) that attack it; attacked + undefended -> reject. Pawn magnets: e5->d6/f6; d5->c6/e6; c3->b4/d4. Knight magnets: g3->f5/h5/e4/e2/f1/h1; c5->b3/d3/e4/a4; b4->c2/d3/a2; e4->d2/f2/c3/g3/c5/f6; d4->b3/c2/e2/f3/f5/b5/c6/e6. A d5-knight never reaches d2.
2. Queen safety, both directions. Captures: no queen capture unless every defender is equal or absent; count PAWN defenders first (g12 29...Qxd5?? exd5 = Q for P; g11 26...Qxb4?? cxb4; g9 23.Qxc3??). Moves: never land the queen - even a check - on a square ANY enemy piece can capture, the KING included (g13 26.Qh8+?? Kxh8 = Q for P; h8 sits next to Kg8, was undefended, and Bf6 also covered it; the 'Bg7 then Qh5' idea never happens).
3. Open file/line: never my queen or rook on a square an enemy rook/queen attacks along that line, even if defended (g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+). No quiet trade onto a square an extra enemy piece attacks (g8 20...Bf5?? Nxf5).
4. A moving piece stops defending: before moving Q/B/R list the squares it defends; if one becomes loose and attacked, fix it first (g13 25.Qxh6?? - Qd2 had covered c2; 25...Qxc2! won a bishop).
5. Mate net: king c1 + d2 blocked -> ...Qa1# (g6). Enemy Ng5+Qf6 vs king f8 -> Qxf7# (g12 m34; defense Re7). King g1/h2 + enemy rook on rank 1 -> ...Qf2# (g10). King g1 + enemy queen on g2 backed by a bishop on the b7-g2 diagonal -> ...Qxg2# (g13 m29; my Nf1 does NOT guard g2).
6. After checks/forced sequences re-scan; the threat may remain (g6 14.Nxe7+ Bxe7).
7. Loose pieces: my undefended pieces + enemy queen/rook/knight lines to them (g8 26...Qd7?? Qxb6; g5 Qd2?? Nb3 fork).
8. Attacked piece hard to save: no counterattack that ignores it. A piece defended only by the king is NOT defended when the enemy queen covers the square (g12 25...Nh7?? Nxh7). If a trade is declined, take it or retreat to a safe square (g11 25...Bf5?? Nxf5).
9. Pawn kicks: never push an undefended pawn to hit a defended piece (g12 19...h6?? Bxh6).
10. Legality: clear path, knight geometry, piece exists; illegal tries waste clock (g11, g12, g13 22.Ne3 = 2 tries).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s; if a think passes 25s, play the safest candidate now. g13 repeated the habit: 30-85s on nearly every move 12-29 (84s + illegal try on 22.Ne3), ended 6:28 vs 13:48; the queen blunder 26.Qh8+ came after a 44s think. Long thinks never prevented a blunder; the 5s scan does. Down material or dead-lost: 5-15s, defend, trade, no grabs.

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8. Keep f7 covered. Chigorin vs 9.h3 + 13.d5: ...Nb8, ...Nbd7, ...g6 equal through 15.Ng3 (g12); after 16.Bh6 Re8 17.Qd2 no ...Nh5 and no ...h6??; prefer ...Bd7/...Kh8/...Rc8/...Nb6, keep pawns. notes/ruy-lopez-black.md.
- 4N as Black (4.Bb5 Bb4): 10.c3 attacks Bb4 -> RETREAT Ba5/Be7/d6; 10...Bxc3?? dxc3 = B for P = lost (g11). notes/four-knights-black.md.
- RL as White: 11.d4/13.cxd4/14.d5 fine, then Nf1/Ng3/Bg5/Nd2/Nb3, f4; keep c2 covered (Qd1/Qd2). After ...Qb6 keep the queen OFF the c-file (g10 24.Qc2?? Rxc2). g13 vs Sol: 14...Nb8 15.Nf1 Nbd7 16.Ng3 Bb7 17.Bg5 h6 18.Bh4 Rfe8 19.Nf5 Bf8 20.Qd2 Rad8 was equal; 21.Bxf6?! gives him the bishop pair - keep the bishop, play Rae1/f4; never raid h6/h8 with the queen while Bc2 is loose. notes/ruy-lopez-white.md.
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1#. notes/sicilian-dragon-white.md.

## Opponents
- Sonnet 5.5 (g7, g8, g12 all lost): fast, sound, banks clock. Punishes hanging pieces and queen pawn-grabs instantly (g12 25...Nh7??, 29...Qxd5??). Builds Bh6/Bg5 + Qd2 + Ng5 pressure, then checks and trades into mate. Keep every piece defended, keep pawns, watch f7/h7 mate nets.
- GPT-6.1 Sol (g9, g10, g13 lost): solid closed RL both colors. Takes any undefended piece at once (g13 25...Qxc2), then his queen eats pawns (Qxe4, Qxd5) and mates (Qxg2# backed by Bb7); punishes queens on lines his pieces cover (g10 24.Qc2?? Rxc2). Keep every piece defended at all times; do not create new loose pieces.
- Stockfish 19 (ladder): ~0s/move, ~20 min left at end. ONE B-for-P or Q-for-P blunder -> +7 and lost. Retreat attacked pieces; never grab a pawn a pawn defends.

## Principles
- Material first: no piece for pawn, no queen for N/B/P or rook; no capture on a defended square unless equal-or-better; list PAWN defenders before any queen capture; no queen move/check onto a capturable square (king first).
- Every move: pawn + knight + king attack-squares + enemy queen/rook lines to the destination + mate net + loose pieces + what the moved piece was defending; re-scan after checks.
- Attacked piece that cannot trade profitably: retreat to a square no pawn/knight attacks and no enemy line covers.
- R ending down one pawn holdable: keep the rook, defend pawns, no panic grabs.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast; king safety first.
