# White vs 1.e4 c5 (Stockfish G2 loss, G10/G12 Alapin draws, G16 Alapin loss)

## Alapin main line vs Stockfish (G10, G12, G16): equal to move 17, then I drift
1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 e6 6.Be2 cxd4 7.cxd4 Be7 8.Nc3 Qd8 9.O-O O-O 10.Be3 b6 11.Rc1 Bb7 12.Qd2 (G10: 12.Ne5) Nc6 13.Rfd1 Nb4 14.a3 Nbd5 15.Nxd5 Qxd5 16.Bc4 Qd8 17.Bd3 (G12) or 17.Qe2 (G16).
- G12: 17.Bd3 Bxf3 18.gxf3! (18.Bxh7+?? Nxh7 lost a bishop). Later 23.Bd2?? blocked Rd1 so ...Qxd3 won a queen.
- G16 loss: 17.Qe2 Nd5 18.Bxd5? Qxd5 (eval +0.6 Black; Qd5+Bb7 hit g2, Nf3 pinned, Ne5 impossible) 19.Rc3 (passive) Rfc8 20.Rxc8+ Rxc8 21.Rc1 Rxc1+ 22.Bxc1 Qf5 23.Qe3 Bxf3 24.Qxf3?? Qc2! (hits Bc1 + b2, back rank has no luft) 25.Be3 Qb1+ 26.Bc1 Qxc1+ 27.Qd1 Qxd1#.
- Fixes for next time: (a) play h3 around move 12-13 (luft, also kills ...Bg4/...Ng4). (b) 17.Qe2 Nd5: do not trade 18.Bxd5; 18.Bd3 or 18.Nd2?? is risky - prefer 17.Bd3 or 17.Bb5 so the Nd5 jump is met by Bxd5 only when recapture Bxd5 is useless for Black. (c) 19.Rc3 was too passive; 19.Rc2/Rxc... check, or 19.Bd3 with h3 ideas. (d) After 23...Bxf3 recapture 24.gxf3 (Qe3 keeps Bc1 defended; f3 doubled but Qxf3 Qxf3 trades safely). Never leave the lone Bc1 undefended while my queen leaves e3. (e) Once rooks are traded and my queen is tied to d1, a single queen check wins: count luft first.
- Move 25 alternatives were all lost; the mistake was 24.Qxf3. Engine marks: 22.Bxc1! (only), 24.Qxf3??.

## G10: line with 12.Ne5, result 1/2 after a rook blunder
12.Ne5 Nc6 13.Nxc6 Bxc6 14.Bf3 Rc8 15.Qe2 Bxf3 16.Qxf3 h6 17.Rfd1 Qd6 18.Qg3 Qxg3 19.fxg3 Rc4 20.Nb5?! Rb4 21.Nxa7! Rxb2 22.Nc6?! Ba3 23.Rc2?? Rxc2.
- 18.Qg3 Qxg3 19.fxg3 doubled pawns, avoid; 23.Rc2 offered a trade with no recapture.

## G2: what happened
1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5! 7.Bb3?? c4 (bishop trapped). 6.Bxc6 dxc6 or 6.Bf1/Re1 were safe.

## Alternatives
- Consider 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Open Sicilian if Alapin keeps giving Black free development. If 3.Bb5: vs ...g6 4.O-O Bg7 5.Re1 e5 6.c3; vs ...Nf6 play 4.Nc3 or 4.Bxc6.
- Vs 2...Nf6 3.e5 Nd5 4.d4 cxd4 5.cxd4 d6 6.Nf3.

## Checklist
1. Bishop retreat: list squares after the opponent's best pawn push.
2. Every rook/queen/bishop move or capture: which piece recaptures, does my own piece block, and which of my pieces lose protection when the queen moves?
3. Never make an in-between capture while my own piece is attacked unless computed.
4. Back rank: luft before trading rooks.
5. Prefer main-line moves; long thought belongs at captures and trades.
