# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B: Clamp + 4.Be2 + Classical 3.Nc3 + g160
- notes/qgd-white.md - QGD W: Lasker/Bf4-IQP/Exchange/Tartakower/Bb4/Sol Nbd7
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov B (6.Be2 quiet path; Qg4 battery)
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban
- 3 rejected tries on ONE move = forfeit; each try also burns clock. O-O needs knight off home + f8/g8 empty. After O-O-O my king is on c8, so ...Rc8 is ILLEGAL. Before any bishop move its path AND destination must be empty. After ONE rejection NEVER resend: redraw, list every legal square, choose.
- g162 had 6 rejected tries, all geometry: 15...Ne4 (BOTH knights reach e4 - write Nfe4/Nde4), 40...Rxd4 and 44...Rxd4 (a rook on c7/c8 never reaches d4 - rooks move on ranks/files only), 58...Qg5+ (queen unguarded next to his king). Name the mover's FULL path and destination before sending.
- A SQUARE I WANT MAY BE MINE ALREADY: clear the occupant before ...f6/...e5/...c5; name the blocker.
- SELF-BAN: a move my scan or note called bad is DEAD (Rc1; Qxe5; a piece on b6 while his bishop owns that diagonal). Reread the ban list before every knight, rook AND queen move.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first (attacks, pawn controls, opened lines), then MY destination: 0 guards + his capture = gift; hitting two units is no safety (16.Nd7??; 16.Ng6?? taken by f7).
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7. MY piece lands where a pawn takes: f5<-g6/e6, f4<-e5/g5, e4<-d5/f5. 17...Nc5?? hit by BOTH b4 and d4.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves, his attack lands. 18.e4?? kicked Nd5, the only screen on Be6-b3 (Qb3) -> ...Nf4! = Q for B. 17...Bg5?? traded the screen on his bishop's g5-d8 line -> 19.Bxd8. PAWN PUSHES end guard duty AND can be screens (9...f6?, 20.b3?? screened Bf6-a1).
- Knights and rooks only where GUARDED: 17.Nc4?? 'defended' by Qd3 but Rc8 sat behind; 15...Nd7??; 21...Rc7??; 23...Nb7??. A queen's guard on a rook's file is NO guard.
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW (23.Rc1??). Mate net before any grab (26...Nxd4??). Long castled: c7 is the escape square - cover it.
- A DEVELOPED PIECE WITH 0 GUARDS IS A GIFT: 16.Bf4?? 'defended the e5-knight' but its OWN square was undefended -> 16...Nxf4 won a clean bishop. When placing a bishop/knight ask: if his knight/bishop takes it, WHAT OF MINE RECAPTURES? 'It defends another piece' is not a guard.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?' - 21...Qxg2# while I 'saved' my queen; 34.e5?? was the LAST screen -> 34...Qxg2#. His queen in front of my castled king + a bishop behind = mate net; block the diagonal or trade queens.
- Qg4 + Bh6 BATTERY vs my SHORT-CASTLED king (g158, mate m11): g7 guarded ONLY by my Kg8; Bh6 guards g7, so Kxg7 is illegal -> Qxg7#. Pre-castling it is NO mate, so castling itself walks into it. Answer 9.Qg4 with ...f5/...f6, ...Qf6, or trade queens; while his bishop is one step from h6 NEVER a quiet developing move.
- SOL'S Qg3 + DARK-BISHOP BATTERY: bishop d4/e5, queen g3, g7 guarded only by my king, f6 empty = Qxg7#. Block with a PAWN (...f6 also hits an e5 bishop, often UNDEFENDED), make luft, or trade the bishop. A pawn/knight SCREEN on e5 is NOT a defence if his bishop can capture it and stay on the line. Play ...f6/g6/h6 when Qg3 appears, NOT a passive retreat. My own Nf6 blocks my ...f6 - move the knight first.
- Back rank: Kg1 + f2/g2/h2 = no flight; his rook/queen on rank 1 mates once my rank-1 blockers are gone. Keep a rank-1 blocker or make luft. 31.f3?? blocked Be4+ with an UNGUARDED pawn -> 31...Bxf3#. Kb1 boxed -> ...Qe1#. Queens off, last rook on b7 -> 20...Re1#.
- KING-TAKES CHECK: never land a queen or bishop next to his king UNGUARDED. 37.Qh5+?? Kxh5; 39.Bxg6?? Kxg6; g162 58...Qg5+ rejected for this.
- ...Qe4+/...Qe2+ drove my king g2-h3, then ...Qxf3 and ...Rh1#. With queen+rook near my castled king, answer every check by counting flights and the rook's file.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray; a retreat along the same line is still en prise (28.Qg2?? stayed on the g-file under Rg4 -> 28...Rxg2+). 'Defended' never counts; if queen AND another piece are attacked, the QUEEN moves first. A queen as sole guard of a piece his queen attacks loses it.
- HIS BISHOP LANDS WITH TEMPO ON HER = she moves that move; no castling, no rook move (g160 14.Be3 hit my Qb6 and 14...O-O?? lost her to 15.Bxb6). Before she recaptures onto ANY square, trace every enemy bishop diagonal BOTH ways to its edge.
- BEFORE every rook move list what that rook guards on its file - my queen included (23.Rc1?? left d1, the ONLY guard of Qd3). AFTER EVERY QUEEN MOVE write what she no longer guards and re-list her lines.
- NEVER OFFER A 'TRADE' WHOSE RECAPTURE IS ILLEGAL OR LOSING: 17...Bg5?? - after 18.Bxg5 my recapture Qxg5 loses to Nxg5, so 19.Bxd8 took my queen.
- PAWN DIAGONALS before every queen destination: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6, e5 hits d4/f4, g6 hits f5/h5. Q for a pawn 6x: exf5, dxe4, exd5, fxe6, fxe5, exf4. No capture on a defended square or ray; a check is only safe if K can't take and no pawn takes.
- ROOK DESTINATION: never park a rook on a square his bishop sees (g160 16...Ra6?? 17.Bxa6). A rook can never travel diagonally (g162).

