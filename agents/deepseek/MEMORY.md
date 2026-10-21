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
- 3 rejected replies on ONE move = forfeit; empty = same. Walk MY OWN pieces' paths FIRST: piece, ACTUAL square, occupant, destination, path, off the board. T55R1 0 invalid in 37 moves; T55R3 2 invalid on queen moves (...Qb6, ...Qd6) - write the queen's path and destination attackers before sending; keep the square-by-square habit.
- Position turns: write the ONE-MOVE answer (recapture first, move the attacked piece), send within 15 s.
- SELF-BAN: a move my scan called bad is DEAD.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first, then MY destination: 0 guards + his capture = gift; two attackers is not safety. Quiet/retreat/tempo same sweep.
- HIS ATTACKING BISHOP WITH NO GUARD IS FREE (T54R1 11...Bc5?? Qxc5). Count the attacker's guards before retreating from it.
- A KNIGHT THAT LANDS HITTING A LOOSE PIECE IS ANSWERED FIRST; A PAWN KICK IS NOT AN ANSWER. T55 8...Ng4 (guarded by Bc8 through d7-e6-f5) hit my UNGUARDED Be3; 9.h3?? Nxe3 = B for N, and SF's +0.6 became +1.1, +2, then +6. Before any ...Ng4/...Nf5/...Nd4/...Nc4-class landing list the guards of EVERY piece it hits and move/defend that piece.
- A PINNED PAWN IS NOT A GUARD. T55 22.h4?? I wrote 'guarded by g3' - g3 was pinned by Be5 to my h2-king, so gxh4 was ILLEGAL and ...Qxh4+ won a pawn. Before pushing a pawn onto a square his queen/knight can take, verify each named guard against pins and screens on the NEW board.
- Screens: his own piece between his heavy piece and my destination is NO shield; MY guard is void if my own piece stands between. T45R4 20...Qc7?? only Bc5 blocked Qc2-c7; 21.Bxf8/22.Qxc7.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e5, c5<-b4/d4, a3/c3<-b4, e5<-d4/f4, f5<-e6/g6, g5<-f4/h4, d4<-c5/e5, h6<-g7, h4<-g5/g3. A moved pawn still attacks; its NEXT PUSH hits too (T52R3 25.Ra3?? bxa3; T53R1 13...Qxd4?? 14.c3).
- HIS QUEEN ON A PAWN'S CAPTURE SQUARE IS FREE (T53R3 ...Qe6?? dxe6). HIS UNGUARDED BISHOP ON AN OPEN LINE FALLS (T53R3 ...Bf5?? Rxf5).
- KNIGHT/BISHOP LANDINGS: walk his queen's and both bishops' diagonals and EVERY knight jump; a central jump needs EVERY recapturer. A FORK IS ONLY A FORK IF THE LANDING IS SAFE AND ITS TARGETS CANNOT STEP WITH TEMPO (T53R3 15.Nd5?? Nf6).
- HIS KNIGHT ON A SQUARE WHOSE RECAPTURE HIS OWN PAWN BLOCKS IS FREE: T53R2 Bxd5.
- WHITE'S e5 PAWN OWNS d6 AND f6 - no-go for every piece, QUEEN included; a knight on d5 covers e3/f4/c3/b4/b6/c7/e7/f6 (T53S2G1 27.Qf4?? Nxf4).
- Rooks and knights only where GUARDED; before a rook CAPTURE walk pawn recaptures; before a ROOK CHECK ask can his king take. The recapturer must ACTUALLY REACH it - MY OWN PIECE OFTEN SCREENS THE PATH.
- THE MOVING UNIT ABANDONS ITS GUARD: name it. AN ATTACKED PIECE NEEDS AN ANSWER BEFORE ANY QUIET MOVE ELSEWHERE (T55: e3 lost that way).
- TRADING A ROOK OFF MY KING's rank-2 square: name g2/h2's guards on the NEW board (T51R4 27...Qxg2#). PAWN HITS TWO PIECES: move the MORE valuable and count the recapture.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask what mates if I pass. BLOCKING A MATE STILL OBEYS THE SWEEP. King on g1/g2 + his Qd5/f5 + Bb7 = ...Qxg2 mate unless a rook stands f2 or h3 is luft - play the luft EARLY.
- TWO ROOKS GUARDING EACH OTHER on f2+f3 (king shuttling g2/h2/f1) stop ...Qh2+/...Qg2+ nets: T55 held ~15 moves that way down a rook. The safety was the rooks' mutual guard, not the king.
- g3 WITH MY KING ON g2/h2 AND HIS BISHOP ABLE TO REACH e5: g3 is PINNED (e5-h2) = a hook for ...h5-h4 and ...Qh4+. T55 19.g3?! let ...Be5/...Qg5/...h5-h4 roll and 22.h4?? lost the pawn. Play g3 only when the h-push is answerable.
- Qg4+Bh6 vs short-castled king (g7 guarded only by the king): answer ...f5/...f6, ...Qf6, or trade queens. With my e8-king the Qxg7 net needs a PIECE on g7. MY SHORT-CASTLED g8-KING behind g6+g7: his Qf6+Bh6 = Qg7#. MY e8-KING + Bf8 covering g7: keep f8 guarded too (T51R1 15.Nd6+).
- Back rank: keep a rank-1 blocker or luft. A rook that is the LAST guard of an entry square must not leave for a pawn.
- KING-TAKES: an unguarded piece beside his king (KNIGHT included) is a king capture. Before ANY check write what captures the checker, KING included. QUEEN CHECKS: list EVERY block.
- KING-HUNT WITH R+B: ...Rh3+ with my Bf5/e6 guarding h3 boxes Kg5; ...Be6, then ...f6#/...h6#. Do not take h5 with the rook (T55R3).
- WON POSITION: prefer the forcing check over a slow lift (T53R2 28.Rf3+ Rf7 29.Qxf7#).
- Q+B vs bare king: Qc1+ Ke2 Qd2+ Kf1 Qd1#; T54R1 Bf5#. Q vs lone K: box with the queen a knight's move away, walk my king up, leave him a legal square - no stalemate.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray. A BISHOP LANDING WITH TEMPO ON HER = she moves.
- QUEEN NEVER on an enemy bishop's diagonal or knight jump square, tempo included (T53R2 ...Qe6?? Bxe6; 27.Qf4?? Nxf4; T53R5 10.Qc2?? Ncb4/Nxc2).
- BEFORE every queen move list what she defended where she stood AND every enemy knight/pawn hitting the destination. A BLOCKED GUARD IS NOT A GUARD. Count HIS recapture on a pawn push.
- BEFORE A QUEEN MOVE WRITE THE ATTACKER'S ACTUAL SQUARE: T55R3 28...Qc3?? I wrote 'the c3-rook' but his rook stood on c7 and took her along the empty c-file. A queen on his rook's file/rank is lost unless one of MY pieces blocks it; name that blocker from the board.
- NEVER a queen on a PAWN's capture square, or where a pawn push hits her next move. DOWN = NO grabs; defend WITHOUT her.
- HIS QUEEN IN MY CAMP: list every unguarded piece she reaches next move. A queen hit by a rook must leave BOTH the file AND the rank.
- QUEEN BEHIND A SCREEN ON AN OPEN FILE IS LOST when the screen is pinned: T54R2 14.Qd3?? ...e5! + Rxd3. Move her OFF the file, or move the screen only after she leaves.
- Queen + rook/king on one line = skewer: separate them BEFORE the quiet move (T42R5 32.Kh2?? Bh6!).

## Rule 3 - captures & trade offers
- RECAPTURE != TRADE: my recapturer must reach the destination in ONE move and stay guarded after landing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE PIECE. Count EVERY recapturer, PAWNS FIRST; trace the chain to the end.
- AN UNDEFENDED PIECE IS NOT FREE IF HIS ANSWER COMES WITH TEMPO. NEVER TRADE R FOR B OR P: T54R1 56.Rxf7? Kxf7.
- A ROOK THAT GRABS IN HIS CAMP MUST BE DEFENDED: T53S2G1 26.Rxa6?? Qxa6; T54R5 32...Rxa3 had a recapture but his a-pawn then ran.
- AFTER A CAPTURE THAT WINS A PIECE, RESCAN FOR MY OWN LOOSE UNIT; after ANY trade re-count guards of ALL my units (T50R4 14...Bxe5??).
- QUEEN TRADE WHEN AHEAD: take his queen if she lands on my queen's ray/square (T51R5 18...Qxc5).
- UP THE EXCHANGE WITH QUEENS ON: no pawn-grabs with a rook, keep both rooks guarded, trade rooks on my own terms, then bank.

## Rule 4 - material, conversion, clock
- MATERIAL FROM THE BOARD, EVERY MOVE (count pieces, never prose); rescan after every trade. NO GRABS WHEN LEVEL OR BEHIND. KEEP THE WON QUEEN off his rook's rank/file and off pawn capture squares all the way to mate.
- LEVEL MATERIAL WITH A BROKEN KING IS LOST vs SF: T55 was level again after 26.Bxb5 and still +5 - h-pawns gone, g3 pinned, king on g2. The piece count is not the evaluation; count my king's guards and my pinned pawns too.
- CONVERTING UP: guard every unit, trade pieces not pawns, escort passers, stalemate-check, 5-15 s a move. Models: T54R1 (queen traded, Bxd8, d6 passer, rook trade, promotion, Bf5#); T53R3 (trade his last rook WITH CHECK, then mate).
- BIG LEAD = SIMPLIFY FAST: trade queens/rooks when safe, keep every unit guarded, 5-10 s a move.
- UP A PIECE, DO NOT PAWN-BOX HIS QUEEN: T54S2G1 15.c3/17.a3 were pokes at a tied-down queen while Rfd1/f5/Bd4 waited.
- DOWN A PIECE VS SF IS LOST: no pawn-grabbing with the queen, guard every unit, hunt ONE freeing trade (T54R5).
- CLOCK - 3600+10: cap 30 s, routine 10-15 s, <15 min left -> 5-10 s. T54R3 LOST ON TIME. T55R1: ~20 min on quiet moves in a +2 position and 9.h3 was the blunder. T55R3: 4:02 on ...Qd6 (2 invalid), 6:49 on ...Qe7, 6:27 on ...exf3, 2:05 on ...Qc3??. The miss is in the guard scan, not the long think.

## Openings (only the lines I actually play)
- English as Black (WINS T38R2, T41R4, T45R4, T50R4, T51R5, T52R5, T53R5, T55R3; LOSS T54R3): 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.g3 Be7 6.Bg2 O-O 7.O-O c6 8.d3 (16 plies); then ...Bf5, ...Nbd7, ...Re8, ...Qb6; ...c5 only when d5 is guarded. vs d4/e3/Bf4 (T55R3 WIN): same ...c6/...Bf5/...Nbd7/...Re8; ...Qb6?! gives Na4 tempo (use ...Qc7/...Qd6); ...c5 once his Bg2 is blocked. T54R3: ...a5/...a4 with White b3 is a gift (23.bxa4); wait for ...b5/...Nb4.
- Ruy Lopez Closed (Chigorin, both colours): 1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O (16 plies); then ...Na5 with Bc2, ...c5 and d4/Nbd2. As Black move the queen OFF c7 BEFORE d5; ...Nc4 only when Bb3 cannot come with tempo; Qc7 'defended' by Rc8 is still Rxc7. As White keep Rc1; no piece on a square his g6-pawn covers (f5/h5).
- Four Knights Spanish as Black: ...Bb4 and castle, ...Nd5 then exd5, ...Nd4 with tempo. T54R5 v SF19 LOSS: after 11.a3 kicked the b4-bishop, 11...Bxc3?? grabbed the knight; 12.dxc3 left White the bishop pair and centre and my c3-pawn fell to Bc1 - eval +5 by move 12. RETREAT (...Bf8/...Be7) and keep the pin; take Nc3 only for concrete material. BANS: 13...Qxd4?? 14.c3, ...Qf6 while his queen takes f6, ...Re8?? (Rxe8+).
- Italian Giuoco Pianissimo W: 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 d6 6.O-O O-O 7.Nbd2 Be6 8.Bb3 h6 (16 plies); then ...Qd7, ...Rfe8 and ...d5. If ...Bg4 comes, meet it with Re1 and h3. T53R2 WIN: Bxd5 won a knight; his ...Nxd4 allowed cxd4 and his ...Qe6 hung the bishop to Bxe6; Rf3+ finished. BANS: 10.d4?!, 12.c4?, 13.Bc2??, 14.Bg5??, 15.Nxe5??, b4 WHILE MY KNIGHT IS ON b3, queen on d5 while his f6-knight lives.
- Open Sicilian Taimanov W 6.Be2: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); then f4, Qd2, Rad1, Kh1. 9.f4 b5 10.e5! is best; after ...Nd5 take it and recapture on d5 with the queen. T54S2G1 WIN v GLM: ...b4/...Qa5 met Qb3/Na4; his Bg5 landed on my f4-pawn's square, 19.fxg5. T54R1 WIN v mirror: 11...Bc5?? met 12.Qxc5. T53R3 WIN: ...Bf5 fell to Rxf5 and ...Qe6 to dxe6. BANS: 12.Qd2?? after ...Bc5, 15.Nd5?? (Nf6 recaptures), 26.Rxa6??, 27.Qf4?? Nxf4; when up the exchange use Rc6-c4, Rd4 and Re1.
- Open Sicilian vs ...Nc6/...g6 with Bc3/Bc4 (T55 L v SF19): 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.O-O (7 plies), then f3/Qd2 or Qd2/Rf2 plan. THE OPENING WAS FINE (+0.3 for White after 8.O-O); the loss was 9.h3?? letting ...Nxe3. If ...Ng4 comes: defend/move e3 FIRST (Qd2, Bd4, or accept the trade only with a recapture), kick with h3 ONLY once e3 is guarded twice. Later ...Be5 pins g3 - see Rule 1b.
- Taimanov B: 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies); 9.Qg4. With my king on e8 g7 has NO guard - never ...d6, never castle, never ...Nf6; cover g7 with a PIECE (...Bf8); never ...f5 while exf6 opens lines. T50R3: 11...g6?? 15.Qf6 won h8, 17.Bh6 Qxf8#. T51R1: 14...Qe7?? screened Bf8 from d6 - 15.Nd6+!. T49R4: ...a6 BEFORE White's Nb5.
- Caro B: ...Bf5 and ...e6, knights d7 then e7-f5, ...Bg6; recapture ...hxg6, never ...Nxg6?!; ...Be4 loses to Nxe4; vs 12.f4/13.g4! move Bf5 first (T52R2 13...cxd4?! 14.Nxd5!).

## Opponents
- SF19: instant. Punishes loose units, passive retreats, queens on his rays/pawn diagonals/knight squares, and voluntarily given pieces. Give him NO loose unit; resolve central tension before castling. 10-15 s. T54R2: up Q+R v B it still took a threefold when its rook was attacked every move; keep hitting the loose unit. T54R5: he converted a piece lead with no gifts. T55: 8...Ng4 took my unguarded Be3 after 9.h3??, then ...Be5/...Qg5/...h5-h4 punished a pinned g3 and he mated in 37 with zero errors; from +0.6 to mate on ONE loose piece. He does not repeat when he can progress, and he never blocks his own attack.
- Fable 5.1: solid 6.Be2 + Qh5/Bd3 battery vs my castled king; converts the moment I leave a piece on an enemy pawn's capture square.
- Sonnet 5.5 (never beaten): banks clock, quiet space moves, then takes every UNGUARDED unit. 10-15 s from move 1, assume 60+ moves, keep a rank-1 blocker.
- GPT-6.1 Sol: fast; takes every free piece incl. a queen on any pawn/bishop diagonal or knight square, and any loose recapture.
- GPT-6 Astra: Open Sicilian 6.Be2 + f4/Qe1-g3, and the Chigorin; gives nothing loose.
- GLM 5.3 Flash (my wins T51R5, T52R1, T52R5, T53R2, T53R5, T54S2G1; T54R3 L on time): slow, miscounts material, hangs queens/rooks/knights when worse or even, but punishes MY loose knight jumps and won T54R3 on my clock. It goes passive and drops pieces on my pawns' capture squares (18...Bg5?? f4xg5). Vs it: 10-15 s, guard every unit, take every loose unit/queen, never an empty or illegal reply.
- Haiku 5.5: fast, solid Italian Pianissimo, no free material; I forfeited T44R3 and lost T45R3 on the clock. 10-15 s a move, bank time, check legality twice.
- DeepSeek V4.1 Flash 1017 (mirror): Taimanov both ways; keeps units guarded but leaves an 'active' piece loose and can put a piece on my queen/pawn's capture square (T54R1 11...Bc5?? Qxc5). I won T50R2, T51R3, T51S2G1, T53R3, T54R1, T55R3; lost T51R4, T52R3, T52S2A, T53S2G1. T55R3: he hung Qd4?? cxd4, Bc6?? bxc6, Rc2?? Bxc2; I hung my queen 28...Qc3?? to Rc7xc3. Against him: take every loose unit, convert with guarded rooks, no grabs, no 5-9 minute thinks; win on legality, guard counts, active conversion.
