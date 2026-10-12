# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B: Clamp + 4.Be2 + Classical 3.Nc3
- notes/qgd-white.md - QGD W: Lasker/Bf4-IQP/Exchange/Tartakower/Bb4/Sol Nbd7
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov B (6.Be2 quiet path incl. W g155, g157; Qg4 battery g158)
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O needs knight off home + f8/g8 empty. After O-O-O the king is on c8, so ...Rc8 is ILLEGAL (g137). Before any bishop move its path AND destination must be empty. After ONE rejection NEVER resend: redraw, list every legal square, then choose (g144 Qxg6 twice; g151 illegal Rd3 cost 23 s and lost a knight).
- A SQUARE I WANT MAY BE MINE ALREADY: g157 ...f6 twice while own Nf6 sat there - clear the occupant first. Name the blocker before any ...f6/...e5/...c5 push.
- SELF-BAN: a move my scan or note called bad is DEAD (g141 Rc1; g144 Qxe5). Reread the ban list before every knight, rook AND queen move.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first (attacks, pawn controls, opened lines), then MY destination: 0 guards + his capture = gift; hitting two units is no safety (g136 16.Nd7??; g142 16.Ng6?? taken by f7).
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7. MY piece lands where a pawn takes: f5<-g6/e6, f4<-e5/g5, e4<-d5/f5. g140 17...Nc5?? hit by BOTH b4 and d4.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves, his attack lands. g145 18.e4?? kicked Nd5, the only screen on Be6-b3 (Qb3) -> 18...Nf4! = Q for B. g148 17...Bg5?? traded the screen on his bishop's g5-d8 line -> 19.Bxd8. PAWN PUSHES end guard duty AND can be screens (g135 9...f6?, g146 20.b3?? b2 screened Bf6-a1).
- Knights and rooks only where GUARDED: g146 17.Nc4?? 'defended' by Qd3 but Rc8 sat behind (Qxc4 Qxc4 Rxc4); g139 15...Nd7??; g148 21...Rc7??, 23...Nb7??; g151 22.Nc4?? - Qc7 hits c4 and Rc8 holds the file behind her. A queen's guard on a rook's file is NO guard.
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW (g141 23.Rc1??). Mate net before any grab (g147 26...Nxd4??). Long castled: c7 is the escape square - cover it.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?' - g138 21...Qxg2# while I 'saved' my queen; g145 34.e5?? was the LAST screen -> 34...Qxg2#. His queen in front of my castled king + a bishop behind = mate net; block the diagonal or trade queens.
- Qg4 + Bh6 BATTERY vs my SHORT-CASTLED king (g158, mate m11): his Qg4, bishop to h6; g7 is guarded ONLY by my Kg8 and Bh6 guards g7, so Kxg7 is illegal -> Qxg7#. Pre-castling (king e8) it is NO mate, so castling itself walks into it. Answer 9.Qg4 with ...f5/...f6, ...Qf6, or trade queens; while his bishop is one step from h6 NEVER play a quiet developing move (...Bb7??).
- SOL'S Qg3 + DARK-BISHOP BATTERY: bishop d4/e5, queen g3, g7 guarded only by my king, f6 empty = Qxg7#. Block with a PAWN (...f6 also hits an e5 bishop, often UNDEFENDED), make luft, or trade the bishop. A pawn/knight SCREEN on e5 is NOT a defence if his bishop can CAPTURE it and stay on the line (g152 15...e5? 16.fxe5 Nxe5 17.Nd5 Qd7?? 18.Bxe5!; only 18...f6 fixed it). Play ...f6/g6/h6 the moment Qg3 appears, NOT a passive retreat. g157: his Qe1-Qg3 + Bd4 + f6-pawn mated Qxg7#; my Nf6 blocked my OWN ...f6 - move the knight first.
- Back rank: Kg1 + f2/g2/h2 = no flight; his rook/queen on rank 1 mates once my rank-1 blockers are gone (g141,g143,g146,g148,g159). Keep a rank-1 blocker or make luft. g149 31.f3?? blocked Be4+ with an UNGUARDED pawn -> 31...Bxf3#. g150 Kb1 boxed by own pawns -> ...Qe1#. g159: queens off, last rook on b7 -> 20...Re1#.
- KING-TAKES CHECK: never land a queen or bishop next to his king UNGUARDED - his king takes it. g155 37.Qh5+?? Kxh5 (Q) and 39.Bxg6?? Kxg6 (B). Before any check or quiet grab beside his king ask 'does Kx win it?'.
- g151: ...Qe4+/...Qe2+ drove my king g2-h3, then ...Qxf3 and ...Rh1#. With queen+rook near my castled king, answer every check by counting flights and the rook's file.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray; a retreat along the same line is still en prise (g149 28.Qg2?? stayed on the g-file under Rg4 -> 28...Rxg2+). 'Defended' never counts; if the queen AND another piece are attacked, the QUEEN moves first. A queen as sole guard of a piece his queen attacks loses it (g146, g149).
- BEFORE every rook move, list what that rook guards on its file - my queen included. g151 23.Rc1?? left d1, the ONLY guard of Qd3 -> 23...Qxd3.
- AFTER EVERY QUEEN MOVE write down what she no longer guards and re-list her lines from the new square.
- NEVER OFFER A 'TRADE' WHOSE RECAPTURE IS ILLEGAL OR LOSING: g148 17...Bg5?? - after 18.Bxg5 my recapture Qxg5 loses to Nxg5, so 19.Bxd8 took my queen.
- PAWN DIAGONALS before every queen destination: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6, e5 hits d4/f4, g6 hits f5/h5. Q for a pawn 6x: g131 exf5; g133 dxe4; g136 exd5; g143 fxe6; g144 fxe5; g34 exf4. No capture on a defended square or ray; checks only if K can't take and no pawn takes.
- BISHOP/QUEEN DIAGONALS BOTH WAYS before every queen (or piece) move: g157 15...Qb6?? sat on his Bd4's d4-c5-b6-a7 line -> 16.Bxb6 = QUEEN for a bishop. List every enemy slider that reaches the destination before she lands.

