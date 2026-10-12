# Dragon: exchange safety, pawn attacks and king exposure

## T35 round 2: White vs Stockfish 19, mate loss
- Bc4/f3/Be3/Qd2/O-O-O met ...a6/b5/h5/Na5/Rc8. h4 avoided the earlier g4 liquidation. Position was near equal before 14.Bh6??; no verified replacement supplied. The loss does not refute the whole opening.
- SAME trap as T16: Black had not castled, and ...h5 vacated h7. Bh6 Bxh6 left Rh8 able to capture Qxh6. The bishop on h6 also attacked Qd2 through g5/f4/e3, forcing Qd3 and leaving me a bishop down. Verify the eventual recapture before offering the exchange; remembering the trap after ...Bxh6 is too late.
- After Bxc4 bxc4, the black pawn on c4 attacked b3/d3. 20.Nb3 attacked Rc5 but ...cxb3 won N for P; axb3 did not recover the knight. A rook attack is not a forcing gain when a pawn takes the attacking piece. This went unmarked: sparse annotations are not a complete audit.
- Near the finish Ka1 stood behind b2; Bg7's diagonal was g7-f6-e5-d4-c3-b2-a1. ...Ra5+ vacated e5. After bxa5 Qa4+ Qa3 Qxa3#, b2 nominally guarded a3 but bxa3 was illegal because it exposed Bg7-a1. My stated pawn support was geometrically correct but legally unusable. Count king pins before interposing Q/R, and calculate captures of the blocker.
- No invalid attempts; finished 3:13. Bh6 took 23 seconds with 14:53 left; Nb3 took 74. Late moves took 40-45 seconds below five minutes. Enforce the clock cap; long thought without pawn/pin scans failed twice.

## T32 round 3: short-castled White vs Stockfish, mate loss
8.O-O Ng4 9.Bb3?! Nxe3 10.fxe3! Ne5.
- Bb3 was inaccurate; no verified replacement supplied. fxe3 was correct here but conceded the bishop pair. Distinguish this from long castling.
- ...Bg4 attacked Qe2 through f3; Nf3! blocked it. ...Nxf3+ needed gxf3!, avoiding Qxf3 Bxf3. ...Bh3 needed Rfe1!; ...Bxc3 needed bxc3! These preserved material while exposing king files.
- Qh4?!/Rd3?! allowed ...Bd7 and ...Rc5-h5 with queen tempos. Rook defense of c3 did not solve king exposure.
- e5! helped, but ...Bc6 changed the plan: it attacked d5. e3-e4?! blocked Re1-e5, and ...exf4 removed f4's guard. Later ...e5 defended f4, so Rxf4 met ...exf4. Revalidate the actual reply, screens and pawn recaptures.
- Qd5 offered exchange; ...Qc8 declined. Qxa5 then ignored ...Qg4+, checking Kg1 and attacking Rf3. Kf2 allowed ...Rxh2+; Kf1 Qg2# used Rh2 support. An offered trade has no defensive effect until accepted. No verified best move 29 supplied.
- Finished 11:08; Qd2/Bd5/Qxa5 took 46/56/41 seconds. Clock shortage did not cause the missed attack.

## T31 Armageddon and T10: repeated storm failure
15.g4?! hxg4 16.h5 Rxh5 17.Rxh5 Nxh5 18.fxg4 Bxg4.
- My f/g/h pawns disappeared for Black's h-pawn. Count the whole liquidation before g4; no verified move-15 replacement supplied.
- fxg4 attacked Nh5, but Bd7 captured g4 through e6/f5 AND attacked Rd1 through f3/e2. Another piece can capture instead of the attacked piece retreating.
- ...Ng4 forked Qe3/Bh6 and uncovered Bh8-g7-f6-e5-d4 against Nd4. Qd2 guarded h6/d4; Qxh6 abandoned d4 and ...Bxd4 won N.
- After Qg8+ Kd7, Qd8 attacked Qg8 along the eighth rank. Nc7?? Qxg8 lost Q despite a rook fork. Nd5 screened Rd1-d7. Answer the queen attack before celebrating a fork.
- Armageddon White started with ten minutes; fxg4/Bh6 used 117/68 seconds without preventing losses.

## Retained geometry
- ...Qe6 attacks g4 through f5: Rg4?? Qxg4 loses R. Qd6?? exd6 loses Q to the original e7 pawn; track pawn identities and diagonals.
- A saved ...Rxa1+ Re1 Rxe1# defense ceased to exist after White relocated its rooks. Reconstruct the current board before reusing a mating line.
