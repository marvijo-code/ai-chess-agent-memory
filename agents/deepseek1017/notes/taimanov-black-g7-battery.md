# Taimanov as Black v Stockfish 19 - g7 battery and recapture chains

## T48 Final (loss Qxg7# m15)
Opening played (16 plies): 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3. Then 9.bxc3 Be7 10.Be2 O-O 11.O-O Qc7 12.Bf4 d6 13.Qg3.

Eval: -0.02 after 11.O-O, +0.20 after 8...Nxc3, +0.47 after 9.bxc3 (the d5-knight was not attacked when I traded it off; the recapture gave White c3+d4+e5). If ...Nxc3 comes, want a concrete gain.

The loss: 13...dxe5?? (only blunder). 14.Bxe5 Qd8 (58 s, position already lost) 15.Qxg7#. My Kg8 had g7 covered by the king only; Bf4-e5 gave the queen on g3 a protected landing square on g7, so Kxg7 was illegal.

Rule: with his queen on g3 (or any g-file aim) and a bishop that can reach e5 or f6 (f4, h6, c1-e3-f4), do not open the centre with ...dxe5 or a ...f-push. Get a PIECE onto the g7 defence first or keep the pawn tension. A capture that hands his bishop a diagonal is not a pawn win. Check g7's guards before each central break.

## T60R3 (loss m25) - the ...g6 answer WORKS, the queen grab does not
1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies) 9.Qg4.
- 9...g6! was right (SF marked my Nd5! earlier, then only my queen moves were errors): it removes every Qxg7/Bh6 net and keeps the king on e8. 10...Qc7 hit the loose e5 pawn, 11...O-O was safe BECAUSE the g6-pawn blocks the g-file.
- 13.Bh6 hit the f8 rook: ...Re8 is the correct retreat. Keep the f8 rook off f8 while his bishop can reach h6; ...f6 and ...g5 later were forced defenders and worked.
- 17...Bc5 18...Bxe3 won the exchange (B for R). Correct, but the position was already +4.7 for him by then: an exchange up with queens on and his Re3/Rae1 battery is a guard-everything state.
- THE LOSS: 20...Qc6 21...Qxa4?? I called it 'offering a queen trade; queens off suits me'. My Qc6 and his Qg4 stood on the SAME 4th rank with b4/c4/d4/e4/f4 all empty: HIS queen recaptured, none of mine did. 22.Qf4 and the attack rolled on to 24.Qxf6 25.Rxg5#.

Rule: a capture is only an offer if I can name MY recapturer on the resulting board. Name 'he takes with X, I take with Y' and point at Y before touching his pawn. No Y = queen for a pawn.

## T50 Semifinal 1 G1 (loss Qb6# m43) - the ...Bxe5 recapture trap
Same Taimanov to 8...Nxc3 9.bxc3 Qc7 10.Qg3 g6 11.h4 Bg7 12.Bf4 O-O?! (marked an inaccuracy) 13.h5: his h5+g4 clamp against my g6 with Qg3+Bf4, engine +1.5. Open question for next time: hit the centre or the queen before the clamp locks (...c5/...Qc6, unverified), or castle with a concrete answer to h5-g4.

14...Bxe5?? - my count was 'e5 defended only by Bf4; after Bxe5 Qxe5+ the queens come off and I am +1'. Actual: 15.Bxe5 Qxe5+ 16.Qxe5. His Qg3 stood behind his Bf4 on the g3-f4-e5 diagonal, so when his bishop landed on e5 the screen was gone and HIS QUEEN recaptured mine with no answer. Queen for bishop, +8 for White at move 16.

Rule: in every recapture chain, especially one I describe as ending with 'queens off', name HIS LAST capturer from the board. A piece of his standing between his queen and the square I capture on is a SECOND GUARD once it moves onto (or off) that diagonal.

## Holding a queen down (same game, 25+ moves)
Quiet fortress: Rd8 on d7, Rf8 on f6, Bd5 poisoned to Qxd5 (exd5), ...c4 hitting Be2/Bd3, Kh8-g8-h7-g7-f8-e7. He needed checks (Qe7+, Qxd8+, Qg6+, Rf2+) and mate with Q+R. My errors were only time: 1:43-3:06 on ...c4/...h6/...Bd5/...Rfe8 with 45 min left; shuffles there need 5-15 s and no plan.
