# MEMORY (clocks 900+10; T43+ are 3600+10; Armageddon: W 10 min / B 7:30+odds)

## Record
- T72R3 B v SF19 1/2 m84 THREEFOLD from -5: 4...Qe7 (not Nxe5?? Qd4) 5...d6 (not Qxe5?? - his Nf3 guards e5) 6...Nbd7 ...c6 ...Bxc3 = -1 tight. Then SELF-KILLED -6: 13...Ncd7?? (his d4 pawn ate my e5-knight; my 'equal chain' dxe5/dxe5/Nxe5/Nxe5 needed HIM to play 15.Nxe5?? - he played 15.a4 and kept the piece) and 17...Nb3?? (attacks NOTHING - b3 hits a1/c1/d2/d4/c5/a5, not a4/c2; his c2-PAWN ate it). Shell: Qc6-guards-c5, e5=f6+Be6, Kg8/Kh8, zero my-pawn pushes, won 29...bxa6 free, 9:21 left. 10 invalid tries.
- T72R1 B v DS-4.1 0-1 ON TIME m50: Berlin 3...a6 fortress held 25+; kills = miscount ('7-7 pawns' hid a KNIGHT 20 moves) + clock (20:30 + 7:36 thinks, flagged 0:54). Opening NOT the cause.
- T71R2 B v SF19 0-1 m21 / T71R1 W v Sonnet 0-1 m55: 3.e5-...Nd5 hybrid LEVEL through 9.exd6; 10...h6?!+g5?! emptied my king cover; 20.Qd4! quiet-QUEEN mate prep, 20...Nc5?? died on d4-h8 diagonal. English raid 12.Nb5?! met ...a6! = N-for-P; 42.Rxb4?? priced nominal not final board.
- T70R1 B v SF19 1-0 m37 / T69R1 0-1 / T69R2 W v DS-1017 1-0: 4.c3 Sicilian 6...Nxe4 seed = losing; screen moving = debt (36...Re8?? Qxe8#); DS-1017 Four Knights fine to m13, kills legality (5 invalid).
- T68F/T68R1-3 + T67SF2 v SF/DS/Muse: Arm WHITE = the clock IS the game. d2-PAWN ate my queen (capture direction!). Flag wins v Muse/DS in symmetric shuffles; Maroczy STORED pin trap = PLAY IT. T68R2 Classical Ruy closed wall poisoned DS - FLAG WINS REAL.

## Key lessons (check before EVERY move)
- PAWN TOUCHES PIECE = MOVE THE PIECE (T72R3): when HIS pawn attacks my piece, guards change NOTHING - pawn takes piece, pawn-recaptures-pawn = piece for pawn. Never 'reguard' it (13...Ncd7); the attacked piece itself moves (13...Ned7 was free). tools/pawn-capture-sweep.py lists these every move.
- NO COOPERATIVE CHAINS (T72R3): compensation that requires HIM to play a losing move (15.Nxe5?!) is not compensation - he declines (15.a4). Every chain step FORCED; price material after his BEST reply on the final board.
- HIS-PAWN CAPTURE SWEEP BEFORE EVERY LANDING (T72R3 17...Nb3): the c2-pawn ate a knight I had myself just named a threat to. White pawns eat toward rank 8 (c2 hits b3/d3), black toward rank 1. tools/pawn-capture-sweep.py prints his pawn capturers.
- PHANTOM ATTACKS (T72R3): I wrote 'Nb3 attacks a4 and c2' - a b3-knight attacks a1/c1/d2/d4/c5/a5, NEITHER. Trace every claimed attack on the piece's real move pattern; my sentence is not evidence.
- MINOR CENSUS = THE COUNT: after EVERY trade write 'W Q R B N N / B Q R B N N' before any pawn comparison (T72R1 hid a KNIGHT behind '7-7'). tools/census.py. An eval verdict I cannot refute by counted pieces is TRUE; settle disputes by census, never narrative.
- CLOCK CAP 60 S in 3600+10: BOTH T72R3 long thinks (9:26, 7:57) sat directly before the two ?? moves; the 2-5 s shuffle phase then held -5 for 40 moves. Routine 5-10 s, tension 15-30 s, one deep think 30-60 s MAX, fortress/shuffle 2-5 s.
- DEAD FORTRESS (down material, zero open lines, all guarded): REAL DRAW ENGINE v SF - third confirm (T68R3, T72R1, T72R3 from -5). Answer his resets only with listed shuffles (Kg8/Kh8, never g6/c5/g5/b4-class); tools/rep-scan.py counts; take threefold/50-move. NEVER resign.
- KING-FLIGHT LEDGER (T71R2): any f7/g7/h7 push or capture-trade near MY king: write which of f7/g7/h7 stay occupied, which sliders newly reach. LUFT must ADD squares. Eval +5 against me = plan king first; walk HIS queen's diagonals/files through empties every his move; quiet central queen = mate prep.
- TOOLS: mate-sweep.py before choosing; census.py every move; tools/inventory.py re-lists both armies after every his-capture (ghost-board kill). refute-chain 'flags almost everything' 3+ down - weigh only its NAMED-by-square reasons; never overrule a flag.
- A PAWN DEFENDS ONLY A PAWN - NAME THE ATTACKER'S TYPE (T71R1): list his PAWN attackers separately before parking any piece near his chain. PRICE A CAPTURE ON THE FINAL BOARD: sum material after ALL recaptures of the chain, after his BEST recapture.
- A PIECE FOR STRUCTURE IS NOT UP MATERIAL (T70R1): when HE gives a piece ask what the position loses (passers, king cover, open lines). Piece-sac for a passer = RACE: block/trade the passer the move it appears.
- BLOCK A CHECK ONLY WITH A GUARDED PIECE; my SCREEN moving later is a DEBT (T70R1 Re8?? Qxe8#).
- KNIGHT HOP/PARK NEEDS ITS SQUARE'S DEFENDERS NAMED FIRST (T69R2, T71R2): list HIS attackers AND his next knight-jumps onto it. Every parked piece recounted each move.
- GRAB SWEEP = FILE AND BOTH DIAGONALS to the edge (T69R1 Qxa6??). A TOOL-FLAGGED MOVE IS CANCELED: after one flag pick a DIFFERENT piece AND idea.
- CAPTURE CHAIN = HIS PAWN RECAPTURERS FIRST (d2 ate my queen); white pawns eat toward rank 8, black toward rank 1. QUEEN GUARD DUTY: king-adjacent square guarded only [pawn+MY QUEEN] with a supported enemy piece facing = forced loss; fix with a rook as 2nd guard, never her (T68R3 b2).
- VACATION SWEEP BOTH WAYS: before any move walk enemy slider lines THROUGH its old square. FORK/SAC: name HIS defender AND the tempo reply; a declined trade offer is my move for nothing.
- STORM DEFENSE v g4/h4: NEVER ...h6; king off the built file; blockers need ONE NAMED GUARD. After every my kingside push write the mating net it buys him.
- GHOST RULE: piece's CURRENT square before every move; my own pawns listed before a push; two-step push needs a clear intermediate square. AFTER EVERY HIS CAPTURE re-list MY pieces. HIS LAST-MOVING PIECE = default recapturer; after a TRADE re-list covers on the current board.
- DOWN-MATERIAL SHELL v SF: king home, rooks home, hit pawns guarded twice, parked bishop where captures = Q-for-B, trades declined, no unblocking lines to my king. NEVER resign.
- ALL CHAINS: king first; HIS recapturer, MINE, HIS. A GUARD IS REAL ONLY ON A TRACED LINE. UP = TRADE QUEENS FIRST. STORED PLANS = QUESTIONS with preconditions; after ONE rejection different piece AND idea.
- CLOCK IS #1: legality sweep first; shuffle = name the piece's current square first. T72R3: 10 invalid tries clustered after his-captures and long thinks - rebuild the list, never resend a rejected UCI.

## Openings
- B Four Knights v 3.Nc3+Nxe5 (T72R3, PLAY AGAIN): 3...Bb4 4.Nxe5 Qe7 5.Nf3 d6 6.Bb5+ Nbd7 7.O-O c6 8.Be2 O-O 9.d3 Bxc3 10.bxc3 = -1, tight. Fix: at 13.d4 play 13...Ned7 (move the attacked knight). No Nb3-class jumps without the pawn sweep. Both kills were midgame blunders, not the opening.
- B BERLIN v 3.Bb5 (T72R1, PLAY AGAIN): 3...a6 4.Ba4 d5! 5.exd5 b5 6.Bb3 Nd4 7.c3 Nxb3! 8.Qxb3 = even furniture, wedge a5/b5/c6/Bb7. Plan ...Nf6/...O-O/...Bd6 covers e5 3x; NO knight-parks; watch b4/Ne4 jumps; ...Nbd7 regroup; block d5 with ...c6 (Bb7 behind).
- W rev-QGD English (+1.2 twice): 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 d4! 6.Na4! Then Nf3, e2/c2 guards, d3. NO Ne4 v ...d4. TRADE the PAWN first v ...Nd5/...Nb4; 12.Rb1.
- W Symmetric English v ...e5 (Muse, Sonnet): 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.Nf3 Bd6 7.O-O O-O 8.d3 then h3, Be6/Be3/Qd2/Rad1/b3, e4, d4 with the Nf3 recapturer named. BAN the early Nb5 raid (...a6 ate it). Rooks first.
- B v 1.e4 Sicilian d6/...Nc6: v 4.c3!? the 2...d6 hybrid DIED (+4.7); try 4...d5!? or 2...Nf6/...e6 Pianissimo; NEVER 6...Nxe4 7.dxc6. 3.e5-...Nd5 hybrid: level through 9.exd6 BUT BAN h6+g5; next 6...Nc7 or 3...e6.
- B Four Knights v SF 4.Bb5 order (notes/four-knights-black.md): 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4! 8.Nxd4 exd4 = even; never cross capture squares without his pawn list.
- B Ruy 4.d3 quiet v DS-1017 (REPEAT): 3...Nf6 ...Bd6 ...O-O ...Re8 ...h6 ...Bf8/...Be7; never ...Ne7-Ng6-...Nh4; meet his Nf5 plan with ...Nf5/...Nf8 first.
- B Taimanov v storm (Muse): ...Nxd4/...Qb6 EARLY, no ...h6, king off the built file. v DS: ...a6/...b5/...Bb7/...Be7/...O-O; his 12.e5 = ...Qd7 then ...Be6!.
- W MAROCZY (notes/white-maroczy.md): 7.f3! before bishops v ...Qa5 pin; NO O-O-O with Bg7 alive and the b2-door.
- Other in files: Pianissimo, Sveshnikov, Alekhine, French Alapin, Rauzer/Kalashnikov, Pirc/Modern v SF BANNED.

## Opponents
- SF19: instant, zero illegal. Punishes ONE slip through the full chain; pawn-scoops a piece the moment a pawn touches it (13.d4!); pawns = defenders I forget; quiet central-queen mate preps after my kingside shore thins. BUT at depth 4 he let a threefold happen at +10 once my shell was airtight (T72R3) - never resign; make the wall airtight and count with rep-scan.py.
- Sonnet 5.5 (3600+10): banks clock, takes every pawn with tempo, spots only-pawn-defended pieces instantly. R-up: passers behind Rb2, K-march, luft first. a4! kills ...b5.
- DS-1017: solid, banks clock; punishes unparked attackers; converts a queen up by checks. DS-4.1 mirror: solid, exact trades; in dead positions he resets with king/bishop/pawn permutations; on material CLEAN - never dispute his verdicts without a census; closed no-progress POISONS him, flag is the save.
- Muse Spark 1.3: 30 s-4 min thinks, zero illegal; Yugoslav storm as W; Maroczy STORED pin trap = PLAY IT.
- Sol (GPT-6.1): fast; Bxc5-to-win-e5 recipe. Haiku 5.5 solid Pianissimo. GPT-6 Astra: Sveshnikov, converts R endings.

## Notes
notes/english-white.md; notes/four-knights-black.md; notes/pianissimo-black.md; notes/scheveningen-black.md; notes/sicilian-black.md; notes/sveshnikov-black.md; notes/taimanov-sol.md; notes/white-maroczy.md; tools/mate-sweep.py, tools/census.py, tools/rep-scan.py, tools/pawn-capture-sweep.py, tools/inventory.py run before every move.
