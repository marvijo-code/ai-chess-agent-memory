# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T66F B v Stockfish 19: L 1-0 m40 flag. Advance h5/Bh7, 11...O-O?! into Ne2/Nf4/g4/Rg1, Qb6 drift, 23...Nf5 24.gxf5 break. Burned 2-4 min while +3 to +10 down, flagged 0:40 vs 66min. 0 illegal.
- T66SF2G1 W DeepSeek V4.1 Flash: W 0-1 m40 Qa1#. Advance Caro Bf5/e6, h5/Bh7 dodge, Bxb4/a5/Qc7 hold, Rc7/Ra7 won Ba6, Rxc6/Qxf4 finish.
- T66R3 B v Stockfish 19: L 0-1 m38 flag. Advance Caro Bf5/e6/Nd7/Ne7/Bg6/Nf5/Bxf5/Be7/O-O/c5. 13.g4 Bg6 14.f5! exf5 15.gxf5 Bxf5 won piece. Down +7-8 flagged after 2-4 min defends. 0 illegal.
- T66R2 W v GLM 5.3 Flash: W 1-0 m17 Qxh7#. Taimanov. g4/h4/g5 break, hxg5+ opened h-file, Qh2 doubled, Bxg5 left N alone, mate covered by Rh1.
- T66R1 W v DeepSeek V4.1 Flash: D 1/2-1/2 m67 flag draw. Caro. 24.Re4?? Qxc4 dropped Q through own Bd4 screen. Held down Q 40+ moves to RR vs bare K flag.
- T64R1 W v Stockfish 19: D 1/2-1/2 m37 threefold. Yugoslav. 11.Bd4 over Bc4?, 12.Bc5! vs e5, 13.Ba3? Qb6, 14.Rb1?? Nxc3 e4! Bxf8 Bxc3+ bxc3 Qxb1+.
- T63R1 B v DeepSeek 1017: W 0-1 m54 Rh4#. English 1.c4 e5. Exchange up after Nxa8/Qxa8, won via Re6/Bxb7, Be8 blockade, a-passer, Q+R mate.
- T63F W v Stockfish 19: L 0-1 m18 Bxc3#. Yugoslav bxc6! line. O-O-O into Bf5/Qc7/Rfb8, Qc1? met Rxb2+ Ka1 Rb7+ c3 Qxc3 Bxc3#. 0 illegal.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: walk piece, actual square, occupant, destination, path. After 1 rejection pick different piece/idea; 3 rejects = forfeit. Zero illegal; keep it.
- DESTINATION SWEEP EVERY move, quiet included: enemy pawn captures first, then knights, bishop/rook/queen rays, king captures. Development does not make a square safe.
- MOVER ABANDONS A GUARD: name what left and who hits it now. Do not hold triple-attacked pawn with loose pieces.
- OWN SCREEN KILLS BATTERIES: trace guard through own men square by square. A piece behind own bishop/pawn/knight guards nothing. Same as Nd2 blocks Qd1-d3, Be3 blocks Re1-e4.
- ADVANCE Bg6 DIES TO g4/f5: Bg6 + e6/d5/c6 chain, White f4/g4 then f5 hits e6+g6 together. exf5 gxf5 traps B, Bxf5 Rxf5 wins piece. Before ...Nf5/Bg6/...c5 with f4 on board prefer ...f6/...h5 or keep Bf5 mobile; never park Bg6 vs coming f5, never ...c5 that leaves d5 held by e6 only.
- CARO ADVANCE h5/Bh7 DODGE: h5 met b4/g4 idea, Bh7 dodged Nh4 fork and f5 double-hit. Keep Nf5/Bg6 guarded, d5 x2, no early ...c5 into clamp.
- NO O-O INTO Ne2/Nf4/g4 STORM: vs Bd3/Ne2/Nf4 + g4/Rg1 plan, 11...O-O?! marked ?! and eval went +0.3 to +1.4 to +2.9. Keep K central, delay O-O, trade Bxd3 or break c5 first, tuck Kh8 BEFORE g4 if committed. Never follow with g6 + Qb6/Qc7 drift that invites Nhg5/a4 with tempo.
- Rg1 + g4 KILLS Nf5 BLOCK: with Rg1 on g-file, ...Nf5 allows gxf5 opening file with Ngf3+/Qxh5 coming. 23...Nf5 24.gxf5 gxf5 25.Ngf3+ jumped +5.5 to +9.7. Before any ...Nf5 with Rg1/Bg5/Ne5 live list gxf5 recapture and file checks; answer g4 with f6/Kh8 first, not a loose N.
- CARO ADVANCE Bxb4 PUNISH: b4/c4 push left b-pawn loose, Bxb4 free with a5+Qc7 hold. Kept d5 x2 throughout, never ...c5 into clamp.
- BA6 TRAP: Ba6 hit Rc8, Rc7 stepped off, Ra7 won Ba6. b6/b5 held c6/d5, Qb8/Rc7 cover escapes.
- UP EXCHANGE FINISH: Rxc6 won N hitting Q, then Qxf4 Qxf3 Qxe2 Qxd2 Qxc5 to Qa1# squeeze. Rc2 cut rank, avoid stalemate.
- CARO Qc4 DANCE IS LOOSE: keep Q off c4 while Qb6/Qb4/Be7 live. Meet c5 with guards on d4, no Rab1/Qe3 drift.
- YUGOSLAV d5 BREAK + B-FILE RULE: after exd5 Nxd5 Nxc6 Black plays bxc6 to keep d5 and open b-file. Bd4 guards c3 and is fix over Bc4. After e5 Bc5 escapes with tempo on f8. BANS after bxc6: Bc4, b3, O-O-O, Ba3, Rb1. Before Ba3/Rb1 list Nxc3 plus e4 opening Bg7 to c3, Qb6/Rb8 hits on b2, and Bxc3+ bxc3 Qxb1+ idea. Rb1 on b-file invites Qxb1+.
- Nxc3 + e4 PATTERN: Qxc3 is right recapture but e4 opens g7-c3 and hits f3/d3. Do not assume consolidation; after e4 keep f3 covered, expect Bxc3+ sac, keep rook off b1.
- NEVER CASTLE LONG INTO OPEN B-FILE: bxc6 removed b7 so Rb8/Qc7/Qb6/Bg7 see b2. O-O-O went losing after Bf5 then Qc7. With b-file open keep K central/short, Bd4/Be2, block c2, contest b-file first. Needs b2 x2 guarded and c2 covered.
- Qc1 DOES NOT HOLD b2 vs SAC: K-only guard loses to Rxb2+ Ka1 Rb7+ c3 Qxc3+ Qxc3 Bxc3#. Before Qc1 count Rxb2+ Kxb2 Qb6+/Qc7+, Rxa2+ ideas, Bg7 x-ray on b2, a2 loose.
- TAIMANOV g4-h4-g5 STORM: vs h6 + Kh8 + Bb7 + Rc8 shell, g4 gains space, h4 supports g5, g5 kicks Nf6, hxg5+ opened h-file with tempo, Qh2 doubles on pinned Nh7. Bxg5 grabs but leaves h7 to N alone; Qxh7 mate when Rh1 covers. Do not play g5 before h-file and Qh2 idea ready; keep Kb1 off c-file first.
- TRAPPED CORNER KNIGHT: after Nbc7/Nxa8, Ne7 held f5/d5 and Q+d5 held escapes. Qxa8 recovered. Centralize, cover escapes, take it.
- FREE UNIT FIRST, THEN CONSOLIDATE: take only after sweep, recount material, rescan loose units.
- UP MATERIAL = BLOCKADE + PASSER: keep blockader on, push passer with support, 5-15 s moves.
- DOWN HUGE CAN DRAW VS FLAGGABLE OPP: shell Kf1/Kg1/Kf2 holds f2/g2, Rf2/Rd2/Re2 2nd rank, Be5/Bd4 central, Ng3 blocks Qh2+, NO pawn pushes. Seek Rxe5 Bxe5 Q-for-R cuts, BxN/KxN freebies. Never resign; up clock force checks, 10-30 s moves, let him flag.
- DOWN HUGE v SF CAN DRAW: K behind f2/f3/g2, rooks covering, no pawn pushes, no open files, repeat same shell. Model down Q vs R+B at +11: Bc2 blockades passer, Kg3 holds f3/g2/h2, Kf2 behind f3, invite Qc5+/Qg5+/Qd2+ for Kg3/Kf2 threefold.
- LOST SHELL = 5-10 S MOVES, HARD CAP 60: T66R3 burned 3:30/4:34/4:27/4:11/3:10 at +7-8 then flagged; T66F burned 2:58/3:39/2:21/2:23/3:11/3:01/4:02/3:50/3:07 at +3 to +10 then flagged 0:40 vs 66min. Down huge vs SF never 2-min defends; shuffle Nc6/d4 + Qd7/d5 + Rg7/f7 + Ba7, invite repeats, save clock.
- Q+R v bare K finisher: drive to edge with defended checks. Rook check seals. Check flights first.
- MATERIAL FROM BOARD EVERY move; after every trade recount guards. Equal trades preserve deficit.
- CLOCK: routine 10-20 s, capture/check 30-40 s, hard cap 60 s; up material 5-15 s; under 5 min 3-5 s. Lost shell 5-10 s, never think. Time goes on destination list, never narrative.

