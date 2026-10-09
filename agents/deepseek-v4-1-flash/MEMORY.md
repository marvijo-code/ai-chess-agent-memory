# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (scan + blunder catalogue g1-g35)
- notes/sicilian-black.md (g28,g29,g30,g32)
- notes/sicilian-dragon-white.md (g6,g34)
- notes/four-knights-black.md (g3,g4,g11,g14,g17,g20,g24,g25,g26)
- notes/ruy-lopez-black.md (g1,g7,g8,g12,g15,g16,g19,g35)
- notes/ruy-lopez-white.md (g2,g5,g9,g10,g13,g18,g21,g22,g23,g27,g31,g33)

## Rule 1 - pre-move scan (EVERY move; all losses g1-g35)
0. Scan the FINAL move, not the plan.
1. Destination: which enemy PAWNS, KNIGHTS, BISHOPS, KING, QUEEN, ROOKS attack it? Attacked+undefended -> reject. King attacks: no rook beside his king (g29). Pawn magnets: h3->g4, f3->g4/e4, c3->b4/d4, b3/b5->a4/c4, c4->b3/d3, g6->f5/h5, e6->d7/f7. Knight magnets: b3/b4->a1/c1/d2/d4; c2->a1/e1/a3/e3; no N to d4/c4 under his Q/B (g28); c6: a5/a7/b4/b8/d4/d8/e5/e7 only. Lines: d3/c2-B hits g6+h7; his Qf3 hits f5; Qc7+Rc8 cover c2; his e3-B covers d2+c1 (g35).
2. MY attacked piece: save/trade/defend it next; no side pawn-grabs. Knight hit by a pawn -> safe flight, never grab the pawn with a piece.
3. Knight captures: never take a defended pawn/square with a knight; count recapturers, even a check (g19,g22,g23).
3b. QUEEN moves/captures: list ALL attackers AND defenders of the destination, incl. rooks on files and bishops on diagonals (g35: e3-B defends c1). 'Defended' is not enough: Bxc4 takes the QUEEN (g28); NEVER take a defended rook with the queen = Q for R (g35 18...Qxc1?? Bxc1!: net Q+R for R+B); Q for B/N/P loses; d5 is a trap (g12,g17,g18,g19,g25).
3c. Queen trade offers need a legal recapturer on the square; 14.Qe3?? Qxe3 = queen for nothing (g34). Queen attacked by a rook: retreat to a safe square, never 'answer' with a grab (g35).
3d. ROOK moves: an undefended rook attacking an enemy rook loses (g27); a rook where his KING attacks it loses (g29); use a DEFENDED rook; scan his rooks/king on the destination rank/file.
4. Next move must save/trade/defend any attacked piece; a moving piece/pawn stops defending its old squares; re-scan after checks and every enemy move (g16,g27,g30); retreat to a square no pawn/knight/rook attacks and no line covers; declined trade -> take it or walk away (g11).
5. Knight forks: cover BOTH targets or vacate one (g23,g27); never move onto a forker's square (g23); 2v2 means the LAST recapturer lands there (g27).
6. Pinned Nd7 (Ba4, Re8): moving it loses the exchange; unpin ...Rb8 (g15).
7. Mate nets: Qa1# (king c1, g6); Qxh7+ when his Qh5+Bd3 cover h7 - defend ...g6, never ...Qf6?? (g25); Qxf7#/Qf2#/Qxg2# (g10,g12,g13); Q/R on the 8th mates a king with f7/g7/h7 and no guard: Re8#/Qc8#/Qd8#/Qxe8#/Rxd8# (g14,g16,g19,g20,g24,g25,g26,g29,g32); Rb1# (g21); Qg8# (g24). Mate threat > material.
8. Never push an undefended pawn onto a defended piece (g12), a knight-attacked square (g16), an enemy pawn's attack (g24), a bishop's capture (g25), where a queen takes with tempo (g19), or when it guards one of my pieces (g30).
9. Loose pieces: my undefended units + all enemy lines; undefended minor where his queen attacks = lost (g26); king-only defense fails vs a queen (g12); every undefended pawn is a target (g29).
12. No rook grab of a pawn a rook/queen/king recaptures (g18,g29); no bishop/major grab of a twice-defended pawn (g23,g34); no pawn grabs while down material or while a piece hangs.
13. Legality BEFORE sending (3 invalid tries = forfeit, g34): path clear, own pieces block (g25,g30); knight geometry (c6 cannot reach d5/d7, g28); bishop geometry (d3 cannot reach e3, g34).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s. Long thinks never prevented a blunder; the 5s scan did (g22,g23,g25,g26,g28,g29,g32,g34,g35: 24-95s on routine moves). HARD: from move 10 no move >30s unless forced tactic/mate; down material 5-15s: defend loose pieces, trade, no pawn grabs, no new loose piece.

## Openings
- Sicilian as Black: Dragon (...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O/...a6/...Bd7/...Rc8/...Qa5) equal (g28); c4 is a B/Q magnet - never ...Qxc4/Bxc4 or N to d4. Rauzer (g29,g32): equal to 15...Rac8; 11...gxf6! not Bxf6; never Bxc3 while Bd7 hangs. g30: no ...f5?? (Nxc5); ...Bxe6 needs a defender.
- 4N as Black (4.Bb5 Bb4): 6.Nd5 Nxd5! 7.exd5 Nd4!; 7.h3 kills ...Bg4; c8-B needs ...d6 first; 10.c3 -> retreat Bb4; no 10...d3?!; 12.Qh5 ...g6!; 15.Qf3: no ...Bf5??/...Qd7??; play ...Qe7/...Qc8/...Bb5.
- RL as White (Chigorin): 14...Nb4 -> 15.Bb1!; 14...Nb8 15.Nf1 Nbd7 16.Be3 Bb7 17.Qd2 Nc5 18.Ng3; after ...g6 no Nf5 tour (g22); 18...Nc5 -> 19.Nd2! (19.Ng3?? Nb3!, g23); keep Q off d5; 14...Rac8 15.Ne3 Nc4: keep e3 EMPTY (e4's rescuer, g33).
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; keep f7 covered; never ...Nc4 once White has b3 (g16). g35: White's Nf1-g3/Bd3/Be3 then Rc1 hits Qc7 -> retreat ...Qb8/...Qd8, never ...Qxc1?? (Be3 recaptures: Q+R for R+B).
- Dragon as White (g6,g34): 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1# (g6). After 6...d5 7.Nxc6 bxc6 8.Nc3 e5 9.Bd3 d4!: move the hit Nc3 (Ne2/Nb1); 10.Bxd4?? Qxd4 = B for P (e5-pawn+Qd8 defend d4).

## Opponents
- Stockfish 19 (g6,g17,g20,g24,g25,g26,g28,g30,g34): ~0s/move; punishes any loose piece or queen on an attacked square/line. Solid known lines only.
- Sonnet 5.5 (g7,g8,g12,g15,g16,g19,g23,g27,g29,g32): banks clock; takes free/attacked units at once (Nxa1, Rxb2, Rxd6, Kxc2, Qxd6). Keep every piece and pawn defended; no rook near his king.
- GPT-6.1 Sol (g9,g10,g13,g18,g21,g22,g31,g33,g35): solid closed RL; punishes queens on his lines; my captures must survive his recapture; g35: his 18.Rc1 hit my Qc7 - retreat the queen, never grab the defended rook.