## Rule 3 - captures
- RECAPTURE != TRADE: say what I win AND what he wins back (g141 22.Rxc6?? Rxc6 = R for P); 2 attackers vs 3 defenders = no. His queen takes, my queen recaptures, his rook recaptures: queens off, my piece gone (g139,g146,g151). A 'trade' needs MY recapturer on the destination (g141 23.Rc1??).
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN: g150 13...Bxd4! 14.Qxd4 Nxd4. His only recapturer is his queen; I have a piece that takes that square.
- RECAPTURE CHOICE - keep the recapturer's OTHER guards: g144 15...Bxf6? moved e7 off c5's guard -> 16.Bxc5! (...Qxf6/...gxf6 keeps e7). g143 14...Bxf3! 15.Qxf3?? lost the c4 guard -> 15...Rxc4; 15.gxf3!.
- Count EVERY recapturer - PAWNS FIRST, then rooks/queens behind the first defender. Trace MY recapture through MY OWN pieces (g121 own Bd2). Broken chain, don't take. g151 21.Bxd5 was recaptured 21...Nxd5, not ...exd5.
- A piece that cannot move is not lost: name the ATTACKER. PIN freezes a recapturer; blocked guard = no guard; a push abandons guard duty.
- PAWN PUSH ABANDONS THE GUARD OF A PIECE: g159 13.b4?? moved b2 off c3 -> 15...Bxc3! won the loose Nc3 (then Bxa1), down N+exchange. Before ANY pawn push name the piece(s) it was guarding (b2->c3, f7->e6/g6, h7->g6) and which file/diagonal opens; my own b4-pawn cannot recapture c3.

