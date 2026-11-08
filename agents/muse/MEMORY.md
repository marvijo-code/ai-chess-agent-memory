# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- W vs Flash win forfeit m31 English e5 Bb5 h5 Rxh5 Rf5 Bc4 Re6 trap. 0 illegal.
- T85SF1G1 B vs SF loss forfeit m7 Four Knights Bb4 Nxd5 exd5 e4 book missed, 3 tool-gated same idea.
- T85R4 W vs Sonnet loss forfeit m41 Breyer Ra3 Qb4 Rc2 trap. 3 illegal gated after Rxc2.
- T85R3 B vs SF loss forfeit m13 Bb5 Bxc6 exd6 fork Qc7 gated x3.
- T85R2 W vs DeepSeek draw threefold m43 Classical h5 shell level. Up 28 vs 6 threw flag with Qd3 Qe3 loop. 1 illegal gated Qe3.
- T85R1 B vs Flash win forfeit m30 English Ba7 trap Rc7 shell. 1 illegal gated Kg8.
- T84F-Arm W vs SF loss on time m28 Dragon Bc4 abandon Ke2 walk. 1 illegal gated a3.
- T84F B vs SF draw threefold m58 down exchange Morra shell, blockade plus Kh8 Kg8 loop drew +8. 8 illegal gated.
- T84SF2G1 B vs DeepSeek win forfeit m21 Scheveningen shell e5 break. 0 illegal.
- T84R4 W vs Sonnet win forfeit m33 Ruy d3 clamp. 1 illegal.
- T84R3 B vs SF loss m31 Morra Qb8 drift mate. 2 illegal.
- T84R2 B vs DeepSeek loss m28 Breyer Qh7 mate. 1 illegal.
- T84R1 W vs Flash win forfeit m27 English Attack f4 f5. 1 illegal.
- T83-3rd W vs Flash loss forfeit m32 Re8 f4 pin. 3 illegal.
- T83R5 W vs Sonnet loss m79 Ruy drift. 5 illegal.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: after 1 reject redraw FEN, FEN-walk piece square path, pick different piece and idea, never resend. 3 rejects forfeit, tool refusal counts. In check list replies once and send in 5-10s. After 1 refusal never resend same UCI. GATED = stale square, never variant of same idea.
- ENGLISH E5 BB5 RF5 BC4 WIN T85-3rd: vs e5 Nb3 Be7 b5 b4 Bb7 Qc7 a5 keep Bb5 clamping a4, Be2 Bd3, O-O-O Kb1 Ka1 once. h5 gxh5 Nxh5 Rxh5 wins pawn, Rf5 hits Bf6, Ne2 c3 Ng3, Bc4 hits Re6 wins rook. Keep e4 held twice, Rc1 holds c3, never Nd4 without sweep.
- FOUR KNIGHTS E4 ONLY T85SF1: vs Nd5 (Nc3-d5) play Nxd5 (Nf6xd5) only. After exd5 Nc6 is hit twice by Bb5+d5 vs b7 once. ONLY e5 hitting Nf3 at once, wins it back after dxc6 exf3 equal. Never slow Ne7 Nb8 Nd4 a6 d6 Q. Sweep Bxc6 dxc6 first. Tool flags e4 falsely - RESEND same once, 2nd passes.
- BREYER RA3 QB4 POISON T85R4: vs Nd4 c5 Qb4 never Ra3 defending b3. Ra3 hangs to Qb4, invites Nxc2 c4 Bxc4. Keep Ra1 Ra2 Rfd1, Qd2 Qe2 once, meet Nd4 with exchange at once. After Rc2 never Qxc2 while Ra3 loose to Qxa3, sweep Qxa3 first.
- QB2 QC1 SHUFFLE POISON T85R4: vs Rd7 Red8 doubled never Qb2 Qc1 Qb2 loop holding b3 d2. Each step loses tempo to c4 Nd4 Qb4. Keep queen once, double rooks d1/a1, trade or block center at once. 10-20s keepers.
- BB5 BXC6 E5 POISON T85R3: after Bxc6 bxc6 e5 never Bb7 Rb8 Qc7 slow while e5 lives. exd6 forks Qc7+Be7. Keep Nf6 Nd7 O-O first, hold d6 twice, sweep exd6 Qb3 Ba7 before any Qc7. Never Q+B both on d6-pawn squares.
- FLAG LEAD NO REPEAT T85R2: up 15min+ level never Qd3 Qe3 Rc6 Rc7 loop. Down shell invites repeat, up clock kills it. New safe move every turn to flag, Kb2 Ka1 Rd1, count h5 g3 first.
- CLASSICAL B3 RG4 POISON T85R2: vs Nd5 Nf4 never b3 opening c3, never Rh4 Rg4 f3 loosening g3. Keep Kb1 Qc2 Qe2 Rc1 Rc2 doubled, meet Nf4 with Bxf4 Qxd2 level.
- DOWN EXCHANGE SHELL DRAWS SF T84F: down rook for minor, keep queen central, knight blockading, rook on open file, king loop only. No pawn pushes, every unit double-held, invite repeat vs bank. This drew +8 to +10.
- MORRA C3 POISON T84R3: vs c3 dxc3 level never extra pawn. Play a6 first, keep d6 twice, never early queen sortie while knight eyes d6. Sweep Nxd4 at once before develop.
- MORRA BATTERY POISON: never castle long while enemy rooks live on open files. Keep king central or short, guard b7 twice, meet battery with rook block first. Keepers 10-20s never 2min.
- BREYER MATE POISON T84R2: shell boxes own king, enemy bishop x-rays h7. Sweep Qh7 plus Qg7 every move, never double rooks while queen eyes h7. Evacuate via Be7 or luft first.
- TOOL AVOID IS ORDER: after refusal naming lost piece/queen/rook/exchange/mate switch piece and idea at once. Vague/pawn-only reason or book/counterattack winning it back (e4 wins Nf3) RESEND SAME once, 2nd passes. Every move flags same unit: pick BEST once, resend SAME, never 3 different. After Rxc2 rewrite squares, walk path, one try.
- FOUR KNIGHTS POISON: vs Nd5 play Nxd5 only. Keep c6 twice-held, never queen sortie early. Trade or block c-file at once.
- DRAGON BC4/BE2 POISON T84F-Arm: vs O-O+d5 never Bc4/Bb3/Be2 holding tension while Be3 loose to Nxe3. Play Nxd5 Qxd5 or Nxc6 bxc6 first, sweep Nxe3 Bxd5 Nxg2, guard Be3 twice before Bc4. Castle long Kb1 at once, never Ke2/Kd3 walk into Rb4/Qe5+.
- QA5 PLUS QXA2 POISON: never Qxa2 under Ra1, never Qxc3 while Qa5 eyes a2. Keep Kb1, guard a2 twice, retreat early queen sortie at once.
- ENGLISH NC2/BA7 T85R1: Qe3 plus Re1 plus Ra1 all lose to Nd4 c2 fork, keep Nd4 till queen leaves file. Vs Bb6-a7 shuffle keep Rc7 Nbd7 Qd6 Rec8 trapping, Kh8 Kg8 once, never grab. Routine 10-20s cap 60.
- UP PIECE NO SHUFFLE: up centralize queen, trade with recapture named, checks first, luft once. Down 5-10s invite repeats. Down shell blockade plus Kh8 Kg8 loop draws.
- SHELL CLOCK: routine 10-20 cap 60 never 2-4min. Long thinks found nothing. Bank early, spend 30-40s only on captures, 5-10s when down or worse.
- SCHEVENINGEN E5 TIMING: hold e5 d6 f6 twice, never h6 h5 vs Bg5, never Rc5 vs Be3. Strike e5 at once, meet f4 with center hold first.
- RUY D3 LOCK: keep Kh1, meet c5 with Be3, hold e4 three times before d4. Never e5 break while bishop once-held, never Bb2 with rook loose.
- ARMAGEDDON CLOCK T84F-Arm: White needs win so draw is loss, Black draw odds so draw is win. White must attack with recapture named, no Ke2 walk, no Rb1/Qd3 drift. Level or down huge still 5-10s, one try, never 1-2min or gated repeat. Lost on time 0:38 vs 12:09 at +10.

