# Black vs 3.Bc4 Giuoco Pianissimo (T9R1 vs Sol, LOST mate 47, 900+10)

1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d3 d6 6.O-O O-O 7.Re1 h6 8.Nbd2 a6 9.a4 Ba7 10.Nf1 Re8 11.h3 Be6 12.Bb3 Qd7 13.Ng3 Kh7 14.Be3 Bxe3 15.Rxe3 Bxb3 16.Qxb3 Rab8 17.d4 exd4 18.cxd4 d5 19.e5 Ng8 20.Rc1 Nge7 21.Qd3+ Kg8 22.Nh5 Nf5? 23.Re2 Qe6 24.Nf4 Qd7 25.g4 Nfe7 26.e6 fxe6 27.Nxe6 Ng6 28.Qe3 Rbd8?? 29.g5 hxg5?? 30.Nfxg5 Rc8 31.Qg3 Qd6 32.Qxd6 cxd6 33.Kg2 ... 44.h6 a5 45.h7+ Kh8 46.Rh3 Nf5 47.Nf7#.

## What went wrong
- Opening equal until 17.d4. I traded both bishops (14...Bxe3, 15...Bxb3), leaving only knights, no light-square control, and a knight pair vs White's central break.
- 18...d5 19.e5 kicked Nf6 to g8 (passive, lost tempi: Ng8, Nge7). Then Nh5, g4 hit Nf5, 26.e6 gave White Ne6 (outpost forking c7/d8/f8/g7).
- Engine marks: 22...Nf5?, 28...Rbd8??, 29...hxg5??. White's 28.Qe3?? and 29.g5?? were errors, so I had real chances there; I did not see the refutations (spent 34 s and 58 s). 29...hxg5 let Nfxg5 add a defender to Ne6 and opened h-file; afterwards I only shuffled Kh7/Kg8/Kh8 (moves 35-43) while White played h4-h5-h6-h7+ and Nf7#.
- My in-game notes said 'never rooks on c7/d8/f8, never Kh8, keep g7 guarded' - correct, but the real problem was having no plan against a pawn storm.

## Fixes for next time (unverified, calculate)
- Keep one bishop pair piece: after Bxe3 Rxe3 do NOT also trade Bxb3 automatically; consider 14...Bxe3 15.Rxe3 Rad8/Nh5 or leave Be6, or avoid ...Kh7 and ...Qd7 setups that let Nh5/g4.
- Against d4: after 17.d4 exd4 18.cxd4 prefer 18...Bb6/Na5 hitting Qb3 or ...Nb4/...Ne4 over 18...d5 19.e5. If ...d5 is played, answer e5 with ...Ne4 (ok only if Nxe4 dxe4 Rxe4 isn't winning a pawn) or ...Nd7.
- Better early plan: ...Nh5-f4 or ...d5 before White gets d4; ...Bb6/...Ba7 with ...Nd7 and ...f5 ideas; ...Re8 and ...Bf8 without the Qd7/Kh7 clumsiness.
- When e6 appears: 26.e6 fxe6? 27.Nxe6 is a bind; look at 26...Qd6/Qc8/Qe8 first and count 27.exf7+.
- Don't open the h-file with ...hxg5 if the recapture adds an attacker. Prefer ...Nxg5 or ...Rxe6 sacrifices only after counting.
- Spend the clock on plan-making at moves 17-30, not on 40-60 s waiting moves later (I ended with 2:57 vs White 5:01 at the end).
