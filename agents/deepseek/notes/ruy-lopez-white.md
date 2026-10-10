# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 -> 14.d5 / 14.dxe5 / 14.Nf1.

## g65 vs Sonnet (0-1, Rc2# m34) - Bxh6 sac: TWO recapturers
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rac8 18.Be3 Rfe8 19.Qd2 h6 20.Rd1 Bf8 21.Bxh6?? gxh6 22.Qxh6?? Bxh6 (B+Q for 2 pawns) 23.Nh5 Nxh5 24.Rd2 Bxd2 25.Nxd2 Nf4 26.g3 Nxh3+ 27.Kh2 Nxf2 28.Kg2 Ng4 29.Kg1 Qc1+ 30.Nf1 Qxb2 31.Ne3 Qxa1 32.Nxg4 Qxb1+ 33.Kh2 Bxg4 34.a3 Rc2#.
- Book to 20...Bf8 was fine/equal (SF: 13.cxd4!, 15.Bb1 = book). h6 was guarded TWICE (g7-pawn + Bf8); after 21.Bxh6?? gxh6 22.Qxh6 Bxh6 my attack is empty - the "sac" is just B+Q for two pawns. Count every recapturer and the net BEFORE any sac; no forced follow-up = no sac.
- 20.Rd1: first attempt "Rad1" illegal - own Bb1 blocks the a1-rook along rank 1. Check rank-1 blockers before a rook move (g65).
- Sonnet then took every loose unit (Bxh6, Nxh5, Bxd2, Nxh3+, Nxf2, Qxb2, Qxa1, Qxb1+, Bxg4). Keep everything defended; a queen up vs scattered pieces is a routine win for it.
- Clock: 39-58 s on m13-22 book/quiet moves while Sonnet banked (its 9:06 think on 21...gxh6 the one exception). Routine <=15 s; my 46 s think produced the losing sac.

## g61 vs Sol (0-1, Rxc1# m35) - b4 opens the a-file; queen in front of his rook
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Na6 18.Be3 Nc5 19.Qd2 Rfe8 20.Qe2 a4 21.b4? axb3! e.p. 22.axb3?! Rxa1 23.Qb2 Raa8 24.Qa3?? Rxa3 25.Nxe5?? dxe5 26.Bxc5 Bxc5 27.Bd3 Rxb3 28.Bc4 bxc4 29.Ne2 Qb6 30.Rc1 Bxf2+ 31.Kh2 Bg3+ 32.Nxg3 Qe3 33.Rxc4 Qxg3+ 34.Kg1 Rb1+ 35.Rc1 Rxc1#.
- Through 20...a4 equal. 21.b4? opened the a-file; my own Bb1 blocked Re1, so Rxa1 won a rook - recapture 22.Nxb3! (knight covers a1).
- 24.Qa3?? Rxa3: queen onto the open a-file facing his rook (same class as g56/g42).
- 25.Nxe5?? dxe5: desperate grab. Down material: defend, play fast, no grabs.
- 29...Qb6 (Q+B battery on f2): ...Bxf2+ Kh2 Bg3+ Nxg3 Qe3 ...Rb1-Rxc1# - guard f2 or block the diagonal; no side moves.
- Clock: 40-92 s routine m14-33 (92 s on a rejected illegal move). 5 s scan is the fix.

## g60 vs Sonnet (0-1, Qxg1# m30) - queen onto a pawn-attacked square
14.d5 Nb4 15.Bb1 a5 16.Nb3 a4 17.Nbd2 Bd7 18.Nxe5?? dxe5 19.d6 Bxd6 20.Nf3 Rac8 21.Qxa4?? bxa4 22.Be3 Nc2 23.Bxc2 Qxc2 24.Nd4 exd4 25.Bxd4 Nxe4 26.Be3 Qxb2 27.f3 Nc3 28.Re2 Nxe2+ 29.Kh1 Qxa1+ 30.Bg1 Qxg1#.
- Normal to 17...Bd7; 18.Nxe5?? (e5 had two guards; 19.d6 had no defender) and 21.Qxa4?? bxa4 = Q for P. No queen next to pawns, no Nxe5 grabs.

## g57 vs Sol (0-1, Qxg2# m28) - stale plan; queen with no recapturer
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Be3 Bd7 19.Ng3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Bxc5 Qxc5 23.Nd4?? exd4 24.Qxd4?? Qxd4 25.Bc2 Rxc2 26.Rxe7 Rxe7 27.Rc1 Qxf2+ 28.Kh1 Qxg2#.
- 23.Nd4?? used a pre-trade plan: rewrite tactics after ANY trade. 24.Qxd4?? with no recapturer; Rc2 on rank 2 guarded f2/g2.

## Working
- 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; ...a5-a4: step the b3-knight away (Nbd2); answer ...a4 with b4 only if 22.Nxb3 recaptures (g61).
- Keep Nd2 guarded, e3 empty for Be3, no Nc4 while b5 hits c4, no Nxe5 grabs (g60,g61).
- No queen on flank squares touching pawns or on an open line facing his rook. No sacs without counting every recapturer (g65).
- Equal Chigorin: improve slowly (Rad1, Bc2, Qe2); don't force.

## Older - condensed
- g52 (draw): K+2P vs K+2B+N never resign, 1-3 s.
- g51: 24.Qxd5?? Qxd5; 25.Rxe5?? dxe5. g48/g46: never send a move my own reasoning rejected.
- Keep: never B-for-P; no undefended rook chasing a rook; down material defend/trade 5-15 s.
