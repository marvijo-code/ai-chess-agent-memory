# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B: Clamp + 4.Be2 + Classical 3.Nc3
- notes/qgd-white.md - QGD W: Lasker/Bf4-IQP/Exchange/Tartakower/Bb4/Sol Nbd7
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban
- 3 rejected tries on ONE move = forfeit; each try also burns clock. O-O needs knight off home + f8/g8 empty. After O-O-O my king is on c8, so ...Rc8 is ILLEGAL. Before any bishop move path AND destination must be empty. After ONE rejection NEVER resend: redraw, list every legal square, choose.
- g168 had 5 rejected tries - all geometry: ...Rac8 with my Bc8 still home; ...Ke7 where his Kf8 guards e7. Before a ROOK move check the path squares for my own pieces; before a KING move list every enemy piece guarding the destination.
- A SQUARE I WANT MAY BE MINE ALREADY: name the blocker before ...f6/...e5/...c5.
- SELF-BAN: a move my scan/note called bad is DEAD. Reread the ban list before every knight, rook AND queen move.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; hitting two units is no safety.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7. MY piece lands where a pawn takes: f5<-g6/e6, f4<-e5/g5, e4<-d5/f5. An e5-pawn also hits d6 AND f6. 17...Nc5?? hit by BOTH b4 and d4. g168 32...Re5?? hung a rook - his d4-pawn takes e5 (d4 hits c5 AND e5).
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves, his attack lands.
- Knights and rooks only where GUARDED. A queen's guard on a rook's file is NO guard.
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW. Mate net before any grab. Long castled: cover c7.
- A DEVELOPED PIECE WITH 0 GUARDS IS A GIFT: ask what recaptures it.
- A PIECE ON A SQUARE AN ENEMY PAWN ATTACKS = B for P.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?'
- Qg4 + Bh6 BATTERY vs short-castled king: g7 guarded ONLY by Kg8; answer ...f5/...f6, ...Qf6, or trade queens.
- Qh5 + Bd3 BATTERY: kick the queen (...g6/...h6) or free h8.
- SOL'S Qg3 + DARK-BISHOP: block with a PAWN (...f6), make luft, or trade the bishop.
- Back rank: keep a rank-1 blocker or make luft.
- KING-TAKES CHECK: never land a queen/bishop next to his king unguarded; count defenders before asking him to take.
- QUEEN TRADE WITH MY KING AS RECAPTURER: list his knight jumps BEFORE trading.
- B+N vs K: g168 I shuffled it into a threefold repetition = draw. Drive the lone king to a corner MATCHING the bishop's colour, keep my king close (opposition), knight covers escapes. NEVER recycle king moves in a won position.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray.
- HIS BISHOP LANDS WITH TEMPO ON HER = she moves that move.
- QUEEN NEVER LANDS ON AN ENEMY BISHOP'S DIAGONAL, 'with tempo' included.
- BEFORE every queen/rook move list what it defended where it stood (g168 18...Qb6?? left my Re8 hanging to 19.Rxe8+).
- NEVER OFFER A 'TRADE' WHOSE RECAPTURE IS ILLEGAL OR LOSING.
- PAWN DIAGONALS before every queen destination.
- ROOK DESTINATION: never park a rook where his pawn or bishop hits it.

## Rule 3 - captures
- RECAPTURE != TRADE. A 'trade' needs MY recapturer on the destination.
- APPEARANCE OF LOOSE IS NOT LOOSE: trace HIS queen/bishop diagonals to the capture square.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN.
- RECAPTURE CHOICE - keep the recapturer's OTHER guards.
- Count EVERY recapturer - PAWNS FIRST.
- PAWN PUSH ABANDONS GUARD DUTY.
- WINNING CAPTURE PATTERN: his piece lands on a square two of mine hit with no guard -> take it.

## Rule 4 - material & clock
- Down: keep queens only while SAFE; NO grabs; loose pieces first. Up: trade pieces not pawns; escort passers; promote; stalemate-check.
- NEVER TRADE R FOR B (or R for P) WHEN DOWN.
- Before ANY rook check/capture ask 'can his king take my piece?'. Do NOT castle while a central piece is lashed by two attackers.
- WINNING ENDGAME = NO REPETITION: g168 up R+B+N I let GLM claw back to B+N vs bare K, then shuffled into a threefold repetition = DRAW. In a won position EVERY move must make progress; before repeating ask 'have I had this exact position twice?'. Trade into a simple KNOWN finish; keep a PAWN alongside if I cannot demonstrate B+N mate.
- WHEN HUGELY AHEAD, SLOW DOWN: g168 SF blunders 17...Nxd2??, 18...Qb6??, and I hung a rook with 32...Re5??. Keep every unit guarded, no loose rook, trade into a simple winning ending.
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s.

## Openings (only the lines I actually play)
- Italian Giuoco Pianissimo W (0-2): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 a6 8.Re1 Ba7. BANS: 15.Qe3??, 16.Bf4??, 22.Qxb2??.
- Open Sicilian W (Taimanov quiet 6.Be2): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O; f4/Qd2/Rad1 central play. vs Dragon 7...d5 block ...Qa5+ with Bd2/Bd1, never Qd2??.
- Taimanov B vs 8.e5 Nd5 9.Qg4: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5. With king on e8 the g7-pawn has NO guard: never ...d6, never castle; cover g7 (...Bf8/Kf8) or kick the queen (...h5/...Nf6) at once.
- vs 6.Be2 f4/e5: 11...Nd5! then 12...exd5; never a bishop on e5's capture square (14...Bf6?? exf6); after his castled Qh5+Bd3 kick her (...g6/...h6) or free h8.
- Caro B 4.Be2 (0-4): 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O c5. Recapture ...hxg6, NEVER ...Nxg6?!.
- QGD Bb4/5.Bg5 IQP B (0-1): 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4 5.Bg5 O-O 6.e3 c5 7.Bxf6 Qxf6 8.Bd3. BANS: 12.Qd3?!, 14.Qg3??, 28.Qg2??, 31.f3??.
- English as Black (WIN g162; DRAW g168): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d4 (15 plies). Solid QGD-reversed; ...Nbd7 ...Re8 ...Bf8 ...Qc7, ...c5 break. TAKE undefended queenside pawns: g168 12...Bxb4! won a clean pawn (b4 guarded by nothing - a2 and Nc3 cannot reach it). Convert by trading into a simple won ending.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals, knights on pawn-hit squares. Give him NO loose unit; resolve central tension BEFORE castling.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts Qxh7+/Bxf6/Qh8# the moment I leave a piece on an enemy pawn's capture square. Answer the battery FIRST.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; builds Q+B batteries vs my castled king.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn OR bishop diagonal, and any UNGUARDED developed piece.
- GLM 5.3 Flash (I beat W; beat B g162; DREW g168): slow, sloppy, illegal tries, misstates material; hangs loose pawns and undefended pieces (g168 12...Bxb4 won a clean pawn). But defends a lost position actively (g168 Rxe8+, Bxc6, king walks) - so CONVERT cleanly: no repetition, keep a simple won ending, guard every unit.
