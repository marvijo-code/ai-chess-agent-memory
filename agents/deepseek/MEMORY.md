# Chess memory

Notes:
- notes/capture-safety.md - scan, self-ban, blunder catalogue
- notes/ruy-lopez-black.md - Chigorin/Breyer as Black
- notes/ruy-lopez-white.md - Chigorin as White
- notes/sicilian-black.md - Alapin/Dragon as Black
- notes/sicilian-soltis-black.md - Soltis 9.Bc4
- notes/sicilian-yugoslav-black.md - Yugoslav 9.O-O-O: 9...d5 and 9...Nxd4
- notes/sicilian-dragon-white.md - Yugoslav as White
- notes/four-knights-black.md - 4.Bb5 Bb4

## Rule 0 - send-time legality & self-ban (3 invalid = forfeit)
- SELF-BAN: if my note/scan called the move bad, illegal or 'not on', NEVER send it - play the traced alternative (g67 26.Rxe7??, g70 23.Rxe5??; g72 ply-28 note said 'avoid the trade' and I still played 14...Qb6?). Identifying a danger is not enough: after choosing a move, check that it does NOT contain the danger.
- Legality: my turn, my pieces; never echo his move or repeat a piece's current square (g72 tried Kg8 while the king stood on g8); PATH clear of ALL pieces, own AND his (g70 Be3/Nd2; g68 Bg4-f5; g72 Rfb8 blocked by own Bc8); destination empty/enemy; two pieces to one square -> full name; one rejected attempt -> different move, never resend.

