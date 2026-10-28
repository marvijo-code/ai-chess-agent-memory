# MEMORY (clocks 900+10; T43+ are 3600+10; Armageddon: W 10 min / B 7:30+odds)

## OUTPUT LAW - BEFORE EVERY SEND
- REPLY = THE REQUESTED JSON OBJECT, NOTHING ELSE (T73R3 forfeit, 57 min left, LEVEL position): all 3 tries at m15 were prose analysis ('BEST SO FAR: Rb1...') - refused as non-JSON = forfeit. No prose before/after, no preamble, no analysis outside the object; notes go INSIDE the JSON fields or nowhere. An imperfect but legal JSON move ALWAYS beats prose - the object IS the deliverable; never run out of tries on formatting.
- A malformed reply costs a try; 3 = forfeit. T73 = TWO forfeits in three games, both without a losing chess move (R1 illegal e4 x3, R3 prose x3); every opponent file says 'GLM forfeits'. Verify OBJECT SHAPE first, then move legality. After ANY rejected reply: fresh object, DIFFERENT move - never resend or reformat.

## Record
- T73R3 W v Muse 0-1 FORFEIT m15: symmetric English, his SOLID branch (...d6/...Nc6/...Be7/...Re8/...Be6/...Qd7/...Rad8/...h6/...Bf8, no ...d5). Qd2/Rad1/a3/b4/b5 ALL ?! - the a3-b4-b5 expansion outran piece support; 14...Na5! hit c4 (held by d3: ...Nxc4?? dxc4) and readied ...Nb3 v Qd2; even my final prose forked a GHOST Ra1 (rook went d1 at m11). He burned 10:57 + an illegal try on 13...a6?!. Level chess; the forfeit decided it.
- T73R1 W v Sonnet 0-1 FORFEIT m14: symmetric English LEVEL throughout; 12...Nd5 13.Nxd5 Bxd5, then I played e4 three times - my OWN Be3 blocked e2-e4, the move did not exist. Ghost board; 0 clock pressure; opening not the cause.
- T72R3 B v SF19 1/2 m84 THREEFOLD from -5: 4...Qe7 5...d6 6...Nbd7 = -1 tight; then SELF-KILLED: 13...Ncd7?? (his d4-PAWN ate my e5-knight; the 'equal chain' needed HIM to play Nxe5?? - he declined) and 17...Nb3?? (attacks NOTHING; his c2-PAWN ate it). Shell: Qc6-guards-c5, e5=f6+Be6, Kg8/Kh8, zero my-pawn pushes; threefold at +10. 10 invalid tries.
- T72R1 B v DS-4.1 0-1 ON TIME m50: Berlin 3...a6 fortress held 25+; kills = miscount ('7-7 pawns' hid a KNIGHT) + clock (20:30+7:36 thinks, flagged 0:54). Opening NOT the cause.
- T71R2 B v SF19 0-1 m21 / T71R1 W v Sonnet 0-1 m55: 3.e5-...Nd5 hybrid LEVEL through 9.exd6; 10...h6?!+g5?! emptied my king cover; 20...Nc5?? died on the d4-h8 diagonal. English raid 12.Nb5?! met ...a6! = N-for-P; 42.Rxb4?? priced nominal not final board.
- T70R1 B v SF19 1-0 m37 / T69R1 0-1 / T69R2 W v DS-1017 1-0: 4.c3 Sicilian 6...Nxe4 seed = losing; screen moving = debt (36...Re8?? Qxe8#); DS-1017 Four Knights fine to m13, kills legality (5 invalid).
- T68F/T68R1-3 + T67SF2 v SF/DS/Muse: Arm WHITE = the clock IS the game. d2-PAWN ate my queen (capture direction!). Flag wins v Muse/DS in symmetric shuffles; Maroczy STORED pin trap = PLAY IT (7.f3 first). Classical Ruy closed wall poisoned DS - FLAG WINS REAL.

## Key lessons (check before EVERY move)
- GHOST BOARD = THE RECURRING KILL (T73R1 forfeit; T73R3 even my last analysis forked a ghost Ra1): AFTER EVERY HIS CAPTURE rebuild BOTH armies from the FEN. Before ANY pawn push: name the occupant of the destination AND every intermediate square - my OWN pieces block most (Be3 blocked e2-e4). tools/inventory.py + pawn-paths.py.
- ONE REJECTION = REDRAW + DIFFERENT PIECE AND IDEA (T73R1: 3 tries on the same illegal e4; T72R3: 10): never resend or reformat. Write a move only after walking it square by square from the CURRENT board or seeing it in tool output; send full from-square-to-square.
- PAWN TOUCHES PIECE = MOVE THE PIECE (T72R3): when HIS pawn attacks my piece, guards change NOTHING - the attacked piece itself moves (13...Ned7 was free), never 'reguard' it (13...Ncd7??). tools/pawn-capture-sweep.py before every landing.
- NO COOPERATIVE CHAINS (T72R3): compensation requiring HIM to play a losing move is not compensation - he declines. Every chain step FORCED; price material after his BEST reply on the final board.
- PHANTOM ATTACKS (T72R3): 'Nb3 attacks a4 and c2' - a b3-knight attacks a1/c1/d2/d4/c5/a5, NEITHER. Trace every claimed attack on the real move pattern; my sentence is not evidence.
- MINOR CENSUS = THE COUNT (T72R1 hid a KNIGHT behind '7-7 pawns' for 20 moves): after EVERY trade write 'W Q R B N N / B Q R B N N' before pawn comparisons. tools/census.py. An eval verdict I cannot refute by counted pieces is TRUE.
- CLOCK CAP 60 S in 3600+10: BOTH T72R3 long thinks (9:26, 7:57) sat directly before ?? moves; the 2-5 s shuffle phase held -5 for 40 moves. Routine 5-10 s, tension 15-30 s, one deep think 30-60 s MAX, fortress/shuffle 2-5 s. Long thinks cluster before invalid tries.
- DEAD FORTRESS (down material, zero open lines, all guarded): REAL DRAW ENGINE v SF - 3 confirms. Answer his resets only with listed shuffles (Kg8/Kh8, never g6/c5/g5/b4-class); tools/rep-scan.py counts; take threefold/50-move. NEVER resign.
- KING-FLIGHT LEDGER (T71R2): any f7/g7/h7 push or capture-trade near MY king: write which of f7/g7/h7 stay occupied, which sliders newly reach. LUFT must ADD squares. Eval +5 against me = plan king first; quiet central queen = mate prep.
- TOOLS (all run before every move): mate-sweep.py before choosing; census.py every move; inventory.py re-lists both armies + my loose units + the FORMAT reminder; pawn-capture-sweep.py; rep-scan.py; pawn-paths.py (push paths, blockers, pawn-hang AVOIDs). Never overrule a tool flag.
- A PAWN DEFENDS ONLY A PAWN - NAME THE ATTACKER'S TYPE (T71R1): list his PAWN attackers separately before parking a piece near his chain. PRICE A CAPTURE ON THE FINAL BOARD: after ALL recaptures, his BEST recapture.
- A PIECE FOR STRUCTURE IS NOT UP MATERIAL (T70R1): piece-sac for a passer = RACE - block/trade the passer the move it appears.
- BLOCK A CHECK ONLY WITH A GUARDED PIECE; my SCREEN moving later is a DEBT (T70R1 36...Re8?? Qxe8#).
- KNIGHT HOP/PARK NEEDS ITS SQUARE'S DEFENDERS NAMED FIRST (T69R2, T71R2); every parked piece recounted each move.
- GRAB SWEEP = FILE AND BOTH DIAGONALS to the edge (T69R1 Qxa6??). A TOOL-FLAGGED MOVE IS CANCELED: after one flag pick a DIFFERENT piece AND idea.
- CAPTURE CHAIN = HIS PAWN RECAPTURERS FIRST (d2 ate my queen); white pawns eat toward rank 8, black toward rank 1; HIS last-moving piece = default recapturer; after a TRADE re-list covers. QUEEN GUARD DUTY: king-adjacent square guarded only [pawn+MY QUEEN] with a supported enemy piece facing = forced loss; fix with a ROOK as 2nd guard, never her (T68R3 b2).
- VACATION SWEEP BOTH WAYS: before any move walk enemy slider lines THROUGH its old square. FORK/SAC: name HIS defender AND the tempo reply; a declined trade offer is my move for nothing.
- STORM DEFENSE v g4/h4: NEVER ...h6; king off the built file; blockers need ONE NAMED GUARD. After every my kingside push write the mating net it buys him.
- DOWN-MATERIAL SHELL v SF: king home, rooks home, hit pawns guarded twice, parked bishop where captures = Q-for-B, trades declined, no unblocking lines to my king. NEVER resign.
- ALL CHAINS: king first; HIS recapturer, MINE, HIS. A GUARD IS REAL ONLY ON A TRACED LINE. UP = TRADE QUEENS FIRST. STORED PLANS = QUESTIONS with preconditions - re-derive them on the CURRENT board at execution time.
- CLOCK IS #1: legality sweep first; shuffle = name the piece's current square first.

## Openings
- W SYMMETRIC ENGLISH v ...e5 (PLAY AGAIN - level every time; both T73 losses were forfeits): v ...d5: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.Nf3 Nc6 7.O-O Bd6 8.d3 O-O (16 plies), then h3 ...Be6, Be3 ...Qd7, Qd2 ...Rad8, Rad1. After ...Nd5 13.Nxd5 Bxd5 the e4 break is TWO moves (my Be3 blocks e2-e4): Nd4! Nxd4 Bxd4 or Bd2/Bf4 FIRST, then e4. BAN the early Nb5 raid; rooks first.
- W v the SOLID ...d6 branch (T73R3): same build through 9.h3/Be3; his ...Re8/...Be6/...Qd7/...Rad8/...h6/...Bf8 wall. DO NOT expand a3-b4-b5 (4x?!): his ...a6/...Na5! holds everything, hits c4, readies ...Nb3 v Qd2; the bxa6 and Nd5 replies both cost a pawn (my Bg2 can never recapture on d5 - OWN Nf3 blocks g2-f3-e4-d5). Instead Be3-d2 THEN e2-e4 (f4/Nd5 next), or a4-hold with Rad1/Qd2 done; his 1-10 min thinks + self-flags = the flag is MY win condition. Details notes/english-white.md.
- B Four Knights v 3.Nc3+Nxe5 (T72R3, PLAY AGAIN): 3...Bb4 4.Nxe5 Qe7 5.Nf3 d6 6.Bb5+ Nbd7 7.O-O c6 8.Be2 O-O 9.d3 Bxc3 10.bxc3 = -1, tight. At 13.d4 play 13...Ned7 (move the attacked knight). No Nb3-class jumps without the pawn sweep. Both kills were midgame blunders, not the opening.
- B BERLIN v 3.Bb5 (T72R1, PLAY AGAIN): 3...a6 4.Ba4 d5! 5.exd5 b5 6.Bb3 Nd4 7.c3 Nxb3! 8.Qxb3 = even furniture, wedge a5/b5/c6/Bb7. Plan ...Nf6/...O-O/...Bd6 covers e5 3x; NO knight-parks; ...Nbd7 regroup; block d5 with ...c6 (Bb7 behind).
- W rev-QGD English (+1.2 twice): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 d4! 6.Na4! Then Nf3, e2/c2 guards, d3. NO Ne4 v ...d4. TRADE the PAWN first v ...Nd5/...Nb4; 12.Rb1.
- B v 1.e4 Sicilian d6/...Nc6: v 4.c3!? the 2...d6 hybrid DIED (+4.7); try 4...d5!? or 2...Nf6/...e6 Pianissimo; NEVER 6...Nxe4 7.dxc6. 3.e5-...Nd5 hybrid: level through 9.exd6 BUT BAN h6+g5; next 6...Nc7 or 3...e6.
- B Four Knights v SF 4.Bb5 order (notes/four-knights-black.md): 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4! 8.Nxd4 exd4 = even; never cross capture squares without his pawn list.
- B Ruy 4.d3 quiet v DS-1017 (REPEAT): 3...Nf6 ...Bd6 ...O-O ...Re8 ...h6 ...Bf8/...Be7; never ...Ne7-Ng6-...Nh4; meet his Nf5 plan with ...Nf5/...Nf8 first.
- B Taimanov v storm (Muse): ...Nxd4/...Qb6 EARLY, no ...h6, king off the built file. v DS: ...a6/...b5/...Bb7/...Be7/...O-O; his 12.e5 = ...Qd7 then ...Be6!.
- W MAROCZY (notes/white-maroczy.md): 7.f3! before bishops v ...Qa5 pin; NO O-O-O with Bg7 alive and the b2-door.
- Other in files: Pianissimo, Sveshnikov, Alekhine, French Alapin, Rauzer/Kalashnikov, Pirc/Modern v SF BANNED.

## Opponents
- Sonnet 5.5 (3600+10): mirrored my symmetric English and OFFERED the Nd5 trade himself (T73R1); zero illegal, banks clock, takes every pawn with tempo, spots only-pawn-defended pieces instantly. R-up: passers behind Rb2, K-march, luft first. a4! kills ...b5.
- SF19: instant, zero illegal. Punishes ONE slip through the full chain; pawn-scoops a piece the moment a pawn touches it; quiet central-queen mate preps. BUT at depth 4 he let a threefold happen at +10 once my shell was airtight (T72R3) - never resign; airtight wall + rep-scan.py.
- DS-1017: solid, banks clock; punishes unparked attackers; converts a queen up by checks. DS-4.1 mirror: solid, exact trades; resets with king/bishop/pawn permutations; on material CLEAN - never dispute verdicts without a census; closed no-progress POISONS him, flag is the save.
- Muse Spark 1.3 (beat me T72R2 AND T73R3 - BOTH by MY forfeit, not her chess): as Black English she builds the ...d6/...Be7/...Rad8 wall and just collects forfeits; 30 s-11 min thinks clustered in the shell, 10:57 + an illegal try on ...a6?!; she flagged twice in her own shuffles (T71R4 0:10, T72-3rd 0:31). PLAN: mirror-solid, 5-15 s/move, ZERO tries given - the flag is on HER side. As W: Yugoslav storm - ...Nxd4/...Qb6 early, no ...h6.
- Sol (GPT-6.1): fast; Bxc5-to-win-e5 recipe. Haiku 5.5 solid Pianissimo. GPT-6 Astra: Sveshnikov, converts R endings.

## Notes
notes/english-white.md; notes/four-knights-black.md; notes/pianissimo-black.md; notes/scheveningen-black.md; notes/sicilian-black.md; notes/sveshnikov-black.md; notes/taimanov-sol.md; notes/white-maroczy.md; tools/mate-sweep.py, census.py, rep-scan.py, pawn-capture-sweep.py, inventory.py, pawn-paths.py run before every move.
