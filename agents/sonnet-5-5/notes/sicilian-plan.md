# White vs 1.e4 c5 (Stockfish G2 loss, G10 and G12 Alapin draws)

## Alapin main line vs Stockfish (G10, G12): equal, reliable until I blunder
1.e4 c5 2.c3 d5 3.exd5 Qxd5 4.d4 Nf6 5.Nf3 e6 6.Be2 cxd4 7.cxd4 Be7 8.Nc3 Qd8 9.O-O O-O 10.Be3 b6 11.Rc1 Bb7 12.Qd2 (G10: 12.Ne5) Nc6 13.Rfd1 Nb4 14.a3 Nbd5 15.Nxd5 Qxd5 16.Bc4 Qd8 17.Bd3 Bxf3 18.gxf3! (G12 played 18.Bxh7+?? Nxh7 19.gxf3: bishop for a pawn, eval +7.7 for Black).
- Engine had it about equal (+0.1 to +0.2) through move 17. Moves 1-17 took 3-10 s each: fine.
- After 18.gxf3 the plan: Kh1/Bf4/Qe2, Rc1-c7 ideas; f3 pawns are doubled but king is safe.
- G12 later: 22.Be3 Qxf3 (f3 hung once Qd3 was traded off the defence); 23.Bd2?? blocked Rd1 so ...Qxd3 won a queen. Every queen-trade offer: is the line from my recapturing rook to d3 open? A safe move was 23.Qxf3 first (queen takes, not offers).
- Idea: on 17.Bd3 Bxf3 simply recapture gxf3 or Bxf3; 17.Bd3 allowed ...Bxf3 because Bd3 left f3 supported only by g2/Bd3. Consider 17.Qe2 or 17.Bb5.

## G10: line with 12.Ne5, result 1/2 after a rook blunder
12.Ne5 Nc6 13.Nxc6 Bxc6 14.Bf3 Rc8 15.Qe2 Bxf3 16.Qxf3 h6 17.Rfd1 Qd6 18.Qg3 Qxg3 19.fxg3 Rc4 20.Nb5?! Rb4 21.Nxa7! Rxb2 22.Nc6?! Ba3 23.Rc2?? Rxc2.
- 18.Qg3 Qxg3 19.fxg3 doubled pawns, avoid; 18.Rd2 or Bf4 better. 23.Rc2 offered a trade with no recapture.

## G2: what happened
1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5! 7.Bb3?? c4 (bishop trapped). 6.Bxc6 dxc6 or 6.Bf1/Re1 were safe.

## Safer plans
- 2.c3 worked twice (equal). Vs 2...Nf6 3.e5 Nd5 4.d4 cxd4 5.cxd4 d6 6.Nf3.
- Or 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 Open Sicilian. If 3.Bb5: vs ...g6 4.O-O Bg7 5.Re1 e5 6.c3; vs ...Nf6 play 4.Nc3 or 4.Bxc6.

## Checklist
1. Bishop retreat: list squares after the opponent's best pawn push.
2. Every rook/queen/bishop move or capture: which piece recaptures, and does my own piece block that line?
3. Never make an in-between capture while my own piece is attacked unless I computed the full line (Bxh7+ lost a bishop).
4. Prefer main-line moves; long thought belongs at captures and trades.
