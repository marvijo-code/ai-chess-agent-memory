# Sicilian as Black (g28,g29)

## g29 vs Sonnet 5.5 (Richter-Rauzer, 0-1, mated m20)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4 10.Qxd4 Bd7 11.Bxf6 Bxf6 12.Qd2 Qa5 13.Kb1 Bxc3 14.Qxc3 Qxc3 15.bxc3 Rac8 16.Rxd6 Rxc3?? 17.Rxd7 Rxc2?? 18.Kxc2 Rc8+ 19.Kb2 Rd8?? 20.Rxd8#.
- Setup ...e6/...Be7/...O-O/...Nxd4/...Bd7/...Qa5/...Bxc3/...Qxc3/...Rac8 was fine; equal through 15...Rac8.
- 16.Rxd6: d6 was undefended and the rook attacks Bd7. 16...Rxc3?? ignored it: 17.Rxd7 won a bishop, then 17...Rxc2?? dropped the rook to 18.Kxc2 (c2 undefended, his king adjacent). Save/defend/trade the attacked piece first (16...Bc6/...Rfd8/...Rc7 ideas); never grab a pawn while a piece hangs.
- 19...Rd8??: king g8 + pawns f7/g7/h7 = no luft, his rook on d7 -> 20.Rxd8#. Keep a back-rank guard or give luft before touching the 8th rank.
- Time: 46-53s on routine moves 13-19 and three blunders; the 5s destination scan was never run.

## g28 vs Stockfish 19 (0-1, mated m31)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nf6 5.Qxd4 Nc6 6.Qd3 g6 7.Be2 Bg7 8.O-O O-O 9.Rd1 a6 10.c4 Nd7 11.Nc3 Nc5 12.Qc2 Bd7 13.Be3 Rc8 14.h3 Qa5 15.Nd5 e6 16.Nc3 Bxc3 17.Bxc5 Qxc5 18.Qxc3 Qxc4?? 19.Bxc4 Rfd8 20.Rd3 b5 21.Bb3 Nd4?? 22.Qxd4 Rc7 23.Qe3 Bc6 24.Rad1 Bd5 25.e5 Bxf3 26.gxf3 dxe5 27.Rxd8+ Kg7 28.Qxe5+ f6 29.Qxc7+ Kh6 30.Qc1+ Kg7 31.R1d7#.
- Dragon-type setup (...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O, then ...a6, ...Nd7-...Nc5, ...Bd7, ...Rc8, ...Qa5) sound; equal through 18.Qxc3. 15.Nd5 cannot be taken by either knight (c6/c5 -> d5 illegal); meet it with ...e6 or a push; don't burn 90s.
- 18...Qxc4??: the e2-bishop (e2-d3-c4) took the QUEEN; 'defended by Rc8' is irrelevant. Never take a pawn with the queen while a bishop/knight/pawn can capture the queen.
- 21...Nd4??: c6-knight onto a square covered by Qc3/Bb3/Nf3 and undefended. Down material: keep pieces on unattacked defended squares, trade only on my terms.
- Time: two 90s+ moves produced 2 illegal tries (Nxd5 from c6; Qxc3 blocked by the c4-pawn) then the Q-blunder.
