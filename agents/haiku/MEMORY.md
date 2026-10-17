# MEMORY (Haiku 5.5; clock 60+10, both colours)

## Record
- T44R1 B v GPT-6.1 Sol, Closed Ruy: L m33 (Ra8#). Level to m28 (...d5 break, Nxd3!). Then 29...Rxb2?? and 31...Rc1?? lost.
- T44R2 W v Sonnet 5.5, Giuoco Pianissimo: L m32 (Qe4#). 14.Qe3?! queen behind e4 facing Re8; 19.exd5?? Rxe3; 26.a4?? Qxb3 fork; Kg3-f4 walked into Ne4+.
- T44R3 B v DeepSeek V4.1 Flash, Giuoco Pianissimo: W FORFEIT m14 (three illegal replies). Level all game.
- T44R4 W v GLM 5.3 Flash, Modern (...g6): W WIN m35, GLM flagged. 10...Ned5?? lost a knight to 11.exd5.
- T44R5 B v Stockfish 19, Four Knights (4.Bb5 Bb4): L m20 (Qh3#). 6...Nxe4? lost a knight; 11.d4 opened Bg5 onto my queen; 18...f6? allowed 19.Ng6+ hxg6 20.Qh3#.
- T44 Semi1 G1 B v Stockfish 19, Four Knights (same start): L m50 (Bxd5#). Level to m13 with 6...Nxd5 (line in notes). 14...Bf4?! let 15.Rae1 double on the e-file (+2). 16...Bd6? allowed 17.Re8+ Bf8. 19...Bf5?? moved my Bc8, the only piece between my Ra8 and his Re8: 20.Rxa8. Clock 57:31 left.

## Key lessons (read before EVERY move)
- MY OWN PIECE IS A SCREEN ON MY 8TH RANK (Semi1 G1 19...Bf5?? 20.Rxa8): my Ra8 sat behind my Bc8 with his Re8 on that rank. Before moving any piece on rank 1 or 8, trace the rank both ways to the first piece on each side. A rook behind my own piece is not defended.
- LAST FILE ROOK TRADE = HIS ROOK CHECKS MY BACK RANK (Semi1 G1 16...Bd6? 17.Re8+ Bf8: Bf8 pinned to Kg8). After each rook trade, list every square his remaining rook reaches with check next move. Make luft (...h6) or block before any passive move.
- TWO ROOKS v ONE ON AN OPEN FILE (Semi1 G1 14...Bf4?! 15.Rae1): before a trade on a file, count his rooks that reach it against my rooks and any piece guarding it. A trade that hands him the file is a tempo loss.
- OVERLOADED DEFENDER BEFORE ANY GRAB (T44R5 6...Nxe4?): his Nd5 hit my Bb4, whose only defender Nc6 was also hit by Bb5. Before any capture, name the piece his last move attacked and every defender; if a defender is also attacked, take the ATTACKER first (Nxd5).
- HIS PAWN PUSH OPENS A BISHOP ONTO MY QUEEN (T44R5 11.d4 cleared c1-g5): after each enemy pawn push or capture, walk every bishop line to my queen; move the queen or block before the bishop lands.
- KNIGHT CHECK SHUTTLE + PAWN MOVE ON MY KING'S WING (T44R5 15.Ne7+ Kh8 16.Ng6+ Kg8 17.Ne7+ Kh8, then 18...f6? 19.Ng6+ hxg6 20.Qh3#): before any f/g/h pawn move with my king on h8/g8, check Ng6+ hxg6 and a queen on the h-file.
- SCREEN CHECK BEFORE ANY PAWN CAPTURE (T44R2 19.exd5?? Rxe3): the capturing pawn LEAVES its square. If that square screened a line to my queen or king, the line opens now. Name the line and the piece at its far end before exd5, dxe5, dxc5.
- MY QUEEN BEHIND MY OWN PAWN IS A SCREEN, NOT A BATTERY (T44R2 14.Qe3?!): before parking the queen on a file with his rook, count the pawn between them and every break that removes it.
- A PAWN MOVE DROPS ITS GUARD (T44R2 26.a4?? Qxb3): before any pawn push, list the squares that pawn guarded, then his queen and knight captures on them.
- BACK-RANK RETREATS CHECK PINS (T44R2 27.Be1): with his queen on d1 and my K on g1, Be1 was pinned. Before any retreat, trace pins to the king along rank, file and diagonal.
- NAME THE PIECE FROM THE CURRENT BOARD (T44R2 28.Kh2: 'Bc3' when the bishop stood on e1): after each move re-list my pieces with their squares. A piece's old square is dead.
- KING STEP = KNIGHT-JUMP SCAN (T44R2 29.Kg3 Ne4+ ... 32.Kf5 Qe4#): with his queen and knight alive, write all 8 jumps of every knight and his queen's lines to each king square.
- HIS KNIGHT JUMP ONTO MY PAWN'S ATTACK = FREE KNIGHT (T44R4 W 11.exd5 after 10...Ned5??): before each move, list every enemy knight jump and check whether one of my pawns attacks the landing square. Same scan on my own jumps.
- LAST BACK-RANK ROOK (T44R1): my K on g8 behind f7/g7/h7 has no luft. Before my last rank-8 rook leaves (Rxb2, Rc1, Rxd4), ask whether his rook can reach rank 8 next. If yes, play ...h6 first or keep the rook home.
- ROOK DESTINATION SWEEP, DEFENDING MOVES INCLUDED (T44R1 31...Rc1??): for every rook move, walk each enemy bishop diagonal and rook/queen line to the square. A pawn guarded by a rook is not worth a rook. A guard that enters a line is a gift.
- SOL AND SONNET TAKE WITH TEMPO, THEN MATE: every loose piece or rook on an open line is captured at once. Check bishop captures from a distance and the mate after the capture.
- ATTACKED PAWN, TWO ATTACKERS vs ONE DEFENDER (T44R1): count the whole recapture chain and name each recapturer by square.
- CONVERT A PIECE UP WITH KING AND PASSER (T44R4): trade rooks only when the trade removes his last active rook. Walk the king to the centre behind the pawns, make luft, and stop a passer by putting the king in front of it.
- ROOK ENDINGS: after queens come off, count rank-8 and rank-1 defenders every move. Make luft first.

## Openings
- W Modern v GLM (notes/white-modern-glm.md): 1.e4 g6 2.d4 Bg7 3.Nf3 d6 4.Bd3 Nf6 5.O-O O-O 6.Nc3 e6 7.Be3 (14 plies). v 7...Nc6 8.d5 Ne7 9.dxe6 Bxe6 10.Re1: then ...Ned5?? exd5 wins a knight. Level-to-better, easy to play.
- B Giuoco Pianissimo v DeepSeek (notes/black-giuoco-pianissimo.md; T44R3 W forfeit m14): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d3 Bc5 5.c3 O-O 6.O-O d6 7.Bb3 Be6 (14 plies), then Nbd2 Bxb3 Nxb3 Bb6, h3 Re8, Be3 Bxe3 fxe3 Qe7, Qd2 h6. Level and safe. d3 guards e4, so Nxe4 is never a threat.
- B Closed Ruy v Sol (notes/black-ruy-closed.md): 1.e4 e5 2.Nf3 Nc6 3.Bb5 Nf6 4.d3 Be7 5.O-O O-O 6.Re1 a6 7.Ba4 b5 8.Bb3 d6, then ...Bb7 and ...d5. Level and playable. 6...a6 was marked inaccurate by analysis; no verified replacement stored.
- B Four Knights v SF19 (notes/black-four-knights.md): 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 Nd4 held level to m13 (Semi1 G1). NOT 6...Nxe4? (lost a knight to Bxc6). After 14.c3 the Bd2 is loose and Rae1 comes: check the e-file count before any trade. Keep the queen off any diagonal a pawn push opens.
- ...d5 exd5 Nxd5, then ...Nf4 vs d3 (only Bc2 guards it while Nd2 blocks Qd1), is a sound plan.
- W Giuoco Pianissimo v Sonnet (notes/white-giuoco-sonnet.md): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.O-O Nf6 5.d3 d6 6.c3 O-O (12 plies). Then 7.d4 exd4 8.Nxd4 Nxd4 9.cxd4 Bb6 10.Nc3 Bg4 11.Qd2 Re8 was level. Do not park the queen on e3 behind e4 vs Re8 (14.Qe3?!). 16.Nd5?! was marked inaccurate.

## Opponents
- GPT-6.1 Sol (White, T44R1 vs me): fast, zero illegal. Closed Ruy: c3, h3, Re1, Ba4-b3, Nbd2-Bc2. Trades simply, then finds bishop captures and back-rank mates at once. Expect it to punish any rook that stops on an enemy bishop's line.
- Sonnet 5.5 (Black, T44R2 vs me, one illegal try): Giuoco ...Bc5/...Nf6/...d6/...O-O/...exd4, then ...Bg4/...Re8/...h6/...Bh5 pressure on e4. Breaks with ...d5 when the screen is weak, takes the queen the moment a screen leaves, forks with the queen (Qxb3), and mates with Q+N near the king. Never waits.
- DeepSeek V4.1 Flash (White, T44R3 vs me): Giuoco Pianissimo with Bb3, Nbd2, Nxb3, h3, Be3, fxe3, Qd2. Three illegal replies, forfeit m14 on b4 through its own Nb3. Expect it to keep a level structure and then fail on legality; keep playing clean, checked moves.
- GLM 5.3 Flash (Black, T44R4 vs me, 2 illegal tries): Modern ...g6/...Bg7/...d6/...Nf6/...O-O/...e6, then ...Nc6/...Ne7/...Ned5 without checking my pawn attacks. Hung a knight to e4xd5 at once; then long 3-8 minute thinks in a simplified ending and flagged with 3:33 left. Trade pieces, keep material, and it will drop more.
- Stockfish 19 (White, T44R5 and Semi1 G1, both Four Knights): instant, engine-accurate. In T44R5 it hit my overloaded defender, pushed d4 to open Bc1 onto my queen, and finished with the Ng6+ hxg6 Qh3# knight shuttle. In Semi1 G1 it played quiet doubling (Qg4 vs d4, Bb2 giving a pawn to force the queen trade, Rae1 on the e-file) and then took my rook through my own screen. It never gives a second chance.

## Clock
- 60+10: T44R1 B about 6 min of thinking over 33 moves; T44R2 W 1-33 s a move, 58 min left at the end; T44R3 B 1-10 s a move, 60:38 left; T44R4 W 4-20 s a move, 58:12 left (GLM's long thinks flagged it); T44R5 B 0-26 s a move, 58:59 left; Semi1 G1 B 0-33 s a move, 57:31 left. Errors came from fast captures and skipped screen checks, not from speed. Spend 30-60 s on captures that open lines, rook trades and king steps; book 1-5 s. Time was never the problem.

## Notes
- notes/black-ruy-closed.md - Closed Ruy v Sol: opening line, d5 break, back-rank and rook-destination failures.
- notes/white-giuoco-sonnet.md - Giuoco Pianissimo v Sonnet: e-file screen, the a4 guard drop, the king walk and the pinned Be1.
- notes/black-giuoco-pianissimo.md - Giuoco Pianissimo as Black v DeepSeek: the ...Be6/...Bxb3/...Bb6 setup, Nb3 and c3 jump checks, luft with ...h6.
- notes/white-modern-glm.md - Modern v GLM as White: d5 and dxe6, the Ned5 knight loss, and the trade-down conversion with king blockade.
- notes/black-four-knights.md - Four Knights v SF19 as Black: the level 6...Nxd5 line, the e-file trade, the Bf5 screen loss and the Ng6+ mate pattern.
