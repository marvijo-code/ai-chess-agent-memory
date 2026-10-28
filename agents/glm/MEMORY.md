# MEMORY (clocks 900+10; T43+ are 3600+10; Armageddon: W 10 min / B 7:30+odds)

## OUTPUT LAW - BEFORE EVERY SEND
- REPLY = THE REQUESTED JSON OBJECT, NOTHING ELSE (T73R3: 3 prose replies = forfeit; T73R1: illegal e4 x3 = forfeit). No prose/preamble/analysis outside the object; notes go INSIDE the JSON fields or nowhere. An imperfect but legal JSON move ALWAYS beats prose. Verify OBJECT SHAPE first, then legality. After ANY rejected reply: fresh object, DIFFERENT move - never resend or reformat.
- A malformed reply costs a try; 3 = forfeit; every opponent file says 'GLM forfeits'. Write a move only after walking it square by square from the CURRENT board or seeing it in tool output; send full from-square-to-square.

## Record
- T74R1 W v Muse 1-0 ON TIME m51 (her 0:42 left): symmetric English v ...d6 wall LEVEL to m12; crack = 13.d4! exd4 14.Nxd4, then Qd3/Bd2/17.e4, her gifts ...d5??/...Ne5??/...Qd6?? gave a piece (20.dxe6). 30.Rxd4! Q-for-R = +2 pawns - then 31.Qd2?? attacked her rook promising a d1-rook recapture that had ALREADY died on d4 (queen gift; -5). 38.exf6! + 41.Nxb2! clawed to -1; her flag decided, not chess. 5 illegal tries of mine from ghost anxieties.
- T73: both losses 0-1 by MY forfeit with LEVEL chess (R1 v Sonnet m14: e4 blocked by my own Be3, 3 tries; R3 v Muse m15: a3-b4-b5 raid 4x?!). T72R3 B 1/2 threefold from -5 v SF19 (Ncd7??/Nb3??). T72R1 B 0-1 flag (Berlin held; kill = hidden knight + clock). T71R2/R1, T70R1 1-0, T69 x2. T68 Armageddon v Muse/DS = WHITE FLAG WINS; d2-PAWN eats queen (capture direction!).

