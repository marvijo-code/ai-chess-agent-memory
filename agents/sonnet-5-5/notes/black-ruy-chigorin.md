# Black Closed Ruy / Chigorin (vs Sol: T9SF2G1 W, T5R1 W, T6SF2G1 W, T7R1 L, G3 L, G4 D; vs DeepSeek: T6R2, T7R2, T7R5.2, T11R2 W)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 Nb4 15.Bb1 a5 (a3 Na6, ...Nc5) / 14.Nb3 / 14.Nf1.

## T11R2 vs DeepSeek: WON (mate 34, 900+10, used ~1 min of 15)
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.b4 axb4 18.axb4 Bd7! 19.Ba3 Nxb4 20.Bxb4 Rxa1! 21.Bxd6 Bxd6 22.Qa4?? Rxa4 23.Nc4 Rxc4 ... Qxe1+, Qxe4, mate Qe2#.
- 18...Nxb4? would allow Rxa8 (Bc8 blocks Rf8 recapture), so 18...Bd7 first. Then 19...Nxb4 threat is real; Bxb4 Rxa1 works because Bb1 blocks BOTH Qd1 and Re1 from guarding Ra1. SF marks: 14... 15...a5!, 16...Na6!, 20...Rxa1!.
- Pattern: vs 16.a3 Na6 17.b4 axb4 18.axb4, check Ra1 defenders each move; the Bb1 retreat blocks the d1/e1 line to a1.
- Conversion: kept everything protected, luft ...h6, traded rooks, stalemate check; DeepSeek only blundered more.

## T9SF2G1 vs Sol: WON (mate 67, 900+10, I had 5 min left, Sol 2)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rfc8 18.a3 Na6 19.Be3 Nc5 20.Bc2 a4 21.Rc1 h6 22.Qe2 Rab8 23.Nf5 Bxf5 24.exf5 Rb6 25.Red1 Nfd7 26.g4 Bf6 27.g5 Bxg5 28.Nxg5 hxg5 29.Bxg5 f6 30.Be3 Qb7 31.Qg4 Nf8 32.h4 Qd7 33.h5 Nh7 34.Qg6 Qe8 35.h6 Qxg6+ 36.fxg6 Nf8 37.h7+ Kh8 38.Bg5?? fxg5 (piece up) ... ladder mate.
- Good: 23...Bxf5 (trade outpost knight), 26...Bf6 vs g5, 30...Qb7 (queen off the c-file), queen-trade offers + 33...Nh7 killed the storm.
- Slips: 44...b4?? 45.Be6 threatened Rf8# (Kh8 boxed by g6/h7). Keep Nd7 guarding f8, Rc8 home.

## T7 R5.2 vs DeepSeek (WON, mate 35)
14.Nb3 a5 15.dxe5 dxe5 16.Be3 a4 17.Nc5? Bxc5 18.Bxc5 Rd8! hits Qd1 with Qc7 behind. Check ...Rd8 when Qd1 faces the d-file. DeepSeek leaves pieces hanging: check 'defended?' before each capture.

## T7R2 / T6R2 vs DeepSeek (WON)
T7R2: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rfc8 18.Be3 h6 19.Qd2 Nc2! 20.Bxc2 Qxc2 21.Qxc2 Rxc2 22.Rac1 Rxb2 23.Rc2? Rxc2; rook up.
T6R2: 16.a3 Na6 17.Qe2 Bd7 18.Nf1 Nc5 19.Ng3?? Nb3! forks Ra1+Bc1. Setup vs d5: ...Nb4, ...a5, ...Na6, ...Bd7, ...Nc5.

## T7R1 vs Sol: LOSS (mate 36) after winning a piece
14.Nf1 Bd7 15.Ng3 Rac8 16.Be3 Nxd4! 17.Nxd4 exd4 18.Qxd4 Qxc2 19.Rac1 Qc4?? 20.Rxc4 (Q for R). List queen escape squares before any queen grab; 19...Qxb2/Qa4 were candidates.

## T6SF2G1 vs Sol (won, mate 63) and T5R1 (won)
SF2G1: 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Nc2! 31...Bxc5 was ILLEGAL (d6 blocks e7-c5).
T5R1: 24.Bd3! discovers Rc1 on Qc7; queen on c-file facing Rc1 with Bc2 sole blocker: move the queen first.

## G3 / G4 (Sol)
G3: 22...Na6 pawn up, thrown away by 42...Qe6?? and 45...Bd4+??. G4: 28.f4 exf4?? opened e5 / b1-h7 diagonal. Keep Kg8.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Ladder mate with two rooks: stalemate check every ply.
