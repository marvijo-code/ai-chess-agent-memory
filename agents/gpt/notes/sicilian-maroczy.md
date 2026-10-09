# Sicilian Maroczy: exchanges, passers and rook checks

## Opening geometry
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5.
- Qa5 pins Nc3 to Ke1 via b4/c3/d2. Nc3 cannot recapture on e4/d4. Qd1 can recapture on d4 only while d2/d3 remain clear. f3 supports e4; Bd2 obstructs Qxd4.
- T14: 7.Nb3 Qd8 8.Be2 d6 9.O-O b6 10.Be3 Bg7 11.Rc1 Bb7 12.Qd2 Nd7 13.f3 Nc5 14.Nxc5 dxc5. Nb3 avoided the earlier forcing pawn-loss sequence; this game does not establish optimal preparation.
- 15.Nd5 e6 16.Nc3 Qxd2 17.Bxd2! O-O-O 18.Be3 Nd4. My claim that d6 was a pawn target was false: ...dxc5 had already vacated d6. Reconstruct pawn locations after exchanges.

## T14 round 1: White vs Stockfish 19, mate loss
### Rook exchange creates a passer with tempo
19.Bxd4? Rxd4? 20.Rfd1 Rhd8 21.Rxd4? cxd4 22.Na4 d3 23.Bf1 Bc6 24.Nc3 d2 25.Rd1 Bd4+ 26.Kh1 Bxc3 27.bxc3 Ba4 28.Be2 Bxd1 29.Bxd1.
- Both 19.Bxd4 and 21.Rxd4 were marked mistakes; Black's 19...Rxd4 was also marked a mistake. No engine-best replacements were supplied. Evaluate both ...cxd4 and ...Rxd4 rather than assuming a pawn recapture or cooperative rook exchange.
- 21...cxd4 attacked Nc3; ...d3 then attacked Be2. Black retained Rd8 behind the passer and two active bishops. Equal material after the rook trade did not mean reduced pressure.
- ...Bc6 attacked Na4. Nc3 returned the knight to a square where ...Bxc3 removed it and damaged the structure. ...Ba4 then attacked the rook bound to d1; Be2 allowed a recapture but conceded rook for bishop. Black emerged with R against B and equal pawn counts.
- Before a rook trade, inspect the pawn recapture, its attacks, the surviving rook's file and whether the blockade can be attacked by another piece.

### Enemy capture removes the bishop's recapture protection
After exf5 exf5, Kd1 and Bd5 screened Rd8 from d2:
39.Bd5 b5 40.Kxd2 bxc4 41.Ke2 Rxd5.
- Bd5 made Kxd2 legal by blocking the rook's file. White's c4 pawn defended Bd5 and could recapture a rook on d5.
- ...bxc4 removed that defender. The bishop still screened Rd8 but now had no recapture protection; Ke2 ignored its exposure. Removing the passer did not finish the safety calculation.
- Recompute my attacked pieces and defenders after every enemy capture. A screen that enabled a king capture may itself need immediate rescue.

### Promotion skewer
White Kh5/h7, Black Rg2/Ke6: 55.h8=Q Rh2+ 56.Kg6 Rxh8.
- Rh2 checked up the h-file, forcing the king away and exposing Qh8. The promoted queen did not control h2 because my king on h5 blocked its line.
- Before promotion, test every rook check from behind or beside the king and whether the king can leave while preserving the promoted piece. No saving alternative was established here.

### Final rook mate
After 69.Ka5 Kc5, White had Ka5 and pawns a4/c4/f3; Black Kc5/Rb8.
70.f4 Ra8#.
- ...Kc5 threatened mate: it controlled b4/b5/b6. My own a4 pawn occupied the remaining downward escape; ...Ra8 checked along the clear a-file and controlled a6.
- A distant passer supplied no tempo against mate. Enumerate enemy rook checks and all king escapes before a pawn push, especially near the edge.
- No invalid attempts; 15:03 after Rxd4, 10:30 at mate. Long calculations and sparse marks did not prevent these concrete misses.

## Earlier failures to retain
- T12/T7: 7.f3 Nxd4 8.Qxd4 Bg7 9.Qd2?! d6 10.Be2 Be6 11.O-O Bxc4 12.Bxc4 Qc5+ 13.Qf2 Qxc4 lost c4. The intermediate check enabled the second capture.
- T12 16.Nd5?? Nxd5 exd5 Qxa2: Black removed the proposed forking knight first. Moving both knights opened Bg7's diagonal to b2; Rac1 had abandoned a2.
- Qa2/Rb8 versus Rb7: Rb3?? Qxb3 lost the rook on a2-b3. b2 attacks a3/c3, not b3. A retreat's purpose does not establish destination safety.
- With Ra3/Rb8 blockading b7, Ba7?? Rxa7 lost the bishop to the OTHER rook while preserving the blockade.
- T8 Qb4?? Rxb4+ cxb4 Qxb4+ lost queen for rook. Count the complete liquidation; later repetition did not prove compensation.
- Rb1?? axb1=Q lost a rook: a2 can promote on a1 or capture-promote on b1. Scan both.
