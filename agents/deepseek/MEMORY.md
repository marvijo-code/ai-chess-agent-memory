# Chess memory

Notes:
- notes/capture-safety.md - pre-move scan + blunder catalogue
- notes/caro-advance-black.md - Caro Advance B: Clamp + 4.Be2 + Classical 3.Nc3
- notes/qgd-white.md - QGD W: Lasker/Bf4-IQP/Exchange/Tartakower/Bb4/Sol Nbd7
- notes/ruy-lopez-black.md - Chigorin/Breyer B
- notes/ruy-lopez-white.md - Chigorin W
- notes/sicilian-black.md - Alapin/Dragon/Taimanov + 4.Bb5/5.e5
- notes/sicilian-soltis-black.md - Soltis B
- notes/sicilian-yugoslav-black.md - Yugoslav B

## Rule 0 - legality & self-ban (3 invalid = forfeit)
- O-O needs knight off home + f8/g8 empty (g124). After O-O-O the king is on c8, so ...Rc8 is ILLEGAL (g137, 1:16 wasted). Before any bishop move its path AND destination must be empty (g140,g145,g148). After ONE rejection NEVER resend: redraw, write out every legal square of that piece, then choose (g144 Qxg6 twice; g149 Qe3 rejected then Qg2?? still a blunder; g151 illegal Rd3 cost 23 s and the retry lost a knight).
- SELF-BAN: a move my scan or note called bad is DEAD (g141 Rc1; g144 Qxe5). Reread the ban list before every knight, rook AND queen move.

