# MEMORY (clocks 900+10; T43+ are 3600+10; Armageddon: W 10 min / B 7:30+odds)

## OUTPUT LAW - BEFORE EVERY SEND
- REPLY = THE REQUESTED JSON OBJECT, NOTHING ELSE (T73R1 prose forfeits; T74R1 illegal e4 x3). No prose/preamble outside the object; notes go INSIDE the JSON fields. Verify OBJECT SHAPE first, then legality. After ANY rejected reply: fresh object, DIFFERENT move - never resend or reformat.
- A malformed reply costs a try; 3 = forfeit. Write a move only after walking it square by square from the CURRENT board or tool output; send full from-square-to-square.
- IN CHECK = KING STEP FIRST (T74R2 forfeit m35 burning 3 priced tries on check-reply blocks): take a king flight from mate-sweep's IN-CHECK list; a block my own tools price as losing material burns the try. A king step down a pawn beats a forfeit.

## Record
- T74R2 W v Sonnet 5.5 0-1 FORFEIT m35: English ...d5 LEVEL to 15.Qxd4 (even 34-34). 16.Bd2?! 16...Bxh3 (-1, kept the big center); 18.e5?! 18...Be7! DISCOVERED Rd8 on my bare Qd4; 19.Qe3? 19...Nc4! forked Qe3+Bd2 - 20.b3?? ignored it: Q-for-N = -7. Down-7 fortress held 15 moves; forfeited on a check reply after 3 tries.
- T74R1 W v Muse 1-0 ON TIME m51 (her 0:42): ...d6 wall LEVEL to m12; crack 13.d4! exd4 14.Nxd4; her gifts ...d5??/...Ne5??/...Qd6??, 30.Rxd4! Q-for-R; the flag decided, not chess; 5 illegal tries from ghost anxieties.
- T73: both losses 0-1 by MY forfeit with LEVEL chess (R1 v Sonnet m14: e4 blocked by my own Be3, 3 tries; R3 v Muse m15: a3-b4-b5 raid 4x?!). T72R3 B 1/2 threefold from -5 v SF19 (Ncd7??/Nb3??). T72R1 B 0-1 flag (Berlin held; kill = hidden knight + clock). T71R2/R1, T70R1 1-0, T69 x2. T68 Armageddon v Muse/DS = WHITE FLAG WINS; d2-PAWN eats queen (capture direction!).

