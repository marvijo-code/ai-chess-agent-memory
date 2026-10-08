# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder catalogue g1-g16)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md (g3, g4, g11, g14)
- notes/ruy-lopez-black.md (g1, g7, g8, g12, g15, g16)
- notes/ruy-lopez-white.md (g2, g5, g9, g10, g13)

## Rule 1 - pre-move scan (ALL losses g1-g16)
1. Destination: list enemy PAWNS, KNIGHTS and the KING squares that attack it; attacked+undefended -> reject. PAWN MAGNETS MOVE WITH THE PAWN: e5->d6/f6; d5->c6/e6; c3->b4/d4; b3->a4/c4 (g16 18...Nc4?? bxc4 = N for P; "the b-pawn already advanced" is WRONG - b3 attacks c4); a2->b3. Knights: g3->f5/h5/e4/e2/f1/h1; c5->b3/d3/e4/a4; b4->c2/d3/a2; e4->d2/f2/c3/g3/c5/f6; d4->b3/c2/e2/f3/f5/b5/c6/e6; d2->c4/e4/f1/f3/b1/b3.
2. Queen safety, both directions. No capture/move - even a check - onto a square any enemy piece or the KING can capture (g13 26.Qh8+?? Kxh8; g14 17...Qe1+?? Rxe1). List ALL defenders, pawns first, plus QUEENS/ROOKS on lines (g12 29...Qxd5?? exd5; g15 23...Qxe5?? Qxe5; g16 27...Bxd5?? Qd1 shows down the d-file).
3. Open file/line: never my queen or rook on a square an enemy rook/queen attacks along it, even if defended (g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+).
4. A moving piece stops defending: list its squares and fix loose ones first (g13 25.Qxh6??). Reverse: an enemy move can RESTORE a defense - recheck targets after every enemy move (g16 26...Nxe4?? Bc1 left the e-file, Re1 re-covered e4).
5. Pinned knight: bishop pin Ba4-Nd7-Re8 -> moving the knight loses the exchange (g15 17...Nb6? 18.Bxe8). Unpin with the rook first or keep it home.
6. Mate net: king c1 + d2 blocked -> ...Qa1# (g6). Enemy Ng5+Qf6 vs king f8 -> Qxf7# (g12). King g1/h2 + enemy rook rank 1 -> ...Qf2# (g10). King g1 + enemy Qg2 backed by Bb7 -> ...Qxg2# (g13; Nf1 does not guard g2). Back rank: king g8, f8/h8 uncovered -> Re8#/Rd8# (g14, g16 41.Rd8#).
7. Pawn kicks/pushes: never push an undefended pawn to hit a defended piece (g12 19...h6?? Bxh6) and never push a pawn onto a square an enemy knight attacks (g16 21...f5?? Nxf5, then Nxe7+ won B+P).
8. Loose pieces: my undefended pieces + enemy queen/rook/knight lines. A piece defended only by the king is not defended vs a queen (g12 25...Nh7??).
9. Attacked piece hard to save: no counterattack that ignores it; retreat to a square no pawn/knight attacks and no line covers; if a trade is declined, take it (g11 25...Bf5??; g15 25...Nc4).
10. Legality: path clear, knight geometry, own piece blocks a pawn push (g16 20...f5 illegal with Nf6, 91s wasted), piece exists.
11. After checks/forced sequences re-scan; the threat may remain (g6).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s; past 25s play the safest candidate now. g16 repeated g15: 40-91s on moves 15-31, exactly where every blunder happened (16...Nc4 46s, 18...Nc4 46s, 26...Nxe4 63s, 27...Bxd5 54s), ended 1:44 vs 15:18. Long thinks never prevented a blunder; the 5s scan does. Down material: 5-15s, defend, trade like for like (g16 30...Rxc4/31...Rxf2 gave R for B and R for P - worse).

## Openings
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; keep f7 covered. Chigorin equal through 14...Rac8 (g16): 15...Rfe8?? and 16...Nc4?? flagged; after 16.d5 the a5-knight has no good square (c4 kicked by b3, c6 hangs to dxc6) - keep it on b6/d7, consolidate (...Bf8/...Nb6) before activity. NEVER return a knight to c4 once White has b3: 18...Nc4?? bxc4 = N for P, lost (g16). Breyer: after 16.Bxa4 pins Nd7 to Re8, no ...c5?! (g15 17.d5 Nb6? 18.Bxe8); unpin with Rb8 or keep the knight home. notes/ruy-lopez-black.md.
- 4N as Black (4.Bb5 Bb4): 10.c3 attacks Bb4 -> RETREAT Ba5/Be7/d6; 10...Bxc3?? dxc3 = B for P (g11).
- RL as White: 11.d4/13.cxd4/14.d5 fine, then Nf1/Ng3/Bg5/Nd2/Nb3, f4; keep c2 covered (Qd1/Qd2). After ...Qb6 keep the queen OFF the c-file (g10 24.Qc2?? Rxc2). 21.Bxf6?! gives the bishop pair - keep the bishop (g13). notes/ruy-lopez-white.md.
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1#. notes/sicilian-dragon-white.md.

## Opponents
- Sonnet 5.5 (g7, g8, g12, g15, g16 all lost): fast, sound, banks clock (15:18 vs my 1:44 in g16). Takes any free/piece-attacked unit at once (g16 19.bxc4, 27.Rxe4, 28.Qxd5+) and redefends loose pawns by unblocking lines (g16 26.Bc1 made Re1 guard e4). Keep every piece on unattacked squares; never a knight on a b3-pawn-attacked square.
- GPT-6.1 Sol (g9, g10, g13 lost): solid closed RL both colors. Takes any undefended piece at once (g13 25...Qxc2) and punishes queens on lines his pieces cover (g10 24.Qc2?? Rxc2). Keep every piece defended.
- Stockfish 19 (ladder): ~0s/move. ONE B-for-P or Q-for-P blunder -> +7 and lost. Retreat attacked pieces; never grab a pawn a pawn defends.

## Principles
- Material first: no piece for pawn (g16 N for P after 18...Nc4??); no queen for N/B/P or rook; list ALL defenders (pawns, knights, bishops, queens/rooks on lines) before any capture, and recheck them after the opponent's move.
- Every move: pawn + knight + king attack-squares of the destination + enemy queen/rook lines + mate net + loose pieces + what the moved piece was defending; re-scan after checks.
- A pawn advance shifts the squares it attacks (b2->a3/c3, b3->a4/c4): recompute at once.
- Attacked piece that cannot trade profitably: retreat to a square no pawn/knight attacks and no line covers.
- R ending down one pawn holdable: keep the rook, defend pawns, no panic grabs.
- After a blunder: defend loose pieces, trade down, no panic captures, play fast; king safety first.
