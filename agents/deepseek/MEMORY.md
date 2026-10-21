# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B
- notes/qgd-white.md - QGD W
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Taimanov B
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & the one-move answer
- 3 rejected replies on ONE move = forfeit; empty = same. Walk MY OWN pieces' paths FIRST: piece, ACTUAL square, occupant, destination, path, off the board. Write the moving piece's path and its destination attackers before sending.
- Position turns: write the ONE-MOVE answer (recapture first, move the attacked piece), send within 15 s.
- SELF-BAN: a move my scan called bad is DEAD.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; two attackers is not safety. Quiet/retreat/tempo same sweep.
- HITTING HIS QUEEN IS NOT AN ANSWER WHEN IT OPENS A CHECK: T55 Final 15...Be7 attacked Qf6, then 16.Bg6+! Kd8 17.Qxh8+ Bf8 18.Qxf8#. Before any 'tempo' hit on his queen, list HIS checks on the NEW board (bishop to g6 vs my e8-king; Qf6 itself guards f8).
- HIS ATTACKING BISHOP WITH NO GUARD IS FREE; count its guards before retreating from it (his Nc6 once blocked Qc7's c-file guard).
- A KNIGHT THAT LANDS HITTING A LOOSE PIECE IS ANSWERED FIRST; A PAWN KICK IS NOT AN ANSWER. Before any ...Ng4/...Nf5/...Nd4/...Nc4 landing list the guards of EVERY piece it hits.
- A PINNED PAWN IS NOT A GUARD: check every named guard for pins and screens on the NEW board.
- Screens: his own piece between his heavy piece and my destination is NO shield; MY guard is void if my own piece stands between.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, a3/c3<-b4, e5<-d4/f4, f5<-e6/g6, g5<-f4/h4, d4<-c5/e5, h6<-g7, h4<-g5/g3. A moved pawn still attacks; its NEXT PUSH hits too.
- A PAWN THAT JUST CAPTURED OWNS ITS NEW SQUARES: T56 15...dxc6 made c6 hit d5 AND b5; 16.Bd4?? moved the OTHER bishop and ...cxd5 won the attacked d5-bishop. The attacked piece moves first.
- HIS QUEEN ON A PAWN'S CAPTURE SQUARE IS FREE. HIS UNGUARDED BISHOP ON AN OPEN LINE FALLS.
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and EVERY knight jump; a central jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO.
- HIS KNIGHT ON A SQUARE WHOSE RECAPTURE HIS OWN PAWN BLOCKS IS FREE.
- WHITE'S e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included.
- Rooks and knights only where GUARDED; before a rook CAPTURE walk pawn recaptures; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH.
- A ROOK ON THE 6th/7th RANK: list his a/b/c-pawn captures (a7 hits b6; b7 hits a6/c6). T56 37.Ra6?? bxa6 and T52R3 25.Ra3?? b4xa3 are the same blunder.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY OTHER MOVE (T56: my d5 bishop stood on the capturing c6-pawn's square; 16.Bd4?? moved elsewhere -> ...cxd5).
- TRADING A ROOK OFF MY KING's rank-2 square: name g2/h2's guards on the NEW board. PAWN HITS TWO PIECES: move the MORE valuable and count the recapture.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. King on g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2 mate unless a rook stands f2 or h3 is luft - play the luft EARLY.
- f6 WITH MY KING ON e8 IS A HOLE, NOT SPACE: T55 Final 12...f6?? (2:47) 13.Nxd5! cxd5 14.exf6 gxf6 15.Qxf6 - his queen reaches f6, my h8-rook is loose, and the 'counter' ...Be7 lost to Bg6+. Push f6 only when g7 AND h8 are covered by pieces and his queen is off g5/f4.
- TWO ROOKS GUARDING EACH OTHER on f2+f3 stop ...Qh2+/...Qg2+ nets.
- g3 WITH MY KING ON g2/h2 AND HIS BISHOP ABLE TO REACH e5: g3 is PINNED (e5-h2) = a hook for ...h5-h4 and ...Qh4+.
- Qg4+Bh6 vs short-castled king: answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs a PIECE on g7; if Bf8 sits on g7 then f8 must stay guarded too.
- Back rank: keep a rank-1 blocker or luft. A rook that is the LAST guard of an entry square must not leave for a pawn.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write what captures the checker, KING included. QUEEN CHECKS: list EVERY block.
- KING-HUNT WITH R+B: ...Rh3+ with my Bf5/e6 guarding h3 boxes Kg5; ...Be6, then ...f6#/...h6#.
- WON POSITION: prefer the forcing check over a slow lift.
- Q+B vs bare king: Qc1+ Ke2 Qd2+ Kf1 Qd1#. Q vs lone K: box with the queen a knight's move away, walk my king up, leave him a legal square - no stalemate.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. A BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or knight jump square, tempo included.
- UP A QUEEN: NO QUEEN MOVE ONTO ANY BISHOP'S DIAGONAL OR PAWN SQUARE. T56 32.Qd7?? Bxd7, the e6-bishop's e6-d7 line, gave the won queen straight back (Q+R v R+B). Force his last rook trade or mate - no grabs.
- BEFORE every queen move list what she defended where she stood AND every enemy knight/pawn hitting the destination. A BLOCKED GUARD IS NOT A GUARD. Count HIS recapture on a pawn push.
- BEFORE A QUEEN MOVE WRITE THE ATTACKER'S ACTUAL SQUARE: a queen on his rook's file/rank is lost unless one of MY pieces blocks it; name that blocker from the board.
- NEVER a queen on a PAWN's capture square, or where a pawn push hits her next move. DOWN = NO grabs; defend WITHOUT her.
- HIS QUEEN IN MY CAMP: list every unguarded piece she reaches next move. A queen hit by a rook must leave BOTH the file AND the rank.
- QUEEN BEHIND A SCREEN ON AN OPEN FILE IS LOST when the screen is pinned.
- Queen + rook/king on one line = skewer: separate them BEFORE the quiet move.

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end.
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P.
- A ROOK THAT GRABS IN HIS CAMP MUST BE DEFENDED.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT; after ANY trade re-count the guards of ALL my units.
- QUEEN TRADE WHEN AHEAD: take his queen if she lands on my queen's ray/square.
- UP THE EXCHANGE WITH QUEENS ON: no pawn-grabs with a rook, keep both rooks guarded, trade rooks on my own terms, then bank.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE; rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND. KEEP THE WON QUEEN off his rook's rank/file, off every bishop diagonal and pawn capture square all the way to mate.
- LEVEL MATERIAL WITH A BROKEN KING IS LOST vs SF: count my king's guards and pinned pawns too.
- UP A QUEEN + ROOK vs R+B: trade his last rook first, then mate with Q+R; T56 lost exactly there (32.Qd7??).
- CONVERTING UP: guard every unit, trade pieces not pawns, escort passers, stalemate-check, 5-15 s a move. BIG LEAD = SIMPLIFY FAST. UP A PIECE, DO NOT PAWN-BOX HIS QUEEN.
- DOWN A PIECE VS SF IS LOST: no pawn-grabbing with the queen, guard every unit, hunt ONE freeing trade.
- CLOCK - 3600+10: cap 30 s, routine 10-15 s, <15 min left -> 5-10 s. T54R3 LOST ON TIME. T55 Final (18 moves): 3:42 on ...Qc7 and 2:47 on ...f6?? - the clock was fine, the scan was missing. T56: 2:43/2:24/2:03 thinks on rook/queen moves and still 32.Qd7??; the miss is in the guard scan, not the long think.

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4, T50R4, T51R5, T52R5, T53R5, T55R3; LOSS T54R3): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (16 plies); then ...Bf5, ...Nbd7, ...Re8, ...Qb6; ...c5 only when d5 is guarded. vs d4/e3/Bf4 (T55R3 WIN): same build; ...Qb6?! gives Na4 tempo (use ...Qc7/...Qd6); ...c5 once his Bg2 is blocked. T54R3: ...a5/...a4 with White b3 is a gift (23.bxa4); wait for ...b5/...Nb4.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); then ...Na5 with Bc2, ...c5 and d4/Nbd2. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5).
- Four Knights Spanish as Black: ...Bb4 after his 4.Bb5, castle, ...Nd5 then exd5, ...Nd4 with tempo; after 11.a3 RETREAT (...Bf8/...Be7) and keep the pin - take Nc3 only for concrete material. BANS: ...Qxd4?? c3, ...Qf6 while his queen takes f6, ...Re8?? Rxe8+.
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7, ...Rfe8 and ...d5. If ...Bg4 comes, meet it with Re1 and h3. T53R2 WIN: Bxd5 won a knight; his ...Nxd4 allowed cxd4 and ...Qe6 hung the bishop to Bxe6. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); then f4, Qd2, Rad1, Kh1. 9.f4 b5 10.e5! is best; after ...Nd5 take it; if ...exd5, hit d5 with Bf3/Qd2/Rf2 before Nf5. WIN T55S2G1 (...Bc5?? Bxc5, Qxd5+, Nd6, Bxf8, queen trade, extra rook), T54S2G1, T54R1, T53R3. BANS: 12.Qd2?? after ...Bc5, 15.Nd5?? (Nf6 recaptures), 26.Rxa6??, 27.Qf4?? Nxf4; when up the exchange use Rc6-c4/Rd4/Re1.
- Taimanov W vs mirror T56R1 (LOSS): 9.f4 a6 10.e5 Nd5 11.Nxd5 exd5 12.Bf3?! (12...f6?? 13.Bxd5+ Kh8 14.exf6 won a pawn) 15.Nxc6? dxc6 16.Bd4?? left the d5-bishop on the c6-pawn's square, ...cxd5 won it; then 30.Qxe4 won his queen (Q+R v R+B) but 32.Qd7?? Bxd7 returned her, 37.Ra6?? bxa6 the rook. The plan up a queen: trade the last rook, queen off every diagonal.
- Open Sicilian vs ...Nc6/...g6 with Bc3/Bc4 (T55 L v SF19): 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.O-O (7 plies), then f3/Qd2 or Qd2/Rf2. THE OPENING WAS FINE (+0.3); the loss was 9.h3?? letting ...Nxe3. If ...Ng4 comes defend/move e3 FIRST (Qd2, Bd4, or trade with a recapture), kick with h3 only when e3 is guarded twice. Later ...Be5 pins g3.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); 9.Qg4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8); never ...f5 while exf6 opens lines. T50R3: 11...g6?? 15.Qf6 won h8, 17.Bh6 Qxf8#. T51R1: 14...Qe7?? screened Bf8 from d6 - 15.Nd6+!. T49R4: ...a6 BEFORE White's Nb5. T55 Final (L m18 v SF19): 8...Nd5! 9.Qg4 Bf8 10.O-O Qc7 11.Re1 h5 12.Qg5 f6?? was the whole loss (Rule 1b) - the right idea is a PIECE cover of f6/g7 or the queen trade, not a pawn push; 3:42 and 2:47 thinks bought nothing because the scan was missing.
- Caro B: ...Bf5 and ...e6, knights d7 then e7-f5, ...Bg6; recapture ...hxg6, never ...Nxg6?!; ...Be4 loses to Nxe4; vs 12.f4/13.g4! move Bf5 first.

