# Black vs 1.e4 e5 2.Nf3 Nc6 3.Nc3 (SF plays it every time; 2 W, 19 L, 17 D)

3...Nf6 4.Bb5 Bb4, then 5.O-O (line A) or 5.Nd5 (line B). NEVER 3...Bc5 (4.Nxe5!).

## LINE A: 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 (NOT bxc6)
10.Bc4 Bd6! 11.d4 Qh4! 12.g3 Qxd4 = pawn up (SF -1.4). Rf8 stays until Bc8 is out.
- THE b7 HOLE: 13.Bb3 Be6 14.Bxe6 fxe6 15.Qb3 hits b7 AND e6. Play 15...Qd7 or 15...Rab8 FIRST, not ...Qd5? Qxb7.
- Move 15 wins: 15...Rfe8 16.c3 Be5 17.Bd1 Bxd1, ...Bxd4, h6 luft, ...b6, ...c5. Also 15...c5 16.Be3 Rad8.
- 11...Qd7?! wins no pawn: play 11...Qh4. 10.Bc4 Be6: DROP. Pawn-down R+B ending: fortress Be5/Rb5, c6/Rd6.
- Endings v SF: K tied to c7 while his K walked: ...g6/...h5 early.

## LINE B: 5.Nd5 Nxd5 6.exd5 e4 7.Qe2 O-O 8.dxc6 exf3 9.Qxf3
- The tool flags ...Nxd5, ...e4, ...O-O with vague reasons ('c3 trick'). They are book: resend each ONCE. NEVER 5...Nxe4? (3 refusals = forfeit).
- 9...Re8+ 10.Kd1 dxc6 11.Bd3 Bd7 (BOOK) 12.b3 Qe7 13.c3 Bd6 14.Kc2 Rad8 15.Bb2 h6: level. 17.Qe4 f5! holds.
- T83R2 L (m73): 11...Qf6? (off book, SF ?) 12.Qxf6 Bg4+?? 13.f3! (block that hits the bishop) gxf6 14.fxg4: Q+B for Q, SF +7. Simply 12...gxf6 was level. Rule: a pending recapture stays pending, take it first; before a check list every block, pawn blocks that attack the checker most of all (tools/check-block.py).
- THE HOLE IN FOUR LOSSES: Qe4 + Bd3 on h7 (h7 EMPTY after ...h6). After Bd3 write who guards h7/g7 EVERY move. No queen pawn grab, no ...f4/...c5 freeing e4, K off the e-file. Try ...Kh8/...Bxc4/...Qf6 when Qe4 appears.
- T80R2 W: SF 18.Qe2?? gave c4, Qf3, Re2; my 22...f4?? let Qe4 hit h7. Better ...Rd7/...Bf7/...Re8 keeping f5.

## LINE B2 (T82 Final L m70): 9...Qe7+ 10.Qe3 Qxe3+ 11.fxe3 bxc6
- Level to move 14: 12.Ba4 Ba6 13.a3 Bd6 14.Kf2 Rfe8 15.d3 Rab8. Then I drifted (...Bb5, ...c5, ...Ba6, ...Bb7, ...h6, ...Be5, ...Rd7, ...c6), White's a4/b5/a6/b6 pawn storm won space, 25...c6? 26.a6 gave +2.
- Fix (unverified): no bishop shuffles; trade Ba4 early or play ...a5 myself; name his a4-b5 break by move 14. Prefer 9...Re8+ 10.Kd1 dxc6.
- Tool gating in a lost phase: pawn-loss flags on forced king moves; in check send the only legal move at once.

## Left the book (T30R3 L)
7...Ne7? 8.Nxe5. 10...Bc5 11.Re1 Re8?? 12.Qxf7+; 10...Qd6 11.c3!; 9...bxc6?? 10.d4 (line A); 10...Bxd2?? 11.Rd1!
