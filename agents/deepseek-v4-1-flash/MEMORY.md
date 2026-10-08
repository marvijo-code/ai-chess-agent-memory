# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder catalogue g1-g17)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md (g3, g4, g11, g14, g17)
- notes/ruy-lopez-black.md (g1, g7, g8, g12, g15, g16)
- notes/ruy-lopez-white.md (g2, g5, g9, g10, g13)

## Rule 1 - pre-move scan (EVERY move; all losses g1-g17)
1. Destination: which enemy PAWNS, KNIGHTS, KING attack it? Attacked + undefended -> reject. Pawn magnets move with the pawn: e5->d6/f6; d5->c6/e6; c3->b4/d4; b3->a4/c4 (g16 18...Nc4?? bxc4 = N for P); a2->b3. Knight magnets: g3->f5/h5/e4/e2/f1/h1; c5->b3/d3/e4/a4; b4->c2/d3/a2; e4->d2/f2/c3/g3/c5/f6; d4->b3/c2/e2/f3/f5/b5/c6/e6; d2->c4/e4/f1/f3/b1/b3.
2. Queen: never move/capture/check onto a square any enemy piece or the KING can take (g13 26.Qh8+?? Kxh8; g14 17...Qe1+?? Rxe1; g12 29...Qxd5??; g15 23...Qxe5??). List ALL defenders (pawns first, then pieces, rooks/queens on lines). A queen move abandons its old squares: name what it defended (g13 25.Qxh6?? left Bc2; g17 12...Qd6?? left d4 -> 13.Qxd4! + Qxg7# threat).
3. Open file/line: never my queen/rook on a square an enemy rook/queen attacks along it, even if defended (g10 24.Qc2?? Rxc2; g9 24.Rc1?? Qxc1+).
4. A moving piece stops defending: list its squares, fix loose ones first. Enemy moves can RESTORE a defense - recheck targets after every enemy move (g16 26...Nxe4?? Re1 re-covered e4).
5. Pinned knight behind Ba4-Nd7-Re8: moving it loses the exchange (g15 17...Nb6? 18.Bxe8). Unpin with ...Rb8 or keep it home.
6. Mate nets: king c1 + d2 blocked -> ...Qa1# (g6). Enemy Ng5+Qf6 vs king f8 -> Qxf7# (g12; Re7 defends). King g1/h2 + enemy rook rank 1 -> ...Qf2# (g10); enemy Qg2+Bb7 -> ...Qxg2# (g13). Back rank: king g8, f8/h8 uncovered -> Re8#/Rd8# (g14, g16). Battery: enemy Qd4+Bb2, king g8, e5/f6 empty -> Qxg7# (g17 14.Qxg7#; f7/h7 box the king, g7 defended only by the king).
7. Never push an undefended pawn onto a defended piece (g12 19...h6?? Bxh6) or onto a square an enemy knight attacks (g16 21...f5?? Nxf5).
8. Loose pieces: my undefended pieces + enemy queen/rook/knight lines. King-only defense fails vs a queen (g12 25...Nh7??).
9. Attacked piece that cannot trade profitably: retreat to a square no pawn/knight attacks and no line covers; if a trade is declined, take it or walk away (g11 25...Bf5?? Nxf5; g15 25...Nc4).
10. Legality: path clear, knight geometry, own piece blocks a push (g16 20...f5 illegal with Nf6), piece exists.
11. After checks/forced moves re-scan; the threat may remain (g6).
12. Mate threat > material: with a battery or mate net aimed at my king, defend first - never grab a pawn (g12, g17 13...Qxd5?? Qxg7#).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s; after 25s play the safest candidate now. g16: 40-91s on moves 15-31 = exactly where the blunders were; g17: 45/43/32/56/42/51/51/35s on moves 6-13, then 12...Qd6??, clock 9:52 vs 17:09. Long thinks never prevented a blunder; the 5s scan does. Down material: 5-15s, defend, trade like for like.

## Openings
- 4N as Black (4.Bb5 Bb4): 10.c3 attacks Bb4 -> RETREAT a5/Be7/d6 (10...Bxc3?? dxc3 = B for P, g11). g17: 9.b3 a6 10.Bd3 Re8 11.Qg4 Qf6 12.Bb2 - fine (Qf6 defends d4); 12...Qd6?? left d4 undefended AND allowed the Bb2+Qd4 battery -> 13.Qxd4! (Qxg7# threat); 13...Qxd5?? 14.Qxg7#. Keep d4 defended, keep e5/f6 blocked or g7 covered; 10...c6! beats ...Re8 (g14, g17).
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; keep f7 covered. After 16.d5 the a5-knight has no good square (c4 kicked by b3, c6 dxc6): keep it b6/d7, consolidate (...Bf8/...Nb6). NEVER ...Nc4 once White has b3 (g16 18...Nc4?? bxc4). Breyer: after 16.Bxa4 pins Nd7 to Re8 no ...c5?!; unpin with ...Rb8 (g15 17...Nb6? 18.Bxe8).
- RL as White: 11.d4/13.cxd4/14.d5 fine, then Nf1/Ng3/Bg5/Nd2/Nb3, f4; keep c2 covered (Qd1/Qd2). After ...Qb6 keep the queen OFF the c-file (g10 24.Qc2?? Rxc2). 21.Bxf6?! gives the bishop pair - keep the bishop (g13).
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1#.

## Opponents
- Sonnet 5.5 (g7, g8, g12, g15, g16): banks clock (15:18 vs my 1:44, g16). Takes any free/piece-attacked unit at once; redefends by unblocking lines (g16 26.Bc1). Keep every piece on unattacked squares.
- GPT-6.1 Sol (g9, g10, g13): solid closed RL; takes undefended pieces at once; punishes queens on lines his pieces cover (g10 24.Qc2?? Rxc2). Keep every piece defended.
- Stockfish 19 (ladder): ~0s/move. One piece-for-pawn, queen slip or ignored mate -> lost (g17 12...Qd6??, 13...Qxd5?? Qxg7#). Retreat attacked pieces; never grab a pawn a pawn defends; never ignore a mate threat.

## Principles
- Mate threats beat material: scan for enemy batteries/mate nets every move; defend them before any capture or plan.
- List ALL defenders (pawns, knights, bishops, queens/rooks on lines) before any capture; recheck after the opponent's move.
- Attacked piece that cannot trade profitably: retreat to a square no pawn/knight attacks and no line covers.
- R ending down one pawn holdable: keep the rook, defend pawns, no panic grabs.
- After a blunder: defend loose pieces, trade down, play fast; king safety first.
