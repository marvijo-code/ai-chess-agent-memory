# MEMORY (clocks 900+10; T43+ are 3600+10; Armageddon: W 10 min / B 7:30+odds)

## Record
- T68F B v SF19 1/2 THREEFOLD at +10.6: Four Knights 4...Bb4 recipe level to m13; 13...dxc3! 14.Bxc3 Qxc3?? 15.dxc3 - his d2-PAWN (permanent 2nd defender of c3) ate my queen = Q for B. Down Q+P for B, shell m16-47 (king g8/h8, Rd8+Re7 double d7, parked bishop, a8=Q met Rxa8, no bait grabs); his queen looped Qa3/Qc3+/Qb2+, deterministic replies + occurrence counting led to threefold.
- T68R3 W v SF19 0-1 m29 (Qxb2#): Maroczy 6...Qa5 7.Be3?! Nxe4! PIN POISON; 8.Bd2?! Nxd2 9.Qxd2!, 10.O-O-O? 10...Bxd4 = -B-2P. Guarded wall 20+ moves at +9; his 27...Ba4 touched my frozen queen, 28.Qxa4?? left b2 to Kb1 alone - Qb6xb2#. Down heavy = 10-20 s scans, not 3-5 min thinks.
- T68R1 B v DS-4.1 FORFEIT (his flag 1:40, my 30:43): Classical Ruy level to m11; 12.d5! hit Nc6+Be6; 12...Ne5?? vacated a4-d7 to MY QUEEN on d7 - Q for B. Closed wall ground out on his 7-10 min thinks; I shuffled 10-15 s. FLAG WINS REAL v DS.
- T67R5.2 W v Muse 1.3 WON ON TIME (his 0:12): symmetric English; gave back edge to phantom-ledger landings; K+2P v B+5P closed shuffle he could not break. Count his clock.
- T67S1 Arm W v SF19 0-1 m31: 4.cxd5 exd5 5.Bg2 d4! eats my Nc3 (fix 6.Na4!). T67S1G1 B v SF19 1/2 THREEFOLD at +18: 9...Bxd4?? (Qd3+Nc3); 14.Bxd8 ate my queen after my f6-SCREEN moved; K+5P shell v Q army drew.
- T62-66: ghost landings + pawn-square captures + checks HE takes. T55-61: 2x time; 2 stalemate + 1 threefold draw v SF.

## Key lessons (check before EVERY move)
- CAPTURE CHAIN = HIS PAWN RECAPTURERS FIRST (T68F Qxc3?? dxc3): WHITE PAWNS EAT TOWARD RANK 8 (d2 is the permanent pawn-defender of c3-class squares), BLACK TOWARD RANK 1. For every capture square (a grab, a trade landing, a recapture): name his PAWN defenders by exact direction FIRST, then his pieces by traced lines, then recount both totals - and recount AGAIN after MY own capture. A pawn recapture re-opens the square for the NEXT attacker.
- THE FROZEN-QUEEN GUARD DUTY (T68R3): a king-adjacent square guarded ONLY [pawn + my queen] while a supported enemy piece faces it = a pin; the first touch wins her. FIX: ROOK as the permanent 2nd guard, never the queen; before castling with a g7-class bishop alive, walk his supported queen entries there; a FREE CAPTURE = FIRST list the supported checks it enables vs my king; mate check before bait.
- MAROCZY PIN POISON v 6...Qa5: Nc3 FROZEN by the pin; ...Nxe4! wins free; any Bd2/Be3 shield dies to ...Nxd2 first. Fix: 7.f3! with the pin live, or develop away / O-O before any bishop enters d2/e3.
- VACATION SWEEP, BOTH DIRECTIONS: before ANY piece moves, walk every enemy slider line THROUGH MY PIECE old SQUARE and name MY units (above all the QUEEN) on the far side - a safe-looking move can open HIS attack (T68R1 12...Ne5?? cost the game).
- A REACHABILITY CLAIM IS A SQUARE-BY-SQUARE WALK (T67S1G1: claimed Bg5 cannot reach d8, 14.Bxd8 ate the queen). MY PIECE ON A LINE TO MY QUEEN = a SCREEN; before it moves, move HER, or re-walk. A SCREEN I MUST MOVE LATER IS A DEBT: never grab the pawn that pins me to it.
- A PAWN PUSH/CENTER PAWN I IGNORE = A LIVE ATTACKER: before ANY quiet move write what EVERY his pawn attacks NOW; name BOTH exits before a fork lands; where knights stay also shades the FANGS (...Ne5 unmasked the a4-bishop).
- MISS-CHECK FOR QUEENS: sweep the checker square vs his pawns, sliders, the piece he JUST moved. A CHECK HE ANSWERS BY TAKING IS A GIFT. An attack on his piece is not a defense when it opens a check. While worse: defense ONLY - no gesture checks, no king walks.
- WINNING BIG: a knight ATTACKING MY QUEEN = she moves THAT move; trade queens or stay a knight-jump clear; each his pawn take of MY LOOSE units every move.
- GHOST RULE AFTER MY OWN MOVES TOO: before EVERY move WRITE the piece CURRENT square (illegal Kh8 with the king already there, T68F); one invalid try = slow down and re-list. Multi-square move = WALK THE PATH; list MY OWN pawns before a push.
- A FORK/SAC NEEDS HIS DEFENDER NAMED: both targets capturers AND the tempo reply. A TRADE OFFER HE CAN DECLINE is a move for nothing.
- MY OWN PAWN BLOCKING MY QUEEN GUARD LINE = THAT PIECE UNGUARDED. His move ATTACKS MY PIECE: retreats FIRST, prefer the retreat that also guards my other hanging unit. IN-BETWEEN CHECK: my capture can land ON his vacated square.
- STORM DEFENSE v g4/h4: NEVER ...h6; pawn-off central counters BEFORE his g5 lands; king never parks on the built file; a blocker needs ONE NAMED GUARD.
- QUEEN WITHIN ONE HIS-KNIGHT JUMP OF HER SQUARE = HIS FREE TEMPO: walk each his knight jump vs her square BEFORE every queen move, parking included.
- BOARD MAP FROM HIS LAST MOVE + CAPTURE LIST; a piece he just ate CANNOT MOVE. HIS LAST-MOVING PIECE = THE DEFAULT RECAPTURER. Before ANY attack write HIS flat captures of MY attacker - an unguarded target is DEAD.
- LANDINGS: walk every his rook file and rank, bishop diagonal SQUARE BY SQUARE. AFTER A TRADE: the departing piece STOPPED covering one-jump squares - re-list covers on the CURRENT board before landing there.
- DOWN-HEAVY SHELL v SF (3 DRAWS): king HOME alternating TWO SQUARES, luft; rooks home, the hit pawn guarded TWICE; parked bishop where her captures = Q-for-B; pawns FROZEN (never touch one in the shell); every trade offer declined; NO bait grabs - anything that unblocks a line to my king or frees his pieces (Bxc4 then Rxh6-class) is a trap. COUNT REPETITION OCCURRENCES of each position: even when his QUEEN loops checks (Qa3/Qc3+/Qb2+ rotation, T68F), the deterministic 2-square king reply alone reaches threefold - a repetition is a RESULT. NEVER resign. 5-10 s a move, no long thinks down material.
- THE FLAG AS A RESULT (T68R1, T67R5.2): v clock-burners in a closed quiet game, 5-10 s shuffles on a NAMED cycle, every unit guarded, count HIS clock every few moves - a 7 min think on a quiet move is a GIFT. DOWN-MOVING PIECE ON MY PAWN CAPTURE SQUARE = THE PAWN EATS IT.
- ALL CHAINS: defenders KING first; HIS recapturer, MINE, HIS. A GUARD IS REAL ON A TRACED LINE ONLY. THE GRAB SWEEP RUNS BOTH WAYS. UP = TRADE QUEENS FIRST.
- STORED PLANS = QUESTIONS with preconditions; after ONE rejection pick a DIFFERENT piece AND idea (3 illegal = forfeit). A note that names the FIX is an ORDER - deviations lost games.
- CLOCK IS #1, EVEN AHEAD: routine 10-20 s, capture/check 30-40 s, cap 60 s; lost/down 5-15 s. NEVER a long think after an illegal try or with material miscounted. AMBIGUOUS SAN = name the file; SHUFFLE = name the piece CURRENT square first.

## Openings
- B Italian Four Knights v SF (T68F, recipe PLAYED AND WORKED to m13 - keep): 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4! 8.Nxd4 exd4 = even; then ...a6/...Bd6/...Qf6 (holds d4, keeps breaks alive) and ...c5 supported. Details in notes/four-knights-black.md.
- W rev-QGD English: 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 - 5...d4! killer: 6.Na4! fixes it, or skip 4.cxd5 (Maroczy/2.Nf3 order, unverified). NO Ne4 (d5-pawn); at ...Nd5/...Nb4 TRADE, PAWN takes first; never 8.d4; 12.Rb1.
- W v ...e5 Symmetric English (Muse, level, repeat): 1.c4 e5 2.Nc3 Nf6 3.g3 Nc6 4.Bg2 d6 5.Nf3 Be7 6.O-O O-O 7.d3 Re8 8.Re1; then e4/Be3, later d4 with the recapturer chain NAMED first. h3 kills ...Bg4 pins cheaply.
- B Ruy Classical v 3.Bb5 (T68R1, PLAY AGAIN with the fork fix): to 9.d4 exd4 10.cxd4 Bb6; 11...Qd7 was THE blunder square - she must NOT sit on the a4-d7 diagonal while the c6-knight stands on it; prefer 11...h6/...Re8. His 12.d5 hits Nc6+Be6; ...Ne7 unverified. The wall (c6/b5/a6/f6, Bc8, Rd7 v the d-passer) GROUND OUT a Q-for-2P deficit on his clock.
- B v SF19 1.e4 PIANISSIMO: prefer the Four Knights recipe above; v his early Nxe5 try: 4...d6 5.Nxc6! bxc6 6.d4 was +3 (drop the recipe there). After his Bg5 faces my Qd8 the f6-knight is a PRISONER - ...Be7 first, NO d4-grab.
- B TAIMANOV v 6.Be3/f3/Qd2/O-O-O STORM (Muse): ...Nxd4/...Qb6-class counter EARLY; NO ...h6; king AWAY from the built file.
- B Taimanov ...e6 v 6.Be2/f4/Qd2/Rad1 build (DS/Sol): ...a6/...b5/...Bb7/...Be7/...O-O; 12.e5!: ...Qd7 BEFORE any rook drift; his Bxf6 then ...Be6!, NEVER ...Bxf6; NEVER ...Qd6??.
- W MAROCZY v ...g6 SF (notes/white-maroczy.md): 6...Qa5 = BAN bishop develops (7.f3! first or O-O); O-O-O with Bg7 live = BAN (the b2-door); short castling preferred.
- v DS-1017 Symmetric English (both colours): 4.cxd5 Nxd5 5.Bg2 Nxc3 6.bxc3; then Bd6/Nf3/O-O/Nc6; his early Bg5 aims Qd8: move her or ...Be7.
- Other (in files): B Scheveningen v Sol; ...e6 Sicilian general; Sveshnikov; Alekhine (drift only); French Alapin; W Rauzer/Kalashnikov; B Pirc/Modern v SF 5.f4 BANNED.

## Opponents
- SF19: instant, zero illegal. Punishes ONE slip with the full chain; wins by PAWN and FLAT captures (his PAWNS are the defenders I keep forgetting); mates by BATTERIES behind his own sliders and advanced pawns; after every my kingside pawn push his file/diagonal net starts. Even at +9/+10 nothing is gifted - he walks, probes and VARIES his queen checks waiting for MY scan miss; when nothing can push he LOOPS checks - if my replies are deterministic, threefold is a REAL SET (T67S1G1, T68F). NEVER resign.
- DS-4.1 Flash: solid, ~1 invalid/game, no gifts. AS WHITE Taimanov: Be2-Be3/f4/Qd2/Rad1 + 12.e5. AS BLACK rev-QGD: ...c6/...Bf5/...Nbd7/...Re8. AS WHITE Ruy Classical: cracks = a center-pawn FORK and huge thinks while stuck in a snagged winning position - a closed no-progress position POISONS him; guard everything, count his clock, the FLAG is the save (repetition is not).
- Muse Spark 1.3: patient 30 s-4+ MIN thinks, ZERO illegal, converts without gifts. AS WHITE Taimanov runs the Yugoslav storm (STORM rule), O-O-O long before g5. Symmetric English he burned the bank - BOTH my wins on HIS clock; bank the flag. His Maroczy pin trap verified by my own loss: STORED = PLAY IT.
- DS-1017: solid build, exact trades, 1-3 invalid tries. LEAK parks units on MY pawn capture squares. While UP never leave a unit loose. He answers pawn kicks by capturing on the bishop OTHER ray - walk BOTH diagonals before kicks.
- Sol (GPT-6.1): fast, zero illegal, no gifts; Bxc5-to-win-e5 recipe; flag with insufficient material = DRAW. Haiku 5.5: solid Pianissimo, cracks at lines meeting pawn diagonals. GPT-6 Astra: Sveshnikov side, converts R endings. Sonnet 5.5: a4! kills ...b5.

## Notes
notes/english-white.md; notes/four-knights-black.md; notes/pianissimo-black.md; notes/scheveningen-black.md; notes/sicilian-black.md; notes/sveshnikov-black.md; notes/taimanov-sol.md; notes/white-maroczy.md
