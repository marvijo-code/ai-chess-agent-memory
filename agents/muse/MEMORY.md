# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T83R1 W vs SF loss 0-1 m19 mate. Dragon Yugoslav Be2?? repeat of T80R1 left Be3 to Nxe3 then Bxd4. Down shell Ka1 Kb1 loop then Bxc3 Qxa2 mate. 0 illegal.
- T82-3rd-AD B vs Flash loss time m20 level. Classical simplify plan good but 55s+ thinks flagged to 0:39. 0 illegal.
- T82-3rd W vs Flash draw threefold m48 level. Classical shell then Rh3 Rh4 loop drew vs bank. Early pushes flagged. 2 illegal.
- T82SF1G1 B vs SF loss forfeit m7 even. FourKnights correct to exd5 then book e4 flagged Nxe5 loss x3 REPEAT. 0 illegal.
- T82R5 W vs Flash win forfeit m39 level. Classical storm then Rd7 Qe4 won on 3 invalid. 0 illegal.
- T82R4 B vs SF loss forfeit m48 down 5. FourKnights correct then Qf6 c5 Ke6 errors then h-run gated. 4 illegal.
- T82R3 W vs Sonnet draw threefold m62 down P. Ruy blockade then Nc5 Ne4 plus Qd1 Qd2 plus Kh1 Kh2 Kg1 loop drew. 3 illegal.
- T82R1 B vs Flash loss forfeit m35 level. English pin then slow shuffle flagged. 1 illegal.
- T81F W vs SF loss forfeit m41 down exchange. Yugoslav Bd4 error then Bxb7 Qxg2 run then Qxc2 gated. 3 illegal.
- T81SF1G1 B vs Sonnet win forfeit m24 level. Breyer shell then exd4 cxd5 break won on tool flood. 0 illegal.
- T81R5 B vs Flash loss forfeit m36 level. Ruy shell then b3 c3 b2 Rxb2 won B then Rb5 c4 fork gated. 2 illegal.
- T81R4 W vs Sonnet loss forfeit m31 down P. Ruy shell then d4 Nxe4 errors then a3 flood gated. 0 illegal.
- T81R3 W vs Flash win forfeit m22 even. English Attack then g5 plus f4 plus hxg3 won on 3 invalid. 1 illegal.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: after 1 reject redraw FEN, pick different piece and idea, never resend stale UCI. 3 rejects forfeit, tool refusal = reject. In check list replies once and send in 5-10s. T79 plus T81 e4 flood plus T81R4 a3 pawn flood x3: after 1 tool refusal NEVER resend same UCI, switch square at once. EXCEPT down 4+ rook ending where every move loses same pawn (T82R4): resend BEST once, 2nd send passes, never cycle 3 losers. EXCEPT FourKnights e4 book false flag (T82SF1G1 3rd repeat): RESEND e4 once, 2nd try d6 keeper, never 3x e4. Castle early. Sweep Nxe3 Bxd5 first or guard Be3 twice.
- TOOL AVOID IS AN ORDER: after one refusal switch piece and idea at once, never resend flagged UCI. DOWN FALSE FLOOD: recount W and B from FEN, move king or rook off ray in ONE try, never burn 3 tries.
- FOUR KNIGHTS ND5 POISON: vs 6.Nd5 play Nxd5 only, never d6 Nxe4. After exd5 play e4 hits Nf3 (e5 vacates so Nxe5 flag FALSE). Then dxc6 exf3 Qxf3 dxc6. c6 has two guards via b7 and d7 so Bxc6 dxc6 safe. T82SF1G1 3rd forfeit repeating T81R1: RESEND e4 once, 2nd try d6 keeper, never 3x e4. Castle early. No Qf6 while Bf4 lives, no c5 while Bf4 lives, no Ke6 while Rh7 lives.
- DRAGON BE2 POISON REPEAT T83R1: vs O-O plus d5 never Be2 holding tension while Be3 loose to Nxe3. Play Nxc6 bxc6 or Nxd5 Qxd5 first. Sweep Nxe3 plus Bxd5 plus Nxg2 before develop. After Nxe3 play Qxe3 at once, never Nxc6 ignoring g2. T80R1 and T83R1 both 10.Be2 lost piece then Bxd4 plus Qa5 plus Rd8 battery won more. Keep Kb1 never Ka1 vs Qa5, guard a2 twice, Bd3 blocks Rd8.
- OPEN QA5 PLUS QXA2 POISON: 4.Qa5 after Nxd4 meets Nc3 tempo. Never Qxa2 under Ra1 to Rxa2. Play Nf6 Nc6 e6, never early queen sortie. If hit retreat at once. T83R1 Qxc3 left a2 so Qxa2 mate: keep Kb1 and a2 twice-held.
- RUY NA5 C5 C6 POISON: 10.c6 chases Nd5 weakens d6, 14.c5 hits Bd4 opens d5, 15.b5 meets c3 doubling. Keep Ne7 Nc6 Bd7 Re8, hold d6 twice, meet d4 exd4 only.
- YUGOSLAV BC4 POISON: T79R4 11.Bc4 abandoned Be3 to Nxe3 won piece, Rb8 Bd8 won game. Never Bc4 Bb3 while Be3 loose. Sweep Nxe3 Bxd5 first or guard Be3 twice. Keep Be2 then f3 then Qd2 then O-O-O order.
- ADVANCE C4 E6 FORK POISON: T80R5 Nd7 onto e6 fork met cxd5 exd5 e6 hitting Nd7 then Ne5 winning c6. Vs c4 resolve dxc4 or cxd5 at once, never retreat onto e-push. Before any Nd7 Nf6 list e6 fork. In check list flights then blocks then captures once.
- ENGLISH BB4 PIN SHELL: T82R1 Bb4 pin met a3 kick to Bc5 then Bd4, b4 space holds. Never Kh8 Nd7 shuffle while clock burns, keep 10-20s keepers. Timeout forfeits like flag.
- CARO CLASSICAL WHITE CLOCK POISON: T79R7 even flagged 0:13. T80R4 shuttle all flagged. T82R5 win but Be3 plus Rd2 plus b3 plus Nd2 plus c3 plus Qc2 plus Qd2 plus Na5 plus dxc5 plus Ne3 all flagged: keep Bd3 Qd3, Kb1 once never Ka1 Kb1, Rg1 Rd1 only, b3 c3 only twice-held, no Rd2 Rd1 Rd3 shuffle. h5 Ne5 Rh3 f4 never 2-4min. Routine 10-20s cap 60. T82-3rd: early pushes flagged but Rh3 Rh4 plus Qd1 Rc2 plus Kb1 shell drew vs bank: low clock 5-10s keepers, invite repeat.
- ITALIAN SHUTTLE SHELL POISON: T79R5 up P flagged on time. Never Nd7 Nf6 loop vs Nf1 g3 h4 f5. Never passive keepers while up. One develop then 10-20s keepers, push d5 c5 once with recapture named.
- ITALIAN BG6 BB8 RB8 POISON: 8.Bg4 9.Bh5 passive vs Be3 d4, 17.Rb8 18.a6 met Bd5 f3 clamp. Contest e-file with Re8 first, Qe7 h6 after, never Rb8 a6 while Bd5 lives.
- NAJDORF E5 TIMING: T78R4 e5 shell burned shuffling Qc8 Qc7 Qb6 plus Re8 Re7 Rd7. Re8 Bd6 Be6 hold e5. Never Nc5 while Be3 loose, never Bf6 gxf6 while Qf3 lives, never queen rook king shuffle.
- DRAGON D5 QA5 BF5: Vs d5 resolve exd5 Nxc6 or Nxd5 at once, never Be2 Bc4 holding tension. Never c3 blocking Bc1 while Qa5 lives. Never Bd4 while b2 c3 loose and Qd2 faces Rd8 Qb6: T81F 12.Bd4 met Rd8 Bxd4 Qb6 Rc8 won exchange. Play Be2 then O-O-O first. MOVER ABANDONS GUARD: name what left and who hits it now.
- MAROCZY PIN POISON: 7.Bd2 met Nxd4 winning N, 8.Be3 met retreat holding it. Never block pin leaving knight loose. Support pawn first.
- CLASSICAL E5 BREAK PLUS BLACK SIMPLIFY: vs Bd6 Nd7 Re8 Qc7 e5 hits d4. Never dxe5 without Nxe5 counted twice. Never Bd4 while f4 Ng3 loose, never Ne4 while e4 loose, never b3 while c1 loose. As Black Classical: Bf5 Bg6 h6 Bh7 Nf6 e6 Nbd7 then Be7 O-O Nd5 Nb4 Nxd3 then Bf6 Bxe5 Qxd3 levels vs h4 h5 clamp. Idea right but 55s thinks flag: play each in 10-20s.
- CARO CLAMP PLUS ENGLISH GRABS: vs c5 c4 b5 b4 Qb6 b3 opens c3 to cxb3 won N, Nc4 met b3 tempo. Keep Kb1 never Ka2, Rd1 Rd2 Be1 Qf3. Only with Re8 d6 e5 held. T82R5: meet Nc4 with b3 once, c3 only with dxc5 counted, keep Rd1 not Rd2 Rd3.
- BLOCKER LEAVES QUEEN: Nd4 blocked Rd8 Qd7, Nb4 unblocked it so Rxd7 won Q. T80 Nd4 blocked Qd8 Qd2, Nxc6 unblocked it so Qxd2 won Q gated. Before moving blocker move queen off file or guard it. Same for rook leaving rook: guard b8 before Rxc4. Ke2 Kd3 walked into check.
- ENGLISH NC2 FORK: Qe3 plus Re1 plus Ra1 all lose to Nd4 c2 triple fork wins exchange. Keep Nd4 until Q leaves d-file, play c5 Bxd5 Qd5 Qc7 Rac8, strike on Qe3. Routine 10-20 cap 60.
- UP PIECE FINISH NO SHUFFLE: Up = centralize Q, trade rook with recapture named, checks first, luft once. Down = 5-10s, invite repeats. T82R3 down P Bd3 blockade plus Nc5 Ne4 plus Qd1 Qd2 plus Kh1 Kh2 Kg1 loop drew vs bank: correct down shell. T82R4 down 5: keep Rd7 7th, Ke7 central, no b6 h7 loosening, no Ke5 Ke6 shuffle, 5-10s, invite repeat vs SF.
- SHELL CLOCK: Routine 10-20, cap 60, never 2-4min. T79R5 5x to 0:41 forfeited UP pawn. T81F plus T81R3 plus T81R4 plus T82R3 Bb1 Qb2 plus Bc2 plus Qd2 plus Kh shuffles 2-4min each to 1:34 vs 39:48 prove again. Down = 5-10s, invite repeat vs bank. Long think finds nothing.
- WHITE SCHEVENINGEN HASTE PLUS BF4 PIN: f3 Bxf4 vs e5 wedge level. Qe1 Qe2 waste tempi, f5 Bxd4, Rb1 missed recapture. RECAPTURE FIRST. Storm only e4 twice f5 counted. Nb5 f5 10-20s. T79R3 g3 blocks Qxh2, b3 chases Bc4, Qd3 holds, exd5 hits Be6, Bf4 pins Qc7 to Kb8 won Q.
- SCHEVENINGEN QB8 RB8 RE6 POISON: Qc7 Rac8 Rfe8 passive vs f4 e5. Qb8 leaves Rb8 on Bg3. Never block queen queen rook that gets pinned. Vs Nf5 e5 never d5.
- RUY D3 LOCK: c3 Re1 Nbd2 Bc2 Nf1 g3 h3, d4 only with e4 twice after Be3 blocks Re1. T81R4 cxd4 left e-pawn to Nxe4; take back at once. T81R5 exd4 cxd4 e5 Nd5 exd6 fine, b3 c3 b2 Rxb2 won B but Rb5 hung to c4 fork: move rook at once after 1 flag. T82R3 Bb1 Qb2 Bc4 Bc2 Qd2 all bad while d4 loose: keep Bd3 blockade plus Nc5 at once, never passive retreat. Vs d5 hold d6 twice.
- F3 KICK PLUS CXD4 FIRST: f3 hits Ne4 but Ne4 has Nxc3 hitting Qe2 tempo, then c5 kicks Nd4. List escapes before pawn kick. Prefer Bxe4 Qxe4. Always cxd4 first vs d4, never Nf6 Nc6 holding. Vs 4.c3 answer Nf6 dxc3 e6 first. Bans: Qb6 b6, Rxd8 gives file, Kh8 shuffle.
- BB5 PIN SHELL: vs Bb4 Ba4 Bb3 play Bd7 a6 b5 tempo, e6 Be7 O-O Qc7. Ne5 Ng6 Nf4 hit Qe2, c4 b4 tempo, bxc3 wins N. Keep e6 closed.
- ARMAGEDDON CLOCK: White needs win so draw loss, Black draw odds so draw win. Both: level or down huge still 5-10s, no 1-2min thinks, no pushes, keep Qd2 Nc3 or Bd3 Nd7 only if instant. T82-3rd-AD Black: correct simplify plan flagged on time 0:39 vs 7:07 - 60s thinks kill draw odds, keep 5-15s keepers, bank for endgame.

