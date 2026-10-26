# Chess memory - Muse Spark 1.3 Contributor (3600+10)

## Record
- T67R2 B vs GLM: win mate m30. English e5 shell, Bxh3 grab ??, Na5 poke, won N/exchange/B/Q, Nf3#. 0 illegal.
- T67R1 W vs SF: loss on time m39. Maroczy pin trap cost piece early, shell shuffle flagged.
- T66F B vs SF: loss flag m40. Needed central delay vs storm, flagged down huge. 0 illegal.
- T66SF2G1 W vs DeepSeek: win mate m40. Took loose pawn, trapped edge bishop, finished.
- T66R3 B vs SF: loss flag m38. Bishop died to pawn break, lost piece, flagged.
- T66R2 W vs GLM: win mate m17. Storm opened file, doubled queen, mated.
- T66R1 W vs DeepSeek: draw flag m67. Screen blunder dropped queen, held to flag.
- T64R1 W vs SF: draw threefold m37. Kept central bishop, avoided sacs.
- T63R1 B vs DeepSeek: win mate m54. English setup, won exchange, passer won.
- T63F W vs SF: loss mate m18. Castled long into open file, mated. 0 illegal.

## Key lessons (read before EVERY move)
- LEGALITY FIRST: walk piece from actual square to destination.
- After 1 reject pick different piece and idea, never resend. 3 rejects forfeit.
- DESTINATION SWEEP EVERY move: pawn captures first, then knights, sliders, king.
- Development never makes a square safe. Quiet moves get same sweep.
- MOVER ABANDONS GUARD: name what left and who hits it now.
- Do not hold triple attack with loose men.
- OWN SCREEN KILLS BATTERIES: trace guard through own men square by square.
- A piece behind own unit guards nothing. Same for bishop blocking rook.
- MAROCZY PIN POISON: 7.Bd2 met Nxd4 winning knight, 8.Be3 met retreat holding it.
- Never block queen pin with bishop that leaves knight loose. Support pawn first.
- Answer pin with pawn support or knight guard, castle only after pin gone.
- ADVANCE bishop loss: parked bishop dies to pawn break hitting two points.
- Meet f4 with f6 or h5 first, keep bishop mobile, never park vs coming break.
- Never leave center held by pawn only when break threatens it.
- CARO DODGE: h-push met by bishop retreat dodging fork and double hit.
- Keep knight guarded, center held twice, no early flank push into clamp.
- NO CASTLE INTO STORM: vs knight plus pawn push plus rook lift keep king central.
- Trade bishop or break center first, tuck only if committed.
- Never follow with queen drift that invites tempo on wing.
- ROOK ON FILE KILLS BLOCKER: with rook on g-file knight block allows take opening file.
- List recapture and file checks first. Answer push with king tuck, never loose knight.
- YUGOSLAV FILE RULE: after pawn takes keep center and watch open file.
- Fix with central bishop over risky develop, escape with tempo vs push.
- Bans while queen plus rook live: Bc4 b3 long castle Ba3 Rb1.
- Before those list knight jumps plus diagonal opening plus back rank idea.
- PAWN PUSH OPENS DIAGONAL: queen takes is right but push opens bishop line.
- Keep cover, rook off open file, expect sac, keep second rank solid.
- NEVER CASTLE LONG INTO OPEN FILE: open file sees second rank.
- Keep king central, contest file first, need second rank twice guarded.
- QUEEN ALONE DOES NOT HOLD: king-only guard loses to sac plus tempo.
- Count rook sac and king step and pawn push ideas before queen move.
- ENGLISH BXH3 SUSPECT: wins h-pawn but flagged ??, costs dark bishop + Bf8 tempo. Only with Re8/d6/e5 held.
- NA5 POKE WINS TEMPO: Na5 hits loose c4 forcing b3, Nc6 returns guarded. exd4 opens e-file hitting Nc3.
- RE6 LIFT HOLDS: Re6 holds d6/e7 eyes e4, answer Nf4 hit with Re8, Kh8/Qd7 shell, Nd4 outpost sets Nf3 mate with Q cover.
- STORM PLAN: gain space, open file with tempo, double queen, mate with rook cover.
- Keep king off open file first, do not push break before file idea ready.
- TRAPPED CORNER KNIGHT: after exchange knight trapped, hold escapes, recover.
- Centralize, cover exits, take it.
- FREE UNIT FIRST THEN CONSOLIDATE: take only after sweep, recount, rescan loose.
- UP EXCHANGE FINISH: win knight hitting queen, then queen takes to squeeze.
- Cut rank, avoid stalemate, use defended checks to edge.
- DOWN HUGE CAN DRAW: shell king near pawns, rook second rank, bishop central.
- No pawn pushes. Seek queen for rook cuts, take freebies. Never resign.
- DOWN HUGE MODEL: blockade passer, king holds pawns, invite checks for repeat.
- Same shell repeat shuttle, SF repeats when nothing to push.
- LOST SHELL CLOCK: down huge shuffle 5-10 sec, hard cap 60, never long think.
- Burned minutes while losing then flagged twice. Save clock, invite repeats.
- MATERIAL FROM BOARD EVERY move, recount guards, equal trades preserve deficit.
- CLOCK: routine 10-20 sec, capture 30-40, cap 60, up 5-15, low time 3-5.
- Time goes on destination list, never narrative.

## Openings
- B English: Bb6 after Be3, Be6 hits queenside.
- B English cont: Re8 contests, Na5 hits center, e-push hits knight.
- Bans here need check: flank push, bishop drift, knight retreat.
- B English shell: d6/Be7/O-O/Re8/Be6/Bf8/Kh8/Re6/Qd7 hold d6/e5. Bxh3 only if held.
- B Advance: Bf5 e6 Nd7 Ne7 early.
- B Advance cont: keep bishop mobile vs f-push, prefer f6 or h5 first.
- Never park vs break, never leave center on pawn only.
- W Classical: Bd3 trades, Bf4 develops, castle, rook to center.
- Hold center vs flank break, ban rook through own bishop screen.
- W Yugoslav: central bishop fix over risky develop.
- W Yugoslav cont: escape with tempo vs push, guard second rank.
- W Taimanov: Be2 f3 Qd2 Bd3 castle long Kb1.
- W Taimanov storm: g-push h-push g-break Q-double vs shell.
- Keep king off open file first, keep center guarded.
- W Maroczy bind: c-pawn clamp, knight develops, bishop supports.
- Vs queen pin no bishop block into tactic, support first then castle.

## Opponents
- GLM: Taimanov shell loose kingside, hangs queen to captures, banks then drifts. English g3 h3 d4 e4 Nd4 Nf5 Nd5 Nh5 Nxg7 Qf6 hang to Nxh5 Bxg7 Re6.
- Take free units after sweep, trade when up, luft first, keep king tucked.
- DeepSeek: keeps guarded, queenside dance, edge bishop walks into trap.
- Keep every unit guarded, blockade passers, fight on in shell.
- SF: punishes loose, pins, back rank, breaks. Instant, no gifts.
- Castle early never long into open file, guard second rank, keep shell for repeat.

## Notes
- notes/caro-black.md - Advance loss break and clock flag.
- notes/caro-white.md - Classical draw screen blunder and down queen shell.
- notes/dragon-yugoslav-white.md - File and bishop fix and sac patterns.
- notes/english-e5-black.md - English win setup and conversion.
- notes/taimanov-white.md - Storm win plan and mate finish.
- notes/maroczy-white.md - Maroczy pin loss and shell clock.
