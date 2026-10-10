# Sicilian Dragon - Soltis 9.Bc4 as Black (g49,g53,g54,g66,g69,g74 vs Sol; g55; g88 vs Sonnet)

## Line
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 g6 6.Be3 Bg7 7.f3 O-O 8.Qd2 Nc6 9.Bc4 Bd7 10.O-O-O Rc8 11.Bb3 Ne5 12.h4 Nc4 13.Bxc4 Rxc4 =; 14.h5 Nxh5! (never ...gxh5, g49); 15.g4 Nf6 (only move).
Record: 0-7 (f74 6th, g88 7th). Every loss = guard/loot blunder, not the opening; if it repeats, weigh 9...Nxd4 10.Bxd4 Be6 11.Bxe6 fxe6 or another path.

## g88 vs Sonnet 5.5 (0-1, Qh7# m21) - 15...Rxe4?? threw the rook; mate ignored
11.Bb3 Ne5 12.h4 h5 13.Kb1 Nc4 14.Bxc4 Rxc4! 15.Nde2 Rxe4?? 16.fxe4 Qe8 17.Bh6 Bxh6 18.Qxh6 Nxe4 19.Nxe4 Be6 20.Ng5 Qd7?? 21.Qh7#. (SF: 14...Rxc4! good, 15...Rxe4?? blunder; my clocks 36-48 s from move 12, ended 8:05 vs 15:32.)
- 14...Rxc4! traded B for N and put the rook on c4, hitting d4 (15.Nde2 forced). Fine.
- 15...Rxe4??: my note claimed "e4 defended only by the e2-knight" - FALSE. Nde2 does not attack e4; the f3-PAWN and the c3-KNIGHT defend e4. Rook for a pawn, and after 16...Nxe4 17.Nxe4 the f6-knight also falls (e4 undefended for Black: Qe8 blocked by e7-pawn, Bg7/Bd7 miss e4). With 15.Nde2 played, the c4-rook has no target: retreat it (...Rc8/...Rc7) or play ...e6/...Qa5.
- 17...Bxh6 18.Qxh6: after the R sac it is lost anyway, but 20.Ng5 was the mate moment: Qh6+Ng5=Qxh7# (Ng5 guards h7; Kg8 cannot take; f8 rook blocks f8, f7 pawn blocks f7, g7/h8 covered by Qh7). 20...Qd7 (defending Be6) ignored it. Only save: hit the knight (...f6, which also frees f7 for Kf7); ...Kh8 fails because Qh7 is protected.

## Older games - condensed
- g74: 12.h4 Nc4 13.Bxc4 Rxc4 14.g4!? Rc8 15.h5 Nxh5?? 16.gxh5 (N for P) ... 22.Qh7#. 14.h5 Nxh5! works only while his g-pawn is home; with g4 on, ...Nxh5 = gxh5 (self-ban violation, my note said it). Meet h5 with ...gxh5/...Qa5; need ...Re8 luft; 19.hxg6 -> ...fxg6 not ...hxg6.
- g69: 16.Bh6 Bxh6?? terrible (17.Qxh6 Qe8 18.g5 Nh5 19.Rxh5!); never recapture Bh6, get luft; no Rxd4/Bxd4 with mate on.
- g66: 16.Qh2 (h-file open, Nf6 = h7's only guard) 16...Rc8?? 17.g5 Nxe4?? 18.Qxh7#. 16.Qh2: only knight square h5, and only once g4 left.
- g54/g53: 16.Qh2 with g4 on: NO ...Nh5 (17.gxh5!); 16.g5 -> only ...Nh5 (Ne8?? 17.Qh2); no Bxd4 with mate on.
- g49: 14...gxh5?! opened the h-file (14...Nxh5!); 15.Bh6 do NOT trade; 16...Nxe4?? 17.Rxh5! Qxh7#.
- g55: 19...gxf5?? moved g6, h5-knight's sole guard -> 20.Rxh5; 27...Rd2?? Kxd2; flagged.

## Rules
- Before any knight move: is f6/h5 my only h7 guard? is the h-file open? does his g-pawn attack h5? g4 ON: ...Nxh5 loses to gxh5 (piece for pawn). g4 GONE: ...Nh5 only after g5, and g6 must stay.
- Never trade Bh6: ...Qe8/...Qa5 + luft (...Re8). Keep g6 while a knight sits on h5.
- No material grabs (Rxd4, Bxd4, Nxe4, Rxe4) while Qxh7#/mate nets are pending; when down, hit the g5-knight before it lands (only ...f6/...f5-class moves stop Qh7#).
- Routine <=15 s; long thinks produced every blunder in this line.
