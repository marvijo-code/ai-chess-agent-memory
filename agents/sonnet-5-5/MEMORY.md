# MEMORY (chess tournament; clocks seen: 600+10 and 900+10; Armageddon: White 10 min, Black 7:30 + draw odds)

## Record
- G1 (W vs DeepSeek): 1-0 on time. Closed Ruy.
- G2 (W vs Stockfish): 0-1. 1.e4 c5 2.Nf3 Nc6 3.Bb5 Nf6 4.e5 Nd5 5.O-O Nc7 6.Bc4? b5 7.Bb3?? c4 trapped the bishop.
- G3 (B vs Sol): 0-1. Chigorin gave +B+2P, then 42...Qe6?? 45...Bd4+?? threw it away.
- G4 (B vs Sol): draw (Sol flagged). Lost after 27...Kh7?, 28...exf4?, 30...a5??, 31...b4?? 32.e5!. notes/black-ruy-chigorin.md.
- G5 (W vs Sol, Armageddon): 1-0, mate 32. 4.d3 anti-Berlin. notes/white-ruy-d3.md.
- G6 (B vs Stockfish): 0-1 in 25. 3.Nc3 Nf6 4.Bb5 Bb4 ... 9...bxc6? notes/black-four-knights.md.
- G7 (T2 R1, B vs Stockfish): 1/2 (threefold move 69, piece down). 8...d6?? 9.f4!.
- G8 (T2 R2, W vs Sol): 1-0, back-rank mate 24. 4.d3 line.
- G9 (T2 R3, W vs DeepSeek): 1-0, mate 53. Closed Ruy. notes/white-closed-ruy.md.
- G10 (T2 Final, W vs Stockfish): 1/2 threefold move 81, down R+B. 23.Rc2?? lost a rook. notes/sicilian-plan.md.
- G11 (T2 Armageddon decider, B vs Stockfish): 0-1, mate move 34. Caro-Kann Advance 7...Nbc6?? 8.Nb5! (Nd6+/Nxf7 fork), later 33...Bf7?? Rxf7#. notes/black-caro-kann.md.

## Key lessons (read before EVERY move)
- Output: only the JSON move object. Illegal moves count as attempts (max 3). Check destination is not my own piece and no own piece blocks the line.
- PROTECTED-SQUARE CHECK (G10, G11): for every move, name the piece that recaptures on the destination square, and which enemy rook/queen/bishop attacks it (G11: Bf7 into Rxf7#). Write 'if ...Rxc2 then X takes' with X's exact path. If I cannot name X, do not play it.
- KNIGHT-JUMP CHECK (G11, cost the game): before developing or pushing a pawn (...c5, ...Nbc6, ...a6), ask where an enemy knight can land (b5, d6, c7, f7, e5, d5) and what it forks (K+Q, Q+R). Holes appear on d6/e6/f7 once I push ...c5/...e6 and Bf5 leaves. Compute forced lines 3 plies for every enemy knight outpost. Stockfish's depth 4 finds these every time.
- BLUNDER CHECK: for the intended move (1) list every enemy piece that can capture on the destination; (2) list enemy checks, captures, discovered checks, pawn pushes (f4! e5! c5! b5! c4!), knight forks; (3) what does the move leave undefended or block?
- GREED CHECK (G10): no wing-pawn raids with a knight; keep pieces connected.
- RECAPTURE CHECK (G9): before any capture or trade, who recaptures, and does one of MY pieces block the line?
- RETREAT-SQUARE CHECK (G2, G7): which of my pieces can be hit by a pawn push (f4, e5, c4, b5) and where would it go? Never fill my own bishop's retreat square.
- PIN/FILE CHECK (G6, G7, G11): do not leave a knight pinned to the queen (Ne7 vs Bg5) or put pieces where a rook/bishop pins them.
- KING SAFETY: no king behind a pawn on a diagonal/file with an enemy bishop/rook behind it. Keep luft. Check luft for both kings.
- Do not give a check just because it is a check. Ask who recaptures.
- OPENING DISCIPLINE (G6, G7, G11 all lost at moves 7-9 in lines I did not know): play only lines I know move by move. As Black vs Stockfish, prefer the line with prepared notes and slow down at moves 5-10 (60-90 s), not 15 s. If unsure: simplest developing/castling move, keep bishops safe.
- TIME: 60-90 s on moves 6-12 when unsure, and whenever a piece can be attacked, a pin/fork is possible, or I offer a trade. 1-8 s on book moves. In Armageddon Black has 7:30, but still spend 40-60 s at the first critical move; G11 I used 15-19 s there and later burned time in a lost position.
- When ahead: trade pieces only after the blunder check; keep simple. In won endings check stalemate each move.
- WHEN LOST: play fast, safe legal moves. Stockfish drew by repetition in G7/G10 but did NOT in G11 (it kept attacking and mated). Do not count on repetition: keep king covered, avoid moving pieces to squares on open files (Rf1 vs f7).
- BISHOP SAFETY: list escape squares after ...b5, ...c4, ...a6, ...d5, f4.
- Armageddon as White (draw loses): solid d3/c3 setup, trade queens only if safe, let Sol err. As Black (draw wins): choose the safest known setup.
- Opening as White vs 1...e5: vs 3...Nf6 play 4.d3 (notes/white-ruy-d3.md); vs 3...a6 closed Ruy (notes/white-closed-ruy.md). Vs 1...c5: 2.c3 is fine (notes/sicilian-plan.md).
- Opening as Black vs 1.e4: 1...e5 (notes/black-ruy-chigorin.md; vs Stockfish's 3.Nc3 see notes/black-four-knights.md). 1...c6 Advance: see notes/black-caro-kann.md before using again.

## Opponents
- DeepSeek V4.1 Flash: Chigorin Ruy as Black quickly, then 40-50 s/move; time trouble by move 25; blunders pieces, tries illegal moves. Stay solid, convert safely.
- Stockfish 19 (depth-4 ladder): instant moves. As White: 1.e4, 2.Nf3, 3.Nc3 vs 1...e5; vs Caro-Kann plays 2.d4 3.e5 4.Be2 5.Nc3 6.a3 7.Bg5 8.Nb5 and finds knight forks. As Black: 1...c5; vs 2.c3 it plays 2...d5 (equal). Finds trapping pawn pushes, pins and forks; takes any free material; may shuffle into repetition when winning but converts when I stay passive.
- GPT-6.1 Sol: as White main-line Ruy with kingside battery (Nf1-g3, Be3, Rc1, d5, Bb1, Nh4-f5, f4, Re3-g3, e5), finds sacrifices (Nxg7+). As Black Berlin-style or ...Bc5/...Ba7 setups vs 4.d3; gets passive and blunders. Thinks 5-60 s.

## Notes files
- notes/sicilian-plan.md: White vs 1...c5: G2 loss, G10 Alapin game and the Rc2?? blunder.
- notes/black-ruy-chigorin.md: Black Chigorin lines from G3/G4.
- notes/white-ruy-d3.md: G5/G8 winning 4.d3 lines vs Sol.
- notes/white-closed-ruy.md: G9 closed Ruy win, Qxd4?? recapture lesson, rook-ending mate technique.
- notes/black-four-knights.md: G6/G7 losses vs Stockfish's 3.Nc3.
- notes/black-caro-kann.md: G11 Advance Caro-Kann loss, Nb5/Nd6+ fork pattern.
