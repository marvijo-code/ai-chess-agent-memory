# Sicilian as Black - Dragon/Alapin/Rauzer (g28-g50, g58)

## g58 vs SF19 (4.c3 5.Qxd4, 0-1, mated m35)
1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nf6 5.Qxd4 Nc6 6.Qd3 g6 7.Be2 Bg7 8.O-O O-O 9.Rd1 a6 10.c4 Nd7 11.Nc3 Nc5 12.Qc2 = (evals -0.3..0.0); the ...Nd7(f6)-...Nc5 reroute is fine.
- 12...Nd4?? decided the game: only Bg7 defended d4 (my d6-pawn blocked Qd8); 13.Rxd4! Bxd4 14.Nxd4 = my N+B for his R+N (down 1) and Bg7, my king's guard, is gone.
- Before ANY knight jump: list enemy attackers of the square incl. rooks on its file/rank, then value the whole capture chain. A 'fork' he can just take is not a fork.
- 22...Qxd5?? cxd5: his c4-PAWN took my queen for a knight. Same class as g48/g50/g51/g56/g57; even in lost positions scan every queen destination.
- Clock fine (3:30 left at m34): the loss was tactical, not time.

## g50 vs SF19 (4.c3 delayed Alapin, 0-1, Qa3# m21)
...cxd4 4.c3 dxc3 5.Nxc3 Nc6 6.Bb5 Bd7 7.O-O Nf6 8.Bf4 e6 9.Bxd6 Bxd6 10.Qxd6 Qc7?? 11.Qxc7! - nothing of mine covers c7 (a8-rook, b8-knight, d7-bishop, f6-knight, b7/e6 pawns all miss).
- Before any queen move: can his queen/bishop/rook/PAWN take the destination, and what recaptures? Attacking his queen excuses nothing.
- Rxc7 first was illegal (no rook reaches c7): 1 invalid attempt. Trace the capturer's path before a recapture.
- Time: 0:54 on m1, 37-99 s m5-12. Routine/book <=15 s.

## g47 vs SF19 (delayed Alapin, 0-1, flag m24)
Dragon ...d6/...Nc6/...g6/...Bg7/...O-O, ...Bg4/Bxf3 fine. 11...Nxe4?? (56 s): e4 DEFENDED by Qf3 - a grab wins only if no piece, esp. his QUEEN, recaptures. 15...Nb4?? 16.cxb4: his c3-PAWN takes b4. 16...Qxb4 illegal twice = ~2 min; never resend a rejected move. Down 2 pieces vs SF: defend, trade, 5-15 s.

## g45 (4.c3 5.Qxd4; forfeit m14)
With b5 gone Bb7 is loose: ...Qd7/...Rb8 defend, ...Bc8 retreats. NEVER a rook swing ignoring a hanging bishop. Setup fine to 12...axb5 (+0.55). Clock 18-77 s.

## Older - condensed
- g36: setup + ...Bd7/...Rc8/...Ne5/...Qa5 fine to 13...Qa5. 14...Qxa4??: a4 defended by Ra1 (open a-file) + Qc2. Never Qx a flank pawn on a rook's file.
- g30/g28: 5...Nh5?! offside; 9...f5?? 10.Nxc5; 13.e6! forks; 20...f4?? pushed f5, sole guard of Ne4 (21.Rxe4). g28 setup equal at 18.Qxc3; 18...Qxc4?? Bxc4.
- g32/g29 Rauzer: 11...gxf6! (Be7 still guards d6); Bxf6?? left d6 loose -> 12.Qxd6!; no B-for-P, no R-for-B (17...Rxd3?? cxd3); guard the back rank (19...Rd8?? Rxd8#).
- g49 Soltis: full fixes in notes/sicilian-soltis-black.md. Never move the f6-knight while h5 hangs (16...Nxe4?? 17.Rxh5! Qxh7#).

## Recurring
- Queen: never on a square his queen/rook/bishop/PAWN takes with no recapture; his Q+R bearing on my queen = move it THAT move (g45,g46,g50,g58).
- d6/d7 weak: never Bd7 as d6's only shield; recapture Bxf6 with ...gxf6. b7 loose once b5 leaves: defend (Qd7/Rb8) or retreat (Bc8).
- Knight: check enemy PAWNS on the destination, rooks on its file, and his QUEEN/rook recaptures (g47,g58).
- One illegal rejection -> play a different traced legal move; never resend.
- Time: long thinks never fixed anything; routine <=15 s; flags are the norm when down (g30,g36,g45,g47,g50).
