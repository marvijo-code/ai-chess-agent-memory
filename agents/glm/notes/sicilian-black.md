# Sicilian Black - v 4.c3 Morra OFFER (SF19)

## T90R1 0-1 forfeit m51: the ACCEPTED Morra - the opener was CLEAN, the scramble killed me
- 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 dxc3! 5.Nxc3 Nf6 6.e5 dxe5 7.Qxd8+ Kxd8 = queens OFF, +1 pawn, tool-verified; his 8.Ng5? was a marker. Marks on MY moves: 8...Be6? (defensive piece landed INTO his tempo piece's fork web - price each his knight/pawn raid landing before my guard adds), 11...Kd7? (Kd8 kept more per tool), 13...b5??.
- THE b5 KILL (the lesson of the game): b5 attacked Na4+Bc4 as a named double attack, but NEVER swept his knight CHECK lanes along my king trail: 14.Nb6+ forked king AND trapped Ra8 - Nxa8 recovered a full piece and the net ran +2 to +6 in one hit. LAW: a double-attack pawn push goes ONLY after a knight-check sweep of every jump landing on the king path - the check beats the attack.
- PHASE SHIFTS: keepers 5-10 s held -6 to -3; my f2-run (after his Be3 left) + Nxf2 counter recovered two pawns of eval; his Re1?!/a4?!/Ra8?! classes came at +3 and I priced them right, ending -3.7 v his 68 min bank.
- THE LOSS WAS THE SEND RACE: 36...Kh8 cost 9:03 of a 25-min bank on a king shuffle; at m48 AND m51 I cycled 3 DIFFERENT gated keeps instead of least-bad-keep + resend SAME = forfeit with 18 min left, game already lost material from m31. Material decided nothing; discipline decided everything.

## T88SF1G1 Semifinal: the SAME delay burn, AGAIN, under a written law
- The stored node after 4...Nc6 5.cxd4 was 5...Nxd4! 6.Nxd4 = level. I re-derived it in my own ply-8 comment DURING the game and STILL played 5...Nf6 two plies later.
- His 6.d5! hit the c6-knight immediately; 6...Nb4?? 7.Qa4+ hit knight+king, 8.dxc6 bxc6 left N-for-P with the c6 wedge - about +7 by m7. Terminal.
- BRANCH LAW (the fix): when his move lands on a stored node, the answer is NAMED, not debated. Read the stored branch BEFORE his move arrives (by move 3-4 for a branch at move 5); if the FEN matches, send the written UCI with no fresh sweep and no keeper derivation.

## T87SF1G1 L 0-1 on time as Black, 13 gated tries total

## THE KEPT DECLINE (the escape branch if I decline 4.c3)
- 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 Nc6 5.cxd4 Nxd4! 6.Nxd4 = even. Take on d4 BY MOVE 5, always.
- MY DELAY KILLED IT: 5...Nf6 6.d5! Ne5 7.Be3 = +1.5 him before any blunder; then 7...Nxe4?? grabbed e4 and 8.Qa4+ = CHECK + queen hit down the open 4th rank. The error was the grab itself, not the block.
- TOOL/ARGUMENT KILL: safe-keepers flagged 8...b5 at -3; I re-rated it and burned 3 tries + 4:57. When a flag names the MOVED unit = hand-verify ALL his replies or change keepers; semantics arguing loses the game.

## HIS CONVERSION, +1.5 to +9 (no gifts, no pauses)
- Quiet compounding (wing pawn chain, rook doubling, one lock move g4) with ZERO mistakes from +1.5 to +9. Only a named attack of mine or a his-blunder pays at any minus. Activity is never "rerun keepers": at -3 the send race IS the plan.

## GATE ECONOMY (the actual losses)
- Down material vs SF = ONE pre-verified keeper per move, 5-10 s, resend ONLY per flag classifier (verify-by-hand if it names the moved piece), ZERO narrations. Bank 40+ minutes and let his conversion run the race against nothing.
- Refused branch tries (m4, m6) are re-derivations at stored nodes; the m16/m51 races are pure one-send/resend-same discipline. Apply stored-line logic AS stored, never as 'solve it fresh'.

## Older laws that held (T87R2 Morra decline line)
- ...a6 into his Bb5 pin banned - UNPIN FIRST; no O-O-O while his rooks live on open files; even trades only, piece-first build; strikes against his tempo pieces DO come (11.Bg3?! class was my mark to profit).
