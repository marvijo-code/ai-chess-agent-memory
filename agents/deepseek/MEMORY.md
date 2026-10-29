# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance/Classical B (T73R4/R6, T74R1/R3)
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Ruy W
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-dragon-white.md - Accelerated Dragon W
- notes/sicilian-soltis-black.md - Soltis B
- tools/: material-clock, clock-guard, repetition-guard, legal-list, fork-alert, queen-rook-safety, late-mate-scan

## Rule 0 - board, legality, clock
- CLOCK IS THE #1 LOSS MODE: T74R1 forfeited m49 11:47 vs 50:12 after 48 min (provider 103 s); >100 s reply loses. T73R6 7:07 vs 53:31; T73R3 0:55 vs 42:31; T73R5 2:12 vs 19:28. Routine 5-15 s, capture/trade 20-30 s, HARD CAP 60 s; level or worse after m25 cap 15 s (8 s after 40). Count minutes vs moves every move. Closed shell: quiet retreats 5-10 s, one plan, repeat. T74R3 banked 23:08 vs 11:02 at 5-60 s a move. T74R4 up exchange: 3:09 on 29.Qd3, 3:03 on 30.Bxb5; won position = 5-10 s.
- LONG THINKS BUY NOTHING: T73R4/R5/R7 and T74 48 min found no save; pick the list, send, move on.
- TOOL AVOID IS NOT MATERIAL: T73R7 17.Bxb8! won Q for B (Rc8 recaptures) but my loose-piece tool flagged it; I played 17.Bg3??. Count Q for B/R before obeying a flag; expect one refusal, resubmit once with the count.
- INVALID TRIES come after his captures and my long thinks (T72R5 4, T73R6 8, T74R2 5, T74R3 2: ...Bf4, ...Rd5). Rebuild every square from the FEN after his move; check the UCI with tools/legal-list.py; 3 tries = forfeit; after ONE rejection change piece AND idea. ROOK/BISHOP SWINGS: walk transit AND landing through MY pieces (T74R3 ...Rd5 blocked by my own Nd7). In check, enumerate every legal king move/block from the FEN; T74R2 23.Kh1 took 3 tries.
- BOARD MAP FROM HIS LAST MOVE before any capture: a moved piece is not on its old square (T67R5.1 Qd4?? on a ghost d4-knight cost my queen).
- LEGALITY: actual square, occupant, path squares, my own blockers; a pinned pawn cannot recapture; O-O needs king/rook unmoved and empty flights; two-step push needs empty transit.
- HIS last move first, then my destination: 0 guards + his capture = gift; quiets and retreats too.
- ONE MINOR MUST NOT MAKE FOUR MOVES: when a piece is kicked, develop ANOTHER piece or trade it (T73R5 Bf4/Bg3/Bf3/Be2 tours cost 20 moves).

