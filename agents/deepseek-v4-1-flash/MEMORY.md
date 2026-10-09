# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (scan + blunder catalogue g1-g22)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md (g3,g4,g11,g14,g17,g20)
- notes/ruy-lopez-black.md (g1,g7,g8,g12,g15,g16,g19)
- notes/ruy-lopez-white.md (g2,g5,g9,g10,g13,g18,g21,g22)

## Rule 1 - pre-move scan (EVERY move; all losses g1-g22)
0. Scan the FINAL chosen move, not the plan (g21: noted Nb4 attacks a2,c2,d3,d5, then played 15.Bd3?? anyway).
1. Destination: which enemy PAWNS, KNIGHTS, KING attack it? Attacked+undefended -> reject. Pawn magnets: e5->d6/f6; d5->c6/e6; c3->b4/d4; b3->a4/c4; b5->a4/c4; c4->b3/d3 (g21 22.Qb3?? cxb3); g6->f5/h5 (g22 23.Nef5?? gxf5 = N for P). Knight magnets: b4->a2/c2/d3/d5 (g21 15.Bd3?? Nxd3/Nxe1 = B+R for N); d4->b3/c2/e2/f3/f5/b5/c6/e6; e4->d2/f2/c3/g3/c5/f6; c6->a5/a7/b4/b8/d4/d8/e5/e7 (NOT d7); b8->a6/c6/d7 only if no enemy Q/B (g20 11...Nd7?? Qxd7!).
2. Knight captures: never take a defended pawn/square with a knight - count recapturers first (g19 18...Nd7?! dxc6; g22 26.Nxd6?? Qxd6 = N for P). N for P is a loss even when it wins a pawn.
3. Queen/rook moves: list ALL attackers (pawns, knights, king, sliders on file/rank/diagonal, INCLUDING rooks on the target's file: g22 31.Qxc4?? Rc8xc4 = Q for R). Defended is not enough if the trade is Q for B/N/P (g18 23.Qd5?? Bxd5; g19 28...Qxd5?? Bxd5). d5 is a queen trap (g12,g17,g18,g19): never put the queen there while any P/N/B/R can take. Name the squares a queen leaves (g17 12...Qd6?? left d4 -> 13.Qxd4!; g13 25.Qxh6?? left c2).
4. A moving piece stops defending: fix the squares it leaves; re-scan after checks/forced moves and after every enemy move (g16 26...Nxe4?? Re1 re-covered e4).
5. Pinned knight behind Ba4-Nd7-Re8: moving it loses the exchange (g15 17...Nb6? 18.Bxe8); unpin with ...Rb8.
6. Mate nets: king c1+d2 blocked -> Qa1# (g6); Ng5+Qf6 vs king f8 -> Qxf7# (g12); king g1/h2 + enemy rook rank 1 -> Qf2# (g10); Qg2+Bb7 -> Qxg2# (g13); king g8/h8, f7/g7/h7, 8th rank open -> Re8#/Qc8# (g14,g16,g19,g20); king h1, own g2 pawn, enemy rook rank 1, queen covers h2 -> Rb1# (g21).
7. Never push an undefended pawn onto a defended piece (g12 19...h6?? Bxh6), a knight-attacked square (g16 21...f5?? Nxf5), or where the queen takes with tempo (g19 24...b3?? Qxb3+).
8. Loose pieces: my undefended units + enemy Q/R/N lines; king-only defense fails vs a queen (g12 25...Nh7??).
9. Attacked piece with no profitable trade: retreat to a square no pawn/knight attacks, no line covers; declined trade -> take it or walk away (g11 25...Bf5?? Nxf5).
10. Enemy pawn attacks a knight -> move it or defend it; pawn-for-knight is fatal even if recapturable (g19 18...Nd7?! dxc6).
11. No rook grab of a pawn a rook/queen recaptures (g18 25.Rxe5 Rxe5 = R for P).
12. Legality: path clear (own pieces block!), knight geometry; illegal tries waste clock (g18:4, g19:2, g21:1).
13. Mate threat > material: with a mate net on my king defend first, never grab a pawn (g12,g17).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s; after 25s play the safest candidate now. Long thinks never prevented a blunder; the 5s scan does (g21: 91s on 16.Qe2 then 15.Bd3??). g22: 40-60s on almost every move 12-31 (routine N/B/Q moves), 5:43 left at move 26, 2:47 at move 31, lost on time (0:13 vs 12:45). HARD: from move 10, no move >30s unless a forced tactic/mate; check the clock every move; when down material play 5-15s.

## Openings
- RL as White (Chigorin): 11.d4/13.cxd4/14.d5 fine. 14...Nb4 -> 15.Bb1! (b4-knight attacks a2/c2/d3/d5; g21 15.Bd3??). 14...Nb8: 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3 Rfe8 19.Nf5 Bf8 20.Bxc5 Qxc5 is equal, no plan left (g18,g22); do not tour Nf5-e3-h4-f5 while ...g6 controls f5 (g22 23.Nef5?? gxf5). Keep queen off c-file after ...Qb6 (g10 24.Qc2?? Rxc2) and off d5 while ...Bb7 covers it (g18). Keep the dark bishop (g13,g18).
- 4N as Black (4.Bb5 Bb4): 6.Nd5 -> TAKE 6...Nxd5! (7.exd5 Nd4! 8.Nxd4 exd4). 6...Be7?! lets 7.c3 and 9.Nxe5! (g20). 10.c3 attacks Bb4 -> retreat (10...Bxc3?? dxc3, g11). 12...Qd6?? left d4 -> 13.Qxd4! (g17). 10...c6! beats ...Re8.
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; keep f7 covered. Never ...Nc4 once White has b3 (g16). Breyer: 16.Bxa4 pins Nd7 to Re8 -> no ...c5?!, unpin ...Rb8 (g15). Chigorin g19: 16...a5?! 17...b4?! weakened the queenside; 18.d5! hit Nc6.
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1#.

## Opponents
- Sonnet 5.5 (g7,g8,g12,g15,g16,g19): banks clock (15:15 vs 1:32, g19). Takes free/attacked units at once; redefends by unblocking lines (g16 26.Bc1). Keep every piece on unattacked squares.
- GPT-6.1 Sol (g9,g10,g13,g18,g21,g22): solid closed RL; takes exposed units at once (g18 Bxd5; g21 Nxd3/Nxe1/bxc4/cxb3; g22 Qxd6/Rxc4/Nxe4); punishes queens on his lines; banks clock (12:45 vs 0:13, g22). Any capture I make must survive his recapture.
- Stockfish 19 (ladder, g17,g20): ~0s/move; punishes every opening deviation and loose piece (g20: 9.Nxe5 after 6...Be7?!; 12.Qxd7 after 11...Nd7??; 18.Rxe8#). Play only known-solid lines; retreat attacked pieces.

## Principles
- Scan mate nets and ALL attackers of every queen/rook/knight destination; queen/knight safety before material; a knight taking a defended pawn is a blunder.
- Attacked piece with no profitable trade: retreat to a square no pawn/knight attacks and no line covers.
- The 5s scan on the final move beats any long think; routine <=15s, no move >30s from move 10.
- After a blunder: defend loose pieces, trade down, play fast; king safety first.
