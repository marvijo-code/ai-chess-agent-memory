# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
- tools/: material-clock, clock-guard, repetition-guard, legal-list, fork-alert, queen-rook-safety, late-mate-scan, forcing-moves

## Rule 0 - board, legality, clock
- CLOCK IS #1 LOSS MODE: >100 s reply loses; T74R1 forfeited after 48 min, T73R6 7:07 vs 53:31, T73R3 0:55 vs 42:31. Routine 5-15 s, capture 20-30 s, CAP 60 s; level/worse after m25 cap 15 s (8 s after 40). T74 Arm W: 2:56 on 28.Qb2??. No 2-min thinks; bank clock from move 1. Won = 5-10 s; level = 10-20 s.
- LONG THINKS BUY NOTHING: T73R4/R5/R7, T74 48 min, T74R7 4:06 on 12...Bd6? and 2:28 on 13...c5? (both SF-flagged mistakes) found no save; T74 Arm W 1:57 on 11.Rad1 and 1:29 on 15.Qd3 in a level Scheveningen bought nothing. Pick the list, send, move on.
- TOOL AVOID IS NOT MATERIAL: T73R7 17.Bxb8! won Q for B but my loose-piece tool flagged it; I played 17.Bg3??. Count Q for B/R before obeying; expect one refusal, resubmit once with the count.
- INVALID TRIES come in pairs (T72R5 4, T73R6 8, T74R2 5, T74R3 2, T74R7 2: ...Bd6, ...dxe4). Rebuild every square from the FEN; check UCI with tools/legal-list.py; 3 tries = forfeit; after ONE rejection change piece AND idea. ROOK/BISHOP SWINGS: walk transit AND landing through MY pieces (T74R3 ...Rd5 blocked by own Nd7; T74R6 ...Nc6 blocked by own c6 pawn). In check, enumerate every legal king move/block from the FEN.
- BOARD MAP FROM HIS LAST MOVE before any capture: a moved piece is not on its old square (T67R5.1 Qd4?? on a ghost d4-knight).
- LEGALITY: actual square, occupant, path, my own blockers; pinned pawn cannot recapture; O-O needs king/rook unmoved and empty flights; two-step push needs empty transit.
- HIS last move first, then my destination: 0 guards + his capture = gift; quiets and retreats too.

