# Sicilian as Black - Dragon/Alapin/Rauzer (g28,g29,g30,g32,g36,g45,g47,g49)

## g49 vs GPT-6.1 Sol (9.Bc4 Soltis, 0-1, Qxh7# m18)
- Full game and fixes: notes/sicilian-soltis-black.md. Key: 14...Nxh5! keeps g6 guarding h5; 14...gxh5?! opens the h-file; after 15.Bh6 do NOT take; never move the f6-knight while h5 hangs (16...Nxe4?? 17.Rxh5! Qxh7#).

## g47 vs Stockfish 19 (4.c3 delayed Alapin, 0-1 flag m24)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nf6 5.Qxd4 Nc6 6.Qd3 g6 7.Be2 Bg7 8.O-O O-O 9.Rd1 Bg4 10.h3 Bxf3 11.Qxf3 Nxe4?? 12.Qxe4 (N for nothing).
- Dragon setup (d6/Nc6/g6/Bg7/O-O, ...Bg4/Bxf3) was fine (-0.15..+0.12); 11...Nxe4?? (56 s think) was the whole game: e4 is DEFENDED by his queen on f3. A pawn grab wins only if no piece, especially his QUEEN, recaptures.
- 12...Bxc3 13.bxc3, then 15...Nb4?? 16.cxb4: his c3-PAWN (ex-b2) takes b4. Before any jump/capture list every enemy PAWN attacking the destination (a/c-pawns).
- 16...Qxb4 attempted twice = illegal (Qd8 has no line to b4): 2 invalid attempts, ~2 min burnt. Never resend a rejected move - play a different simple legal move.
- Down 2 pieces vs SF by m16: no recovery; 5-15 s/move, defend, trade. Flagged 0:36 vs his 17:39 (37-70 s/moves m6-14, 49 s m1).

## g45 (4.c3 5.Qxd4; 13...Ra5?? 14.Qxb7; forfeit m14)
After ...a6 ...b5 ...Bb7: with the b5-pawn gone, Bb7 is loose. 13...Qd7!/...Rb8 defends b7; ...Bc8 retreats. NEVER a rook swing like 13...Ra5?? that ignores a hanging bishop. Save the attacked piece first; hitting his queen excuses nothing. Setup fine through 12...axb5 (+0.55). Clock 18-77 s/move (7:47 vs 17:19).

## g36 (4.c3 delayed Alapin, 0-1 flag m30)
Dragon setup + ...Bd7/...Rc8/...Ne5/...Qa5 fine to 13...Qa5. 14...Qxa4?? - a4 defended by Ra1 (open a-file) and Qc2 (15.Rxa4 Bxa4 16.Qxa4). Never Qx a flank pawn on a rook's file. 12...Nxe5 illegal (f6-knight cannot reach e5). Clock 30-70 s, flagged 27 s at m30.

## g30 (Dragon vs 4.Bb5, 0-1 m32)
- 5...Nh5?! offside; 9...f5?? 10.Nxc5; 13.e6! forks Bd7+f7, Bxe6 undefended (f5-pawn); 15...Nf6?? after Bxd4; 20...f4?? pushed f5, the sole guard of Ne4 (21.Rxe4).

## g32/g29 (Rauzer) vs Sonnet 5.5
- Bxf6: recapture 11...gxf6! (Be7 still guards d6); Bxf6?? left d6 loose -> 12.Qxd6! hitting Bd7. His Q/R on d6 hitting Bd7: cover with a non-queen piece or give the pawn (...Bc8/...Be8).
- No B-for-P (14...Bxb2+), no R-for-B (17...Rxd3?? cxd3), back-rank guard (19...Rd8?? Rxd8#). Clock 36-59 s routine (4:19 vs 16:38).

## g28 (Dragon vs 4.c3, 0-1 m31)
- Setup ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O/...a6/...Bd7/...Rc8/...Qa5: equal to 18.Qxc3; 15.Nd5 -> ...e6. 18...Qxc4?? Bxc4; 21...Nd4?? loose while down material.

## Recurring
- d6/d7 weak: never Bd7 as d6's only shield; recapture Bxf6 with ...gxf6.
- b7 after ...Bb7+...b5: loose once the b-pawn leaves; defend (Qd7/Rb8) or retreat (Bc8) before his queen arrives (g45).
- Queen: never ...Qxa4/...Qxc4-type grabs when rooks/bishops/pawns hit the square; count ALL recapturers first.
- Knight: check (a) every enemy PAWN attacking the destination (g47 c3-pawn), (b) whether his QUEEN recaptures (g47 Qf3xe4).
- vs his Q+rook on the h-file (Soltis g49): keep g6 to guard h5 (...Nxh5 over ...gxh5), never ...Bxh6 into Qxh6, never move the f6-knight while h5 hangs.
- Time: long thinks never fixed anything; flags are the norm when down (g30,g36,g45,g47: 4-8 min left while he had 16-20).
