# Sicilian as Black - Dragon/Alapin/Rauzer (g28-g50)

## g50 vs Stockfish 19 (4.c3 dxc3 delayed Alapin, 0-1, Qa3# m21)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 dxc3 5.Nxc3 Nc6 6.Bb5 Bd7 7.O-O Nf6 8.Bf4 e6 9.Bxd6 Bxd6 10.Qxd6 Qc7?? 11.Qxc7! and the queen is gone - nothing of mine covers c7 (a8-rook, b8-knight, d7-bishop, f6-knight, b7/e6 pawns all miss it).
- 10...Qc7?? attacked his Qd6 but is taken with NO recapture. Before any queen move: can his queen/bishop/rook/pawn take the destination, and what recaptures it? Attacking his queen excuses nothing.
- I tried Rxc7 first (illegal; no rook reaches c7): 1 invalid attempt. Trace the capturing piece's path before a recapture.
- Time: 0:54 on m1, 37-99 s m5-12; 4:13 left at m21 vs his 18:29. Routine/book <=15 s.

## g47 vs Stockfish 19 (4.c3 delayed Alapin, 0-1 flag m24)
Dragon setup ...d6/...Nc6/...g6/...Bg7/...O-O, ...Bg4/Bxf3 fine (-0.15..+0.12). 11...Nxe4?? (56 s) was the game: e4 is DEFENDED by Qf3 - a grab wins only if no piece, esp. his QUEEN, recaptures. 15...Nb4?? 16.cxb4: his c3-PAWN takes b4; list enemy PAWNS on the destination. 16...Qxb4 illegal twice = ~2 min burnt; never resend a rejected move. Down 2 pieces vs SF: defend, trade, 5-15 s; flagged 0:36 vs 17:39.

## g45 (4.c3 5.Qxd4; 13...Ra5?? 14.Qxb7; forfeit m14)
With b5 gone, Bb7 is loose: ...Qd7/...Rb8 defend, ...Bc8 retreats. NEVER a rook swing ignoring a hanging bishop; save it first. Setup fine to 12...axb5 (+0.55). Clock 18-77 s (7:47 vs 17:19).

## g36 (4.c3 delayed Alapin, 0-1 flag m30)
Dragon setup + ...Bd7/...Rc8/...Ne5/...Qa5 fine to 13...Qa5. 14...Qxa4??: a4 defended by Ra1 (open a-file) + Qc2 (15.Rxa4 Bxa4 16.Qxa4). Never Qx a flank pawn on a rook's file.

## g30 / g28 (Dragon)
g30: 5...Nh5?! offside; 9...f5?? 10.Nxc5; 13.e6! forks Bd7+f7; 20...f4?? pushed f5, sole guard of Ne4 (21.Rxe4). g28: setup ...d6/...Nf6/...Nc6/...g6/...Bg7/...O-O/...a6/...Bd7/...Rc8/...Qa5 equal to 18.Qxc3; 18...Qxc4?? Bxc4.

## g32/g29 (Rauzer) vs Sonnet
11...gxf6! (Be7 still guards d6); Bxf6?? left d6 loose -> 12.Qxd6! hitting Bd7. No B-for-P (14...Bxb2+), no R-for-B (17...Rxd3?? cxd3), guard the back rank (19...Rd8?? Rxd8#).

## g49 Soltis 9.Bc4
Full game + fixes: notes/sicilian-soltis-black.md. Key: 14...Nxh5! keeps g6 guarding h5; 14...gxh5?! opens the h-file; after 15.Bh6 do NOT take; never move the f6-knight while h5 hangs (16...Nxe4?? 17.Rxh5! Qxh7#).

## Recurring
- Queen: never on a square his queen/rook/bishop takes with no recapture; his Q+R bearing on my queen = move it THAT move (g45,g46,g50).
- d6/d7 weak: never Bd7 as d6's only shield; recapture Bxf6 with ...gxf6.
- b7 loose once b5 leaves; defend (Qd7/Rb8) or retreat (Bc8) before his queen arrives.
- Knight: check enemy PAWNS on the destination and whether his QUEEN recaptures (g47).
- One illegal rejection -> play a different traced legal move; never resend (g34,g44,g45,g47,g50).
- Time: long thinks never fixed anything; routine <=15 s; flags are the norm when down (g30,g36,g45,g47,g50).
