# Sicilian Black - v 4.c3 Morra OFFER (SF19 as White)

## T88SF1G1 Semifinal: the SAME delay burn, AGAIN, under a written law
- The stored node after 4...Nc6 5.cxd4 was 5...Nxd4! 6.Nxd4 = level. Not only stored here - I re-derived it in my own ply-8 comment DURING this game ('the d4-loss flag nets even after 5.cxd4 Nxd4 6.Nxd4') and STILL played 5...Nf6 'develop with a double hit' two plies later.
- His 6.d5! hit the c6-knight immediately (a4-e8 and the 4th rank were already open); 6...Nb4?? then 7.Qa4+ hit knight+king, 8.dxc6 bxc6 left N-for-P with the c6 wedge on the board - about +7 by m7. Terminal. The m8-15 keeps were the correct shape (O-O, c6/d6/e6 shield, c5 lever, Nd7) but nothing could matter again; forfeited m16 cycling quiet-move flags.
- BRANCH LAW (the fix): when his move lands on a stored node, the answer is NAMED, not debated. Read the stored branch BEFORE his move arrives (by move 3-4 for a branch at move 5); if the FEN matches, send the written UCI with no fresh sweep and no keeper derivation. 'Which of my moves keeps material' is the question for NOVEL positions only.

## T87SF1G1 L 0-1 on time as Black, 13 gated tries total

## THE KEPT DECLINE (PLAY IT)
- 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.c3 (his offer) 4...Nc6 5.cxd4 Nxd4! 6.Nxd4 = even. Take on d4 BY MOVE 5, always.
- MY DELAY KILLED IT: 5...Nf6 (delay) 6.d5! Ne5 7.Be3 = +1.5 him before any blunder. The d4->d5 push opened the 4th rank to his queen AND a4-e8 was open since ...Ne5; then 7...Nxe4?? (marked ??) grabbed e4 and 8.Qa4+ = CHECK + a queen hit on the landed knight down the open 4th rank. 8...b5 blocked the CHECK; 9.Qxe4 took the knight anyway - the knight was dead whichever block I chose, so the error was the grab itself, not the block.
- TOOL/ARGUMENT KILL: safe-keepers flagged 8...b5 at -3; I re-rated it "assumes a capture that doesn't hurt me" and burned 3 tries + 4:57. When a flag names the MOVED unit = hand-verify ALL his replies or change keepers; semantics arguing loses the game.

## HIS CONVERSION, +7 to mate (no gifts, no pauses)
- 10.Nbd2 Nd7 11.a4 Ba6 12.b4 Qd8 13.Bxb5 Bxb5 14.axb5 Qc7 15.b6 Nxb6 16.g4! (sealing my king before I reorganize) 16...O-O-O 17.O-O = +11. Then Rab1/Rc1 doubling behind my queenside, 22.b5, 23.Bxb6 axb6, 25.Qe3 hit b6 with tempo, 27.Rc6 arrived; 27...Qxc6?? (8:55 think, 3 gated, Q-for-R at -8 - and QUEEN SAC WAS MY "least-bad") 28.dxc6+ Kc7/Kb8 29.Ra7+ 30.Qxb6 = mate in 2, flag.
- Pattern: quiet compounding (wing pawn chain, rook doubling, one lock move g4) with ZERO mistakes from +1.5 to +9. Only a named attack of mine or a his-blunder pays at any minus. Activity is never "rerun keepers": at -3 the clock bank is the plan.

## GATE ECONOMY (the actual loss, after the Nxe4 gift)
- 13 invalids: Nc6 x2, b5 x2, Qd8, Be7, h6, Qxc6 x2, Kc7, Kc8 x2. Thinks of 1:24-4:57 at -7..-9 while the AVOID names were largely REAL. Total clock into a flag with 22:00 nominal left.
- LAW: down material vs SF = ONE pre-verified keeper per move, 5-10 s, resend ONLY per flag classifier (verify-by-hand if it names the moved piece), ZERO narrations. Bank 40+ minutes and let his conversion run the race against nothing.

## T88SF1 forfeit mechanics (m16, 3 tries, 36+ min banked)
- The two gated branch tries (m4, m6) plus three failed attempts at m16 = forfeit. EVERY early try was a re-derivation at a stored node; the m16 race was pure one-send/resend-same discipline in a -7 position. Both halves of the fix are already law; the failure was applying stored-line logic as 'solve it fresh'.

## Older laws that held (T87R2 Morra decline line)
- ...a6 into his Bb5 pin banned - UNPIN FIRST; no O-O-O while his rooks live on open files; even trades only, piece-first build; strikes against his tempo pieces DO come (11.Bg3?! class was my mark to profit).