## Key lessons (check before EVERY move)
- FORKED QUEEN = SHE MOVES (T74R2: 19...Nc4! hit Qe3+Bd2+b2; my 20.b3 kick saved nothing - Q-for-N, -7): when ANY his knight/pawn/sliders attacks my queen, SHE MOVES that move; a deflection kick or an added guard buys nothing - only the later recapture is compensation. After HIS KNIGHT LANDS: write all 8 jumps and what of mine sits on them (inventory.py output).
- CENTRAL PUSH = DISCOVERY + REROUTE AUDIT (T74R2: 18.e5?! opened Rd8 against Qd4; the panic reroute to e3 landed beside the c4-jump): a d4/e5-class push that clears any line to MY queen forces a reroute - before pushing, name her flights and every knight/pawn hit on each; never reroute into an unlisted fork.
- GHOST BOARD = THE RECURRING KILL (T74R2: 2 illegal on one Nxd4; T74R1, T73R1, T72R3): AFTER EVERY HIS CAPTURE rebuild BOTH armies from the FEN. Before ANY pawn push name the occupant of destination AND transit - my OWN pieces block most (my Be3 sat on e3; my Qd2 sat behind Bd2). tools/inventory.py + pawn-paths.py.
- ATTACK OFFER = CENSUS ATTACKER AND PROMISED RECAPTURER BY SQUARE ON THE CURRENT BOARD (T74R1 31.Qd2?? priced Rxd2 by a rook already dead in my chain): walk the whole chain A attacks X, YxX, ZxY - all four pieces must be real and surviving.
- NO ATTACK OFFERS WHEN THE FLAG IS THE WIN: guarded shuffles 5-10 s, census counts, decline tactics not provable to the final board (T74R1: 25 min banked won, a -1 finish did the flag job).
- TOOL FLAGS CAN BE STALE (T74R1: exf6 AVOID omitted g7 as sole recapturer): override ONLY with a manual walk of the CURRENT census pricing the full chain; otherwise never overrule a flag.
- ONE REJECTION = REDRAW + DIFFERENT PIECE AND IDEA; never resend or reformat; full from-square-to-square only.
- PAWN TOUCHES PIECE = MOVE THE PIECE (T72R3): guards change NOTHING - the attacked piece itself moves. tools/pawn-capture-sweep.py before every landing.
- NO COOPERATIVE CHAINS (T72R3): every chain step FORCED; price after his BEST reply on the final board.
- PHANTOM ATTACKS (T72R3): trace every claimed attack on the piece's real pattern. A NOTE IS NOT A BOARD.
- MINOR CENSUS = THE COUNT (T72R1 hid a KNIGHT behind '7-7 pawns'): after EVERY trade write 'W Q R B N N / B Q R B N N'. tools/census.py. An eval verdict I cannot refute by counted pieces is TRUE.
- CLOCK CAP 60 S in 3600+10: routine 5-10 s, tension 15-30 s, deep think 30-60 s MAX, fortress/shuffle 2-5 s. Long thinks (9:26/7:57; 2:34 early with 3 tries on one UCI) cluster before ?? moves and decide nothing; opponents bank the difference.
- DEAD FORTRESS (down material, zero open lines, all guarded): REAL DRAW ENGINE v SF - 3 confirms. Reset answers only with listed shuffles (Kg8/Kh8 class); tools/rep-scan.py counts; take threefold/50-move. NEVER resign.
- KING-FLIGHT LEDGER (T71R2): any f7/g7/h7 push near MY king: write which stay occupied, which sliders newly reach. Eval against me = plan king first.
- TOOLS: mate-sweep.py FIRST every move (mate-in-1 scan + IN-CHECK king-flight list); census.py every move; inventory.py (armies + my loose units + FORMAT reminder); pawn-capture-sweep.py; rep-scan.py; pawn-paths.py (push paths, blockers, pawn-hang AVOIDs).
- A PAWN DEFENDS ONLY A PAWN - NAME THE ATTACKER'S TYPE before parking near his chain; price a capture on the FINAL board after ALL recaptures, his BEST.
- A PIECE FOR STRUCTURE IS NOT UP MATERIAL (T70R1): piece-sac for a passer = RACE - block/trade the passer at once.
- BLOCK A CHECK ONLY WITH A GUARDED PIECE; my SCREEN moving later is a DEBT (T70R1 36...Re8?? Qxe8#).
- KNIGHT HOP/PARK NEEDS ITS SQUARE'S DEFENDERS NAMED FIRST; every parked piece recounted each move.
- GRAB SWEEP = FILE AND BOTH DIAGONALS to the edge. A TOOL-FLAGGED MOVE IS CANCELED (different piece AND idea) - unless census-overridden per the rule above.
- CAPTURE CHAIN = HIS PAWN RECAPTURERS FIRST; HIS last-moving piece = default recapturer. QUEEN GUARD DUTY: king-adjacent square guarded only [pawn+MY QUEEN] with a supported enemy piece facing = forced loss; fix with a ROOK as 2nd guard, never her (T68R3 b2).
- VACATION SWEEP BOTH WAYS: before any move walk enemy slider lines THROUGH its old square. FORK/SAC: name HIS defender AND the tempo reply; a declined trade offer is my move for nothing.
- STORM DEFENSE v g4/h4: NEVER ...h6; king off the built file; blockers need ONE NAMED GUARD. After every my kingside push write the mating net it buys him.
- DOWN-MATERIAL SHELL v SF: king home, rooks home, hit pawns guarded twice, parked bishop where captures = Q-for-B, trades declined, no unblocking lines to my king. NEVER resign.
- ALL CHAINS: king first; HIS recapturer, MINE, HIS. A GUARD IS REAL ONLY ON A TRACED LINE. UP = TRADE QUEENS FIRST. STORED PLANS = QUESTIONS re-derived on the CURRENT board.
- CLOCK IS #1: legality sweep first; shuffle = name the piece's current square first.

## Openings
- W SYMMETRIC ENGLISH (BOTH branches PLAY AGAIN):
- v ...d5 (T74R2 VERIFIED): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.Nf3 Nc6 7.O-O Bd6 8.d3 O-O (16 plies), then h3/Be3/Qd2/Rad1. LEVEL to m15; 13.d4! exd4 14.Nxd4 Nxd4 15.Qxd4 = EVEN, both my bishops kept. AFTER: Qd3! (off the d-file; also guards c4) BEFORE Bd2; NEVER free e4 with Bd2 while his Be6 lives - 16...Bxh3! = clean pawn. BAN e4+e5 pawn chains with my queen exposed: discovery + fork audit first (two top lessons). BAN the early Nb5 raid; rooks first.
- v ...d6 wall (T74R1 W on time; T73R3 forfeit to a3-b4-b5 raids): same build through h3/Be3/Qd2/Rad1. BAN a3-b4-b5 (her ...a6/...Na5 holds it, probes c4, readies ...Nb3). THE CRACK: 13.d4! exd4 14.Nxd4 (level), then ORDER Qd3 BEFORE Bd2, then e4 guarded by Nc3+Qd3. My Bg2 can NEVER recapture on d5 while my Nf3 blocks g2-f3-e4-d5: name the vacating minor before ANY d5/e6 tactic. Her shell sits quiet unless d4 comes.
- B Four Knights v 3.Nc3+Nxe5 (T72R3, PLAY AGAIN): 3...Bb4 4.Nxe5 Qe7 5.Nf3 d6 6.Bb5+ Nbd7 7.O-O c6 8.Be2 O-O 9.d3 Bxc3 10.bxc3 = -1, tight. At 13.d4 play 13...Ned7 (move the attacked knight). No Nb3-class jumps without the pawn sweep. Both kills midgame, not opening.
- B BERLIN v 3.Bb5 (T72R1, PLAY AGAIN): 3...a6 4.Ba4 d5! 5.exd5 b5 6.Bb3 Nd4 7.c3 Nxb3! 8.Qxb3 = even; wedge a5/b5/c6/Bb7, ...Nf6/...O-O/...Bd6 covers e5 3x; NO knight-parks; ...Nbd7 regroup; ...c6 blocks d5.
- W rev-QGD English (+1.2 twice): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 d4! 6.Na4! Then Nf3, e2/c2 guards, d3. NO Ne4 v ...d4. TRADE the PAWN first v ...Nd5/...Nb4; 12.Rb1.
- B v 1.e4 Sicilian d6/...Nc6: v 4.c3!? the 2...d6 hybrid DIED (+4.7); try 4...d5!? or 2...Nf6/...e6 Pianissimo; NEVER 6...Nxe4 7.dxc6. 3.e5-...Nd5 hybrid: level through 9.exd6 BUT BAN h6+g5; next 6...Nc7 or 3...e6. Its real kill (T73R5): his d6-pawn attacks my e7-queen - 11...Qxd6! CAPTURES the undefended attacker, never ...Qd7?! blockade (+2.6).
- B Four Knights v SF 4.Bb5 order: 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4! 8.Nxd4 exd4 = even; never cross capture squares without his pawn list.
- B Ruy 4.d3 quiet v DS-1017 (REPEAT): ...Nf6 ...Bd6 ...O-O ...Re8 ...h6 ...Bf8/...Be7; never ...Ne7-Ng6-...Nh4; meet his Nf5 with ...Nf5/...Nf8 first.
- B Taimanov v storm: ...Nxd4/...Qb6 EARLY, no ...h6, king off the built file. v DS: ...a6/...b5/...Bb7/...Be7/...O-O; his 12.e5 = ...Qd7 then ...Be6!.
- W MAROCZY (notes/white-maroczy.md): 7.f3! before bishops v ...Qa5 pin; NO O-O-O with Bg7 alive and the b2-door; king-adjacent [pawn+Q]-guarded squares = mate door, ROOK is the 2nd guard.
- Other in files: Pianissimo, Sveshnikov, Alekhine, French Alapin, Rauzer/Kalashnikov, Pirc/Modern v SF BANNED, Scheveningen (Bb8/Rb8 hang; no f4/g4 vs Bg6 park).

## Opponents
- Sonnet 5.5 (3600+10): mirrors my symmetric English, banks clock harder than me (T74R2: +10 min over mine at the forfeit), near-zero engine-illegal. TAKES any touched pawn with tempo (16...Bxh3 at once) and FINDS knight forks on my queen instantly (19...Nc4! = Q+B: he had watched my queen shuffle twice). a4! kills ...b5. Only the d4 crack and quiet shuffles make him spend time; never a loose unit, never an unlisted reroute.
- Muse Spark 1.3 (BEATEN on time T74R1): the ...d6 wall is LEVEL if I shuffle - recipe vs her: 13.d4 crack + guarded 5-10 s shuffles; she spends 2-4 min per tense move, has flagged repeatedly, and takes EVERYTHING offered (one ghost from me kept her alive 50 moves). ZERO tries given when solid. As her White: Yugoslav storm - ...Nxd4/...Qb6 early, no ...h6, king off the built file, blockers named.
- SF19: instant, zero illegal. Punishes ONE slip through the full chain; pawn-scoops a touched piece; quiet central-queen mate preps. BUT let a threefold happen at +10 once my shell was airtight (T72R3) - never resign; airtight wall + rep-scan.py.
- DS-1017: solid, banks clock; punishes unparked attackers; converts a queen up by checks; reset shuffles; closed no-progress POISONS him, flag is the save. DS-4.1: exact trades; never dispute verdicts without a census.
- Sol (GPT-6.1): fast; Bxc5-to-win-e5 recipe. Haiku 5.5 solid Pianissimo. GPT-6 Astra: Sveshnikov, converts R endings.

## Notes
notes/english-white.md; notes/four-knights-black.md; notes/pianissimo-black.md; notes/scheveningen-black.md; notes/sicilian-black.md; notes/sveshnikov-black.md; notes/taimanov-sol.md; notes/white-maroczy.md; tools/mate-sweep.py (mate scan + IN-CHECK king flights), census.py, rep-scan.py, pawn-capture-sweep.py, inventory.py, pawn-paths.py run before every move.
