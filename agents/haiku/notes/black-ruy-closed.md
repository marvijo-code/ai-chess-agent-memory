# Black Closed Ruy: v Sonnet 5.5 (T71R2 WIN m37) and v GPT-6.1 Sol (T44R1 L m33)

## v Sonnet 5.5 (win)
Played (16 plies): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 O-O 7.Bb3 Re8 8.c3 h6
Then 9.h3 Bd6 10.Bc2 Qe7 11.d4 exd4 12.cxd4 Bb4 13.Bd2 Bxd2 14.Nbxd2 d6: level.

Why it held:
- ...h6 stopped Ng5 doubling on f7 with Bb3.
- Be7 and Bd6 with Re8 kept e5 guarded twice.
- ...Bb4 hit Re1 on the open diagonal after cxd4; Bd2 blocked it and offered the trade.

Failure:
- 16...Be6? aimed at Nb3. 17.a3 kicked Nb4, whose only safe retreat was c6, and 18.d5 forked Nc6 and Be6.
- 18...Ne5? 19.dxe6 Nxf3+ 20.Qxf3 Qxe6 left me a bishop for a pawn.
- Unverified fix: keep the bishop off e6 (...Bd7 or ...Bf5) while a knight can be kicked to c6.

Recovery:
- 22...c5 kicked Nd4. 23...Qxb2 won a pawn. 25.Rab1 hit my queen; 25...Qxa3 took a pawn with tempo on Bd3.
- 26...Qxe3 traded queens into a queenside pawn majority against none.
- Rc8 behind c4, the Nd4 blockade, then ...d5 and ...g6 (covers f5) held. Re8 held his e7 pawn; Rc7 guarded f7.
- 36...b3 and 37...b2 froze Bb1 on the promotion square. Sonnet's 38th reply failed (provider safeguard error).

## v GPT-6.1 Sol (T44R1, L m33)
Played (16 plies): 1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 Be7 5.O-O O-O 6.Re1 a6 7.Ba4 b5 8.Bb3 d6
Then 9.c3 Bb7 10.h3 d5 worked. After exd5 Nxd5 the knight centralized. Nbd2 Nf4 hit d3, defended only by Bc2 while Nd2 blocks Qd1. Nxd3 Bxd3 Qxd3 won a pawn net. Nxe5 gave it back with Nxe5 Rxe5: level.

Failures:
- 29...Rxb2?? emptied my rank 8 while Kg8 stood behind f7/g7/h7 with no luft. Sol then used Ra6 and Ra8 ideas.
- 31...Rc1?? entered Be3's diagonal (e3-d2-c1). Bxc1 Bxd4 and Ra8#.
- 16...Qd6 was marked inaccurate. No verified replacement.

Plan (unverified):
- Play ...h6 luft before rook trades on the d-file, not after.
- Before every rook move, write the enemy lines to its destination.
- Keep one rook on rank 8 while White's rook can reach a8 or b8.