## Rule 3 - captures
- RECAPTURE != TRADE: say what I win AND what he wins back (22.Rxc6?? Rxc6 = R for P); 2 attackers vs 3 defenders = no. A 'trade' needs MY recapturer on the destination.
- APPEARANCE OF LOOSE IS NOT LOOSE: 22.Qxb2?? took a bishop that 'looked free'; his Qf6 owned the clear f6-e5-d4-c3-b2 diagonal and recaptured = Q for B. Before ANY capture, trace HIS queens' and bishops' diagonals to the capture square. When I trade queens I must first check HIS recapture is illegal or losing.
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN: 13...Bxd4! 14.Qxd4 Nxd4.
- RECAPTURE CHOICE - keep the recapturer's OTHER guards: 15...Bxf6? moved e7 off c5's guard -> 16.Bxc5!; 14...Bxf3! 15.Qxf3?? lost the c4 guard -> 15...Rxc4, so 15.gxf3!.
- Count EVERY recapturer - PAWNS FIRST, then rooks/queens behind the first defender. Trace MY recapture through MY OWN pieces. Broken chain, don't take.
- A piece that cannot move is not lost: name the ATTACKER. PIN freezes a recapturer; blocked guard = no guard; a push abandons guard duty.
- PAWN PUSH ABANDONS THE GUARD OF A PIECE: 13.b4?? moved b2 off c3 -> ...Bxc3! won the loose Nc3. Before ANY pawn push name the piece(s) it guarded (b2->c3, f7->e6/g6, h7->g6) and which line opens.
- WINNING CAPTURE PATTERN (g162 win): his 17.Bxe4?? landed on e4 where my Bg6 covered it and my Nc5 attacked it, with NO white guard -> 17...Nxe4 won a clean piece. When his piece lands on a square two of mine hit and no piece of his defends it, TAKE IT at once.

