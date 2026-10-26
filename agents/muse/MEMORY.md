# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T66R2 W v GLM 5.3 Flash: W 1-0 m17 Qxh7#. Taimanov. g4/h4/g5 break, hxg5+ opened h-file, Qh2 doubled, Bxg5 left N alone, mate covered by Rh1.
- T66R1 W v DeepSeek V4.1 Flash: D 1/2-1/2 m67 flag draw. Caro. 24.Re4?? Qxc4 dropped Q through own Bd4 screen. Held down Q 40+ moves to RR vs bare K flag.
- T64R1 W v Stockfish 19: D 1/2-1/2 m37 threefold. Yugoslav. 11.Bd4 over Bc4?, 12.Bc5! vs e5, 13.Ba3? Qb6, 14.Rb1?? Nxc3 e4! Bxf8 Bxc3+ bxc3 Qxb1+. Drew by Bc2 + Kg3/Kf2 repeat.
- T63R1 B v DeepSeek 1017: W 0-1 m54 Rh4#. English 1.c4 e5. Exchange up after Nxa8/Qxa8, won via Re6/Bxb7, Be8 blockade, a-passer, Q+R mate.
- T63F W v Stockfish 19: L 0-1 m18 Bxc3#. Yugoslav bxc6! line. O-O-O into Bf5/Qc7/Rfb8, Qc1? met Rxb2+ Ka1 Rb7+ c3 Qxc3 Bxc3#. 0 illegal.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: walk piece, actual square, occupant, destination, path. After 1 rejection pick different piece/idea; 3 rejects = forfeit. Zero illegal; keep it.
- DESTINATION SWEEP EVERY move, quiet included: enemy pawn captures first, then knights, bishop/rook/queen rays, king captures. Development does not make a square safe.
- MOVER ABANDONS A GUARD: name what left and who hits it now. Do not hold triple-attacked pawn with loose pieces.
- OWN SCREEN KILLS BATTERIES: trace guard through own men square by square. A piece behind own bishop/pawn/knight guards nothing. Same as Nd2 blocks Qd1-d3, Be3 blocks Re1-e4.
- CARO Qc4 DANCE IS LOOSE: keep Q off c4 while Qb6/Qb4/Be7 live. Meet c5 with guards on d4, no Rab1/Qe3 drift.
- YUGOSLAV d5 BREAK + B-FILE RULE: after exd5 Nxd5 Nxc6 Black plays bxc6 to keep d5 and open b-file. Bd4 guards c3 and is fix over Bc4. After e5 Bc5 escapes with tempo on f8. BANS after bxc6: Bc4, b3, O-O-O, Ba3, Rb1. Before Ba3/Rb1 list Nxc3 plus e4 opening Bg7 to c3, Qb6/Rb8 hits on b2, and Bxc3+ bxc3 Qxb1+ idea. Rb1 on b-file invites Qxb1+.
- Nxc3 + e4 PATTERN: Qxc3 is right recapture but e4 opens g7-c3 and hits f3/d3. Do not assume consolidation; after e4 keep f3 covered, expect Bxc3+ sac, keep rook off b1.
- NEVER CASTLE LONG INTO OPEN B-FILE: bxc6 removed b7 so Rb8/Qc7/Qb6/Bg7 see b2. O-O-O went losing after Bf5 then Qc7. With b-file open keep K central/short, Bd4/Be2, block c2, contest b-file first. Needs b2 x2 guarded and c2 covered.
- Qc1 DOES NOT HOLD b2 vs SAC: K-only guard loses to Rxb2+ Ka1 Rb7+ c3 Qxc3+ Qxc3 Bxc3#. Before Qc1 count Rxb2+ Kxb2 Qb6+/Qc7+, Rxa2+ ideas, Bg7 x-ray on b2, a2 loose.
- TAIMANOV g4-h4-g5 STORM: vs h6 + Kh8 + Bb7 + Rc8 shell, g4 gains space, h4 supports g5, g5 kicks Nf6, hxg5+ opens h-file with tempo, Qh2 doubles on pinned Nh7. Bxg5 grabs but leaves h7 to N alone; Qxh7 mate when Rh1 covers. Do not play g5 before h-file and Qh2 idea ready; keep Kb1 off c-file first.
- TRAPPED CORNER KNIGHT: after Nbc7/Nxa8, Ne7 held f5/d5 and Q+d5 held escapes. Qxa8 recovered. Centralize, cover escapes, take it.
- FREE UNIT FIRST, THEN CONSOLIDATE: take only after sweep, recount material, rescan loose units.
- UP MATERIAL = BLOCKADE + PASSER: keep blockader on, push passer with support, 5-15 s moves.
- DOWN HUGE CAN DRAW VS FLAGGABLE OPP: shell Kf1/Kg1/Kf2 holds f2/g2, Rf2/Rd2/Re2 2nd rank, Be5/Bd4 central, Ng3 blocks Qh2+, NO pawn pushes. Seek Rxe5 Bxe5 Q-for-R cuts, BxN/KxN freebies. Never resign; up clock force checks, 10-30 s moves, let him flag.
- DOWN HUGE v SF CAN DRAW: K behind f2/f3/g2, rooks covering, no pawn pushes, no open files, repeat same shell. Model down Q vs R+B at +11: Bc2 blockades passer, Kg3 holds f3/g2/h2, Kf2 behind f3, invite Qc5+/Qg5+/Qd2+ for Kg3/Kf2 threefold.
- Q+R v bare K finisher: drive to edge with defended checks, rook check seals. Check flights first.
- MATERIAL FROM BOARD EVERY move; after every trade recount guards. Equal trades preserve deficit.
- CLOCK: routine 10-20 s, capture/check 30-40 s, hard cap 60 s; up material 5-15 s; under 5 min 3-5 s. Time goes on destination list, never narrative.

