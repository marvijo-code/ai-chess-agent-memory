# Black vs 1.e4 e5 2.Nf3 Nc6 3.Nc3 (SF plays it every time; 2 W, 21 L, 18 D)

3...Nf6 4.Bb5 Bb4, then 5.O-O (line A) or 5.Nd5 (line B). NEVER 3...Bc5 (4.Nxe5!).

## LINE A: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (NOT bxc6)
10.Bc4 Bd6! 11.d4 Qh4! 12.g3 Qxd4 = pawn up (SF -1.4). Rf8 stays until Bc8 is out.
- THE b7 HOLE: 13.Bb3 Be6 14.Bxe6 fxe6 15.Qb3 hits b7 AND e6. Play 15...Qd7 or 15...Rab8 FIRST, not ...Qd5? Qxb7.
- Move 15 wins: 15...Rfe8 16.c3 Be5 17.Bd1 Bxd1, ...Bxd4, h6 luft, ...b6, ...c5. Also 15...c5 16.Be3 Rad8.
- 11...Qd7?! wins no pawn: play 11...Qh4. 10.Bc4 Be6: DROP. Pawn-down R+B ending: fortress Be5/Rb5, c6/Rd6.

## LINE B: 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 O-O 8.dxc6 exf3 9.Qxf3
- The tool flags ...Nxd5, ...e4, ...O-O with vague reasons. They are book: resend each ONCE. NEVER 5...Nxe4? (3 refusals = forfeit).
- 9...Re8+ 10.Kd1 dxc6 11.Bd3 Bd7 (BOOK) 12.b3 Qe7! 13.c3 Bd6 14.Kc2 Rad8 15.Bb2 Be6 16.c4: level (SF -0.4). Both T84R5 and T84SF1G1 went 16...Qg5?! 17.h4: do NOT play it.
- T85 FINAL L m86: 12...Bd6?! (SF eval -1.3 -> -0.9) 13.Bb2 Be5? 14.Bxh7+! Kxh7 15.Qh5+ Kg8 16.Bxe5 Bg4+ 17.Qxg4 Rxe5 = pawn down (+0.4). Bd3+Qf3/h5 hits h7 again: no bishop-trade offers that move the d6/e7 guard away; 12...Qe7 only. Later ...Rg5/...Rxg2 regained g2, then 26...Qd6 trade, 28.Re7 Rb8 passive.
- Rook ending a pawn down: I walked the king Kf8-g7-f6-e6-f5-g4-h4-h3 (1-2 min thinks) while Kd4, Rg7, Kc5-b6 took b7/c6/a6, a-pawn queened (m65). Fix: Ke6/Kd7 and Rd8/Re8 active; no ...g6/...g5; keep f7/b7 rooks guarded; draw chances only by fortress, never counterplay on the far wing.
- T84SF1G1 L m66: 17...Qf4 18.Qxf4 Bxf4 19.g3 Bd6 20.a4 a5 21.Bc3 Bb4?! 22.Bxb4 axb4 (doubled, loose b4) 23.Rae1 Bd7 24.c5 Rxe1 25.Rxe1 Be6? 26.Re4! (b4 + Be6). Fix: keep the bishop pair (21...Bf8/...b6), after the rook trade ...Kf8/...Bc8 not ...Be6, guard b4 or give it up for activity.
- T84R5 D (m61, threefold at SF +7): 16...Qg5?! 17.h4 Qe7 18.Qe4 (Bd3+Qe4 at h7). 18...g6? 19.Qd4! hits g7/a7. Fix: queen stays e7; v Qe4 play ...Rd7, ...Bf5 or ...f5; NEVER ...g6. The shell held 40 moves; SF repeated Bb5+/Kd8.
- T83R2 L (m73): 11...Qf6? 12.Qxf6 Bg4+?? 13.f3! gxf6 14.fxg4. Simply 12...gxf6. Take the pending recapture first (tools/check-block.py).
- THE HOLE IN SIX GAMES: Qe4/Qf3 + Bd3 on h7. After Bd3 write who guards h7/g7 EVERY move; no ...f4/...c5 freeing e4, K off the e-file.
- T80R2 W: SF 18.Qe2?? gave c4, Qf3, Re2; my 22...f4?? let Qe4 hit h7. Better ...Rd7/...Bf7/...Re8 keeping f5.

## LINE B2 (T82 Final L m70): 9...Qe7+ 10.Qe3 Qxe3+ 11.fxe3 bxc6
- Level to move 14: 12.Ba4 Ba6 13.a3 Bd6 14.Kf2 Rfe8 15.d3 Rab8. Then I drifted (bishop shuffles, ...c5, ...c6); a4/b5/a6/b6 storm won space, 25...c6? 26.a6 gave +2. Fix: no bishop shuffles; trade Ba4 early or play ...a5. Prefer 9...Re8+ 10.Kd1 dxc6.
- Tool gating in a lost phase: pawn-loss flags on forced king moves; in check send the only legal move at once.

## Left the book (T30R3 L)
7...Ne7? 8.Nxe5. 10...Bc5 11.Re1 Re8?? 12.Qxf7+; 10...Qd6 11.c3!; 9...bxc6?? 10.d4 (line A); 10...Bxd2?? 11.Rd1!