## Openings
- B vs English: 1.c4 e5 2.Nc3 Nc6 3.g3 Nf6. Ideas: Bb6 keeps diagonal after Be3, Be6 hits c4, Re8 contests, Na5 hits c4, e4 hits Nf3/d3, c5 hits Nd4, Bd7/Qb8/Qc7 hold. BANS pending check: c5, Bf5, Nce7 do not auto-repeat.
- B vs Advance Caro: 1.e4 c6 2.d4 d5 3.e5. Ideas: Bf5 e6 Nd7 Ne7 Bg6 Nf5 Be7 O-O. BANS: ...c5 with Bg6 vs f4/g4 into f5!, ...exf5 into gxf5, ...Bxf5 into Rxf5. Prefer ...f6/...h5 vs f4, keep d5 x2.
- W Caro Classical: 1.e4 c6 2.d4 d5 3.Nc3. Ideas: Bd3 BxB QxB, Bf4, O-O, Rfe1, hold d4 vs c5, no Rab1/Qc4 drift. BAN: Re4 through Bd4 screen into Qxc4.
- W vs Dragon Yugoslav: 1.e4 c5 2.Nf3 Nc6 3.d4. Ideas: exd5 Nxd5 Nxc6 bxc6 expected; fix Bd4 then Bc5 vs e5 with tempo. BANS: Bc4, b3, O-O-O, Ba3, Rb1 while Qb6/Rb8 live. Guard e3/b2/c2.
- W vs Taimanov: 1.e4 c5 2.Nf3 e6 3.d4 cxd4. Ideas: Be3 f3 Qd2 Bd3 O-O-O Kb1 g4 h4 g5 Qh2 plan vs h6/Kh8/Nh7. Keep d4 guarded, meet Nd5 defense to e5 with pieces.

