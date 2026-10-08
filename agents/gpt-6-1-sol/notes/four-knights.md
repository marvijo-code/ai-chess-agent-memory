# Four Knights: defense before activity

## Shared opening: Black vs Stockfish 19
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Be6 11.Bxe6 fxe6! 12.Qb3.

Both pairs of knights have disappeared. Qb3 attacks Bb4 and pressures b7. Trace actual queen diagonals before claiming simultaneous defense.

## Tournament 2, semifinal 2, game 1: checkmate loss
12...Qe7 13.d4 Rae8 14.c3 Bd6! 15.Qxb7 Qh4 16.f4 Bxf4? 17.Bxf4! Rxf4 18.Qxc6 Ref8 19.Qxe6+ Kh8 20.Qe2 Re4 21.Rxf8#.

### Corrected bishop defense, then failed attack
- Qe7 genuinely defended Bb4 along e7-d6-c5-b4 and e6 along the e-file. Unlike the earlier Qd5, its geometry was correct. No supplied mark established it as the best move.
- c3 attacked Bb4; Bd6 was marked the only good move. White then collected b7.
- Qh4 threatened Qxh2# with Bd6 supporting h2. White's f4 blocked the bishop diagonal.
- Bxf4 was marked a mistake. Bxf4 by White was the only good reply: exchanging bishops removed the bishop supporting the mating attack. The bishop's protection by queen and rook did not establish the soundness of capturing f4.
- After ...Rxf4, both sides had queen, two rooks, and six pawns. Material equality at that instant did not establish adequate counterplay.
- Qxc6 attacked Re8 along c6-d7-e8. ...Ref8 saved the rook but abandoned e6, allowing Qxe6+ and driving the king to h8. White now had six pawns against four.

### Decisive rook geometry
Before 20...Re4: White Kg1/Qe2/Ra1/Rf1, pawns a2 b2 c3 d4 g2 h2; Black Kh8/Qh4/Rf4/Rf8, pawns a7 c7 g7 h7.

- Rf4 blocked White's rook on f1 from reaching f8. It also could recapture on f8 if that square became accessible.
- ...Re4 attacked Qe2 but vacated f4, opening the entire f-file to Rf1. It simultaneously removed the rook's ability to recapture on f8.
- Rxf8# ignored the queen attack and captured the remaining back-rank rook. The white rook covered g8; Black's g7 and h7 pawns occupied the other escape squares. Qh4 could not capture f8 or interpose on g8.
- During play I had already noted that a hypothetical Rxf4 should be met by Qxf4 rather than Rf8xf4 because vacating f8 permits a queen invasion. I failed to apply the same back-rank safety check to my own rook lift.
- Black finished with 12:43. Moves 18...Ref8 and 20...Re4 each consumed about 51 seconds, yet the final candidate still lacked a resulting-position check scan.

No best replacement for Bxf4 or Re4 was supplied. The immediate mate after Re4 is established directly; do not invent an engine-approved alternative.

## Tournament 2, round 3: checkmate loss
12...Qd5?? 13.Qxb4 a5 14.Qa3 Rf5 15.d3 Raf8 16.d4 Qxd4 17.Qg3 R5f6 18.c3 Qd5 19.f4 Rg6 20.Qh3 Rh6 21.Qf3 Qf5 22.a4 e5 23.Qe2 exf4 24.Qc4+ Kh8 25.Rxf4 Qf6 26.b3 Qe7 27.Rxf8+ Qxf8 28.Bxh6 gxh6.

- Qd5 defended e6 but not Bb4: d5 and b4 are not aligned. White escaped the queen attack by taking the bishop. An offered queen exchange was optional.
- Rook lifts and queen harassment did not recover the piece. After Bxh6 gxh6, White had Q+R against Q, with five pawns against six. The bishop deficit had become a rook deficit.

32.g3 Qe7 33.Rd1 c5 34.Qg4+ Kh8 35.Qc8+ Kg7 36.Qg4+ Kh8 37.Rf1 Qe3+ 38.Kh1 Qxc3?? 39.Rf8#.

- Qe3+ did not eliminate the prepared rook invasion after Kh1. Qg4 covered g8/g7; h7 was blocked by Black's pawn.
- Qxc3 neither checked nor defended f8. Qe7 could meet Rf8+ with Qxf8, stopping immediate mate without establishing a drawable position.
- Black had 9:43 after Qxc3. Both Stockfish losses featured missed rook mates with ample time.
