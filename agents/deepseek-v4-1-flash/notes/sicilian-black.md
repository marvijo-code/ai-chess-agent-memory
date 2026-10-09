# Sicilian as Black (g28,g29,g30)

## g30 vs Stockfish 19 (Dragon vs 4.Bb5, 0-1, mated m32)
1.e4 c5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 g6 5.e5 Nh5 6.O-O Bg7 7.Bxc6 dxc6 8.Ne4 O-O 9.h3 f5 10.Nxc5 b6 11.Nb3 Bd7 12.Re1 Qe8 13.e6 Bxe6 14.Nbd4 Bxd4 15.Nxd4 Nf6 16.Nxe6 Nd7 17.Ng5 h6 18.Nf3 Nf6 19.b4 Ne4 20.Bb2 f4 21.Rxe4 Rf5 22.Qe2 Rf7 23.Ne5 Rf8 24.Qc4+ Kh8 25.Nxg6+ Kh7 26.Nxf8+ Qxf8 27.Rae1 Qf6 28.Rxe7+ Qxe7 29.Rxe7+ Kg6 30.Qf7+ Kg5 31.Re5+ Kh4 32.Rh5#.
- White's Bb5+e5 avoids the Open Sicilian; 5.e5 kicks Nf6. 5...Nh5?! offside (sat there 10 moves); retreat 5...Nd5 (central, hits c3) or 5...Ng8.
- After 7...dxc6 the c5-pawn is undefended (b7 guards c6; d-pawn gone). 9...f5?? kicked Ne4 but 10.Nxc5 won a pawn. Guard c5 or don't kick the knight.
- 13.e6! forks Bd7+f7. 13...Bxe6? left e6 with NO defender: f-pawn was on f5 (no longer covers e6) and Qe8 is blocked by the e7-pawn. 14.Nbd4/16.Nxe6 then won a piece. Better 13...Bc8/...Ba4 or accept the wedge; the fix after 14...Bxd4 15.Nxd4 was 15...Qd7! (defends e6, hits d4) - NOT 15...Nf6?? (blunder; a knight on f6 does not defend e6).
- 16...Nd7 was playable but I burned 98s and tried the illegal Qxe6 (blocked by own e7-pawn).
- 20...f4?? pushed f5, the ONLY defender of Ne4 -> 21.Rxe4 won the knight. Never push a pawn that guards one of my pieces.
- Time: 30-45s on moves 5-16 routine; clock ended 4:06 vs 20:09.

## g29 vs Sonnet 5.5 (Richter-Rauzer, 0-1, mated m20)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O 9.f4 Nxd4 10.Qxd4 Bd7 11.Bxf6 Bxf6 12.Qd2 Qa5 13.Kb1 Bxc3 14.Qxc3 Qxc3 15.bxc3 Rac8 16.Rxd6 Rxc3?? 17.Rxd7 Rxc2?? 18.Kxc2 Rc8+ 19.Kb2 Rd8?? 20.Rxd8#.
- Setup ...e6/...Be7/...O-O/...Nxd4/...Bd7/...Qa5/...Bxc3/...Qxc3/...Rac8 was fine; equal through 15...Rac8.
- 16.Rxd6: d6 undefended and the rook attacks Bd7. 16...Rxc3?? ignored it: 17.Rxd7 won a bishop, then 17...Rxc2?? dropped the rook to 18.Kxc2 (c2 undefended, his king adjacent). Save/defend/trade the attacked piece first.
- 19...Rd8??: king g8 + f7/g7/h7, no luft, his rook on d7 -> 20.Rxd8#. Keep a back-rank guard or give luft.
- Time: 46-53s on routine moves 13-19 and 3 blunders.

## g28 vs Stockfish 19 (0-1, mated m31)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nf6 5.Qxd4 Nc6 6.Qd3 g6 7.Be2 Bg7 8.O-O O-O 9.Rd1 a6 10.c4 Nd7 11.Nc3 Nc5 12.Qc2 Bd7 13.Be3 Rc8 14.h3 Qa5 15.Nd5 e6 16.Nc3 Bxc3 17.Bxc5 Qxc5 18.Qxc3 Qxc4?? 19.Bxc4 Rfd8 20.Rd3 b5 21.Bb3 Nd4?? 22.Qxd4 Rc7 23.Qe3 Bc6 24.Rad1 Bd5 25.e5 Bxf3 26.gxf3 dxe5 27.Rxd8+ Kg7 28.Qxe5+ f6 29.Qxc7+ Kh6 30.Qc1+ Kg7 31.R1d7#.
- Dragon-type (...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O, then ...a6, ...Nd7-...Nc5, ...Bd7, ...Rc8, ...Qa5) sound; equal through 18.Qxc3. 15.Nd5 not capturable by c6/c5 knights; meet it with ...e6.
- 18...Qxc4??: the e2-bishop took the QUEEN; 'defended' is irrelevant. Never take a pawn with the queen while a bishop/knight/pawn can capture.
- 21...Nd4??: c6-knight onto a square covered by Qc3/Bb3/Nf3 and undefended. Down material: keep pieces on unattacked defended squares.
- Time: two 90s+ moves produced 2 illegal tries then the Q-blunder.
