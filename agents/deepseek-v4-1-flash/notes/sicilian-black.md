# Sicilian as Black (g28 vs Stockfish 19, lost 0-1, mated m31)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nf6 5.Qxd4 Nc6 6.Qd3 g6 7.Be2 Bg7 8.O-O O-O 9.Rd1 a6 10.c4 Nd7 11.Nc3 Nc5 12.Qc2 Bd7 13.Be3 Rc8 14.h3 Qa5 15.Nd5 e6 16.Nc3 Bxc3 17.Bxc5 Qxc5 18.Qxc3 Qxc4?? 19.Bxc4 Rfd8 20.Rd3 b5 21.Bb3 Nd4?? 22.Qxd4 Rc7 23.Qe3 Bc6 24.Rad1 Bd5 25.e5 Bxf3 26.gxf3 dxe5 27.Rxd8+ Kg7 28.Qxe5+ f6 29.Qxc7+ Kh6 30.Qc1+ Kg7 31.R1d7#.

## Equal through 18.Qxc3 (eval -0.07)
- Dragon setup ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O, then ...a6, ...Nd7-...Nc5, ...Bd7, ...Rc8, ...Qa5 is sound. 16...Bxc3 17.Bxc5 Qxc5 18.Qxc3 trades both bishops for both knights and stays level.
- 15.Nd5 can NOT be taken by either knight (c6->d5, c5->d5 illegal). Attack it with ...e6 or ...c6/d6 push; 15...e6 16.Nc3 is fine - don't burn 94s here.

## 18...Qxc4?? (the game-loser, -0.07 -> +9.69)
- The c4 pawn is attacked by the e2-BISHOP (e2-d3-c4, d3 empty) and defended by Rc8 on the c-file. 'Defended' is irrelevant: 19.Bxc4 takes the QUEEN; even Rxc4 would only regain a bishop = Q for P+B (net -5).
- I thought 'queens can be exchanged afterward' - they cannot: White's Qc3 does not guard c4 and the bishop takes first. Never take a pawn with the queen while any bishop/knight/pawn can capture the queen.

## 21...Nd4?? (knight blunder, +9.57 -> +11.78)
- Down a queen I moved the c6-knight to d4: attacked by Qc3, Bb3, Nf3 and undefended. 22.Qxd4.
- While down material: keep every remaining piece on unattacked, defended squares; trade only on my terms; 5-15s moves, no new loose pieces.

## Time
- 44/30/46/36/45/53/43/34/94/34/45/95s on moves 1-18 (~10 min). The two 90s+ moves produced the 2 illegal tries (Nxd5 from c6: not a knight move; Qxc3 blocked by the c4 pawn) and then the Q-blunder. Routine Sicilian moves: 10-15s, then 5s destination scan.
