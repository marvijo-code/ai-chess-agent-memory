# Ruy Lopez: Chigorin safety and exchanges

## Shared structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6.
Recount e4/d4 defenders after reroutes, exchanges, and rook lifts. Preserve Bc2 against ...Nb4 before a3 if ...Nxc2 forks the rooks.

## T6 semifinal 2, game 1: White vs Sonnet, loss
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.d5 Nb4 18.Bb1! Rfc8 19.a3 Nc2 20.Bxc2 Qxc2! 21.Qxc2 Rxc2! 22.Rab1 Nd7 23.Rec1 Rxc1+ 24.Rxc1! Rc8.
- Bb1 saved the bishop, but a3 still allowed Nc2, attacking both rooks and Be3. The resulting liquidation put Black's rook on c2 against b2/Nd2. Queen exchange did not remove positional threats.

25.Nf1?! Nc5 26.Ng3 h6 27.Nd2 Nd3 28.Rxc8+ Bxc8! 29.b3? axb3? 30.Nxb3! Nc5 31.Nxc5?! dxc5! 32.Nf5? Bxf5! 33.exf5 Bd6?!.
- Nd3 attacked Rc1/b2/f2. b3 was marked a mistake despite moving b2 out of reach; calculate other knight captures and resulting pawn structure. No best replacement was supplied.
- Black's attempted Bxc5 at move 31 was illegal: d6 blocked Be7-d6-c5. ...dxc5 was the legal recapture and cleared d6.
- Clearing d6 opened Bc8-d7-e6-f5. Nf5 attacked Be7 but allowed the OTHER bishop to capture it. exf5 removed e4's support of d5.
- Nxc5 dxc5 produced passed pawns for BOTH sides: White d5 and Black c5. Bd6 blockaded mine while ...c4/...b4 activated Black's. Evaluate blockade, king access, and promotion routes before trading into a passer race.

34.Kf1?! c4 35.Bc1 b4? 36.axb4! Bxb4! 37.Ke2 c3?! 38.Kd3 Kf8 39.Kc4?! Ba5! 40.Kb5?! Bc7?! 41.Kc4? Ba5 42.Bd2?? cxd2.
- Chasing the bishop did not permanently remove c3's defense: Ba5 guarded c3 through b4; after Bc7, Kc4 let it return to a5 before Kxc3.
- Bd2 stood directly on c3's capture square. I calculated Bxc3 Bxc3 Kxc3, but Black instead captured on d2, which Kc4 could not reach.
- After cxd2, Ba5's diagonal a5-b4-c3-d2 opened and protected the new pawn. I lost the bishop and allowed ...d1=Q. Verify the capture square and king distance before claiming a recapture or promotion control.
- Bd2 took 30 seconds with 10:14 remaining. Nxc5 took 52 seconds; Nf5 41. Finished with 7:56 and no illegal attempts. The failure was concrete capture checking, not time pressure.

## T6 round 3: Black vs Sonnet, win from a lost position
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.Rc1 Rac8 18.Qe2 Qb6?? 19.dxe5 Qd8 20.exf6 Bxf6.
- Qb6 stood behind d4 on Be3's diagonal. dxe5 opened an attack on the queen AND attacked Nf6. Qd8 saved the queen but lost the knight. Qb6 took 52 seconds; longer thought did not prevent the error.
- Ne5 attacked Qd7 but allowed d6xe5: Qa4's pin on Nc6 did not prohibit another piece's capture. Qe6 subsequently removed the pin before Nc6 moved.
- ...Nd4?? Nxd4 exd4 created a supported passer but did not establish compensation. After Nc6/Qc7 vacated their squares, Bb6-c7-d8 was clear; ...Rfd8? allowed Bxd8 Rb8xd8, losing the exchange.
- Qc7 defended Bb7, but Rb3 supported Qxb7: ...Qxb7 Rxb7 would exchange queens while conceding the bishop.
- Qf4/Be5 against Kg1/Re2/f2/g2/h3: ...Qh2+ vacated f4, opening Be5's protection of h2. Rb5?? allowed Qh2+ Kf1 Qh1#. Both rooks failed to capture or block. The mate did not validate the earlier errors.

## Earlier failures
- T5 Black: ...Nxe3 Qxe3 Nxe5?? Nxe5 Bc5 Qxc5 Qxc5 Nxc5 Rxc5 left White a knight ahead. Be7 blocked Re8's apparent defense of e5.
- Rb3?? allowed direct ...Rxb3; ...Rc1+ missed it. Later ...Rb1 allowed Rb3xb1 through empty b2, losing the last rook. Compare captures before checks.
- T5 White: Bd3 cleared Rc1's last blocker against Qc7; ...Nxb4 ignored Rxc7. Qa4?? then lost to ...bxa4. Nb3 also previously overlooked ...axb3; releasing a pin did not defend it.
- Nh4-f5 Bxf5 Ng3xf5, f3-f4, and Re3-g3 remove e4 defenders. Recount before attacking.
- Game 4: e5 dxe5 Nxg7+ uncovered Bb1; Nxe8+ uncovered Rg3. Nxc7 exf4 exchanged queens and left an extra rook. Later flagged with queen against bare king after slow elementary conversion. Execute verified mates promptly.