## Rule 1 - pre-move scan (5 s, FINAL position)
1. HIS last move first: name EVERY enemy attacker of my destination - rook file/rank, BISHOP DIAGONALS, knights, pawns (g68 18...Ra6?? Bd3 covers a6; g72 16...Rb8 landed on his Be3-f4-b8 diagonal). Attacked+undefended -> reject.
2. His KING attacks its 8 neighbours (g55 27...Rd2?? Kxd2); his rook on my 2nd rank: moving a blocker drops the piece behind it. Save my hit/loose piece NOW.
3. Pawns: never onto a pawn-attacked square, even defended; is this pawn the sole guard of my piece? Recapture MY pushed pawn (g63 13...b5?? axb5)? Push opens a file - who enters first (g61)?
4. QUEEN: enemy PAWNS'/KNIGHTS' capture squares FIRST, then N/B/R/Q lines. Qd4 next to his e5-pawn = Q for P (g67,g70). No queen on a file/rank/diagonal facing his rook/queen (g61 Qa3?? Rxa3). 'KEEP QUEENS ON' means pick a square with NO contact and no capture by his R: g72 14...Qb6? 15.Qxb6 axb6 = pawn-down queenless endgame = lost; ...Qd7/...Qd8 lose Q for R to Rd1xd7/d8. Move the queen to a no-contact square that still guards what it guarded (e.g. ...Qb7 on rank 7) - and my queen is the sole guard of e7, so e7 stays covered.
5. Trades: count ALL recapturers (PAWNS, bishops, knights); write HIS recapture AND mine - if his is last, don't start (g70 23.Rxe5?? dxe5); never 'offer' a trade that has no recapturer for me (g72 20...Rd8?? dropped my last rook to 21.Rxd8+, nothing recaptures d8). Value the chain (g58); sac: every recapturer + net (g65).
6. Mate nets BEFORE any move: Qh2+Rh1 on an open h-file (Nf6 = h7's only guard); Qh6 + rook h4/h5: Qxh7# through the empty h6 - luft or cover h7 FIRST, no grabs (g66,g69). Q+B on f2 (g61).
7. Loose minor/rook (jump, retreat, rook swing): list every enemy attacker of the destination + chain; the destination must be attacked by NOTHING (g58 Nd4??; g63 Nb4?? cxb4; g68 Ra6??; g70 25.Bd3?? Nxd3).
8. Down material: defend/trade; no 'active' queen onto a pawn-attacked square (g70 24.Qd4?? exd4); pawn down -> keep queens for counterplay (g68 13...Be6? 14.Qxd8) but only on squares with no trade contact (g72); no desperate grabs; repetition/stalemate = half point; when winning make progress.
9. Time: routine <=15 s, book <=10 s; <3 min -> <=5 s; <1 min -> 1-2 s; when lost 1-5 s. Long thinks never prevented a blunder or an illegal try (g46-g72).

## Openings
- Yugoslav 9.O-O-O d5 as Black: 13...Qc7! KEEP QUEENS ON (not Be6? 14.Qxd8); 14.Qc5 -> 14...Qb7 (no contact, rank 7 still guards e7); 14...Qb6? = 15.Qxb6 axb6 lost queenless endgame (g72); 14...Qd7/...Qd8 = Q for R (Rd1). Then ...Bd7 frees f8; do NOT park a rook on b8 (his Be3-f4-b8 diagonal: 16...Rb8 17.Bf4 18.Bxb8; if the rook is attacked, retreat ...Rb7, never ...Be6?! 18.Bxe6 fxe6 19.Bxb8 = R for B).
- Chigorin as White: 14...Nb4 -> 15.Bb1!; ...a5-a4: a3-kick once the b4-knight's retreats are covered (Na6), and/or reroute the d2-knight f1-e3-f5 (g70); 19.Nf5 Bxf5 20.exf5 = good clamp (SF !), then Be3/Qd2/Rc1, not 21.Bg5?!. No Nxe5 grabs; no Bxh6 sac when h6 is guarded twice (g65); no Qd4 next to his e5-pawn (g67,g70).
- Chigorin as Black: ...a6 ...Nf6 ...Be7 ...b5 ...d6 ...O-O then ...Na5/...c5/...Qc7/...Bb7/...Rac8; no ...Bg4 after 9.h3; if his bishop hits my queen, move the queen THAT move (g41 16...Rfd8?? 17.Bxa5); resolve the centre before his d5.
- Sicilian as Black: Dragon ...d6/...cxd4/...Nf6/...Nc6/...g6/...Bg7/...O-O; no ...Nxe4 while his Qf3 covers e4; b7 loose once b5 leaves; Rauzer 11...gxf6!.
- Alapin 5.Qxd4: ...Nc6 ...g6 ...Bg7 ...O-O ...Nd7-...Nc5 = equal; NEVER ...Nb4; no knight to d4; no ...b5 with his a4-pawn or while Rd1 faces Qd8 through d6; no Qa5 once the a-file opens.
- Soltis 9.Bc4: 14.h5 Nxh5! 15.g4 Nf6. 16.g5 -> ONLY 16...Nh5. 16.Qh2 (g4 gone): NO ...Nh5, NO knight move - keep Nf6. 16.Bh6: do NOT recapture - ...Qe8/...Qa5 + luft first. After 19.Rxh5 gxh5: play ...Re8 AT ONCE; g6 = h5's sole guard.
- 4N as Black: 6.Nd5 Nxd5! 7.exd5 Nd4!; no ...Bg4 after h3. Dragon as White: keep Bc5 defended.

## Opponents
- Stockfish 19: ~0 s/move, never errs tactically; punishes loose units, queens on attacked lines, back-rank, loose rooks (Bd3xa6); grabs the queen trade when it favors him; bank clock early; when lost play 1-5 s, never resign.
- Sonnet 5.5: banks clock early (g70: 1:39/3:23 thinks, then instant), takes EVERY free/attacked unit (dxe5, exd4, Nxd3, Qxf4); keep all defended, no speculative sacs; never resign; 1-3 s when lost.
- GPT-6.1 Sol: fast (3-13 s); takes every free piece/open-file loot instantly; vs the Soltis plays Bh6 then the g5+Rxh5 exchange sac with Qh6+rook on the h-file - f8 luft early, never grab with Qxh7# pending (g69).