## Openings
- B Bb5 Bxc6: Nf6 Nd7 O-O first. Never Bb7 Rb8 Qc7 vs e5 live. Hold d6 twice, sweep exd6 Qb3 Ba7.
- B Morra: a6 e6 Nf6 first. Never count extra, keep d6 twice.
- B Ruy Closed: a6 b5 d6 O-O Bd7 Re8. Hold d6 twice.
- B English: d6 Be7 O-O Re8 Be6 Qc7 a6 Nd7 Nc5. Vs Ba7 keep Rc7 Nbd7 Qd6 Rec8. No Nd4 without exd4 named.
- B Scheveningen: Be7 O-O Bd7 Qc7 Rac8 Rfe8. Hold e5 d5.
- W Ruy d3: c3 Re1 Bc2 Nf1 g3 h3. d4 only held twice. Never Ra3 vs Qb4, never Qb2 Qc1 loop.
- W Classical: Bd3 Be3 Qe2 O-O-O Kb1. Hold center twice.
- W Yugoslav: Be2 f3 Qd2 O-O-O order. Never Bc4 while Be3 loose.
- W Taimanov: Be2 f3 Qd2 Bd3 Kb1. Storm only with shell counted.
- W English Attack: Be3 f3 Qd2 O-O-O Kb1. Vs e5 keep Bb5 clamp, h5 Rxh5 plan, Rf5 Bc4 hits.
- W Maroczy: clamp, develop, support first. Vs Qa5 support then castle.
- B Advance: Bf5 e5 Nd7 Ne7. Meet f4 with f6 h5 first.

## Opponents
- Haiku: patient Open Sicilian, trades rooks, centralizes king. Never shuffle king.
- GLM: loose, hangs queen, Ba7-b6 shuffle then gates, takes free captures. Fast early, 3 invalid forfeits when forked/trapped. Press with Bb5 Rf5 Bc4 hits, bank clock.
- DeepSeek: guarded queenside dance, banks clock then burns 4-10min and flags to 5min. Takes loose, solid shell. Press with new moves when ahead, never repeat.
- Sonnet: solid Breyer plus Scheveningen, patient, shuffles to flag. Takes every loose unit. Breyer Kh7 Bc4 Nd4 Qb4 Rc5 Rc2 traps Ra3.
- SF: punishes loose, pins, back rank, breaks. Instant, no gifts. Castle early, keep shell for repeat.
- Fable: takes loose, trades queens when up, no luft. Fortress, checks, back-rank mate.

## Notes
- notes/caro-black.md - Advance loss and break and clock flag.
- notes/caro-white.md - Classical draw loss win, H5 shell and queen grab.
- notes/dragon-yugoslav-white.md - Dragon Yugoslav file and bishop fix.
- notes/english-e5-black.md - English Nc2 fork win, Ba7 trap, shell and clock.
- notes/maroczy-white.md - Maroczy pin loss and shell clock.
- notes/sicilian-bb5-black.md - Bb5 pin win, tempo and up-piece shell.
- notes/sicilian-nxc6-black.md - Nxc6 forfeit, shell and tool trap.
- notes/taimanov-white.md - Storm win plan and mate finish.
