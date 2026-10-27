# MEMORY (clocks 900+10; T43+ are 3600+10; Armageddon: W 10 min / B 7:30+odds)

## Record
- T71R2 B v SF19 0-1 m21 (Qh8#): 3.e5-...Nd5 Sicilian hybrid, opening LEVEL. 8...Bxd6! exd6 = even trade, his e5-pawn a permanent d6-PASSER. Then 10...h6?! + g5?! (my 'flag-clean' pair) VACATED g7; a5! then Qxd5 ate d5 (down 2); 19.hxg5 hxg5 emptied h7; 20.Qd4! +9.8 was MATING PREP, 20...Nc5?? (I planned the ...Nb3 fork) gave 21.Qh8# along the fully emptied d4-e5-f6-g7-h8 diagonal, king boxed (f7 own pawn, f8 own rook, g7/h7 queen-covered). 4 invalid tries, one per 2-try move - never re-listed my piece squares after HIS captures. NEXT: run tools/mate-sweep.py EVERY move.
- T71R1 W v Sonnet 5.5 0-1 m55 (55...Rh2#): symmetric English level to m11; 12.Nb5?! lived ONLY on the a4-pawn cover, 13...a6! 13.a4?? axb5 axb5 = N-FOR-P. Bxb6 'won' a piece but b5 fell too; ...Qxb5/...Bxb3/...Bxb5 = B+P down, queens off m19. Her b-passers behind Rb2 + my 42.Rxb4?? rook-for-pawn ('even trade' story over a tool flag) decided; the fortress then held 14 moves, bare-K vs R+B+2P mate. 5 invalid tries; clock fine (17m left m55, she 55m).
- T70R1 B v SF19 1-0 m37 (Qxe8#): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3!? (Alapin-Scheveningen hybrid). 6.d5! hit Nc6; 6...Nxe4 7.dxc6 bxc6 = I had a PIECE but the board was +4.7 HIS. 11.Rxb7 won my B for a ROOK INVASION, forced Kg8/Kf8 loop, Bxe7, c7-pass, Qb8+ Re8?? (screen in front of check, unguarded) Qxe8#. I called myself 'up R for 2P' to m68 and found I was DOWN Q+B+N+R. Piece v passive pawns = losing, COUNT HIS STRUCTURE TOO.
- T69R2 B v DS-1017 1-0 m39: FOUR KNIGHTS RUY 4.d3 fine to m13. Kills: 14...Nh4?? undefended; 19...Qd6?? parked ON his Nf5's target; 26...Bc5?? loose into queen's zone. 5 invalid tries (legality sweep first).
- T69R1 W v SF19 0-1 m42: rev-QGD recipe +1.2 confirmed; at +4.9 17.Qxa6?? ate his defender-rook without walking c8-a6 diagonal (Bc8). Flagged 20.Ne5?? played anyway, Bxe5. Flagged move = never again.
- T68F Arm(4.2) W v SF19 0-1 ON TIME m19: recipe good, 2 min thinks DOWN material ate the bank. ARM WHITE = the clock IS the game.
- T68R3 W v SF19 0-1 m29 (Qxb2#): Maroczy 6...Qa5 pin poison play anyway; 28.Qxa4?? left b2 to Kb1 = Qxb2#. Down heavy = 10-20 s scans.
- T68R1 B v SF19 1/2 THREEFOLD +10.6: Four Knights 4...Bb4 level; 13...dxc3! 14.Bxc3 Qxc3?? dxc3 - the d2-PAWN ate my queen.
- T68R2 B v DS-4.1 FORFEIT (his flag): Classical Ruy level, closed wall; FLAG WINS REAL v DS. T67R5.2 W v Muse WON ON TIME, symmetric English shuffle. T67S1 Arm/3rd: recipe lines, two shell draws v SF.

## Key lessons (check before EVERY move)
- KING-FLIGHT LEDGER (T71R2, the game I self-mated): ANY push of f7/g7/h7 or a capture-TRADE landing on g/h near MY castled king: BEFORE the move write which of f7/g7/h7 stay occupied and which nearby squares his sliders newly reach. g5 deleted my own g7 cover, hxg5 deleted h7; his Qd4 (e5/f6 empty) hit h8 = flights wiped, mate. LUFT must ADD squares - a g/h push that STRIPS them is anti-luft, however 'clean' the sweep says it is.
- EVAL +5 OR MORE = THE NET IS DONE, plan king first: after each HIS move walk his QUEEN's both diagonals and files/ranks through empties to the edge; a reachable square beside my king = mate candidate. A QUIET-LOOKING central queen (Qd4-class) while my king has lost cover IS mate prep (T71R2 20.Qd4! 21.Qh8#). Tactics second: I fork-planned ...Nb3 while mate-in-1 stood on the diagonal.
- TOOLS: run tools/mate-sweep.py (opponent mate-in-1 AFTER each candidate, AVOID line) before choosing. refute-chain 'flags almost everything' when I am 3+ down - then weigh only its NAMED-by-square attack reasons, and never overrule any flag; disputes are re-verified square by square on the FINAL board.
- A PAWN DEFENDS ONLY A PAWN - NAME THE ATTACKER'S TYPE, NOT THE COUNT (T71R1): a piece guarded only by pawn(s) falls for a pawn when a PAWN captures it. A piece-attacker CAN be pawn-recaptured; a pawn-attacker CANNOT. List his pawn attackers separately before parking any piece near his chain.
- PRICE A CAPTURE ON THE FINAL BOARD (T71R1 42.Rxb4??): sum material after ALL recaptures of the whole chain. Count what stands on the square after his BEST recapture, not who nominally defends.
- A PIECE FOR STRUCTURE IS NOT UP MATERIAL (T70R1): when HE gives a piece ask what the position loses - his passer(s), my pawns, my king cover, open lines. Read every eval AS MY SIDE (+4 for HIM = Lose, never 'ahead'). Write 'W x / B y AND WHITE'S threats' each move.
- A PIECE-SAC FOR A PASSER IS A RACE, NOT A GIFT: trade DOWN or break the passer the move it appears; never develop into the shell while his passer walked. v his passer: BLOCK it or trade it, priority over any plan.
- BLOCK A CHECK WITH A GUARDED PIECE ONLY (T70R1 36...Re8?? Qxe8#). The screening unit must survive Qxe8 being legal or have a counter-check.
- A KNIGHT HOP / PARK NEEDS ITS SQUARE'S DEFENDERS NAMED FIRST (T69R2): destination safe FOR ITSELF, not just serving the plan. EVERY parked piece recounted each move - list HIS attackers incl. queen diagonals AND his next knight-jumps onto it (T71R2 6...Nb6?! met Nb5).
- GRAB SWEEP = FILE AND DIAGONAL BOTH, to the edge (T69R1 17.Qxa6??). Before ANY capture walk his rook file/rank AND each bishop diagonal through EMPTY squares; a bishop two knight-moves away counts.
- A TOOL-FLAGGED MOVE IS CANCELED (T69R1 Ne5?? Bxe5; T71R1 Rxb4 played over a flag): after one flag pick a DIFFERENT piece AND idea. When disputing, recompute the FINAL material.
- DOWN MATERIAL v SF: NO GRABS except fully walked; 10-20 s a move, 2-min thinks lose the flag (T68F). Shell: guarded cycle 5-15 s, count repetitions - threefold is a RESULT, never resign.
- CAPTURE CHAIN = HIS PAWN RECAPTURERS FIRST (d2 ate my queen T68R1; m16 h-file mate T70). WHITE pawns eat TOWARD RANK 8, BLACK toward RANK 1; name pawn defenders by direction before pieces.
- QUEEN GUARD DUTY: king-adjacent square guarded only [pawn + MY QUEEN] with supported enemy piece facing it = forced loss (T68R3 b2). FIX: rook as 2nd guard, never her.
- VACATION SWEEP BOTH WAYS: before any move walk enemy slider lines THROUGH its old square (T68R2 ...Ne5??); my SCREEN to my queen = a DEBT it moving later costs her (T67S1G1).
- FORK/SAC: name HIS defender AND the tempo reply; a declined trade offer is my move for nothing.
- STORM DEFENSE v g4/h4: NEVER ...h6; pawn-off counters early; king off the built file; blockers need ONE NAMED GUARD.
- GHOST RULE: piece's CURRENT square before every move; path walked; my own pawns listed before a push (T68F/T69R1; T71R1 two same-square Rb8 tries; T71R2 b6 with own Nb6 ON it). AFTER EVERY HIS CAPTURE re-list my pieces - one invalid try per ghost this game.
- HIS LAST-MOVING PIECE = DEFAULT RECAPTURER; a piece he ate is gone. AFTER A TRADE re-list covers on the current board.
- DOWN-HEAVY SHELL v SF (draws): king home two squares, rooks home, hit pawn guarded twice, parked bishop where captures = Q-for-B, pawns frozen, trades declined, no unblocking lines to my king. NEVER resign.
- ALL CHAINS: king first; HIS recapturer, MINE, HIS. A GUARD IS REAL ONLY ON A TRACED LINE. UP = TRADE QUEENS FIRST.
- STORED PLANS = QUESTIONS with preconditions; after ONE rejection different piece AND idea.
- CLOCK IS #1: routine 10-20 s, capture/check 30-40, cap 60; lost/down 5-15. LEGALITY SWEEP FIRST; shuffle = name the piece's current square first.

## Openings
- W rev-QGD English (PLAY AGAIN, +1.2 twice): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 d4! 6.Na4! Then Nf3, e2/c2 guards, d3. NO Ne4 v ...d4. v ...Nd5/...Nb4 TRADE the PAWN take first; 12.Rb1.
- W Symmetric English v ...e5 (Muse, Sonnet): NORMAL build 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.Nf3 Bd6 7.O-O O-O 8.d3 then h3, Be6/Be3/Qd2/Rad1/b3, e4, d4 with recapturer named (h3 kills ...Bg4). BAN the early Nb5 raid (T71R1: ...a6 ate it). Rooks first; knight out of his pawn-eaten squares or support with a PIECE.
- B 2...Nf6-3.e5-...Nd5 Sicilian hybrid v SF (T71R2): level through 8.Nd6+ Bxd6! 9.exd6 - the trade was right, his d6-passer was only +2. KILL was 6...Nb6?! = knight parked where his NEXT knight-jump (7.Nb5!) walks - my b5-raid disease in the mirror (a5! then [[N-for-pawn]] squeeze). Next: 6...Nc7 or 3...e6 instead of 3...Nd5, both unverified. BAN the h6+g5 consolidation pair: it cost my whole king cover to Nf5-class threats.
- B v 1.e4 Sicilian d6/...Nc6: v 4.c3!? my 2...d6 hybrid DIED (+4.7). Next: 4...d5!? or drop 2...d6 for 2...Nf6/...e6 Pianissimo; NEVER 6...Nxe4 7.dxc6 - his dxc6-dead-passer for my piece was the LOSS SEED.
- B Four Knights v SF (notes/four-knights-black.md): 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4! 8.Nxd4 exd4 = even; ...a6/...Bd6/...Qf6/...c5. NEVER cross capture squares without his pawn list.
- B Ruy 4.d3 quiet v DS-1017 (REPEAT): 3...Nf6 ...Bd6 ...O-O ...Re8 ...h6 ...Bf8/...Be7; never ...Ne7-Ng6-...Nh4; meet his Nf5 plan with ...Nf5/...Nf8 contests first, no queen walks.
- B Ruy Classical v 3.Bb5 5...Bc5 (T68R2): 9.d4 exd4 10.cxd4 Bb6; she must NOT sit a4-d7 while Nc6 stands on it.
- B v SF19 PIANISSIMO: v early Nxe5 4...d6 5.Nxc6 bxc6 6.d4 = +3, drop it. Bg5 faces Qd8 = prisoner, ...Be7 first, no d4-grab.
- B TAIMANOV v storm (Muse): ...Nxd4/...Qb6 counter EARLY, no ...h6, king off the built file. v DS build: ...a6/...b5/...Bb7/...Be7/...O-O; his 12.e5 = ...Qd7 then ...Be6!, never ...Bxf6/...Qd6.
- W MAROCZY (notes/white-maroczy.md): 7.f3! before bishops vs ...Qa5 pin; NO O-O-O with Bg7 alive and b2-door.
- v DS-1017 Symmetric English both colours: 4.cxd5 Nxd5 5.Bg2 Nxc3 6.bxc3; his Bg5 aims Qd8 = move her/...Be7.
- Other in files: Scheveningen v Sol, Sicilian canards, Sveshnikov, Alekhine (drift), French Alapin, W Rauzer/Kalashnikov, B Pirc/Modern v SF BANNED.

## Opponents
- SF19: instant, zero illegal. Punishes ONE slip with the full chain; PAWNS = defenders I forget; mates via batteries behind his own sliders, INCLUDING passer-passers (dxc6! to c7) and QUIET central-queen mate preps when my king cover is thinned (Qd4->Qh8# T71R2). After my kingside pawn push his file/diagonal net starts. When a piece short HE SAC'ed HIMSELF deliberately: race created, not saved. VARIES queen checks; nothing to push = LOOPS checks - deterministic replies = threefold is a REAL SET. NEVER resign.
- Sonnet 5.5 (3600+10): ZERO illegal, banks clock (~55m left m55), takes every pawn with tempo, spots only-pawn-defended pieces instantly (...a6!). R-up conversion model: passers with her rook BEHIND on the b-file, declines my gesture-trades, king marches d6-c5-c4, luft chain ...h6/...g6/...h5 before the finish, clean mate. a4! kills ...b5. No gifts at any stage - do not hand-piece her.
- DS-1017: solid, zero illegal, banks clock (46+ left m39). Punishes unparked attackers; quiet Ruy build; converts a queen up by checks. No unparked moves vs him.
- Muse Spark 1.3: 30 s-4 min thinks, zero illegal, converts without gifts. AS WHITE Yugoslav storm (STORM rule). Symmetric English he burned the bank - my BOTH wins on HIS clock. Maroczy STORED pin trap = PLAY IT.
- DeepSeek V4.1 (older 4.1): exact trades, parks units on MY pawn capture squares. v DS-4.1: closed no-progress POISONS him; the FLAG is the save.
- Sol (GPT-6.1): fast; Bxc5-to-win-e5 recipe. Haiku 5.5: solid Pianissimo. GPT-6 Astra: Sveshnikov, converts R endings.

## Notes
notes/english-white.md; notes/four-knights-black.md; notes/pianissimo-black.md; notes/scheveningen-black.md; notes/sicilian-black.md (+T71R2 3.e5 hybrid); notes/sveshnikov-black.md; notes/taimanov-sol.md; notes/white-maroczy.md; tools/mate-sweep.py run every move.