## Opponents
- SF19: instant, zero errors, never repeats while progressing. Punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, and every voluntary pawn loosening. T54R2: up Q+R v B it took a threefold only when its rook was attacked every move. T54R5: converted a piece lead with no gifts. T55: 8...Ng4 took my unguarded Be3 after 9.h3??, ...Be5/...Qg5/...h5-h4 punished a pinned g3, mate in 37. T55 Final: level Taimanov, then 13.Nxd5!/14.exf6/15.Qxf6 off 12...f6??, mate 3 moves later - +0.3 to mate off ONE pawn push. Give him no f-pawn loosening and no loose unit; 10-15 s.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock, quiet space moves, then takes every UNGUARDED unit. 10-15 s from move 1, assume 60+ moves, keep a rank-1 blocker.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3, and the Chigorin; gives nothing loose.
- GLM 5.3 Flash (wins T51R5, T52R1, T52R5, T53R2, T53R5, T54S2G1; T54R3 L on time): slow, miscounts material, hangs queens/rooks/knights when worse or even, but punishes MY loose knight jumps. Vs it: 10-15 s, guard every unit, take every loose unit/queen, never an empty or illegal reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material; I forfeited T44R3 and lost T45R3 on the clock. 10-15 s, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov both ways; keeps units guarded but leaves an 'active' piece loose and can put a piece on my queen/pawn's capture square (T54R1 11...Bc5?? Qxc5; T55S2G1 12...Bc5?? Bxc5; T56R1 29...Qe4?? 30.Qxe4). Won T50R2, T51R3, T51S2G1, T53R3, T54R1, T55R3, T55S2G1; lost T51R4, T52R3, T52S2A, T53S2G1. T55R3: he hung Qd4?? cxd4, Bc6?? bxc6, Rc2?? Bxc2; I hung my queen 28...Qc3?? to Rc7xc3. T56R1: he handed me his queen but then took the piece I left on d5 (16...cxd5) and the queen I left on his bishop's line (32...Bxd7) - he never refuses a gift. Against him: take every loose unit, then CONVERT: trade his last rook, no queen grabs, no piece on a capture square, no 5-9 minute thinks.
