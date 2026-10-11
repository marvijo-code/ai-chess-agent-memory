# Black Berlin vs SF 1.e4 (T28SF2G1 L mate 49; SF 8.Qe2, NOT the Qxd8+ endgame)

1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.O-O Nxe4 5.d4 Nd6 6.Bxc6 dxc6 7.dxe5 Nf5 8.Qe2 Qe7 9.h3 Be6 10.Rd1 h6 11.Nc3 Rd8 12.Bd2 g6 13.Ne4 Bg7 14.Nf6+ Bxf6 15.exf6 Qxf6? 16.Bc3! Rxd1+ 17.Rxd1 Qe7 18.Bxh8 f6 19.a4 Kf7 ... 21.g4 Kxh8 22.a5 Nd6 23.Nd4 Qd7 24.Nxe6 ... 49.b8=Q#.

## What happened
- Opening was fine: SF +0.1 to +0.7 through move 12 (my moves 9-12 took 17-52 s each, too long for book-like moves). 13.Ne4 (+1.25) threatened Nf6+/Nd6+. SF marks: 13...Bg7!, 14...Bxf6! both fine.
- 15...Qxf6? lost: 16.Bc3 hits Qf6 AND Rh8 behind it on a1-h8. King on e8 blocked Rd8 from guarding h8, and the Bg7 was gone. Eval +1.8 -> +7.3. My note after ply 28 said 'Bc3 hits Qf6 (retreat)' but I never asked what stands behind the queen.
- 18...f6 removed the f7 pawn, so Be6 was guarded by Qe7 only. 23.Nd4 attacked it twice (Nd4 + Qe2): 23...Qd7?? 24.Nxe6. Should have moved the bishop (23...Bc8/...Bd7) or kept Qe7 + a second guard.
- Down R for P from move 24, I used 25-50 s per move for 25 moves with no swindle. Cap 10 s when lost.

## Fixes (unverified)
- 15...Qd7! (or ...Qe8/...Qf8): the pawn on f6 blocks White's own Bc3 diagonal; I'm a pawn down but the Rh8 is not skewered. Compare: after exf6 the pawn is weak only if the long diagonal stays shut.
- Rh8 never moved because the king stayed on e8. After ...Be6 and ...Qe7 (Nb8, Bc8, Qd8 off) ...O-O-O is legal: try 10...O-O-O or 11...O-O-O instead of ...h6/...Rd8 (check Rd1 vs Rd8 on the d-file, Nd4 vs Be6, Ne4-d6+). The h8 rook then stops being a target.
- Alternatively ...Kf8/...Rg8 early (not ...Rd8 with Ke8 between rooks).
- Before every queen landing on f6/g7/d4/b6: list his bishop moves that hit that square, then the piece BEHIND it on the same line.
- Do not play ...f6 when Be6 depends on the f7 pawn.
- Vs 7.dxe5 8.Qxd8+ Kxd8 (older games): ...Bd7, ...Ke8, ...h6, ...g6 is the plan.

## Prep for 8.Qe2 (SF at depth 6 picks it)
- 8...Qe7 9.h3 Be6 10.Rd1 is the line played. Watch: Ng5 (hxg5/Bxg5), g4 hitting Nf5 (...Nd6 exd6 Qxe2 only when the e-file is clear; Be6 on e6 blocks it, so g4 Nd6 exd6 is NOT a trade), Bd2-c3 diagonal, Ne4-f6+/Nd6+.
- Test the Be6/Qe7 x-ray with Qe2: the bishop on e6 pinned to the queen.
