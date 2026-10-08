# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder catalogue g1-g18)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md (g3, g4, g11, g14, g17)
- notes/ruy-lopez-black.md (g1, g7, g8, g12, g15, g16)
- notes/ruy-lopez-white.md (g2, g5, g9, g10, g13, g18)

## Rule 1 - pre-move scan (EVERY move; all losses g1-g18)
1. Destination: which enemy PAWNS, KNIGHTS, KING attack it? Attacked + undefended -> reject. Pawn magnets move with the pawn: e5->d6/f6; d5->c6/e6; c3->b4/d4; b3->a4/c4 (g16 18...Nc4?? bxc4 = N for P); a2->b3. Knight magnets: g3->f5/h5/e4/e2/f1/h1; c5->b3/d3/e4/a4; b4->c2/d3/a2; e4->d2/f2/c3/g3/c5/f6; d4->b3/c2/e2/f3/f5/b5/c6/e6; d2->c4/e4/f1/f3/b1/b3.
2. Queen/rook/bishop moves: list ALL attackers of the destination - pawns, knights, KING, rooks/queens on files/ranks, BISHOPS/queens on diagonals. Even a defended square fails if the trade is Q for B/N/P: g18 23.Qd5?? Bb7xd5 = Q for B (e4 recaptures only a bishop); g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+; g13 26.Qh8+?? Kxh8; g14 17...Qe1+?? Rxe1. A queen move also abandons its old squares: name them (g13 25.Qxh6?? left Bc2; g17 12...Qd6?? left d4 -> 13.Qxd4! + Qxg7# threat).
3. A moving piece stops defending: list its squares, fix loose ones first. Enemy moves can RESTORE a defense - recheck targets after every enemy move (g16 26...Nxe4?? Re1 re-covered e4).
4. Pinned knight behind Ba4-Nd7-Re8: moving it loses the exchange (g15 17...Nb6? 18.Bxe8). Unpin with ...Rb8 or keep it home.
5. Mate nets: king c1 + d2 blocked -> ...Qa1# (g6). Enemy Ng5+Qf6 vs king f8 -> Qxf7# (g12). King g1/h2 + enemy rook rank 1 -> ...Qf2# (g10); enemy Qg2+Bb7 -> ...Qxg2# (g13). Back rank: king g8, f8/h8 uncovered -> Re8#/Rd8# (g14, g16). Battery: enemy Qd4+Bb2, king g8, e5/f6 empty -> Qxg7# (g17).
6. Never push an undefended pawn onto a defended piece (g12 19...h6?? Bxh6) or onto a square an enemy knight attacks (g16 21...f5?? Nxf5).
7. Loose pieces: my undefended pieces + enemy queen/rook/knight lines. King-only defense fails vs a queen (g12 25...Nh7??).
8. Attacked piece that cannot trade profitably: retreat to a square no pawn/knight attacks and no line covers; if a trade is declined, take it or walk away (g11 25...Bf5?? Nxf5; g15 25...Nc4).
9. Never take a pawn with a rook when a rook/queen recaptures: g18 25.Rxe5 Rxe5 = R for P.
10. Legality: path clear, knight geometry, own piece blocks a push (g16 20...f5 illegal with Nf6); piece exists. Illegal tries waste clock (g18: 4).
11. After checks/forced moves re-scan; the threat may remain (g6).
12. Mate threat > material: with a battery or mate net aimed at my king, defend first - never grab a pawn (g12, g17).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s; after 25s play the safest candidate now. g16/g17: 40-91s on moves 15-31 = exactly where the blunders were; g18: 37/45/60/46/40/47s on moves 13-20, 117s on 21.Bxc5?!, 98s on 23.Qd5?? (queen lost), ended 2:29 vs 14:45. Long thinks never prevented a blunder; the 5s scan does. Down material: 5-15s, defend, trade like for like.

## Openings
- 4N as Black (4.Bb5 Bb4): 10.c3 attacks Bb4 -> RETREAT a5/Be7/d6 (10...Bxc3?? dxc3 = B for P, g11). g17: 12...Qd6?? left d4 undefended AND allowed Qd4+Bb2 -> 13.Qxd4! (Qxg7# threat); 13...Qxd5?? 14.Qxg7#. 10...c6! beats ...Re8 (g14, g17).
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; keep f7 covered. NEVER ...Nc4 once White has b3 (g16 18...Nc4?? bxc4). Breyer: after 16.Bxa4 pins Nd7 to Re8 no ...c5?!; unpin with ...Rb8 (g15 17...Nb6? 18.Bxe8).
- RL as White: 11.d4/13.cxd4/14.d5 fine, then Nf1/Ng3/Bg5/Be3/Nd2, f4; keep c2 covered (Qd1/Qd2; 16.a3 needs both Qd1+Bb1 on c2, g2). After ...Qb6 keep the queen OFF the c-file (g10 24.Qc2?? Rxc2). Never put the queen on d5/d4 while ...Bb7 covers the long diagonal (g18 23.Qd5?? Bxd5 = Q for B). Keep the dark bishop: 21.Bxf6?! (g13) / 21.Bxc5?! dxc5 (g18) hand Black the bishop pair.
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1#.

## Opponents
- Sonnet 5.5 (g7, g8, g12, g15, g16): banks clock (15:18 vs my 1:44, g16). Takes any free/piece-attacked unit at once; redefends by unblocking lines (g16 26.Bc1). Keep every piece on unattacked squares.
- GPT-6.1 Sol (g9, g10, g13, g18): solid closed RL; takes exposed units at once (g18 23...Bxd5 won the queen); punishes queens on lines his B/R/Q cover (g10 24.Qc2?? Rxc2); banks clock (g18 14:45 vs 2:29). Keep every piece defended AND off his lines.
- Stockfish 19 (ladder): ~0s/move. One piece-for-pawn, queen slip or ignored mate -> lost (g17). Retreat attacked pieces; never grab a pawn a pawn defends; never ignore a mate threat.

## Principles
- Mate threats beat material: scan for enemy batteries/mate nets every move; defend them before any capture or plan.
- Before any queen/rook move list ALL attackers (pawns, knights, king, rooks/queens on lines, bishops/queens on diagonals); a defended square is still fatal if the trade is Q for B/N/P.
- Attacked piece that cannot trade profitably: retreat to a square no pawn/knight attacks and no line covers.
- After a blunder: defend loose pieces, trade down, play fast; king safety first.