## Rule 1 - destination sweep
- ATTACKED PIECE: list its retreat squares before any quiet move; never fill one with another piece. T74R2 11.Be2?? filled the d4-knight's only flight; ...Nxd4 won a piece. A defended piece can still be lost when his capture has a second recapturer; count the chain.
- AN ATTACKED PIECE IS THE MOVE when nothing of mine recaptures there (T72R5 12.Ng3 on the f5-bishop).
- A KNIGHT ON d5 HITS MY Be3 (T74 Arm W): count guards; if hit, move bishop or trade knight.
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included: e5 owns f6/d6, g4 f5/h5 (T66R2 16...Nf5?? gxf5).
- HIS d4-PAWN OWNS c5 AND e5: T74R6 24...Bc5?? met 25.dxc5 = B for P. No bishop/knight/rook on c5 or e5 while his d-pawn stands.
- AN ATTACK IS NOT A DEFENCE (T71R1 22.Bd5?? Bxd5).
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN; moving it exposes (T67R3 ...Bxe3?? 20.Qxc7). A queen does not guard a pawn on the same file through my own bishop (T73R5 13.Qe2?? while Be3 stood on e3).
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING: list my undefended pieces and his queen/rook/bishop reaching them.
- HITTING HIS QUEEN IS NO ANSWER WHEN IT OPENS A CHECK.
- A PAWN THAT LEAVES ABANDONS ITS POST: no ...f6 with my king on e8/f8 and e6 unguarded (T69R4 23.Nxe6#); QGD ...c5 only with a piece guard on d5.
- WITH HIS ROOK ON MY 6TH RANK, EVERY UNGUARDED PAWN THERE FALLS: T74R1 ...f6/...f5 let 34.Rxe6!, 35.Rxg6+, 37.Rxh5. Before ...f6/...f5/...g6/...h5 name that pawn's pawn-or-piece guard.
- NEVER A KNIGHT/BISHOP/QUEEN WHERE HIS PAWN, KNIGHT OR BISHOP FORKS IT WITH ANOTHER UNIT (T72R2 18...Bf3?? 19.Nd4; d5-knight retreats b4/e7/b6/c7; no f6 while e5 lives; no h6 while his dark bishop lives).
- KNIGHT ON h6 WITH HIS Bf4/Bg5 ALIVE IS A GIFT: T73R6 11...Nh6?? 12.Bxh6.
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5.
- ROOKS/KNIGHTS only where guarded; the mover abandons its guard - name it.

## Rule 1b - mate first
- Ask what mates if I pass; tools/late-mate-scan.py lists my moves that allow mate in 1. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3.
- BACK RANK: keep a rank-1 blocker or luft (T67R2 37.Rc1 Rxc1#).
- KING ON c8 WITH b7 EMPTY: his queen on a6 checks down a6-b7-c8 (T73R4 19.Qa6+ 20.Qb7#). Cover b7 twice.
- KING-TAKES: an unguarded piece beside his king is a king capture.
- MY FINISHER: a boxed king on f1 with my knight on f4 (guarded by my rook on the 4th) = Rc1#; the knight covers e2/g2/h3 (T74R3).

## Rule 2 - queen
- NEVER on an enemy pawn's capture square, a bishop diagonal, a rook file or a knight jump square (T69R2 19...Qd6?? 20.Nxd6). ENEMY KNIGHT COUNTS TOO: T74 Arm W 16...Qe4?? landed on Nc3's capture square, 17.Nxe4 = Q for N.
- A KNIGHT JUMP WITH CHECK KILLS HER (T72R5 19.Nc5 20.Nb7+).
- A QUEEN ON HIS QUEEN'S RANK/FILE WITH ONE OF HIS PIECES BETWEEN IS NOT SAFE: that blocker can move with tempo (T75R1 19.Qb6?? her Nc6-d4 opened c6, ...Qxb6 won my queen). Count the blocker's legal moves before she lands; when up material keep her defended and off his queen's lines.
- WANDERING QUEEN: name ONE square and keep her there; T73R3 Qb6-Qa7-Qc7-Qd7-Qb6-Qa5 cost 10 min.
- A QUEEN GRAB IS A DEVELOPMENT LOAN: T73R4 14...Qxd4?! handed him 15.Bf4/16.Nxe4/17.Rad1. Before any queen capture list his developing replies and the file his rook takes.
- HIT -> she moves that move, off every attacker ray; a rook hit leaves file AND rank.
- QUEEN RECAPTURE: walk every enemy attacker of the landing square; a queen who is the sole guard of a piece loses it.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach the square in one move and stay guarded (T73R3 16...exf5 was a trade).
- UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO; never R for B/P.
- HIS PAWN SAC OPENS A LINE (T69R4 13.b4! against my c8-king).
- After long castling behind doubled c-pawns answer ...b4-b5 with ...b5/...a5/...Kb8/...Rc8; never grab, never trade the dark bishop.
- A ROOK THAT BLOCKS IS A ROOK THAT STAYS: name the blockade duty before moving it (T73R3 Rc4).
- ROOK ON AN OPEN FILE FACING HIS ROOK NEEDS A GUARD: T73R6 ...Rd5 with his Rd1 and Nd4 allowed Nxe6+ uncovering the rook.
- A KNIGHT ON d6 GUARDED BY e5 IS A PIVOT: hits f7/b5, forks Qa5+Rd8 from b7 (T74R4 24.Nd6/25.Nb7). Don't offer Bd4 for his passive Bc5 (20.Be3??).

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level or behind.
- DOWN MATERIAL v SF: 5-10 s, every unit guarded, solid first rank, keep the king's pawn cover; T72R2 down a piece held to threefold, T72R5 down Q for N to m26. DOWN Q FOR R: 2N v R+pawns is not a fortress.
- DOWN B FOR P (T74R6): king to the centre, passers ...c4/...d3, rook on the d-file guarding them, take loose wing pawns; a threefold is a real result.
- BLOCKADED PASSER WITH HIS ROOK ON IT: my rook is pinned to the passer and cannot win (T74R6). Free the rook (bishop guards the passer, king attacks his last pawn) or accept the draw.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, trade pieces not pawns; name ONE conversion; never offer queen trades by repetition.
- UP A PIECE v a passive player: trade minors (T74R3 22...Bxd4 into +N), knight shuttle Nd5/Nf6, ...b5 clamp then ...c5-c4-c3 with Rc4 guarding c3, Nf4 guarded by that rook, ...h4, Rc1#. 5-60 s a move; his 3-6 min thinks gift me the clock.
- UP A QUEEN/ROOK IS A MATE PROBLEM: first forcing check or ladder, 5-10 s; recount after each capture; check stalemate before promoting. Then bring a rook to his 2nd rank, attack one fixed pawn with Q+R, or give the extra minor for a rook (Q v R wins). T74R7: up Q+N v 2R from m28 I only centred the queen (Qe6/Qf6/Qd7) and let a THREEFOLD happen - repetition with a queen up is a loss. His shell was Kg2, rooks b1+d1 inter-guarded, pawns a4/b3/f2/h3; use the knight (Nc7-e6-f4+) and a rook lift.
- UP Q FOR N (T74 Arm W won): trade the knight that is his fork source (21.Bxe4), take queen tempo on his rook (22.Qc3 hit Rc8, 23.Qe1 off the knight's squares), then rook lift; his fortress plus 1:49 thinks left him 0:14 at m23 - the CLOCK is the win. 5-15 s a move, no 1:30 quiet moves.
- EXTRA PIECE IN A BLOCKED POSITION: break the blockade (second front, attack the blockader), not a knight tour; blockader pawns must stay guarded by pawns or pieces (T74R1).
- DOWN A PAWN IN A CLOSED SHELL: a draw is a real result, but no 3-4 min bishop retreats. Pick one break (d5/e5/f4) or repeat with purpose; 5-15 s.
- ARMAGEDDON AS WHITE: a draw is a loss. Quiet Ruy 4.d3 is too slow if d4 waits until move 16; play d4 by move 12-14 or choose a sharper line. Level/worse: do not repeat; vary and create chances. T74 Arm W: Open Sicilian, his queen gift at m17, clock win.

## Openings
- Open Sicilian Taimanov W (play): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies). Then f4, Qd2, Rad1, Kh1; e5 hits Nf6; after ...Nd5 Nxd5 exd5 Bf3! hits d5/Nc6. No d5/Rad1 while his knight can jump to e5. Vs GLM's ...Qd7/...Rd7/...Qc6 cluster: Bxf6! gxf6 Nxf6+ Kg7 Bxc6! wins the queen. Vs ...d6/...Nbd7 hedgehog this build is too slow: choose d5/e5 or f4 by move 15-18. Keep tension; e5 only when ...dxe5 is impossible or ...Nxe5 loses to Bf4 (T73R7). T74R4 v GLM: 16.e5! cramped him; Ne2-g3-e4-d6, Nb7 forked Qa5+Rd8. T74 Arm W v his Scheveningen (...d6/...e6/...a6/...Qc7/...b5/...Bb7/...Rd8): 13.e5?! (SF ?!) let ...dxe5/...Qxe5 centralise her (fxe5! was right); then Nf3 hit Qe5 and his ...Qe4?? stood on Nc3's capture square = Q for N. Keep 5-15 s through the build.
- Caro Advance B (play): 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies). Then ...c4/...Nge7/...O-O; c6 guards d5; keep the f5-bishop guarded. NO ...f6 without a piece guard on e6; no ...g5/...h5 uncastled. T74R1: ...f6/...f5/...g6/...h5 handed him e6/g6/h5. v 4.Nf3/Nbd2/c3 (T74R6 draw): ...e6/...Be7/...Nd7/...c5/...cxd4; 9...f6?! freed g8 but gave him e5; 24...Bc5?? = B for P; drew with king + c4/d3 passers.
- Caro Classical 3.Nc3 B (play): ...dxe4, ...Bf5, ...Bg6, meet h4-h5 with ...h6/...Bh7; then ...e6, ...Nf6, ...Be7, O-O, ...Nbd7, ...Re8, ...Qc7, ...Bd6, ...c5 only with a piece guard on d5. THE BREAK: ...e5! with Bd6+Nd7 behind it when his king is on b1 and his Qd3 sits in the centre (T74R3 17...e5 won a pawn: 18.dxe5 Bxe5, Nxe5 Nxe5 hits Qd3).
- English as Black (reversed QGD, play): ...Nf6/...e6/...d5/...Be7/...O-O/...c6, then ...Bf5, ...Nbd7, ...Qb6, ...Re8; ...c5 only with a piece guard on d5. BANS: knight on his e4-pawn's d5/f5, queen on d7 or the c6-pawn. T74R7 v GLM: after his Bg5-Bf4 and Ne5, ...Bd6? and ...c5? (both SF-flagged) let him liquidate with Nxd7 and dxc5; try ...Ne4/...Re8 and keep ...c5 back.
- Ruy Lopez W, Classical 5...Bc5 (play): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies). Then ...Be6, d4; after exd4 cxd4 ...Bb6 and Nc3; later Bg5 ...h6 Bxf6, Nd5.
- Ruy W quiet 4.d3 (worked v GLM): ...Bd6, O-O, c3, ...Re8, Nbd2, h3, Re1; then Bc4, Nf1-g3; avoid Bg5; Nf5 hits Bd6/g7; finisher Bxh6 with g7 pinned, Qf6+/Qf8#. T74 Arm W v Sonnet: ...h6/...a6/...b5/...Na5/...c5/...Qc7/...Bc6/...Nc4/...a5/...b4; play d4 by move 12-14.
- Ruy Four Knights 4...a6 W (play): 1.e4 e5 2.Nf3 Nf6 3.Nc3 Nc6 4.Bb5 a6 5.Ba4 b5 6.Bb3 Be7 7.O-O O-O 8.d3 d6 (16 plies). Then Be3, Qd2, Rad1, h3, d4; keep e4 guarded, no Nd5 while ...Bb7 stands. Before the queen leaves the 2nd rank put Rb1 under b2.
- Italian Giuoco Pianissimo W: ...Nc6/...Bc5/...Nf6, ...d6, castle, ...Be6, ...Qd7/...Re8/...d5; if ...Bg4 then Re1/h3. No 10.d4?! or a queen on d5 while Nf6 lives.
- Accelerated Dragon W: play the Taimanov build; after ...d5 exd5 Nxd5 Nxd5 Qxd5 play Bf3! hitting the queen (not Be2??; T74R2 lost a piece). Meet ...Qa5+ with c3, ...Nxd4 with Bxd4. No queen wander, no Bd5 without a recapture.
- Open Sicilian Taimanov B: ...Nxc6/...bxc6 with Bd3 and Be7. The e5-clamp is answered only by ...Nd5 and ...Bf8. With my king on e8 g7 has NO guard: never ...d6, never castle, never ...Nf6 while e5 stands; cover g7 with a PIECE. After ...Bf8 no ...g6, no ...h5.
- Dragon/Yugoslav B: 13.Qxd5 -> 13...Qc7 only, keep queens. Never move the last screen on a rank/file.
- Maroczy Bind W: c4, Nc3, Be2, Be3, Qd2, Rfd1; watch ...Ng4, ...f5, ...Qa5; never a rook on c4/d4/e4 a pawn captures; h3 before the queen trade.

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on rays/pawn squares/knight squares, ignored attacked pieces, pawn sacs opening lines to my king. Vs my Caro Advance: Be2/Nc3/Nge2/O-O/b3, then Qa6+/Qb7# with my king on c8 and b7 empty. T74R2: vs Yugoslav ...d5 central strike; when my knight's retreat is blocked, ...Nxd4 wins it. 10-15 s; first rank solid.
- Muse Spark 1.3: patient 30 s-4 min, zero illegal, banks clock, takes loose units, sits in a shell; the clock is the game. 5-10 s a move. T73R7 Qxe5! won a piece. T74R3 my ...e5! won a pawn while she burned 3-6 min. T75R1: up B+P, 19.Qb6?? let her Nc6-d4 open c6 and ...Qxb6 won my queen; my Rd4/Rd5 fortress then drew by threefold as her clock ran. No queen on her queen's rank with a movable blocker.
- GLM 5.3 Flash: HIS QUEEN ON MY PAWN'S OR KNIGHT'S CAPTURE SQUARE (7+ times, incl. T74 Arm W 16...Qe4?? 17.Nxe4 = Q for N, and T74R7 19.Qf3?? exf3). 1-7 illegal tries, often 3 on a check reply. Take gifts only after the pawn/bishop/knight capture list; decline queen trades when a pawn down - name a conversion. T74R4: ...b5-b4 hit Nc3; my e5/Ne2-g3-e4-d6/Nb7 won exchange and queen. Down material he fortresses (Bf8/Ndf6/Rb8/h6) but still burns 1:49 thinks (T74 Arm W: flagged 0:14 at m23) - trade the fork-source knight, queen tempo, 5-15 s, let his clock die. T74R7: with Q+N up I let his Kg2 + inter-guarded rooks shell reach a threefold.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded; punishes a piece on his pawn's square and a queen on a rook file.
- Sonnet 5.5: 40-50 min clock, punishes a loose queen/rook and every pawn grab; in endings he centralizes the king, puts a rook on my 6th rank and eats unguarded pawns (T74R1: e6, g6, h5). T73R6 met ...Nh6 with Bxh6 and doubled my pawns, then won the d5-rook with Nxe6+. T74 Arm W: quiet Ruy, ...b5/...Na5/...c5/...Qc7/...Bc6/...Nc4/...a5/...b4; took loose d5 and Be3, then accepted repetition with draw odds. Bank clock from move 1: 5-10 s book, 10-15 s quiet.
- Fable 5.1, GPT-6.1 Sol, Astra: take every unguarded unit, so keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast.
