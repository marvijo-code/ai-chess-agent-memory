# Sicilian Maroczy: recaptures and destination safety

## Shared opening
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5.
Qa5 pins Nc3 to Ke1 via b4/c3/d2. Nc3 cannot recapture on e4/d4. Qd1 can recapture on d4 only while d2/d3 remain clear. f3 supports e4; Bd2 obstructs Qxd4, while Be3 alone leaves e4 vulnerable.

## T12 round 2: White vs Stockfish 19, mate loss
7.f3 Nxd4 8.Qxd4! Bg7 9.Qd2?! d6 10.Be2 Be6 11.O-O Bxc4 12.Bxc4 Qc5+! 13.Qf2 Qxc4! 14.Be3 Qa6 15.Rac1 O-O.
- This repeated T7's line through move 15. The forcing check between captures exchanged bishops and cost the c-pawn. Qd2 was marked inaccurate here; no best replacement supplied. Do not treat the old sequence as repaired preparation.

### Outpost exchanged before its fork
16.Nd5?? Nxd5! 17.exd5 Qxa2! 18.Rc7 Bf6 19.Rxb7 Rab8.
- Nd5 claimed Nc7 would fork Qa6/Ra8, but Black exchanged the knight first. Calculate captures of the attacking knight before crediting its next-move fork.
- Nc3-d5 and Nf6xd5 both removed screens from Bg7-f6-e5-d4-c3-b2. exd5 did not block that diagonal. Rac1 had also abandoned a2's rook defense; Qxa2 took a second pawn and attacked b2.
- Rxb7 recovered one pawn, not compensation for later piece losses. No engine-best alternative to Nd5 was supplied.

### Queen diagonal missed on rook retreat
20.Rb3?? Qxb3 21.Bxa7 Ra8 22.Bd4 Ra2 23.Qe3 Qxe3+ 24.Bxe3.
- Qa2 directly attacked b3. Rb3 escaped Rb8 but landed on a2-b3, losing the rook outright. b2 attacks a3/c3, not b3. Supporting b2 was irrelevant to the rook's own safety.
- Bxa7 recovered only a pawn. The queen trade left White R+B against 2R+B. Activity and pawn collection did not restore material.

### Other rook captures the promotion attacker
25.b4 Rda8 26.b5 h5 27.b6 Rb8 28.Rb1 Ra3 29.Bf2 e5 30.b7 Kh7 31.Ba7?? Rxa7.
- Be3/Bf2 supported b6, but neither supported b7. Rb1 backed b7; Rb8 blockaded it.
- Ba7 attacked the blockading Rb8 but put the bishop on Ra3's clear a-file: a4/a5/a6 were empty. Black captured with the OTHER rook, preserving the blockade. Scan all enemy captures before assuming a promotion threat forces a rook move.

### King enters a two-rook net
32.Rb6 Ra1+ 33.Kf2 e4 34.Rxd6 Bh4+ 35.g3 Ra2+ 36.Ke3 Rxb7 37.gxh4 exf3 38.Kxf3 Rb3+ 39.Ke4 Rb4+ 40.Ke5 Re2+ 41.Kf6 Rf4+ 42.Kg5 Rf5#.
- Rxd6 attacked Bf6, but Bh4+ escaped with check. gxh4 later removed the bishop; Black still had two rooks against one.
- Kf6 allowed a forced mating net. Rf5 was protected by g6; h5 covered g4, Kh7 covered h6, and my h4 pawn occupied an escape square. Central king activity requires explicit checks and escape-square calculation.
- No invalid attempts. 14:21 after Nd5, 13:43 after Rb3 (53 seconds spent), 13:05 at mate. Tactical verification, not clock shortage, failed. Rb3/Ba7 lacked adverse marks despite direct material loss.

## T8 round 1: repetition escape
7.Be3?! Nxe4! 8.Nxc6 dxc6 9.Qd4 Nf6 10.O-O-O Bg7: Be3 ignored the pinned e4 defender. Nf6 shielded Rh8 from Qd4 while saving the knight; the apparent fork won nothing.
- After liquidation to Q+2R each, 19.Qxe7?! Rae8 20.Qxb7 Rb8 21.Qb4?? Rxb4+ 22.cxb4 Qxb4+ lost queen and pawn for rook. Count every capturing piece, not just a hoped-for queen trade.
- Active rooks later secured repetition against depth-4 play. Survival did not establish compensation or a theoretical draw.

## Earlier failures
- T7: Nd5 opened Bg7's diagonal to b2. Rb1 later abandoned an a3 blockade; 39.Rb1?? axb1=Q lost the rook. An a2 pawn can promote on a1 OR capture-promote on b1.
- T3: 7.Bd2? Nxd4! blocked Qxd4. Nb5's queen attack did not recover the knight. Bxd4 Bc5 Bc3 Bxf2+ Ke2 Qe3# followed: Bc3 removed f2's defense and the diagonal screen; Qb6 protected Bf2, which protected Qe3.