## Openings
- B Ruy Closed: a6 b5 Be7 d6 O-O Bd7 Re8 then Bf8 h6 Ne7 Ng6 Rc8 c6 Qc7. c6 for Qc7 after Rc8 ok, never c6 chasing Nd5, never Ra8 passive, never Nf4 exf4, never Rb5 while c4 fork lives. Hold d6 twice, Bc6 hits e4 vs Qe2 good.
- B Bb5: Bd7 a6 b5 e6 Be7 O-O Qc7. Ne5 Ng6 Nf4 hit Qe2, c4 b4 tempo, bxc3 wins N. Keep e6 closed.
- B Nxc6: bxc6 Bd3 e5 shell, Nd7 Nc5, Bb7 Qc7. Bans: queen sortie, rook trade, king shuffle. CXD4 FIRST.
- B English: d6 Be7 O-O Re8 Be6 Qc7 Nd7 then Nf6 Nd4 c5 Rac8 plus Nc2 fork vs Qe3. No Nd4 without exd4 counted. No Qb6 on Be3 ray.
- B Scheveningen: Be7 O-O Bd7 Qc7, no Rac8 Rfe8 vs f4 e5. Vs e5 dxe5 Nxe5 only if Bf4 met Ng6. No Qb8 leaving Rb8, no d5 vs Nf5.
- B Advance: Bf5 e6 Nd7 Ne7 early. Meet f4 with f6 h5 first, never Bg6 park vs f4 g4, never c5 alone, keep Kg8 vs h-storm. Vs c4 meet dxc4 or cxd5 at once, never Nd7 onto e6 fork.
- W Ruy d3 Berlin: c3 Re1 Nbd2 Bc2 Nf1 g3 h3, d4 only held twice, d5 locks, no c4 vs b4 c5, meet Nf4 with g3 after Kh1. Before Ne6 list dxe6. No Qd2 Ne4 loop shuffle.
- W Classical: Bd3, Be3 holds d4 twice, O-O-O Kb1, Rg1 holds g2. Vs c5 c4 b5 keep Rd1 Qf3, never b3 Kb2. Hold e5 f4 twice first.
- W Yugoslav: central bishop fix over risky develop. Keep Be2 then f3 then Qd2 then O-O-O order. Never Bc4 Bd4 while Be3 loose or b2 c3 loose vs Rd8 Qb6. Vs d5 Be2 O-O-O first.
- W Taimanov: Be2 f3 Qd2 Bd3 castle long Kb1. Storm g-push h-push Q-double vs shell.
- W Maroczy: c-pawn clamp, knight develops, bishop supports. Vs Qa5 pin support first then castle.

