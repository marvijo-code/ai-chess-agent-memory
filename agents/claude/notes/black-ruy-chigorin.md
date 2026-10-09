# Black Closed Ruy / Chigorin (vs Sol: W T9SF2G1, T5R1, T6SF2G1; L T7R1, G3; D G4; vs DeepSeek: W T6R2, T7R2, T7R5.2, T11R2, T12R2)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 Nb4 15.Bb1 a5 (a3 Na6, ...Nc5) / 14.Nb3 / 14.Nf1 Bb7.

## T12R2 vs DeepSeek: WON (mate 30, 900+10, used ~2 min of 15)
14.Nf1 Bb7 15.Ng3 Rfe8 16.d5 Nb4 17.Bb1 a5 18.a3 Na6! 19.Be3 Nc5 20.Bxc5 dxc5 21.d6?! Bxd6 22.Qxd6?? Qxd6 23.Nd2 Qxd2 24.Nf1 Qxe1 25.Kh1 Qxf1+ 26.Kh2 Qxf2 ... Rad8, Rd1+, Qf4+ g3 Qf2#.
- Setup vs d5: ...Nb4, ...a5, a3 Na6 (Nc6?? dxc6), ...Nc5 guarded by d6/Qc7/Be7. Bxc5 dxc5 is fine for me.
- 21.d6 hits Qc7 but loses a pawn: Bxd6 is guarded by Qc7. After 22.Qxd6 Qxd6 he has no recapture. Then take what hangs, but check each capture: Re1 and Nf1 hung because Bb1 blocks Ra1; Qxb1 would lose to Rxb1.
- Conversion: Rad8-d1+ with the king on h2 and own pawns on g3/h3 gave Qf4+/Qf2#. Stalemate check every ply.

## T11R2 vs DeepSeek: WON (mate 34)
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.b4 axb4 18.axb4 Bd7! 19.Ba3 Nxb4 20.Bxb4 Rxa1! 21.Bxd6 Bxd6 22.Qa4?? Rxa4 ... mate.
- 18...Nxb4? allows Rxa8 (Bc8 blocks the Rf8 recapture), so 18...Bd7 first. Rxa1 works because Bb1 blocks both Qd1 and Re1 from a1. Check Ra1 defenders each move.

## T9SF2G1 vs Sol: WON (mate 67)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rfc8 18.a3 Na6 19.Be3 Nc5 20.Bc2 a4 21.Rc1 h6 22.Qe2 Rab8 23.Nf5 Bxf5 24.exf5 Rb6 25.Red1 Nfd7 26.g4 Bf6 27.g5 Bxg5 ... 30...Qb7 31.Qg4 Nf8 32.h4 Qd7 33.h5 Nh7 34.Qg6 Qe8 35.h6 Qxg6+ 36.fxg6 Nf8 37.h7+ Kh8 38.Bg5?? fxg5.
- Good: 23...Bxf5 (trade the outpost knight), 26...Bf6 vs g5, queen off the c-file, queen-trade offers + ...Nh7 killed the storm.
- Slip: 44...b4?? 45.Be6 threatened Rf8# (Kh8 boxed by g6/h7). Keep Nd7 guarding f8, Rc8 home.

## Other DeepSeek wins
T7R5.2: 14.Nb3 a5 15.dxe5 dxe5 16.Be3 a4 17.Nc5? Bxc5 18.Bxc5 Rd8! hits Qd1 with Qc7 behind.
T7R2: 14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rfc8 18.Be3 h6 19.Qd2 Nc2! 20.Bxc2 Qxc2 21.Qxc2 Rxc2; rook up.
T6R2: 16.a3 Na6 17.Qe2 Bd7 18.Nf1 Nc5 19.Ng3?? Nb3! forks Ra1+Bc1.
DeepSeek leaves pieces hanging: check 'defended?' before each capture.

## T7R1 vs Sol: LOSS (mate 36) after winning a piece
14.Nf1 Bd7 15.Ng3 Rac8 16.Be3 Nxd4! 17.Nxd4 exd4 18.Qxd4 Qxc2 19.Rac1 Qc4?? 20.Rxc4 (Q for R). List queen escape squares before a queen grab; 19...Qxb2/Qa4 were candidates.

## T6SF2G1 / T5R1 vs Sol (won)
SF2G1: 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Nc2! (31...Bxc5 was ILLEGAL: d6 blocks e7-c5).
T5R1: 24.Bd3! discovers Rc1 on Qc7; with Bc2 as sole blocker, move the queen first.

## G3 / G4 (Sol)
G3: pawn up, thrown away by 42...Qe6?? and 45...Bd4+??. G4: 28.f4 exf4?? opened e5 and the b1-h7 diagonal. Keep Kg8.

## Endgame
Q vs b-pawn is lost. No Rxh3 when gxh3. Ladder mate with two rooks: stalemate check every ply.
