# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 (14...Nb4 / 14...Nb8).

## What works (g2, 5, 9, 10, 13)
- 11.d4, 13.cxd4, 14.d5 (! in four games), 15.Bb1 (!) are good. Main line 14...Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Bd7 18.Ng3 Nc5 fine.
- After 14.d5: Nf1/Ng3/Bg5/Nd2/Nb3, f4; keep c2 covered (Qd1; Qd2 also covers c2/f2 - remember that when the queen leaves).
- 14...Nb8 (g10, g13): 15.Nf1 Nbd7 16.Ng3 Bb7 17.Bg5 h6 18.Bh4 Rfe8 19.Nf5 Bf8 20.Qd2 Rad8 was equal. 21.Bxf6?! (engine) gives Black the bishop pair after ...Nxf6 and ...Bxf6; keep the bishop and improve with Rae1/f4/g3 - no forcing breakthrough, a slow plan is fine.
- 16.a3 is safe only when BOTH Qd1 and Bb1 cover c2; otherwise 16.Rac1/Bb1 (g2 16.a3?? ...Nxc2 = Q for N).
- Never Bxf7+?? Rxf7 = B for P; Bxb5?? axb5 likewise.

## c-file and queen safety - chronic White losses (g9, g10, g13)
- After 13.cxd4 the c-file is open: never my queen/rook on c2/c3/c1 (g10 24.Qc2?? Rxc2 = Q for R; g9 23.Qxc3?? Qxc3, 24.Rc1?? Qxc1+). After ...Qb6 unpin with Kh2 or play Rd1, queen on d1/e2/d2.
- Qd2 defends c2 and f2: before any queen move list what it stops defending (g13 25.Qxh6?? left Bc2 loose; 25...Qxc2! won the bishop, then his queen ate e4, d5 and mated: 29...Qxg2#, Bb7 backs g2, my Nf1 does not guard g2).
- 26.Qh8+?? Kxh8 = QUEEN FOR PAWN (g13 m26): h8 is next to the king on g8 and undefended (Bf6 covered it too). Never move the queen - even with check - to a square any enemy piece or the KING can capture. The 'Bg7 then Qh5' idea never happens.
- 21.b4? Na4! (g9); after ...Na4 the knight goes to c3 with Qc7 behind.

## The 15...Nb4 moment (g2)
- 16.a3?? 16...Nxc2 forks Ra1 and Re1; Qc7 protects c2; 17.Qxc2 Qxc2 = queen for knight. Safe: 16.Rac1 or 16.Bb1. 16.Bd3 hangs to Nxd3.

## Game management
- g2, g5, g9, g10, g13: 30-85s/move on routine moves, then the blunder; g13: 84s + illegal try on 22.Ne3, ended 6:28 vs 13:48; 26.Qh8+ came after a 44s think. Routine <=15s; the 5s scan is the fix, not more time.
- Down queen for rook (g10) or queen for pawn (g13): king safety first, defend, trade, 5-15s moves. g10 mate: 32...Qf2# (rook on rank 1); g13 mate: ...Qxg2# (Bb7 backs g2).
