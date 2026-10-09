# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 (14...Nb4 / 14...Nb8).

## What works (g2, 5, 9, 10, 13, 18)
- 11.d4, 13.cxd4, 14.d5 (! in several games), 15.Bb1 (!) are good. Main line 14...Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Bd7 18.Ng3 Nc5 fine.
- After 14.d5: Nf1/Ng3/Bg5/Be3/Nd2, f4; keep c2 covered (Qd1; Qd2 also covers c2/f2).
- 14...Nb8 (g10, g13, g18): 15.Nf1 Nbd7 16.Ng3 Bb7 17.Bg5 h6 18.Be3 Rfe8 19.Qd2 Bf8 20.Rad1 Nc5 was equal (g18).
- 21.Bxf6?! (g13) or 21.Bxc5?! dxc5 (g18) gives Black the bishop pair - keep the dark bishop; slow plan Rae1/f4/Nf5.
- 16.a3 safe only when BOTH Qd1 and Bb1 cover c2; otherwise 16.Rac1/Bb1 (g2 16.a3?? Nxc2 = Q for N).
- Never Bxf7+?? Rxf7 or Bxb5?? axb5 = B for P.

## g21 vs GPT-6.1 Sol (0-1, mated m29)
9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 14.d5 Nb4 15.Bd3?? Nxd3 16.Qe2 Nxe1 17.Qxe1 Bd7 18.Nc4 bxc4 19.Bd2 Rac8 20.Be3 Qb7 21.Qd1 Qxb2 22.Qb3 cxb3 23.axb3 Qxa1+ 24.Kh2 Rc3 25.Bd2 Rxb3 26.Nh4 Nxe4 27.Bc1 Qxc1 28.f3 Qf4+ 29.Kh1 Rb1#.
- 14...Nb4 15.Bb1! was the known move; 15.Bd3?? is a KNIGHT-MAGNET blunder: the b4-knight attacks a2, c2, d3, d5. 15...Nxd3 16.Qe2 Nxe1! = B+R for N. My in-game note listed "Nb4 attacks a2,c2,d3,d5" and I played d3 anyway - scan the FINAL move.
- After 14...Nb4 the only safe bishop squares: b1 (book). a2 and d3 are knight squares; c2 is attacked.
- 16.Qe2: Qxd3 is illegal (Nd2 blocks the d-file; 1 illegal try).
- 18.Nc4?? undefended onto a square the b5-pawn attacks: bxc4 = N for P. Not worth it; use Nd2-f1/Ng3 or Nf3.
- 22.Qb3?? (offering a queen trade on b2) cxb3! = Q for P: the c4-pawn attacks b3/d3. Check pawn attackers of a queen-offer square before moving the queen.
- Mate: 29...Rb1# - king h1, own g2 pawn blocks the flight, black queen covers h2. Same family as g10: enemy rook on rank 1 vs a cornered king with no luft.

## c-file, d5 and queen safety - chronic White losses (g9, g10, g13, g18)
- After 13.cxd4/14.d5 lines are open: never my queen/rook on a square any enemy slider attacks. g10 24.Qc2?? Rxc2; g9 23.Qxc3?? Qxc3, 24.Rc1?? Qxc1+.
- g18 23.Qd5?? lost the game: Bb7 took the queen; before any queen move list pawns, knights, king, rooks/queens on lines, BISHOPS on diagonals.
- Qd2 defends c2 and f2: before any queen move list what it stops defending (g13 25.Qxh6?? left Bc2).
- 26.Qh8+?? Kxh8 (g13). Never move the queen - even with check - where any enemy piece or the KING can capture.
- 21.b4? Na4! (g9).

## Game management
- g21: 3-21s book, then 43s on 12.Nbd2, 57s on 14.d5, 91s on 16.Qe2 (with an illegal try), then 15.Bd3?? - long thinks never fixed the scan. Black banked 15:16 vs my 5:19.
- Down material (g10, g13, g18): king safety first, defend loose pieces, trade, 5-15s moves.
- g2, 5, 9, 10, 13, 18: 30-117s routine moves, then the blunder; routine <=15s, the 5s scan is the fix.
