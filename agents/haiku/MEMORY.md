# MEMORY (Haiku 5.5; clock 60+10, both colours)

## Record
- T44R1 B v GPT-6.1 Sol, Closed Ruy: L m33 (Ra8#). Level to m28 (...d5 break, Nxd3!). Then 29...Rxb2?? and 31...Rc1?? lost.
- T44R2 W v Sonnet 5.5, Giuoco Pianissimo: L m32 (Qe4#). 14.Qe3?! queen behind e4 facing Re8; 19.exd5?? Rxe3; 26.a4?? Qxb3 fork; K walk into Ne4+.
- T44R3 B v DeepSeek V4.1 Flash, Giuoco Pianissimo: W FORFEIT m14 (three illegal replies).
- T44R4 W v GLM 5.3 Flash, Modern (...g6): W WIN m35, GLM flagged. 10...Ned5?? lost a knight to 11.exd5.
- T44R5 B v Stockfish 19, Four Knights (4.Bb5 Bb4): L m20 (Qh3#). 6...Nxe4? lost a knight; 11.d4 opened Bg5 onto my queen; 18...f6? allowed the Ng6+ shuttle mate.
- T44 Semi1 G1 B v Stockfish 19, Four Knights: L m50 (Bxd5#). Level to m13. 19...Bf5?? moved the piece screening my Ra8 from his Re8: 20.Rxa8.
- T44 3rd place W v Sonnet 5.5, Giuoco Pianissimo: DRAW m74 (insufficient material) after I was winning K+R v K. 8.Re1?! let ...dxc3 win a tempo; 15.Bxf7+ won a pawn; Sonnet's 27...Rxa2?? lost its rook for a pawn. My rook moves 45.Rc1, 61.Rf6 and 66.Rc5 were loose against his rook checks. 74.Ke7?? left Rf5 guarded only by the king: Kxf5. Two rejected first tries (Rae2, R4e5), both rook paths.

## Key lessons (read before EVERY move)
- KING GUARDS, ROOK HANGS (3rd place 74.Ke7?? Kxf5): in rook endings my king is often the only guard of my rook. Before ANY king move, list every piece the king guards and whether his king reaches it next move.
- ROOK MOVE IN A ROOK ENDING: before it, list his rook's checks along the lines my rook leaves open (Rb5+ and Rg6+ pushed my king off its guard), and whether the landing square keeps a guard. In won rook endings I lost to my own rook moves, not to his counterplay.
- ROOK PATHS: trace each square of a rook move, my own pieces included, before naming it.
- MY OWN PIECE IS A SCREEN ON MY 8TH RANK (Semi1 G1 19...Bf5?? 20.Rxa8): my Ra8 sat behind my Bc8 with his Re8 on that rank. Before moving any piece on rank 1 or 8, trace the rank both ways to the first piece on each side. A rook behind my own piece is not defended.
- LAST FILE ROOK TRADE = HIS ROOK CHECKS MY BACK RANK (Semi1 G1 16...Bd6? 17.Re8+ Bf8): after each rook trade, list every square his remaining rook reaches with check next move. Make luft (...h6) or block before any passive move.
- TWO ROOKS v ONE ON AN OPEN FILE (Semi1 G1 14...Bf4?! 15.Rae1): before a trade on a file, count his rooks that reach it against mine and any guard.
- OVERLOADED DEFENDER BEFORE ANY GRAB (T44R5 6...Nxe4?): his Nd5 hit my Bb4, whose only defender Nc6 was also hit by Bb5. Name the piece his last move attacked and each defender; if a defender is attacked too, take the ATTACKER first.
- HIS PAWN PUSH OPENS A BISHOP ONTO MY QUEEN (T44R5 11.d4): after each enemy pawn push or capture, walk every bishop line to my queen; move the queen or block before the bishop lands.
- KNIGHT CHECK SHUTTLE ON MY KING'S WING (T44R5: Ne7+ and Ng6+ shuttled his king to h8, then ...f6? allowed Ng6+ hxg6 Qh3#): before any f/g/h pawn move with my king on g8/h8, check the Ng6+ sacrifice and a queen on the h-file.
- SCREEN CHECK BEFORE ANY PAWN CAPTURE (T44R2 19.exd5?? Rxe3): the capturing pawn LEAVES its square. Name the line it screened and the piece at its far end before exd5, dxe5, dxc5.
- QUEEN BEHIND MY OWN PAWN IS A SCREEN, NOT A BATTERY (T44R2 14.Qe3?!): count the pawn between it and his rook, and every break that removes it.
- A PAWN MOVE DROPS ITS GUARD (T44R2 26.a4?? Qxb3): before any pawn push, list the squares it guarded, then his queen and knight captures on them.
- BACK-RANK RETREATS CHECK PINS (T44R2 27.Be1): trace pins to my king along rank, file and diagonal before any retreat.
- NAME THE PIECE FROM THE CURRENT BOARD (T44R2 28.Kh2 called 'Bc3' when the bishop stood on e1): re-list my pieces with squares after each move. A piece's old square is dead.
- KING STEP = KNIGHT-JUMP SCAN (T44R2 Kg3-f4 walked into Ne4+, then Qe4#): with his queen and knight alive, write all 8 jumps of every knight and his queen's lines to each king square.
- HIS KNIGHT JUMP ONTO MY PAWN'S ATTACK = FREE KNIGHT (T44R4 11.exd5 after 10...Ned5??): before each move, list every enemy knight jump and whether my pawn attacks the landing square. Same scan for my own jumps.
- LAST BACK-RANK ROOK (T44R1): my K on g8 behind f7/g7/h7 has no luft. Before my last rank-8 rook leaves, ask whether his rook can reach rank 8 next. If yes, ...h6 first.
- ROOK DESTINATION SWEEP, DEFENDING MOVES INCLUDED (T44R1 31...Rc1??): for every rook move walk each enemy bishop diagonal and rook/queen line to the square. A guard that enters a line is a gift.
- SOL AND SONNET TAKE WITH TEMPO, THEN MATE: every loose piece on an open line is captured at once. Check bishop captures from a distance and the mate after the capture.
- ATTACKED PAWN, TWO ATTACKERS vs ONE DEFENDER (T44R1): count the whole recapture chain, naming each recapturer by square.
- CONVERT A PIECE UP WITH KING AND PASSER (T44R4): trade rooks only when the trade removes his last active rook. King to the centre behind the pawns, make luft, stop a passer by putting the king in front of it.
- ROOK ENDINGS: after queens come off, count rank-8 and rank-1 defenders every move. Make luft first.

## Openings
- W Modern v GLM (notes/white-modern-glm.md): 1.e4 g6 2.d4 Bg7 3.Nf3 d6 4.Bd3 Nf6 5.O-O O-O 6.Nc3 e6 7.Be3 (14 plies). Against ...Nc6: d5, ...Ne7, dxe6 Bxe6, Re1; then ...Ned5?? exd5 wins a knight. Level-to-better, easy to play.
- W Giuoco Pianissimo v Sonnet (notes/white-giuoco-sonnet.md): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.O-O Nf6 5.d3 d6 6.c3 O-O (12 plies). Then the d4 break: after ...exd4 recapture with Nxd4 or cxd4, never 8.Re1?! (3rd place: ...dxc3 won a tempo). Nxd4 Nxd4 cxd4 Bb6 Nc3 Bg4 was level. Do not park the queen on e3 behind e4 vs Re8 (14.Qe3?!). In the 3rd-place line, Qd3 after ...Nd4 was passive.
- B Giuoco Pianissimo v DeepSeek (notes/black-giuoco-pianissimo.md): ...Nc6/...Nf6/...Bc5/...O-O/...d6/...Be6 v d3/c3/Bb3; then ...Bxb3 and ...Bb6 (Nb3 hits c5), ...Re8, ...Qe7 after Bxe3 fxe3, ...h6 luft. Level and safe. d3 guards e4, so Nxe4 is never a threat.
- B Closed Ruy v Sol (notes/black-ruy-closed.md): ...Nc6/...Nf6/...Be7/...O-O/...a6/...b5/...d6 v d3/O-O/Re1/Ba4/Bb3, then ...Bb7 and ...d5. Level. 6...a6 was marked inaccurate; no verified replacement stored.
- B Four Knights v SF19 (notes/black-four-knights.md): ...Bb4 and castle v Bb5; 6...Nxd5 7.exd5 Nd4 held level (Semi1 G1). NOT 6...Nxe4? (lost a knight to Bxc6). After 14.c3 the Bd2 is loose and Rae1 comes: count the e-file before any trade. Keep the queen off any diagonal a pawn push opens.
- ...d5 exd5 Nxd5, then ...Nf4 vs d3 (only Bc2 guards it while Nd2 blocks Qd1), is a sound plan.

## Opponents
- GPT-6.1 Sol (White, T44R1 vs me): fast, zero illegal. Closed Ruy: c3, h3, Re1, Ba4-b3, Nbd2-Bc2. Trades simply, then finds bishop captures and back-rank mates at once.
- Sonnet 5.5 (T44R2 and 3rd place, both vs me): Giuoco ...Bc5/...Nf6/...d6/...O-O, then ...Bg4/...Re8/...h6 pressure on e4 and ...Nd4/...c6/...Ne6 trades. Breaks with ...d5 when a screen is weak, takes the queen the moment a screen leaves, forks with the queen, mates with Q+N near the king. In the 3rd-place ending it pushed its c-pawn and grabbed a loose a-pawn (27...Rxa2?? lost its rook for a pawn), then blundered when lost (...Kg8??, ...Rg5??). Never waits.
- DeepSeek V4.1 Flash (White, T44R3 vs me): Giuoco Pianissimo with Bb3, Nbd2, Nxb3, h3, Be3, fxe3, Qd2. Three illegal replies, forfeit m14. Keep clean, checked moves.
- GLM 5.3 Flash (Black, T44R4 vs me, 2 illegal tries): Modern ...g6/...Bg7/...d6/...Nf6/...O-O/...e6, then ...Nc6/...Ne7/...Ned5 without checking my pawn attacks. Hangs a knight to e4xd5 at once; long thinks, flagged with 3:33 left.
- Stockfish 19 (Four Knights, T44R5 and Semi1 G1): instant, engine-accurate. Hits the overloaded defender, pushes d4 to open Bc1 onto my queen, finishes with the Ng6+ hxg6 Qh3# shuttle. In Semi1 G1 it played quiet doubling, Rae1 on the e-file, then took my rook through my own screen. No second chances.

## Clock
- 60+10: T44R1 B about 6 min over 33 moves; T44R2 W 1-33 s a move, 58 min left; T44R3 B 1-10 s, 60:38 left; T44R4 W 4-20 s, 58:12 left; T44R5 B 0-26 s, 58:59 left; Semi1 G1 B 0-33 s, 57:31 left; 3rd place W 1-35 s a move, about 2:20 used, 57:38 left (Sonnet 43:45). Errors came from fast captures and skipped screen, king-guard and rook-check scans, not from speed. Spend 30-60 s on captures that open lines, rook moves, rook trades and king steps; book 1-5 s.

## Notes
- notes/black-ruy-closed.md - Closed Ruy v Sol: opening pattern, d5 break, back-rank and rook-destination failures.
- notes/white-giuoco-sonnet.md - Giuoco Pianissimo v Sonnet: e-file screen, a4 guard drop, king walk, pinned Be1.
- notes/black-giuoco-pianissimo.md - Giuoco Pianissimo as Black v DeepSeek: ...Be6/...Bxb3/...Bb6 setup, jump checks, ...h6 luft.
- notes/white-modern-glm.md - Modern v GLM as White: d5 and dxe6, the Ned5 knight loss, the trade-down conversion.
- notes/black-four-knights.md - Four Knights v SF19 as Black: level 6...Nxd5 line, e-file trade, Bf5 screen loss, Ng6+ mate pattern.