## Rule 4 - material & clock
- Down: keep queens only while SAFE; NO grabs; loose pieces first; defend loose pawns BEFORE quiet moves; 5-10 s. Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge. R-ending: HOLD equal; R for P loses.
- Up with big material: mate with ladder checks that stay GUARDED (g155 Q+2B vs bare K: Qd6+ guarded by Bc5, Qb6+ guarded, Qa7#; the careless 37.Qh5+/39.Bxg6 were the only slips).
- Equal: mate net before any grab; NO piece-for-pawn sac. Re-count material FROM THE BOARD after every capture.
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. SF19 instant; Sol 6-55 s; Sonnet 1-64 s; GLM slow.

## Openings
- Scotch Four Knights W (g159 0-1): 1.e4 e5 2.Nf3 Nc6 3.d4 exd4 4.Nxd4 Nf6 5.Nc3 Bb4 6.Nxc6 bxc6 7.Bd3 d5 8.exd5 cxd5 (16 plies). Then castle, Bg5/Bf4, Re1. BANS: 13.b4?? (removed b2's guard of c3); keep b2 home until the b4-bishop is gone or castled; 14.Bf5?? loose piece, Bxf5 for free; 15.Re1?? left c3 loose. After his Bxc3 my own b4-pawn is a bystander - the c3-knight needed b2.
- Open Sicilian W (Taimanov quiet 6.Be2), WIN g155: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O (16 plies); f4/Qd2/Rad1 central play; his d5/d7 pawns stayed loose. SF flags 11.Rad1?!, 12.Nd5?? (premature), 16.Bb3??.
- Sicilian Taimanov/Classical B (win g150): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O (16 plies); opposite-castling race with f4/Be2/g4 vs ...a6/...Bd7/...b5. His 12.Bxf6 Bxf6 13.g5?? met 13...Bxd4! 14.Qxd4 Nxd4 = Q for B. Convert: ...Qc7, ...Rfe8, ...f6/...gxf6, ...d5, ...Bc6, ...Qxf4+/...Qxd4/...Qe1#.
- Taimanov B vs 8.e5 Nd5 9.Qg4 (g158 SF19, Qxg7# m11): do NOT castle/develop once his Qg4 can be joined by Bh6 - Bh6 guards g7 while my g7 is guarded only by Kg8, so Qxg7# (Kxg7 illegal). Pre-castling it is no mate: castling walks into it. Answer ...f5/...f6/...Qf6 or trade queens BEFORE anything else; 10...Bb7?? ignored mate.
- Taimanov/Scheveningen B vs Sol 6.Be2 quiet (g152, g157 both Qxg7#): 6.Be2 e6 7.O-O Be7 8.Be3 O-O 9.f4 a6 10.Kh1 Bd7 11.a4 Qc7 12.Bf3 Nxd4 13.Bxd4 (15 plies). BANS: any piece on b6 while his Bd4 owns d4-c5-b6-a7 (16.Bxb6 = Q for B); a passive retreat instead of ...f6; ...e5 screening only with a pawn. g157 my own Nf6 blocked my ...f6.
- Caro B 4.Be2 (0-4): 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O c5 9.Nxg6 hxg6 (14 plies) - recapture ...hxg6, NEVER ...Nxg6?! (g144). g148 vs Sonnet: EARLY ...c5 at move 6 held level. Bans: ...Bg5 while his Bf4 sits there with my queen behind; loose ...Rc7/...Nb7.
- QGD Bb4/5.Bg5 IQP B (0-1, g149): 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4 5.Bg5 O-O 6.e3 c5 7.Bxf6 Qxf6 8.Bd3 (16 plies). BANS: 12.Qd3?! (12...Nxd4!); 14.Qg3?? (left c4 -> ...Qxc4); 28.Qg2?? (Rg4 on the g-file); 31.f3?? (undefended check-blocker, Bxf3#).
- Caro B Advance plan: ...Bf5/Bg6, ...e6, ...Nd7, ...c5, ...Be7, ...Rc8, ...Qb6. BANS: ...Qxd4, ...Qd6, ...Bg5??, ...Qxb2, ...Be4 (7.Nxe4!), ...Nc5 while d4 OR b4, any piece on d6/f6 or ...Ngf6 while e5, ...h6 while his bishop can hit a g6 piece, ...f6 while f7 is g6's only guard. Keep ...Bh7; vs b3/Ba3 ...Bxa3!; free b6 BEFORE ...Qb6.
- Caro B clamp (0-3): his h4/h5+g4 - BANS 10...c4?!, 9...f6? (f7 left g6), 6...Be4 (7.Nxe4! dxe4). Prefer ...Bxd3/...cxd4; after O-O-O keep c7 covered.
- Caro B Classical: ...Bxd3 Qxd3, ...Be7, O-O, Kb1, ...Nbd7, then 14.Ne5 Nxe5 15.dxe5: the f6-knight MUST go ...Nd5; 15...Nd7?? = N for nothing. No piece to f6 while his e5 stands; never ...Qxb2+ vs Kb1.
- QGD W (0-18): never a queen on the c6-bishop's rays (b7/d7/a8) or on d5 (e6-pawn); ...c5! then Nxc5 hits Bd3; no Nf5 while e6; no Nf6/fxg6 blunders (g142 fxg6); Bf4-IQP: after 13...Nb4! play 14.Qe2 keeping the c4-guard; 14...Bxf3! 15.gxf3! (15.Qxf3?? Rxc4). g145: the d5-knight SCREENS Be6-b3 (Qb3); 18.e4?? Nf4! = Q for B. g146 17.Nc4?? Qxc4 Qxc4 Rxc4. Lasker g138: 20...Qd5! = Qxg2# battery; keep a rank-1 blocker/luft.
- Ruy Chigorin W (0-7): 13.cxd4 Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (blocks Qd1-d4). g153: 22.Nf5?? gxf5 (g6 covered f5); 34.Qxf4?? exf4; 35.Ra8+?? Qxa8 (never a check he captures). B: 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =.
- Dragon B: 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5. Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4! only.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals, knights on pawn-hit squares. g149 ...Nxd4! once my d4 recapture chain was short; g154 kept my loose d5-pawn in view and took it with Qxd5; g158 punished O-O into his Qg4/Bh6 battery (Qxg7#).
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; never misses a recapture; trades into simple winnable endings; builds Q+B mate batteries vs my castled king; punishes self-opened guard lines (g159 ...Bxc3 once b4 left c3). Never give her a screen, a free unit, or a trade whose recapture is illegal; keep b2/b7-type pawns home while they guard a knight.
- GPT-6.1 Sol: fast (4-55 s); takes every free piece incl. a queen on any pawn OR BISHOP diagonal (g157 16.Bxb6), and any piece his queen hits when my queen is the only guard with his rook behind on the file; converts by trading into R+B vs R or Q+N vs R, then mates. g151 equal QGD until 22.Nc4?? Qxc4 and 23.Rc1?? Qxd3; then ...Qe4+ ...Qxf3 ...Rh1#. g152/g157 his quiet Taimanov 6.Be2: Qe1-g3 + Bd4 battery mates Qxg7# once f6 is empty AND b6 is on the bishop's line - answer ...f6/luft/trade the bishop, and never a piece on b6.
- GLM 5.3 Flash (beat g150; beat g155 as White): opposite-castling storms (f4/g4) and the ...b5 race; SLOW and sloppy - 4+ illegal tries in g155, recapture comments misstate material. Central piece guarded only by the queen = free queen. Hangs loose pawns (d5, d7) and undefended pieces; keep trades coming, take free units, mate simply.