## Rule 1 - destination sweep (EVERY move, mine too)
- His LAST move first (attacks, pawn controls, opened lines), then MY destination: 0 of my guards + his capture = gift; hitting two of his units is no safety (g136 16.Nd7??). g142 16.Ng6?? 'fork' taken by f7-pawn.
- PAWN ATTACKS on EVERY destination: g6<-f7/h7, b6<-a7/c7, d6<-c7/e7, c5<-b4/d4, e5<-d4/f4, e6<-f7. MY piece lands where a pawn takes: f5<-g6/e6, f4<-e5/g5, e4<-d5/f5. g140 17...Nc5?? landed on a square hit by BOTH b4 and d4.
- SCREENS: a piece between his bishop/rook and MY queen or king - when it moves, his attack lands. g145 18.e4?? kicked Nd5, the only screen on Be6-b3 (my Qb3) -> 18...Nf4! = Q for B. g148 17...Bg5?? traded the screen on his bishop's g5-d8 line to my queen -> 19.Bxd8.
- PAWN PUSHES end guard duty AND can be screens: g135 9...f6? (f7 left g6), g144 19...h6?? (h7 left g6), g146 20.b3?? (b2 screened Bf6-a1).
- Knights and rooks only where they are GUARDED: g139 15...Nd7??; g146 17.Nc4?? 'defended' by Qd3 but Rc8 sat behind: Qxc4 Qxc4 Rxc4 = N gone; g148 21...Rc7??, 23...Nb7?? undefended; g151 22.Nc4?? - his Qc7 hits c4 and his Rc8 holds the file behind her, so ...Qxc4 won the knight. A queen's guard on a rook's file is NO guard.
- Rook files/bishop rays own whole lines; attacked+undefended -> save NOW (g141 23.Rc1?? walked onto Rc6's file). Mate net before any grab (g147 26...Nxd4??). Long castled: c7 is the escape square - cover it.

## Rule 1b - MATE FIRST (after EVERY his move, quiet ones too)
- Ask 'what mates if I pass?' - g138 21...Qxg2# landed while I 'saved' my attacked queen; g145 34.e5?? was the LAST screen on that diagonal -> 34...Qxg2#. Never push/capture the last screen between his queen and my king.
- His queen landing in front of my castled king + a bishop behind it = mate net. The reply must block that diagonal (e4) or trade queens - saving the queen alone is not a defence.
- SOL'S Qg3 + DARK-BISHOP BATTERY: his bishop lands on d4/e5, his queen on g3, g7 guarded only by my king, f6 empty = Qxg7#. Block with a PAWN (...f6 also hits an e5 bishop, which is often UNDEFENDED), make luft, or trade the bishop. A piece screen on the ray (a pawn/knight on e5) is NOT a defence: if his bishop can CAPTURE the screen and land on the same line, the mate returns (g152 15...e5? 16.fxe5 Nxe5 17.Nd5 Qd7?? 18.Bxe5! - 18...f6 was the fix, 18...Bxd5?? 19.Qxg7#). When the battery appears, spend the move on ...f6/g6/h6, NOT a passive knight retreat (g152 14...Nd7? wasted the tempo and cost 36 s).
- Back rank: Kg1 + f2/g2/h2 pawns = no flight; his rook/queen on rank 1 mates once my rank-1 blockers are gone (g141 Rxc1+/Rxe1#; g143 Qe1#; g146 Re1#; g148 Rc8#). Keep a rank-1 blocker or make luft before the last one leaves. g149 31.f3?? blocked Be4+ with an UNGUARDED pawn on a diagonal to my king -> 31...Bxf3#. g150 his Kb1 boxed by own pawns -> my ...Qe1#.
- g151: his ...Qe4+/...Qe2+ drove my king g2-h3, then ...Qxf3 and ...Rh1#. With queen+rook near my castled king, answer every check by counting flights and the rook's file. A knight kicked to f4 -> Ne2+ forked my Rc1.

## Rule 2 - the queen
- HIT -> she moves THAT move, OFF every attacker ray; a retreat along the same line is still en prise (g134 Qd8?? on a5-b6-c7-d8: Bxd8; g149 28.Qg2?? stayed on the g-file under Rg4 -> 28...Rxg2+ = Q for R). 'Defended' never counts (g95); if the queen AND another piece are attacked, the QUEEN moves first (g145 19.Bc2 then ...Bxb3 = Q for B). A queen as the sole guard of a piece his queen attacks loses it (g146 Qxc4; g149 14.Qg3?? Qxc4).
- BEFORE every rook move, list what that rook guards on its file - my queen included. g151 23.Rc1?? took the rook off d1, the ONLY guard of my Qd3 -> 23...Qxd3.
- AFTER EVERY QUEEN MOVE write down what she no longer guards and re-list her lines from the new square.
- NEVER OFFER A 'TRADE' WHOSE RECAPTURE IS ILLEGAL OR LOSING: g148 17...Bg5?? - after 18.Bxg5 my recapture Qxg5 loses to Nxg5, so 19.Bxd8 took my queen = Q for B. Same in g154: Qd8 was Re8's sole guard; moving her to recapture left the rook en prise.
- PAWN DIAGONALS before every queen destination: e6 hits d5/f5, d5 hits c4/e4, f7 hits e6/g6, e5 hits d4/f4, g6 hits f5/h5. Q for a pawn 6x: g131 Qxf5?? exf5; g133 Qe4?? dxe4; g136 Qd5?? exd5; g143 Qxe6?? fxe6; g144 24...Qxe5?? fxe5; g34 34.Qxf4?? exf4 = Q for R (his e5-pawn guards f4).
- List ranks/files/diagonals + knight jumps; no capture on a defended square or ray; checks only if K can't take and no pawn takes (g127).
- QUEEN takes: count EVERY defender incl. pawns, knights, THE KING (g110,g130 Qxb2+?? Kxb2); pawn recapture before a queen trade.

## Rule 3 - captures
- RECAPTURE != TRADE: say what I win AND what he wins back (g141 22.Rxc6?? Rxc6 = R for P); 2 attackers vs 3 defenders = no (g126). His queen takes my piece, my queen recaptures, his rook recaptures: queens off, my piece gone (g139 d7, g146 c4, g151 c4).
- A 'trade' move needs MY recapturer on the destination or it is a gift (g141 23.Rc1??).
- ONLY-QUEEN-GUARDED + MY SECOND ATTACKER = WIN THE QUEEN: g150 13...Bxd4! 14.Qxd4 Nxd4. His pawn recapture impossible, only recapturer is his queen, and I have a piece that can take that square: capture - his queen must take, my second piece takes HER.
- RECAPTURE CHOICE - keep the recapturer's OTHER guards: g144 15...Bxf6? moved the e7-bishop off c5's guard -> 16.Bxc5!; ...Qxf6/...gxf6 keeps e7. g143 14...Bxf3! 15.Qxf3?? lost the c4 guard -> 15...Rxc4; 15.gxf3! keeps her on post.
- Count EVERY recapturer - PAWNS FIRST, then rooks/queens behind the first defender (g129 missed Re1; g131 e6-pawn = Q for P). Trace MY recapture through MY OWN pieces (g121 own Bd2). Broken chain, don't take. g151 21.Bxd5 was recaptured 21...Nxd5, not ...exd5.
- A piece that cannot move is not lost: name the ATTACKER. PIN freezes a recapturer; blocked guard = no guard; a push abandons guard duty.

## Rule 4 - material & clock
- Down: keep queens (repetition) only while they are SAFE; NO grabs (g132-g151; g148 18...bxa4 grabbed with my queen already lost); loose pieces first; defend loose pawns BEFORE quiet moves; 5-10 s.
- Up: trade pieces not pawns; escort passers; promote; stalemate-check; one hung unit kills a +1 edge (g128). R-ending: HOLD equal; R for P loses (g111). g150 up Q for B: keep the queen off his Bd3 rays (c4/b5/a6/e4/f5/g6) and pick off free units.
- Equal: mate net before any grab; NO piece-for-pawn sac (g127). Re-count material FROM THE BOARD after every capture (g131, g138, g151).
- Time: book <=10 s, routine <=15 s, cap 20 s; <3 min <=5 s. 20-81 s routine thinks still blundered. SF19 instant; Sol 6-55 s; Sonnet 1-64 s; GLM slow.

## Openings
- Sicilian 4.Bb5/5.e5 B (g154, 0-1 vs SF19): with c5/Nc6/Nf6/e6 and my knight chased to d5, the trade Nxd5 exd5 removes the c6-knight - d5's ONLY guard - so my d5-pawn is LOOSE. 8...O-O?! castled past it; after 9.dxc5 Bxc5 his 10.Qxd5 (+1.9) won the pawn. At move 8 play ...cxd4/...Nxd4 or DEFEND d5 (...Qc7/...a6/...Na5). Later 12...Bf6? allowed Qxf7+ Kh8, exf6; recapturing Qxf6 left Re8 (Qd8 was its sole guard) -> Qxe8+ Qf8 Qxf8#. Never move the sole guard of an en-prise piece.
- Sicilian Taimanov/Classical B (my win, g150, Qe1# m27): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Bg5 e6 7.Qd2 Be7 8.O-O-O O-O (16 plies), then 9.f4 a6 10.Be2 Bd7 11.g4 b5 opposite-castling race. His storm 12.Bxf6 Bxf6 13.g5?? met by 13...Bxd4! 14.Qxd4 Nxd4 = Q for B. Convert: ...Qc7, ...Rfe8/...Red8 rook trades, ...f6/...gxf6, ...d5, ...Bc6, then ...Qxf4+/...Qxd2/...Qe1#. Meet a slow storm with ...b5.
- Taimanov/Scheveningen B vs Sol (g152 0-1, Qxg7# m19) - his 6.Be2 QUIET path: 6.Be2 e6 7.O-O Be7 8.Be3 O-O 9.f4 a6 10.Kh1 Bd7 11.a4 Qc7 12.Bf3 Nxd4 13.Bxd4 (15 plies), then 13...Bc6 14.Qe1 Nd7? 15.Qg3. BANS/lessons: (a) trade his Bd4 or play ...f6 BEFORE Qg3, never a passive retreat; (b) 14...Nd7? wasted the tempo; (c) 15...e5? only screened with a pawn - 16.fxe5 Nxe5 17.Nd5 (forks Qc7+Bc6, drives my queen) Qd7?? 18.Bxe5! landed his bishop on d4-g7 with f6 empty = mate; only 18...f6 blocked (and hits the UNDEFENDED e5 bishop); 18...Bxd5?? 19.Qxg7#. When Qg3+P-bishop point at g7, the move is ...f6/g6/h6, not a capture or a piece screen.
- QGD Bb4/5.Bg5 IQP (0-1, g149): 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Bb4 5.Bg5 O-O 6.e3 c5 7.Bxf6 Qxf6 8.Bd3 (16 plies), then ...cxd4/...dxc4/...Nc6/...Rd8. BANS: 12.Qd3?! (12...Nxd4!), 14.Qg3?? (left c4 -> ...Qxc4), 28.Qg2?? (Rg4 on the g-file -> Rxg2+).
- QGD vs Sol g151 (0-1): 1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.Nf3 Be7 5.Bg5 O-O 6.e3 Nbd7 7.Bd3 dxc4 8.Bxc4 (16 plies), then ...c5/...cxd4/...b6/...Bb7/...Rc8/...h6/...Nxf6/...Nd5/...Qc7/...Rfd8; 21...Nxd5 (not ...exd5) recaptured. BANS: 22.Nc4?? (...Qxc4 wins the knight), 23.Rc1?? (left Qd3 unguarded -> ...Qxd3).
- Caro B Advance plan: ...Bf5/Bg6, ...e6, ...Nd7, ...c5, ...Be7, ...Rc8, ...Qb6. BANS: ...Qxd4, ...Qd6 (vs Bf4 exd6), ...Bg5??, ...Qxb2, ...Be4 (7.Nxe4! dxe4), ...Nc5 while d4 OR b4, any piece on d6/f6 or ...Ngf6 while e5, ...h6 while his bishop can hit a g6 piece, ...f6 while f7 is g6's only guard. Keep ...Bh7; vs b3/Ba3 ...Bxa3!; free b6 BEFORE ...Qb6.
- Caro B 4.Be2 (0-4, g140,g144,g147,g148): 3.e5 Bf5 4.Be2 e6 5.Nc3 Nd7 6.Nf3 Ne7 7.Nh4 Bg6 8.O-O c5 9.Nxg6 hxg6 - recapture ...hxg6, NEVER ...Nxg6?! (g144). g148 vs Sonnet: my EARLY ...c5 at move 6 held the game level, with ...cxd4/...Nc6/...Be7/...O-O/...Re8/...Rc8; never a shuffle (g147 18...Bf8?! let 21.f5! win the exchange). Bans: ...Bg5 while his Bf4 sits on it and my queen is behind on g5-f6-e7-d8; ...Rc7/...Nb7 unguarded.
- Caro B clamp (0-3, g135,g137): his h4/h5+g4 clamp - BANS 10...c4?! (d5's only guard is the b6-knight: 11.Bxh7 Rxh7 12.f5! +3.4), 9...f6? (f7 left g6 -> 10.Nf4!, 11.Ng6), 6...Be4 (7.Nxe4! dxe4). Prefer ...Bxd3/...cxd4; after O-O-O keep c7 covered.
- Caro B Classical (g130, g139): ...Bxd3 Qxd3, ...Be7, O-O, Kb1, Nbd7, then 14.Ne5 Nxe5 15.dxe5: the f6-knight MUST go ...Nd5 (c6-pawn covers); 15...Nd7?? = N for nothing. No piece to f6 while his e5 stands; never ...Qxb2+ vs Kb1.
- Caro W 3.Nc3: 15.d5! exd5 16.cxd5 Re8 = space edge; no sacs (Bxh6); NO Qg6 (g127); Kb1 vs ...Rad8: trade rooks/make luft, never grab (g123).
- QGD W (0-18): Lasker g138: 15.Ne5?? only trades; after dxe5 the e5-pawn hangs -> ...Qc5/...Qxe5; 20...Qd5! = Qxg2# battery; never Qx b7/d7/a8 vs c6-bishop; ...c5! then Nxc5 hits Bd3; no Nf5 while e6. g141 22.Rxc6?? R for P; 23.Rc1?? Rxc1+ Rxe1#. g142 16.Ng6?? fxg6. Tartakower g136: never a piece on d7 or d5 (e6-pawn). g145: the d5-knight SCREENS Be6-b3 (my Qb3); 18.e4?? Nf4! = Q for B; move the queen off b3 (Qc2) before any kick. g143 Bf4-IQP: 13...Nb4! hits Qd3; 14.Qe2 keeps the c4-guard; 14...Bxf3! 15.gxf3!. g146 IQP: 13.Bxf6 Nxf6 14.Ne5 Nd5; 17.Nc4?? Qxc4 Qxc4 Rxc4 = N gone.
- Ruy Chigorin W (0-7): 13.cxd4 Nf1 BEFORE Qe2; keep Rc1; 16.Be3, NOT Bd2?! (kills Qd1-d4, g121). g34: 22.Nf5?? gxf5 - after his ...g6 the pawn owns f5 (e6 also covers it); 34.Qxf4?? exf4 = Q for R. B: 10.e5 -> ...Ne8/...d6, never take e5; 9.Bd5! only 9...Nxd5 =; Qc7 retreats when the c-file opens.
- Dragon B: 13.Qxd5 -> ...Qc7 ONLY. Soltis 9.Bc4 (0-8): 14.h5 Nxh5!; 16.g5 -> only ...Nh5. Alapin B: 5.Qxd4 Nc6/g6/Bg7/O-O/Nc5; no ...b5/...Nb4/...Nd4 while Rd1 faces Qd8; 12.Bxe5 12...Nxe4! only.

## Opponents
- SF19: instant; punishes loose units, passive retreats, queens on his ranks/rays/pawn diagonals, knights on pawn-hit squares. g149: it played ...Nxd4! the moment my d4 recapture chain was short, then Qxc4. g154: kept my loose d5-pawn in view and took it with Qxd5 the moment I castled past it. Never shuffle passively vs a pawn clamp; never move the sole guard of an en-prise piece.
- Sonnet 5.5 (never beaten): banks clock; takes every free unit; never misses a recapture; trades into simple winnable endings; builds Q+B mate batteries vs my castled king (g141 Rxc1+/Rxe1#; g145 ...Nf4! then Qxg2#; g148 18.Bxg5 with my recapture illegal, then Rc8#; g34 won the Nf5 gxf5 and Qxf4 exf4 blunders). Never give her a screen, a free unit, or a trade whose recapture is illegal; never land a knight/queen where her pawn takes.
- GPT-6.1 Sol: fast (4-55 s); takes every free piece incl. a queen on any pawn diagonal (g133 dxe4, g136 exd5) and any piece his queen hits when my queen is the only guard with his rook behind on the file (g146 17...Qxc4 Qxc4 Rxc4); no sacs/grabs; converts by trading into R+B vs R or Q+N vs R, then mates (g139 R to 7th + Bf6#; g146 Re1#). g151: equal QGD until 22.Nc4?? Qxc4 and 23.Rc1?? Qxd3; then 29...Qe4+ 30.f3 Qe2+ 31.Kh3 Qxf3 32.Kh2 Rh1#. He recaptures on d5 with the knight (21...Nxd5). g152: his quiet Taimanov 6.Be2 - Qe1-g3 + Bd4 battery mates with Qxg7# once f6 is empty; answer with ...f6/luft/trade the bishop, never a capturable piece screen. Never leave a piece guarded only by my queen, never move a rook off my queen's guard file.
- GLM 5.3 Flash (beat g150): plays opposite-castling pawn storms (f4/g4) and the ...b5 race; SLOW and sloppy - illegal attempts, 17-40 s on routine moves; its recapture comments misstate material. Central piece of his guarded only by the queen = free queen (g150 13...Bxd4!). Answer his slow storm with ...b5/...b4 and keep trades coming.
