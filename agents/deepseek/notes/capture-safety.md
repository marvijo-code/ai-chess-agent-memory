# Pre-move scan & blunder catalogue

## Every move
1. Legality: paths clear; two units = full name; after ONE rejection NEVER resend - redraw the board (g144 Qxg6 twice; g137 ...Rc8 illegal with king on c8).
2. His LAST move first, then MY destination: 0 guards + his capture = gift. Enemy pawns on the target: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7. ALSO walk every enemy BISHOP diagonal square by square to any QUEEN/ROOK destination: T37R5 17.Qg4?? sat on Be6's e6-f5-g4-h3 - 17...Bxg4 won my queen.
3. SCREENS: moving/trading my piece opens a line to my QUEEN or KING (g145 18.e4?? Nd5 screened Be6-b3 -> 18...Nf4!; g148 17...Bg5?? -> 19.Bxd8).
4. Pawn pushes end guard duty: g135 ...f6? (f7 left g6), g144 ...h6?? (h7 left g6), g147 ...f5??.
5. PAWN CAPTURES FIRST: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6, c5 hits b4/d4. 'Defended' never saves.
6. Knight retreats only where that knight cannot take AND his queen/rook do not own the square.
7. Captures: count ALL recapturers - PAWNS first, then behind the first defender; recapture != trade; my defender must land on the destination. RECAPTURE CHOICE: keep the recapturer's OTHER guards.
8. Rook files/bishop rays own whole lines; attacked+undefended -> save NOW. Before any rook CHECK ask 'can his king just take it?': T38R2 43...Rf5+?? Kxf5 lost my extra rook in a won game.
9. QUEEN hit -> she moves THAT move, OFF every attacker ray; 'defended' never counts.
10. Blocked guard = no guard; a push abandons guard duty.
11. Down: keep queens; loose pieces first; NO grab-back. Up: trade pieces, not pawns.
12. Count material FROM THE BOARD after every capture.
13. Clock: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s.
14. MATE FIRST, quiet moves too: back rank with no rank-1 blocker; king on f8 + his rook on the 7th = Rc8#. Nf4 + Qg-file vs my Kg1: Nf4 covers g2 so Qxg2# is real (Kxg2 illegal); a Qg4 block LOSES to ...Bxg4 (T37R5) - answer with Rf1/Qf1/Bf1 or remove Nf4.
15. SELF-BAN: a move my scan/note called bad is DEAD.

## T37R5 Italian W vs Sol (0-1, Qxg2# m19)
1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 O-O 6.O-O d6 7.Nbd2 a6 8.Re1 Ba7 (16 plies). Then 9.Bb3 Re8 10.h3 d5 11.exd5 Nxd5 12.c4? Nf4 13.Bc2?? Be6 14.Nxe5! Nxe5 15.Rxe5 Bd4 16.Re4 Qg5; 17.Qg4?? Bxg4 18.hxg4 Qxg4 19.Rxd4 Qxg2#.
- 17.Qg4??: I meant to block the g-file vs Qxg2#, but g4 sat on the e6-bishop's open diagonal - Q for B. The real answer was to GUARD g2 (Rf1/Qf1/Bf1) or remove Nf4, never put the queen on a bishop's diagonal.
- 12.c4?/13.Bc2??/14.Nxe5??: kicking the d5-knight with c4 let it land on f4, where it supported Qxg2# for the rest of the game. Prefer Ne4/Nf1-g3 and keep d3 guarded after the kick.
- 19.Rxd4 did win the loose Bd4 (his Qg5's rank was blocked by his own Nf4), but the mate had already landed.

## Key games
- T38R2 English B vs GLM (0-1 m60): ...c5 break, ...Qb6 vs d4/b2, ...Bc6; his 25.dxc6?? Qxd3 hung the queen (my Qa6 hit d3 through b5-c4). I converted R+B vs B cleanly - even trades, rooks on open files hitting his loose bishops, pawn harvest, a-passer, Q+B mate; no repetition. Near-miss: 43...Rf5+?? Kxf5.
- g148 Caro B: 17...Bg5?? screen to my Qd8 -> 19.Bxd8; 21...Rc7?? / 23...Nb7?? hung.
- g144 Caro B: 15...Bxf6? 16.Bxc5!; 19...h6?? 20.Bxg6; 24...Qxe5?? fxe5.
- g146 IQP W: 20.b3?? Bxa1; 26.Kf1 Re1#. g143 QGD: 23.Rd2?? Qe1#.
- g141 22.Rxc6?? R for P; g139 15...Nd7??; g135 9...f6?.

## Patterns
- Losses = one-move scan misses (screen / blocked guard / queen on a bishop's diagonal / piece on a pawn's capture square) + plan drift; openings are fine.
- A 'fork'/attack never excuses skipping the destination scan; the recapture choice is a move too.
- When he chains pawns/pieces, counter with a pawn break or piece activity NOW, not a passive retreat.
