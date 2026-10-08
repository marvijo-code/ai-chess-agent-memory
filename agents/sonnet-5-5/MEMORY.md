# MEMORY (chess tournament; clock seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- G1 (W vs DeepSeek V4.1 Flash): 1-0, won on time. Closed Ruy.
- G2 (W vs Stockfish 19): 0-1. 1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5 7.Bb3?? c4 trapped the bishop.
- G3 (B vs GPT-6.1 Sol): 0-1, mate move 67. Chigorin gave me +B+2P, then 42...Qe6?? and 45...Bd4+?? threw it away.
- G4 (B vs Sol): draw (Sol flagged vs my bare king). Lost after 27...Kh7?, 28...exf4?, 30...a5??, 31...b4?? 32.e5!. See notes/black-ruy-chigorin.md.
- G5 (W vs Sol, Armageddon): 1-0, mate move 32. 4.d3 anti-Berlin Ruy, queens off, Sol blundered a piece. See notes/white-ruy-d3.md.
- G6 (B vs Stockfish 19, final): 0-1, mate move 25. 1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 bxc6? and I drifted: eval +2 by move 12, +5 by 17. See notes/black-four-knights.md.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Check the destination is not occupied by my own piece.
- BLUNDER CHECK (all lost games came from skipping it): for my intended move, (1) list every enemy piece, ROOKS AND BISHOPS BEHIND PAWNS INCLUDED, that can capture on the destination; (2) list all enemy checks, captures, discovered checks, pawn pushes (e4-e5!, c4-c5! hitting a bishop) after the move; (3) say what the move leaves undefended. Count attackers vs defenders on every contested square.
- PIN/FILE CHECK (G6): never put a bishop/knight on a file where the enemy can double rooks against it while my own rook is behind it (17...Be7 18.Re3 19.Rfe1 won the exchange). Before retreating a piece attacked by a pawn, count the enemy heavy pieces that can reach that file in 2 moves.
- KING SAFETY: no king on a diagonal/file behind a pawn when an enemy bishop or rook sits behind it (Kh7 vs Bb1+e4). Watch back-rank and h6/g7 mates once pawns are broken (...gxf6 plus Bh6+ and Re8+ mated me in G6). Keep luft.
- Do not give a check just because it is a check (45...Bd4+ lost a bishop). Ask who recaptures.
- OPENING DISCIPLINE: play only lines I know move by move; if unsure at move 5-9, pick the simplest developing move (Bc5/d6/O-O, recapture toward the centre with pawns d/e) not a clever one. Do not recapture away from the centre (9...bxc6) without a concrete reason, and do not shuffle the queen/bishop (Qe8, Qe6, Bd6, Bb7) while White develops with tempo.
- TIME: I used only ~2.5 min of 15 in G6. Spend 60-90 s when a piece is attacked, a pin is possible, I am worse, or I offer a trade. 5-20 s elsewhere.
- When ahead: trade pieces only after the blunder check; keep a simple, safe move. In endings: king to the centre, keep knights defended, look for mating nets.
- BISHOP SAFETY: before bishop moves, list escape squares after ...b5, ...c4, ...a6, ...d5. Prefer Bf1, Bc2 or Bxc6 early.
- Stockfish plays instantly and punishes any hung piece or structure damage; no swindles. Its move comments say depth 4: it sees 2-3 move tactics, so it will not fall for deep traps, but it grows every small plus. Stay solid, avoid doubled pawns/queen trades that wreck my structure, give no tempo.
- NEVER resign mentally: when lost, play fast, safe, legal moves and keep a pawn alive (a flag vs a bare king is only a draw). Better: avoid lost positions.
- Armageddon as White (a draw loses): do not force things. Solid d3/c3 setup, trade queens only if safe, let Sol err.
- Opening as White vs 1...e5: vs 3...Nf6 play 4.d3 (notes/white-ruy-d3.md); vs 3...a6 closed Ruy 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 O-O 8.c3 d6 9.d4.
- Opening as White vs 1...c5: notes/sicilian-plan.md.
- Opening as Black vs 1.e4: 1...e5; vs 2.Nf3 Nc6 3.Bb5 use the Chigorin (notes/black-ruy-chigorin.md); vs 3.Nc3 see notes/black-four-knights.md.

## Opponents
- DeepSeek V4.1 Flash: slow (20-40 s a move), time trouble by move 20, blunders pieces and tries illegal moves. Keep solid.
- Stockfish 19 (depth-4 ladder): instant, tactically precise, as White plays 1.e4 and 3.Nc3 Vienna/Four Knights with 4.Bb5 and 6.Nd5, as Black answers 1.e4 with 1...c5; finds trapping pawn pushes and pins.
- GPT-6.1 Sol: as White plays main-line Ruy and builds a kingside battery (Nf1-g3, Be3, Rc1, d5, Bb1, Nh4-f5, f3-f4, Re3-g3, e5) and finds sacrifices (Nxg7+). As Black it plays Berlin-style ...Nf6/...Bc5, ...d5 and trades queens. Thinks 5-60 s a move, burns clock, blunders (Qxg5+?, Rg3??, 19...Nxe4??). Play solidly, count attackers, wait for errors.

## Notes files
- notes/sicilian-plan.md: safe White setups vs 1...c5 and the G2 loss.
- notes/black-ruy-chigorin.md: Black Chigorin lines from G3 and G4, good setups and the blunders.
- notes/white-ruy-d3.md: G5 winning line with 4.d3 vs Sol and the endgame plan.
- notes/black-four-knights.md: G6 loss vs Stockfish in the Four Knights 6.Nd5 line, what to do instead.
