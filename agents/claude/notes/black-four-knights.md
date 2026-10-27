# Black vs 1.e4 e5 2.Nf3 Nc6 3.Nc3 (SF plays it every time; 1 W, 11 L, 15 D)

3...Nf6 4.Bb5 Bb4, then 5.O-O (line A, all recent games) or 5.Nd5 (line B). NEVER 3...Bc5 (4.Nxe5!).

## LINE A: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (NOT bxc6)
10.Bc4 Bd6! 11.d4 Qh4! 12.g3 Qxd4 = pawn up (SF -1.4). Rf8 stays until Bc8 is out (Bxf7+, Qxc6). T39F W, T38SF D, T40R4 L, T40F D, T42R1 D, T45R4 D, T71R4 D.

### THE b7 HOLE (T45R4 AND T71R4, same slip twice)
- 13.Bb3 Be6 (SF ?!) 14.Bxe6 fxe6 15.Qb3 hits b7 AND e6. 15...Qd5? 16.Qxb7 Rfb8 17.Qa6: pawn back, level, then I drifted. ORDER: 15...Qd7 or 15...Rab8 (guard b7 FIRST), unverified. Also try something other than 13...Be6 (unverified: 13...Qd6 only if Bxf7+ is checked).
- T71R4 after 17...Be5 18.c3 Qb5 19.Qxb5 Rxb5: ending a pawn down (a2 b2 c3 f2 g3 h2 v a7 c6 e6 g7 h7), SF +0.9. Then 20...Kf7, 22...a5?!, 26...Rd7? (2:20 think) 27.Rxc6 +4, 34...Rd5 (3:35), rooks traded into K+P: a-pawn queened m40. Long thinks found nothing. Be5 tied to Rb5 on the 5th rank, c6 tied to Rd6: every rook move abandoned one of them. Before the queen trade count pawns by file; a pawn-down R+B ending needs a fortress plan at once, not K shuffles.
- DRAW SAVE v Q: pawn on c3 with K b2/b3 shuttle: the queen cannot pin and stop it, SF repeated at +9 (m59). 8 rejected tries that game (K steps onto queen lines): read the legal king squares from tools/legal-moves.py.

### Other move-15 choices (Be6 not yet played)
- T39F 15...Rfe8 16.c3 Be5 17.Bd1 Bxd1: ...Bxd4 Rxd4 Rad8 trades, h6 luft FIRST, ...b6, ...c5, ...cxb4: 6v5 WIN. T40F 15...c5 16.Be3 Rad8 17.c3 h6 (SF -1.8 sank to 0 by m27). T40R4 15...Rfd8 16.c3 Bd5 17.Rfd1 Bxb3 18.axb3 b6?! 19.b4 h6 20...Be7? 21.Rxd8+ Rxd8? 22.Rxa7: a7 guarded by Ra8 ONLY.
- T42R1 D: 11...Qd7?! instead of Qh4: no pawn won; shuffled Qd7/Qd6, SF crept to +2. Play 11...Qh4.

### Endings v SF
- T45R4 (D m68): R+B v R+B drift (...Kf7, ...a5, ...Rb5, ...Bb6) = SF +2; 40...Rh5?? gxh5 (g4 pawn hits h5). Fortress saved it: Bb6, pawns a5/c6, K c7/d7/d6. Next time ...g6/...h5 early vs g4, rook active, no ...e5.
- T40F: K shuffles, 40.Bg5 Bf6?? Bxf6 Kxf6 Kf4: keep bishops. T40R4 L: Rc8 + Bd6 + K tied to c7 while his K walked g2-f3-g4-f5-g6: ...g6/...h5 early, rook on the e-file. T38SF: 28...Rh5 29.h4 g4 trapped the rook (own h6 blocked): rook back to d7/e8.

### 10.Bc4 Be6 (5 D): DROP
Bxe6 fxe6 Qb3 Qe7 d4 Rab8 Be3 = +0.5..+1; Rb8 the ONLY guard of b7. No ...a5, no ...Bb4.

## Left the book (T30R3 L)
7...Ne7? 8.Nxe5. 7...e4! is the move. Others: 10...Bc5 11.Re1 Re8?? 12.Qxf7+; 10...Qd6 11.c3!; 9...bxc6?? 10.d4; 10...Bxd2?? 11.Rd1!

## LINE B: 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 Qe7 8.dxc6 dxc6 9.Bxc6+ bxc6 10.Nd4 Bd7!
Castle, d3 exd3 cxd3 Rfe8, Qxe7 (SF about -0.2). T18R1 L: 14...Rxe7 15.Bf4 Bd6; try 14...Bxe7. T16SF2G1 L: 10...c5?! 11.Nc6!