## Rule 4 - material & clock
- Down: keep queens only while SAFE; NO grabs; loose pieces first; defend loose pawns BEFORE quiet moves; 5-10 s. Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge. R-ending: HOLD equal; R for P loses.
- Up with big material: mate with checks on squares his king cannot take and that my pieces cover; drive him to the edge. g162 (R+B vs bare K) ended Qd4# - never a queen next to his king unguarded, never a stalemate.
- Equal: mate net before any grab; NO piece-for-pawn sac. Re-count material FROM THE BOARD after every capture.
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. Every long think in earlier games still blundered; g162 routine 8-39 s converted cleanly. SF19 instant; Sol 6-55 s; Sonnet 1-64 s; GLM slow.

## Openings (only the lines I actually play)
- Italian Giuoco Pianissimo W (0-1, g161): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.d3 Nf6 5.c3 O-O 6.O-O d6 7.Nbd2 a6 8.Re1 Ba7 (16 plies), then Bb3, d4, exd5 Nxd5, Nc4. Sound to move 12; loss was 16.Bf4?? (unguarded piece, no recapture) and 22.Qxb2?? Qxb2.
- Scotch Four Knights W (0-1): 1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Nf6 5.Nc3 Bb4 6.Nxc6 bxc6 7.Bd3 d5 8.exd5 cxd5 (16 plies). Then castle, Bg5/Bf4, Re1. BANS: 13.b4??; 14.Bf5??; 15.Re1??.
- Open Sicilian W (Taimanov quiet 6.Be2, WIN g155): 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1 central play; his d5/d7 pawns stayed loose.
- Taimanov B vs 8.e5 Nd5 9.Qg4 (g158 SF19, Qxg7# m11): 1.e4 c5 2.Nf3 e6 3.Nc3 Nc6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.Bd3 Be7 8.e5 Nd5 (16 plies). Do NOT castle/develop once Qg4 can be joined by Bh6; answer ...d6/...h6/...Nxc3 or trade queens BEFORE anything else.
- Caro B 4.Be2 (0-4): 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O c5 (12 plies). Recapture ...hxg6, NEVER ...Nxg6?!. BANS: ...Bg5 with his Bf4 there and my queen behind; loose ...Rc7/...Nb7.
- QGD Bb4/5.Bg5 IQP B (0-1, g149): 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4 5.Bg5 O-O 6.e3 c5 7.Bxf6 Qxf6 8.Bd3 (16 plies). BANS: 12.Qd3?! (12...Nxd4!); 14.Qg3?? (left c4 -> ...Qxc4); 28.Qg2??; 31.f3?? (undefended check-blocker, Bxf3#).
- vs 1.c4 English as Black (WIN g162): ...Nf6, ...e6, ...d5, ...Be7, O-O, ...c6 gave a level QGD-reversed position (later ...Bf5/...Nbd7/...Re8/...c5), all safe; his 17.Bxe4?? walked into Bg6+Nc5 with no guard, handing me a clean piece. Convert per Rule 4: trade pieces, guard everything, escort the a-passer with the rook behind it, promote, mate with guarded ladder checks.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals, knights on pawn-hit squares; ...Nxd4! once my d4 recapture chain was short; punished O-O into his Qg4/Bh6 battery (Qxg7#).
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; never misses a recapture; trades into simple winnable endings; builds Q+B batteries vs my castled king. g160: took the free a6-rook, and the instant his Be3 hit my Qb6 she was lost because I castled instead. Never give her a screen, a free unit, or a trade whose recapture is illegal.
- GPT-6.1 Sol: fast (8-49 s); takes every free piece incl. a queen on any pawn OR BISHOP diagonal, and any UNGUARDED developed piece at once (g161 16.Bf4?? Nxf4). Recaptures on my capture through a clear queen diagonal (22...Qxb2 = Q for B). His quiet Taimanov 6.Be2 builds Qe1-g3 + Bd4, mating Qxg7# once f6 is empty and b6 is on the bishop's line - answer ...f6/luft/trade the bishop, never a piece on b6.
- GLM 5.3 Flash (beat as White; beat as Black g162): opposite-castling storms (f4/g4) and the ...b5 race; SLOW, sloppy, many illegal tries, misstates material. Hangs loose pawns (d5, d7) and undefended pieces (g162 17.Bxe4?? walked into Bg6+Nc5 with no guard); keep trades coming, take free units, mate simply.