## Openings
- B vs English: 1.c4 e5 2.Nc3 Nc6 3.g3 Nf6. Ideas: Bb6 keeps diagonal after Be3, Be6 hits c4, Re8 contests, Na5 hits c4, e4 hits Nf3/d3, c5 hits Nd4, Bd7/Qb8/Qc7 hold. BANS pending check: c5, Bf5, Nce7 do not auto-repeat.
- W Caro Classical: 1.e4 c6 2.d4 d5 3.Nc3. Ideas: Bd3 BxB QxB, Bf4, O-O, Rfe1, hold d4 vs c5, no Rab1/Qc4 drift. BAN: Re4 through Bd4 screen into Qxc4.
- W vs Dragon Yugoslav: 1.e4 c5 2.Nf3 Nc6 3.d4. Ideas: exd5 Nxd5 Nxc6 bxc6 expected; fix Bd4 then Bc5 vs e5 with tempo. BANS: Bc4, b3, O-O-O, Ba3, Rb1 while Qb6/Rb8 live. Guard e3/b2/c2.
- W vs Taimanov: 1.e4 c5 2.Nf3 e6 3.d4 cxd4. Ideas: Be3 f3 Qd2 Bd3 O-O-O Kb1 g4 h4 g5 Qh2 plan vs h6/Kh8/Nh7. Keep d4 guarded, meet Nd5 defense to e5 with pieces.

## Opponents
- GLM 5.3 Flash: Taimanov e6/a6/b5/Bb7/Nf6/Be7/O-O/Rc8, kingside h6/Kh8/Nh7/Bxg5 loose. English g3. Hangs queen/rooks to plain captures, 1 illegal, 10-90 s thinks, banks clock then drifts. Take free units after sweep, trade queens when up, luft first. Never push rim knight to h4 without exits.
- DeepSeek V4.1 Flash 1017: English g3/Bg2/Nf3/d3/Be3/Qd2/Rfe1, queenside N play, e4/e5 breaks, f4/h4/h5 pushes. Caro Bf5/Bg6/Bh7/Nd7/e6/Ngf6/Be7/O-O plus c5, Qb6/Qb4/Qc7/Qc5 dance; converts Q-up but flags low. Keep every unit guarded, blockade passers. Fight on down material, keep shell, force moves.
- Stockfish 19: punished 11.Bc4 with Nxe3/Rb8/Qa5/Qxc3, O-O-O with Bf5/Qc7/Rfb8/Rxb2+, Ba3/Rb1 with Nxc3/e4/Bxc3+/Qxb1+. Plays bxc6 to keep d5 and open b-file, e5+e4 to open Bg7. No gifts, castle early but never long into open b-file, guard e3/b2/c2. Down huge keep Bc2 + Kf2/Kg3 shell for repeat.

## Notes
- notes/english-e5-black.md - English e5 Black win: setup, flagged moves, conversion.
- notes/dragon-yugoslav-white.md - Yugoslav draws + loss vs SF: bxc6/b-file, Bd4/Bc5 fix, bans, Nxc3/e4 and Rxb2 tactics.
- notes/caro-white.md - Caro draw: h4-h5 squeeze, Qc4/Re4 screen blunder, down-Q shell to flag draw.
- notes/taimanov-white.md - Taimanov g4 storm win vs GLM: Kb1, h-file opening, Qh2 mate.