## Opponents
- Haiku: Open Sicilian Nxc6 patient, trades rooks, centralizes king, Nf5+. Never shuffle king.
- GLM: Taimanov loose, hangs Q, banks then drifts. Fast 3-10s early, 1-3min mid, 3x invalid forfeits when forked. Takes free Bxd5 Bxe3. T79R3 Qc7 Kb8 lost Q to Bf4 after g3 blocked Qxh2.
- DeepSeek: keeps guarded, queenside dance. Classical Bd6 e6 won P then Bf4 Bg5 wins N, c-clamp h-runner Rc1 mate vs Kf1 Nf4. Fast 5-20s banks clock. Flags when worse. T79R5 Italian 2-20s banked 53:05 vs my shell. T82R5 Classical storm gated 3x forfeited m39: keep b3 c3 twice-held, no Ka1 Rd2 shuffle, 10-20s. T82-3rd Classical e5 d5 c5 b4 clamp then Kg8 Kh8 plus R-shuffle fortress: no pawn push wins, low clock Rh3 Rh4 Qd1 Rc2 shell draws. T82-3rd-AD Classical Ne5-trade Nd5 Nb4 Nxd3 Bf6 Bxe5 level: take simplify in 10-20s, bank clock, never 60s with draw odds.
- Sonnet: Ruy Na5 Nxb3 Bb7 Re8 solid, Bg4 pin Nxe4 Nc4 clamp, Breyer Bd7 Re8 h6 Bf8 holds e5. Scheveningen patient 6-20s, shuffles Kg2 Kh2 Rd2 to flag. Takes every loose unit. T80R5 Advance c4 e6 fork won P vs Nd7 shell. T82R3 Chigorin d5 cxd4 exd4 held extra pawn, banks 40min: don't drift, keep Bd3 Nc5 blockade and force repeat.
- SF: punishes loose, pins, back rank, breaks. Instant, no gifts. Dragon d5 break, bxc6 opens file, Qa5 Rb8 Rd8 double kills. Castle early never long into open file, guard second rank, keep shell for repeat.
- Fable: takes loose, trades queens when up, no luft. Model: fortress, checks, back-rank mate.

## Notes
- notes/caro-black.md - Advance loss and break and clock flag.
- notes/caro-white.md - Classical draw loss win, H5 shell, queen grab and Rb2 mate.
- notes/dragon-yugoslav-white.md - File and bishop fix and sac patterns.
- notes/english-e5-black.md - English Nc2 fork win, shell and clock.
- notes/maroczy-white.md - Maroczy pin loss and shell clock.
- notes/sicilian-bb5-black.md - Bb5 pin win on time, Nf4 Qe2 tempo and up-piece shell.
- notes/sicilian-nxc6-black.md - Nxc6 forfeit, Qb6 Rxd8 Kh8 shell and tool trap.
- notes/taimanov-white.md - Storm win plan and mate finish.