## Key lessons (check before EVERY move)
- GHOST BOARD = THE RECURRING KILL (T74R1 x2, T73R1, T72R3): AFTER EVERY HIS CAPTURE rebuild BOTH armies from the FEN. Before ANY pawn push name the occupant of destination AND transit squares - my OWN pieces block most (my Be3 sat on e3; my Qd2 sat behind Bd2). tools/inventory.py + pawn-paths.py.
- ATTACK OFFER = CENSUS ATTACKER AND PROMISED RECAPTURER BY SQUARE ON THE CURRENT BOARD (T74R1 31.Qd2?? gave my queen for an Rxd2 recapture by a rook already dead in my own chain; my notes 'priced' ghost moves twice): pieces traded away in MY OWN chains do not recapture in notes. Walk the whole double attack: A attacks X, if YxX then ZxY - all four must be real surviving pieces.
- NO ATTACK OFFERS WHEN THE FLAG IS THE WIN (T74R1): from 30.Rxd4 White banked 25 min; the offer instead of guarded shuffles gave the queen away, cost 40 scramble moves, and a -1 finish did the flag job anyway (she burned 2-4 min tension thinks and flagged). Recipe: guarded shuffles 5-10 s, census counts, decline tactics not provable to the final board, let her clock die.
- TOOL FLAGS CAN BE STALE (T74R1: AVOID cited pieces two moves old; exf6 AVOID omitted that g7 was the SOLE recapturer - knight for pawn in my favor): override ONLY with a manual walk of the CURRENT census pricing the full chain to the last capture; otherwise never overrule a tool flag.
- ONE REJECTION = REDRAW + DIFFERENT PIECE AND IDEA (T73R1 3 tries on one illegal e4; T72R3 10): never resend or reformat; full from-square-to-square only.
- PAWN TOUCHES PIECE = MOVE THE PIECE (T72R3): when HIS pawn attacks my piece, guards change NOTHING - the attacked piece itself moves, never 'reguard' it. tools/pawn-capture-sweep.py before every landing.
- NO COOPERATIVE CHAINS (T72R3): compensation requiring HIM to play a losing move is not compensation - he declines. Every chain step FORCED; price after his BEST reply on the final board.
- PHANTOM ATTACKS (T72R3): trace every claimed attack on the piece's real pattern ('Nb3 attacks a4 and c2' - a b3-knight attacks a1/c1/d2/d4/c5/a5). A NOTE IS NOT A BOARD.
- MINOR CENSUS = THE COUNT (T72R1 hid a KNIGHT behind '7-7 pawns'): after EVERY trade write 'W Q R B N N / B Q R B N N' before pawn comparisons. tools/census.py. An eval verdict I cannot refute by counted pieces is TRUE.
- CLOCK CAP 60 S in 3600+10: long thinks (T72R3 9:26/7:57, T74R1 her 2-4 min) cluster before ?? moves or decide nothing. Routine 5-10 s, tension 15-30 s, deep think 30-60 s MAX, fortress/shuffle 2-5 s.
- DEAD FORTRESS (down material, zero open lines, all guarded): REAL DRAW ENGINE v SF - 3 confirms. Reset answers only with listed shuffles (Kg8/Kh8 class); tools/rep-scan.py counts; take threefold/50-move. NEVER resign.
- KING-FLIGHT LEDGER (T71R2): any f7/g7/h7 push near MY king: write which stay occupied, which sliders newly reach. Eval against me = plan king first.
- TOOLS (run before every move): mate-sweep.py; census.py every move; inventory.py (armies + my loose units + FORMAT reminder); pawn-capture-sweep.py; rep-scan.py; pawn-paths.py (push paths, blockers, pawn-hang AVOIDs).
- A PAWN DEFENDS ONLY A PAWN - NAME THE ATTACKER'S TYPE before parking near his chain; price a capture on the FINAL board after ALL recaptures, his BEST.
- A PIECE FOR STRUCTURE IS NOT UP MATERIAL (T70R1): piece-sac for a passer = RACE - block/trade the passer at once.
- BLOCK A CHECK ONLY WITH A GUARDED PIECE; my SCREEN moving later is a DEBT (T70R1 36...Re8?? Qxe8#).
- KNIGHT HOP/PARK NEEDS ITS SQUARE'S DEFENDERS NAMED FIRST; every parked piece recounted each move.
- GRAB SWEEP = FILE AND BOTH DIAGONALS to the edge. A TOOL-FLAGGED MOVE IS CANCELED (different piece AND idea) - unless census-overridden per the rule above.
- CAPTURE CHAIN = HIS PAWN RECAPTURERS FIRST; white pawns eat toward rank 8, black toward rank 1; HIS last-moving piece = default recapturer. QUEEN GUARD DUTY: king-adjacent square guarded only [pawn+MY QUEEN] with a supported enemy piece facing = forced loss; fix with a ROOK as 2nd guard, never her (T68R3 b2).
- VACATION SWEEP BOTH WAYS: before any move walk enemy slider lines THROUGH its old square. FORK/SAC: name HIS defender AND the tempo reply; a declined trade offer is my move for nothing.
- STORM DEFENSE v g4/h4: NEVER ...h6; king off the built file; blockers need ONE NAMED GUARD. After every my kingside push write the mating net it buys him.
- DOWN-MATERIAL SHELL v SF: king home, rooks home, hit pawns guarded twice, parked bishop where captures = Q-for-B, trades declined, no unblocking lines to my king. NEVER resign.
- ALL CHAINS: king first; HIS recapturer, MINE, HIS. A GUARD IS REAL ONLY ON A TRACED LINE. UP = TRADE QUEENS FIRST. STORED PLANS = QUESTIONS re-derived on the CURRENT board.
- CLOCK IS #1: legality sweep first; shuffle = name the piece's current square first.

## Openings
- W SYMMETRIC ENGLISH (BOTH branches PLAY AGAIN - level v Sonnet and Muse; the wall cracks on d4):
  - v ...d5: 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.Nf3 Nc6 7.O-O Bd6 8.d3 O-O (16 plies), then h3, Be3, Qd2, Rad1. After ...Nd5 13.Nxd5 Bxd5 the e4 break is TWO moves (my Be3 blocks e2-e4): Nd4! Nxd4 Bxd4, or move a bishop off d2 first. BAN the early Nb5 raid; rooks first.
  - v ...d6 wall (T74R1 W on time; T73R3 forfeit to a3-b4-b5 raids): same build through h3/Be3/Qd2/Rad1. BAN a3-b4-b5 (her ...a6/...Na5 holds everything, probes c4, readies ...Nb3 v Qd2). THE CRACK: 13.d4! exd4 14.Nxd4 (level), then ORDER FIX - Qd3 BEFORE Bd2 (queen off d2 frees the bishop; Qd3 also guards c4 against the ...Na5 probe), then e4, guarded by Nc3+Qd3. My Bg2 can NEVER recapture on d5 while my Nf3 blocks g2-f3-e4-d5: name the vacating minor before ANY d5/e6 tactic. Her shell sits quiet unless d4 comes.
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
- Muse Spark 1.3 (BEATEN on time T74R1): the ...d6/...Be7/...Re8/...Qd7/...Rad8/...h6/...Bf8 wall is LEVEL if I shuffle - the winning recipe vs her: 13.d4 crack + guarded 5-10 s shuffles; she spends 2-4 min per tense move, has flagged repeatedly (0:42 left here; earlier 0:10/0:31 self-flags), and takes EVERYTHING offered (one ghost from me kept her alive 50 moves). ZERO tries given when solid. As her White: Yugoslav storm - ...Nxd4/...Qb6 early, no ...h6, king off the built file, blockers named.
- Sonnet 5.5 (3600+10): mirrored my symmetric English, OFFERED the Nd5 trade himself; zero illegal, banks clock, takes every pawn with tempo, spots only-pawn-defended pieces instantly. a4! kills ...b5.
- SF19: instant, zero illegal. Punishes ONE slip through the full chain; pawn-scoops a touched piece; quiet central-queen mate preps. BUT let a threefold happen at +10 once my shell was airtight (T72R3) - never resign; airtight wall + rep-scan.py.
- DS-1017: solid, banks clock; punishes unparked attackers; converts a queen up by checks; reset shuffles; closed no-progress POISONS him, flag is the save. DS-4.1: exact trades; never dispute verdicts without a census.
- Sol (GPT-6.1): fast; Bxc5-to-win-e5 recipe. Haiku 5.5 solid Pianissimo. GPT-6 Astra: Sveshnikov, converts R endings.

## Notes
notes/english-white.md; notes/four-knights-black.md; notes/pianissimo-black.md; notes/scheveningen-black.md; notes/sicilian-black.md; notes/sveshnikov-black.md; notes/taimanov-sol.md; notes/white-maroczy.md; tools/mate-sweep.py, census.py, rep-scan.py, pawn-capture-sweep.py, inventory.py, pawn-paths.py run before every move.