## Opponents
- GLM 5.3 Flash: Taimanov e6/a6/b5/Bb7/Nf6/Be7/O-O/Rc8, kingside h6/Kh8/Bb7/Nh7/Bxg5 loose. English g3. Hangs queen/rooks to plain captures, 1 illegal, 10-90 s thinks, banks clock then drifts. Take free units after sweep, trade queens when up, luft first. Never push rim knight to h4 without exits.
- DeepSeek V4.1 Flash 1017: English g3/Bg2/Nf3/d3/Be3/Qd2/Rfe1, queenside N play, e5/e5 breaks, f4/h4/h5 pushes. Caro Bf5/Bg6/Bh7/Nd7/e6/Ngf6/Be7/O-O plus c5, Qb6/Qb4/Qc7/Qc5 dance; b4/c4 leaves b-pawn loose, Ba6 walks into Rc7/Ra7, Nxc6?? hangs to Rxc6 hitting Q. Converts Q-up but flags low. Keep every unit guarded, blockade passers. Fight on down material, keep shell, force moves.
- Stockfish 19: punished 11.Bc4 with Nxe3/Rb8/Qa5/Qxc3, O-O-O with Bf5/Qc7/Rfb8/Rxb2+, Ba3/Rb1 with Nxc3/e4/Bxc3+/Qxb1+. Advance: f4/g4/f5! kills Bg6/e6, gxf5 wins B, Rxf5 wins R; Ne2/Nf4/g4/Rg1 kills O-O + ...Nf5. Plays bxc6 to keep d5 and open b-file, e5+e4 to open Bg7. No gifts, castle early but never long into open b-file, guard e3/b2/c2. Down huge keep Bc2 + Kf2/Kg3 shell for repeat.

## Notes
- notes/caro-black.md - Advance Caro Black loss vs SF: Bg6 g4/f5 break, clock flag.
- notes/english-e5-black.md - English e5 Black win: setup, flagged moves, conversion.
- notes/dragon-yugoslav-white.md - Yugoslav draws + loss vs SF: bxc6/b-file, Bd4/Bc5 fix, bans, Nxc3/e4 and Rxb2 tactics.
- notes/caro-white.md - Caro draw: h4-h5 squeeze, Qc4/Re4 screen blunder, down-Q shell to flag draw.
- notes/taimanov-white.md - Taimanov g4 storm win vs GLM: Kb1, h-file opening, Qh2 mate.
