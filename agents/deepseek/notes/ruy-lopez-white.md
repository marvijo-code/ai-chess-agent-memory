# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 -> 14.d5 / 14.dxe5 / 14.Nf1.

## g60 vs Sonnet (0-1, Qxg1# m30) - queen onto a pawn-attacked square
14.d5 Nb4 15.Bb1 a5 16.Nb3 a4 17.Nbd2 Bd7 18.Nxe5?? dxe5 19.d6 Bxd6 20.Nf3 Rac8 21.Qxa4?? bxa4 22.Be3 Nc2 23.Bxc2 Qxc2 24.Nd4 exd4 25.Bxd4 Nxe4 26.Be3 Qxb2 27.f3 Nc3 28.Re2 Nxe2+ 29.Kh1 Qxa1+ 30.Bg1 Qxg1#.
- Normal equal Chigorin through 17...Bd7 (SF: 13.cxd4!, 15.Bb1!; 18.Nxe5?? the losing move).
- 18.Nxe5??: e5 is guarded by BOTH the d6-pawn and Nf6; the planned 19.d6 fork fails because d6 has no defender - Nd2 sits on d2 blocking Qd1 - so Bxd6 just takes it: knight for a pawn. Before a capture that relies on a follow-up, verify every piece it needs is in place on the CURRENT board.
- 21.Qxa4?? bxa4: my queen stepped onto a square the b5-pawn guards and NOTHING recaptured on a4. Before any queen move list the enemy PAWNS touching the destination (a4: b5; also b4/c4 on a5). Same class as g58 22...Qxd5?? cxd5.
- After that pure defense; 28.Re2 walked into Nxe2+ (check the enemy knight's attack squares too).
- Sonnet took every free unit: bxa4, 22...Nc2 fork, 25...Nxe4, 26...Qxb2.
- Clock: 35-51 s on m11-22 routine moves and the queen still hung; 7 min left at m29. The 5 s destination scan is the fix.

## g57 vs Sol (0-1, Qxg2# m28) - stale plan; queen with no recapturer
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Be3 Bd7 19.Ng3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Bxc5 Qxc5 23.Nd4?? exd4 24.Qxd4?? Qxd4 25.Bc2 Rxc2 26.Rxe7 Rxe7 27.Rc1 Qxf2+ 28.Kh1 Qxg2#.
- Sol plays standard Chigorin and takes free pieces instantly; no exploitable error found in his play.
- 23.Nd4?? came from an idea formed BEFORE 22.Bxc5 - the e3-bishop the plan needed was already traded. After ANY trade, rewrite the tactics on the current board.
- 24.Qxd4?? Qxd4 with no recapturer (my last knight was gone). Same class as g48/g50/g51.
- Qxf2+/Qxg2#: his Rc2 guarded f2/g2 along rank 2, so Kxf2/Kxg2 were illegal. When his queen nears my king, check every rook on the 2nd rank.
- Clock: 1:44 (illegal try) + ~60 s per routine move m17-20; ended 5:06 vs 16:02 and was mated.

## g56 vs Sonnet (0-1, m33)
14.Bb3 Bd7 15.dxe5 dxe5 16.Nc4?? bxc4 17.Bxc4 Be6 18.Bxe6 fxe6 19.Qd6?? Bxd6. 16.Nc4: b5-pawn hits c4; play quiet Nf1/Be3. 19.Qd6: Be7 and Qc7 both cover d6, no recapturer.

## Working
- 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; ...a5-a4: step the b3-knight away (Nbd2).
- Keep Nd2 guarded, e3 empty for Be3, no Nc4 while b5 hits c4, no grabs on e5 (g60).
- No queen on flank squares touching pawns (a4/a5/b4/b5/c3/f3/h3).

## Older - condensed
- g52 (draw): Re2/Nf1 defend c2 and d2; then K+2P vs K+2B+N: Sonnet failed to mate ~19 moves -> 1/2 by repetition. NEVER resign; 1-3 s.
- g51 (0-1 m34): 24.Qxd5?? Qxd5 (Qc5 guarded d5); 25.Rxe5?? dxe5.
- g48/g46: never send a move my own reasoning rejected; a rook entering an open file facing my queen -> queen leaves THAT move (g46 17.Qe2!).
- Keep (g10,g13,g18,g21,g22,g23,g33,g37,g40,g43): never B-for-P; if my capture opens a file my rook is on, fix the rook first; no undefended rook chasing a rook; down material: defend loose pieces, trade, 5-15 s; vs ...Nd7 resolve the centre BEFORE 15.d5; vs Nf5/Ng5+Qh5 play ...g6.