## Rule 1 - destination sweep
- ATTACKED PIECE: list its retreat squares before any quiet move; never fill one with another piece. T74R2 11.Be2?? filled e2, the d4-knight's only safe flight (f3 was a pawn), and Qd5 hit d4: 11...Nxd4 won a piece. A defended piece can still be lost when his capture has a second recapturer; count the chain, not just my first recapture.
- AN ATTACKED PIECE IS THE MOVE when nothing of mine recaptures there (T72R5 12.Ng3 on the f5-bishop: ...Bg6/...Bd7/...g6).
- LIST HIS PAWN CAPTURES VS EVERY LANDING, knights included: e5 owns f6/d6, g4 f5/h5 (T66R2 16...Nf5?? gxf5).
- AN ATTACK IS NOT A DEFENCE (T71R1 22.Bd5?? Bxd5).
- MY OWN PIECE ON A LINE IS MY ONLY SCREEN; moving it exposes (T67R3 ...Bxe3?? 20.Qxc7). A queen does not guard a pawn on the same file through my own bishop: T73R5 13.Qe2?? while Be3 stood on e3.
- TWO LOOSE UNITS IN A ROW THROW A WON OPENING: list my undefended pieces and his queen/rook/bishop reaching them.
- HITTING HIS QUEEN IS NO ANSWER WHEN IT OPENS A CHECK.
- A PAWN THAT LEAVES ABANDONS ITS POST: no ...f6 with my king on e8/f8 and e6 unguarded (T69R4 23.Nxe6#); QGD ...c5 only with a piece guard on d5. T74R1: ...f6/...f5 left e6 to nothing.
- WITH HIS ROOK ON MY 6TH RANK, EVERY UNGUARDED PAWN THERE FALLS: T74R1 29...f6 30...f5 -> 34.Rxe6!, 35.Rxg6+, 37.Rxh5. Before ...f6/...f5/...g6/...h5 name that pawn's pawn-or-piece guard.
- A SYMMETRIC TRADE THAT HANDS HIM THE ONLY OPEN FILE AND LEAVES MY LAST MINOR AS A TARGET IS BAD: T74R1 18...Nxd4?? (SF).
- NEVER A KNIGHT/BISHOP/QUEEN WHERE HIS PAWN, KNIGHT OR BISHOP FORKS IT WITH ANOTHER UNIT (T72R2 18...Bf3?? 19.Nd4; d5-knight retreats b4/e7/b6/c7; no f6 while e5 lives; no h6 while his dark bishop lives).
- KNIGHT ON h6 WITH HIS Bf4/Bg5 ALIVE IS A GIFT: T73R6 11...Nh6?? 12.Bxh6.
- DON'T KICK A DEFENDED CENTRAL KNIGHT WITH A PAWN (T67R3 17...e5?? 18.Ndf5).
- PAWN ATTACKS: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, e5<-d4/f4, f5<-e6/g6, f6<-e5.
- ROOKS/KNIGHTS only where guarded; the mover abandons its guard - name it.
- HIS KNIGHT LEAVING c6 CAN OPEN A BISHOP DIAGONAL TO HIS QUEEN.

## Rule 1b - mate first
- Ask what mates if I pass; tools/late-mate-scan.py lists my moves that allow mate in 1. King g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2# unless h3.
- BACK RANK: keep a rank-1 blocker or luft (T67R2 37.Rc1 Rxc1#).
- KING ON c8 WITH b7 EMPTY: his queen on a6 checks down a6-b7-c8 (T73R4 19.Qa6+ 20.Qb7#). Cover b7 twice.
- KING-TAKES: an unguarded piece beside his king is a king capture.
- WON POSITION: forcing checks beat slow lifts; check stalemate before promoting; 5-10 s a move.
- MY FINISHER: a boxed king on f1 with my knight on f4 (guarded by my rook on the 4th) = Rc1#; the knight covers e2/g2/h3 (T74R3).

## Rule 2 - queen
- NEVER on an enemy pawn's capture square, a bishop diagonal, a rook file or a knight jump square (T69R2 19...Qd6?? 20.Nxd6).
- A KNIGHT JUMP WITH CHECK KILLS HER (T72R5 19.Nc5 20.Nb7+).
- WANDERING QUEEN: name ONE square and keep her there; T73R3 Qb6-Qa7-Qc7-Qd7-Qb6-Qa5 cost 10 min.
- A QUEEN GRAB IS A DEVELOPMENT LOAN: T73R4 14...Qxd4?! handed him 15.Bf4/16.Nxe4/17.Rad1. Before any queen capture list his developing replies and the file his rook takes.
- QUEEN ON e2/d2/d3 IN FRONT OF HIS KNIGHTS: ...Ne5/...Nf4 hits her with tempo.
- HIT -> she moves that move, off every attacker ray; a rook hit leaves file AND rank.
- TWO QUEENS ON ONE LINE WITH MY PIECE BETWEEN: that piece is frozen.
- QUEEN RECAPTURE: walk every enemy attacker of the landing square; a queen who is the sole guard of a piece loses it.

## Rule 3 - captures & trades
- RECAPTURE != TRADE: my recapturer must reach the square in one move and stay guarded (T73R3 16...exf5 was a trade).
- UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO; never R for B/P.
- HIS PAWN SAC OPENS A LINE (T69R4 13.b4! against my c8-king).
- After long castling behind doubled c-pawns answer ...b4-b5 with ...b5/...a5/...Kb8/...Rc8; never grab, never trade the dark bishop.
- A BLOCKADED FORTRESS IS NOT CONVERTED BY REPETITION: name an opening file and use the king (T72R1).
- A ROOK THAT BLOCKS IS A ROOK THAT STAYS: name the blockade duty before moving it (T73R3 Rc4).
- ROOK ON AN OPEN FILE FACING HIS ROOK NEEDS A GUARD: T73R6 ...Rd5 with his Rd1 and Nd4 allowed Nxe6+ uncovering the rook.
- A KNIGHT ON d6 GUARDED BY e5 IS A PIVOT: it hits f7/b5 and forks Qa5+Rd8 from b7; before landing check his knight no longer covers d6 and b7 is unattacked (T74R4 24.Nd6/25.Nb7; ...f6?? allowed it). Do not offer your strong Bd4 for his passive Bc5 just to trade (T74R4 20.Be3??; Qf3/Ng3 first).

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD EVERY MOVE; no grabs when level or behind.
- DOWN MATERIAL v SF: 5-10 s, every unit guarded, solid first rank, keep the king's pawn cover; T72R2 down a piece held to threefold, T72R5 down Q for N to m26.
- DOWN Q FOR R: 2N v R+pawns is not a fortress.
- UP MATERIAL IS A CLOCK PROBLEM: 5-10 s, consolidate, trade pieces not pawns; name ONE conversion; never offer queen trades by repetition.
- UP A PIECE v a passive player: trade minors (T74R3 22...Bxd4 into +N), knight shuttle Nd5/Nf6, ...b5 clamp then ...c5-c4-c3 with Rc4 guarding c3, Nf4 guarded by that rook, ...h4, Rc1#. 5-60 s a move; his 3-6 min thinks gift me the clock.
- UP A QUEEN/ROOK: mate clock, first forcing check or ladder, 5-10 s; recount after each capture.
- AFTER A QUEEN TRADE RECOUNT: if the recapture chain loses a queen, do not start it.
- EXTRA PIECE IN A BLOCKED POSITION: break the blockade (second front, attack the blockader), not a knight tour; blockader pawns must stay guarded by pawns or pieces (T74R1).
- DOWN A PAWN IN A CLOSED SHELL: a draw is a real result, but no 3-4 min bishop retreats. Pick one break (d5/e5/f4) or repeat with purpose; 5-15 s.

## Openings
- Open Sicilian Taimanov W (play): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies). Then f4, Qd2, Rad1, Kh1; e5 hits Nf6; after ...Nd5 Nxd5 exd5 Bf3! hits d5/Nc6. No d5/Rad1 while his knight can jump to e5. Vs GLM's ...Qd7/...Rd7/...Qc6 cluster: Bxf6! gxf6 Nxf6+ Kg7 Bxc6! wins the queen. Vs ...d6/...Nbd7 hedgehog this build is too slow: choose d5/e5 or f4 by move 15-18. T73R7 v Muse: 13.e5?! dxe5 14.fxe5 Nxe5! won a pawn. Keep tension; e5 only when ...dxe5 is impossible or ...Nxe5 loses to Bf4. T74R4 v GLM (1-0 forfeit): 5...e6/6...Be7/7...O-O/8...d6; 9.f4 Qc7 10.Qd2 a6 11.Rad1, ...Nxd4 Bxd4, ...b5-b4 Ne2; 16.e5! dxe5 17.fxe5 cramped him; Ne2-g3-e4-d6 (e5 guards d6), Nb7 forked Qa5+Rd8, Nxd8 won exchange then queen.
- Caro Advance B (play): 1.e4 c6 2.d4 d5 3.e5 Bf5 4.Be2 e6 5.Nc3 c5 6.Bb5+ Nc6 7.Bxc6+ bxc6 8.Nge2 Be7 (16 plies). Then ...c4/...Nge7/...O-O; c6 guards d5; keep the f5-bishop guarded. NO ...f6 without a piece guard on e6; no ...g5/...h5 uncastled. T74R1: level to m20 with ...Nd7/...Ne7/...Bg6/...h6/...Qc7/...Nf5/...Be7/O-O; then 18...Nxd4?? and ...f6/...f5/...g6/...h5 handed him e6, g6 and h5. T73R6: 11...Nh6?? lost to Bxh6.
- Caro Classical 3.Nc3 B (play): ...dxe4, ...Bf5, ...Bg6, meet h4-h5 with ...h6/...Bh7; then ...e6, ...Nf6, ...Be7, O-O, ...Nbd7, ...Re8, ...Qc7, ...Bd6, ...c5 only with a piece guard on d5. THE BREAK: ...e5! with Bd6+Nd7 behind it when his king is on b1 and his Qd3 sits in the centre (T74R3 17...e5 won a pawn: 18.dxe5 Bxe5, Nxe5 Nxe5 hits Qd3). T71R2 17...e4! won B for P but four illegal tries; T72S2G1 ...c5-c4 clamp, ...b4, ...bxc3+, ...Rxc2+ converted.
- English as Black (reversed QGD, play): ...Nf6/...e6/...d5/...Be7/...O-O/...c6, then ...Bf5, ...Nbd7, ...Qb6, ...Re8; ...c5 only with a piece guard on d5. BANS: knight on his e4-pawn's d5/f5, queen on d7 or the c6-pawn.
- Ruy Lopez W, Classical 5...Bc5 (play): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Bc5 6.c3 O-O 7.Re1 d6 8.h3 (15 plies). Then ...Be6, d4; after exd4 cxd4 ...Bb6 and Nc3; later Bg5 ...h6 Bxf6, Nd5.
- Ruy W quiet 4.d3 (worked v GLM): ...Bd6, O-O, c3, ...Re8, Nbd2, h3, Re1; then Bc4, Nf1-g3; avoid Bg5; Nf5 hits Bd6/g7; finisher Bxh6 with g7 pinned, Qf6+/Qf8#.
- Ruy Four Knights 4...a6 W (play): 1.e4 e5 2.Nf3 Nf6 3.Nc3 Nc6 4.Bb5 a6 5.Ba4 b5 6.Bb3 Be7 7.O-O O-O 8.d3 d6 (16 plies). Then Be3, Qd2, Rad1, h3, d4; keep e4 guarded, no Nd5 while ...Bb7 stands. Before the queen leaves the 2nd rank put Rb1 under b2.
- Ruy 3...a6 4...d5 (v GLM): 5.exd5 b5 6.Bb3 Nd4 7.c3 Nxb3 8.Qxb3 gave me a pawn but his fortress held - open a second front.
- Italian Giuoco Pianissimo W: ...Nc6/...Bc5/...Nf6, ...d6, castle, ...Be6, ...Qd7/...Re8/...d5; if ...Bg4 then Re1/h3. No 10.d4?! or a queen on d5 while Nf6 lives.
- Accelerated Dragon W: play the Taimanov build; after ...d5 exd5 Nxd5 Nxd5 Qxd5 play Bf3! hitting the queen (not Be2??; T74R2 lost a piece). Meet ...Qa5+ with c3, ...Nxd4 with Bxd4. No queen wander, no Bd5 without a recapture.
- Open Sicilian Taimanov B: ...Nxc6/...bxc6 with Bd3 and Be7. The e5-clamp is answered only by ...Nd5 and ...Bf8. With my king on e8 g7 has NO guard: never ...d6, never castle, never ...Nf6 while e5 stands; cover g7 with a PIECE. After ...Bf8 no ...g6, no ...h5.
- Dragon/Yugoslav B: 13.Qxd5 -> 13...Qc7 only, keep queens. Never move the last screen on a rank/file.
- Maroczy Bind W: c4, Nc3, Be2, Be3, Qd2, Rfd1; watch ...Ng4, ...f5, ...Qa5; never a rook on c4/d4/e4 a pawn captures; h3 before the queen trade.

## Opponents
- SF19: instant, zero errors. Punishes loose units, passive retreats, queens on rays/pawn squares/knight squares, ignored attacked pieces, pawn sacs opening lines to my king. As White vs my Caro Advance: Be2/Nc3/Nge2/O-O/b3-bxc4/Ng3-Nce4/Qe2/Bf4/Rad1, then Qa6+/Qb7# once my king sat on c8 with b7 empty. T74R2: vs Yugoslav ...d5 central strike; when my knight's retreat is blocked, ...Nxd4 wins it. 10-15 s; first rank solid.
- Muse Spark 1.3: patient 30 s-4 min, usually zero illegal, banks clock, takes every loose pawn and undefended piece, sits in a shell; the clock is the game against her. 5-10 s a move, no 7-min thinks. T73R7 Black Open Sicilian: Qxe5! won a piece; 3 invalid replies on 24...Kf8 forfeited. T74R3 W v my Classical Caro: level to m17, then my ...e5! won a pawn; she burned 3-6 min (Rdd1 5:44, Qe3 3:28) while I banked, then took h5 with the knight but went down to ...b5/...c5-c4-c3, Nf4, Rc1#. Keep units guarded, bank clock, clamp and mate.
- GLM 5.3 Flash: HIS QUEEN ON MY PAWN'S OR KNIGHT'S CAPTURE SQUARE (five+ times). 1-7 illegal tries, often 3 on a check reply. Take gifts only after the pawn/bishop capture list; decline queen trades when a pawn down - name a conversion. T74R4: ...b5-b4 hit Nc3; my e5/Ne2-g3-e4-d6/Nb7 won the exchange and queen; he gave 1 illegal then forfeited 3 on a check reply (Be8).
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov/English both ways; keeps units guarded; punishes a piece on his pawn's square and a queen on a rook file.
- Sonnet 5.5: 40-50 min of clock, zero illegal, punishes a loose queen/rook and every pawn grab; in endings he centralizes the king, puts a rook on my 6th rank and eats unguarded pawns (T74R1: e6, g6, h5). T73R6 met ...Nh6 with Bxh6 and doubled my pawns, then won the d5-rook with Nxe6+. Bank clock from move 1: 5-10 s book, 10-15 s quiet.
- Fable 5.1, GPT-6.1 Sol, Astra: take every unguarded unit, so keep every unit guarded and bank clock. Haiku 5.5: solid Italian Pianissimo, fast.
