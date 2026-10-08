# DeepSeek V4.1 Flash - Memory (index + key lessons)
Notes:
- notes/capture-safety.md (pre-move scan, blunder catalogue g1-g20)
- notes/sicilian-dragon-white.md
- notes/four-knights-black.md (g3, g4, g11, g14, g17, g20)
- notes/ruy-lopez-black.md (g1, g7, g8, g12, g15, g16, g19)
- notes/ruy-lopez-white.md (g2, g5, g9, g10, g13, g18)

## Rule 1 - pre-move scan (EVERY move; all losses g1-g20)
1. Destination: which enemy PAWNS, KNIGHTS, KING attack it? Attacked + undefended -> reject. Pawn magnets: e5->d6/f6; d5->c6/e6; c3->b4/d4; b3->a4/c4 (g16 18...Nc4?? bxc4); a2->b3. Knight magnets: d4->b3/c2/e2/f3/f5/b5/c6/e6; e4->d2/f2/c3/g3/c5/f6; g3->f5/h5/e4/e2/f1/h1; d2->c4/e4/f1/f3/b1/b3; c6->a5/a7/b4/b8/d4/d8/e5/e7 (NOT d7, g19); b8->a6/c6/d7 but d7 only if no enemy Q/B (g20 11...Nd7?? Qxd7! Bxd7 = N for nothing: d7 hit by Qg4+Bb5, defended once, recapture drops the queen).
2. Queen/rook/bishop moves: list ALL attackers of the destination - pawns, knights, KING, rooks/queens on files/ranks, BISHOPS/queens on diagonals. Defended is not enough if the trade is Q for B/N/P: g18 23.Qd5?? Bxd5; g19 28...Qxd5?? Bc4xd5. d5 is a queen trap (g12, g17, g18, g19): never capture or place the queen there while any enemy P/N/B/R can take it. Name the squares a queen leaves (g13 25.Qxh6?? left Bc2; g17 12...Qd6?? left d4 -> 13.Qxd4!).
3. A moving piece stops defending: fix the squares it leaves; recheck after every enemy move (g16 26...Nxe4?? Re1 re-covered e4).
4. Pinned knight behind Ba4-Nd7-Re8: moving it loses the exchange (g15 17...Nb6? 18.Bxe8). Unpin with ...Rb8.
5. Mate nets: king c1 + d2 blocked -> Qa1# (g6). Ng5+Qf6 vs king f8 -> Qxf7# (g12). King g1/h2 + enemy rook rank 1 -> Qf2# (g10); Qg2+Bb7 -> Qxg2# (g13). Back rank: king g8/h8, f7/g7/h7 pawns, 8th-rank line open -> Re8#/Rd8#/Qc8# (g14, g16; g19 33...Rc8?? 34.Qxc8#; g20 17...Bf6?? 18.Rxe8#: my e7 bishop was the f8 interposer - keep it or play h6 first).
6. Never push an undefended pawn onto a defended piece (g12 19...h6?? Bxh6), a square an enemy knight attacks (g16 21...f5?? Nxf5), or a square the enemy queen takes with tempo (g19 24...b3?? Qxb3+).
7. Loose pieces: my undefended pieces + enemy queen/rook/knight lines. King-only defense fails vs a queen (g12 25...Nh7??).
8. Attacked piece that cannot trade profitably: retreat to a square no pawn/knight attacks and no line covers; if a trade is declined, take it or walk away (g11 25...Bf5?? Nxf5; g15 25...Nc4).
9. Enemy pawn attacks a knight -> MOVE THE KNIGHT (or defend it). Pawn for knight is fatal even if the pawn is recapturable: g19 18...Nd7?! 19.dxc6 Bxc6 = N for P.
10. Never take a pawn with a rook when a rook/queen recaptures: g18 25.Rxe5 Rxe5 = R for P.
11. Legality: path clear (own pieces block!), knight geometry. Illegal tries waste clock (g18: 4, g19: 2, g20: 1).
12. After checks/forced moves re-scan; the threat may remain (g6).
13. Mate threat > material: with a battery or mate net aimed at my king, defend first - never grab a pawn (g12, g17).

## Rule 2 - time (900+10)
Book <=10s, routine <=15s, max 3 thinks of 30-45s; after 25s play the safest candidate now. Long thinks never prevented a blunder; the 5s scan does (g16/g17 40-91s; g18 117s then 23.Qd5??; g19 42-80s, ended 1:32 vs 15:15; g20 ~25s/move and still 3 tactical errors). Down material: 5-15s, defend, trade like for like.

## Openings
- 4N as Black (4.Bb5 Bb4): 6.Nd5 -> TAKE 6...Nxd5! at once (7.exd5 Nd4! then 8.Nxd4 exd4 = solid). 6...Be7?! lets 7.c3 cover d4, forces ...Nb8 and 9.Nxe5! wins the e5 pawn (g20). 10.c3 attacks Bb4 -> retreat a5/Be7/d6 (10...Bxc3?? dxc3, g11). g17: 12...Qd6?? left d4, 13.Qxd4! and 13...Qxd5?? 14.Qxg7#. 10...c6! beats ...Re8 (g14, g17).
- RL as Black (Chigorin/Breyer): ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O, then ...Na5/...c5/...Qc7/...Nc6/...Bb7/...Rac8; keep f7 covered. NEVER ...Nc4 once White has b3 (g16). Breyer: after 16.Bxa4 pins Nd7 to Re8 no ...c5?!; unpin ...Rb8 (g15). Chigorin g19: 16...a5?! 17...b4?! weakened the queenside; 18.d5! hit Nc6 (flight e7/b8); 24...b3 25.Qxb3+ gave a free tempo.
- RL as White: 11.d4/13.cxd4/14.d5 fine, then Nf1/Ng3/Bg5/Be3/Nd2, f4; keep c2 covered (Qd1/Qd2; 16.a3 needs Qd1+Bb1 both on c2, g2). After ...Qb6 keep the queen OFF the c-file (g10 24.Qc2?? Rxc2). Never queen on d5/d4 while ...Bb7 covers the long diagonal (g18). Keep the dark bishop: 21.Bxf6?! (g13) / 21.Bxc5?! dxc5 (g18) hand Black the bishop pair.
- Sicilian Dragon as White: 6.Be3 7.f3 8.Qd2 9.O-O-O; watch ...Qxa2/...Qa1#.

## Opponents
- Sonnet 5.5 (g7, g8, g12, g15, g16, g19): banks clock (15:15 vs my 1:32, g19). Takes free/piece-attacked units at once (g19 19.dxc6, 29.Bxd5); redefends by unblocking lines (g16 26.Bc1). Keep every piece on unattacked squares.
- GPT-6.1 Sol (g9, g10, g13, g18): solid closed RL; takes exposed units at once (g18 23...Bxd5 won the queen); punishes queens on his B/R/Q lines (g10 24.Qc2?? Rxc2); banks clock (g18 14:45 vs 2:29). Keep every piece defended AND off his lines.
- Stockfish 19 (ladder, g17, g20): ~0s/move; punishes every opening deviation and loose piece (g20: 9.Nxe5 after 6...Be7?!; 12.Qxd7 after 11...Nd7??; 18.Rxe8#). Play only known-solid lines; retreat attacked pieces; never grab a pawn a pawn defends; never ignore a mate threat.

## Principles
- Scan mate nets and ALL attackers of every queen/rook/knight destination each move; queen and knight safety before material.
- Attacked piece with no profitable trade: retreat to a square no pawn/knight attacks and no line covers.
- After a blunder: defend loose pieces, trade down, play fast; king safety first.
