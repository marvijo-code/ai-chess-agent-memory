# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries forfeit. T47R1 had 3 invalid attempts and burned minutes. T48R1 had 2 invalid tries on king moves. T49R1 wasted one on O-O with my Ng8 still at home. Before sending a king move list its legal squares and flights; before CASTLING check the three squares - king and rook unmoved, f8/g8 empty (f1/g1 as White). After ONE rejection redraw, pick a DIFFERENT move, never resend.
- COUNT EVERY DEFENDER BEFORE ANY CAPTURE - FULL DIAGONALS BOTH WAYS. T49R2 (Dragon): 10.Qxg4?? took an 'undefended' Ng4, but his Bc8 guarded g4 through d7-e6-f5; 10...Bxg4 won my QUEEN for a knight (+8.6, then mate m28). 'Undefended' is a count of NAMED pieces, never a word; sweep his queen's and BOTH bishops' diagonals to the landing square plus every pawn/knight. Kick such a knight with h3/f3 or Bg5, or trade it (Nxc6) instead.
- A PAWN-ATTACKED PIECE MUST MOVE; DEFENDING IT DOES NOT SAVE IT. T49R3 12.exf6! won a knight for a pawn - his Nf6 was 'defended twice' (Be7 and g7) and still lost, because a pawn capture of a piece is material whatever recaptures. This is the mirror of the Ng4 miss: when HIS pawn attacks my piece, move it; when MY pawn attacks his, take it.
- QUEEN OR ROOK LANDING ON HIS BACK RANK: WALK BOTH HIS BISHOPS' DIAGONALS AND EVERY SLIDER TO THE SQUARE. T49R3 18.Qxd8+?? - his Bf6 covered d8; 18...Bxd8 19.Rxd8 Rxd8 turned a +piece into queen-for-rook. A check is not a forcing win, and UP MATERIAL THERE IS NO QUEEN GRAB: name every attacker of the landing square first.
- Qg3 + HIS BISHOP REACHING e5/f6 = Qxg7#. T48 Final: Kg8 had g7 guarded by the king alone; 13...dxe5?? 14.Bxe5 15.Qxg7#. With his queen on g3 and a bishop on f4/h6/c1, before any central break write which diagonal covers g7; put a PIECE on g7 or decline the break.
- A QUICK MOVE STILL GETS THE SCAN. T48 Final was 5-20 s a move, 0 illegal, and still lost to a skipped g7 audit. T49R3 was 1-2 s book moves; the one miss (Qxd8+) came where I did not write the list. Speed is fine only if the per-move list is written.
- A LANDING SQUARE IS A CAPTURE SQUARE. 16.Nd6?? Bxd6; T49R1 12...Nd5?! into Nc3. Before a knight jump list every enemy piece that captures the arrival square and whether the exchange helps me. An attack on his queen gains time only if he has no check or counter-capture (T47R1 14.Bf4? ...Bc5+).
- CHECKED? List block/capture squares and which of my pieces sit on the checker's diagonal; T47R1 14...Bc5+ was answered only by 15.Kh1. A king step that keeps a piece attacking his queen is ideal.
- QUEEN TRADE = RECAPTURE CHAIN ON MY CENTRAL KNIGHT. T48R1 11.Qd2?? met ...Qxd2+ then ...Nxd4/...Bxd4 won a bishop. Block with a guarded piece (Bd2/c3) or keep queens; verify the block and the whole chain.
- UP MATERIAL: simplify only when it removes his counterplay; otherwise keep active pieces and take free units. No forced-looking queen/rook sacs "to simplify" (T49R3). DOWN A QUEEN v SF: no rescue, guard every unit, 5-10 s moves - it mates within ~15 moves.

## Endings
- TWO ROOKS (or R+R+N) v QUEEN, down material: draw by blockade, not by raids. T49R3 held it: one rook on the f-file, one on d1 covering e1, the knight on c3 shielding b2/a2; every ...Qe1+/...Qe3+ answered by Rf2 or Rd1. Rook excursions behind a g6/h6 pawn wall (23.Rf4?!/24.Rh3?! with tempo on h6) gain nothing - stay on the files that block checks.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. 2-4 min thinks are a diagnosed loss mode (T47R1). My losses are scan misses, not the clock; keep the pace, never skip the audit. T49R1: opponent burned 6:07 on one move, I used 1-8 s a move and had 61:36 left. T49R3: 1-2 s early moves, ~46 min left at the end while GLM fell to 14 s. Never a time problem - bad captures are.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- T49R3 WHITE plan that worked: 9.Qd2 b5 10.f4 Bb7 11.e5 Qc7 12.exf6! (8 plies to here) 12...Bxf6 13.Nxc6 dxc6 14.Rad1 Bf3/Bxb7 - I was a clean piece up by move 13 with two rooks against his queen later. BAN premature f4-f5 (12.f5? met ...exf5 in T48R1 opening the e-file, e4 hit twice); push f5 only with e4 double-guarded. After ...Qc7 the ...b4/...Qc6 queen activity is his main counterplay; keep c2/b2 and the c3-knight named.
- As BLACK v 9.f4/10.Qd2: 10...Nxd4 11.Bxd4 b5 then ...Bb7/...Rfc8 is sound; ...Qc7 covers c6 and eyes e5. Do NOT jump ...Nd5 into his Nc3 (12...Nd5?! Nxd5) unless the recapture structure favours me. Prefer ...Bb7/...d6/...Rfc8 first.

## Opening: Open Sicilian Dragon (me White)
- Played T49R2: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies). The knight on g4 is GUARDED BY Bc8 (d7-e6-f5). Answer ...Ng4 with h3 (then g4 is a target) or 9.Nxc6 bxc6 10.Bg5/h3; NEVER Qxg4. Full Yugoslav (f3/Qd2/O-O-O) only after the g4 knight is dealt with.
- T48R1 Dragon ...d5: 8.exd5 Nxd5 9.Nxd5 Qxd5! 10.Bf3 Qa5+ - do NOT block with Qd2?? (...Qxd2+ Kxd2 ...Nxd4 Bxd4 Bxd4 wins a bishop). Use a guarded block (Bd2/c3) or keep queens.

## Opening: Taimanov as BLACK v Stockfish
- Played: 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies); then 9.bxc3 Be7 10.Be2 O-O 11.O-O Qc7 12.Bf4 d6. Level to move 12.
- 8...Nxc3 9.bxc3 handed White the big centre (+0.20 -> +0.47) and the d5-knight was not really attacked: take that exchange only for a concrete reason; ...Be7/...Qc7 first. After 13.Qg3 never ...dxe5 (g7 mate net).

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. Punishes any piece I call 'undefended' or 'loose' - it has a hidden defender (T49R2 Bc8-g4). As White v my Taimanov: 6.Nxc6, 7.e5, 8.Qf3, Bf4 then Qg3, pouncing on any capture that opens a bishop to g7. As Black vs my Open Sicilian: Dragon ...g6/...Bg7/...d6/...Ng4, and vs ...d5 lines Qa5+ with a queen trade. Once a queen up it mates cleanly.
- GLM 5.3 Flash: slow multi-minute thinks (7:26, 7:50 here) that burn its clock to seconds while I keep ~46 min; illegal tries (1 here: ...Bb7 through its own b7-pawn before ...b5); takes pawns and free material when offered but defends solidly with queen checks; will sit in a fortress and let the game repeat. Play 10-15 s sound moves, guard every unit, take free captures, and keep a draw in hand rather than forcing.
- DeepSeek V4.1 Flash (other instance, T49R1): long single thinks (6:07 on 12.e5) then engine failure; forfeits readily. Mirror of my play: castled Taimanov, f4/Qd2, e5 space gain. Plan: guard every unit, take free captures, 10-15 s sound moves and let its clock run.

## Record
- T47R1 White v GLM: 1-0 by forfeit (3 invalid replies), one piece up after 19.Nxe4.
- T48R1 White v Stockfish 19: 0-1 checkmate. 11.Qd2?? lost a bishop after the queen trade; two invalid king tries.
- T48 Final Black v Stockfish 19: 0-1 (Qxg7# m15). 13...dxe5?? and 14...Qd8??; level to move 12.
- T49R1 Black v DeepSeek V4.1 Flash: win by forfeit at move 13 (opponent engine failure); 1 illegal try (O-O with Ng8 home); 61:36 left.
- T49R2 White v Stockfish 19: 0-1 checkmate m28. 10.Qxg4?? lost my queen to ...Bxg4 (Bc8 defended g4); 0 illegal, ~60 min left.
- T49R3 White v GLM 5.3 Flash: 1/2-1/2 threefold repetition. +piece after 12.exf6!; 18.Qxd8+?? Bxd8 gave queen for rook (0 illegal, ~46 min left); then held two rooks v queen.

Note files:
- notes/stockfish-dragon-queen-trade.md - SF19 Dragon ...d5, the Qd2?? queen trade and king-move legality.
- notes/taimanov-black-g7-battery.md - SF19 as White in the Taimanov, the dxe5/Bxe5/Qxg7 mate and the g7 audit.
- notes/white-dragon-yugoslav.md - T49R2: the Ng4/Bc8 trap, the Qxg4?? queen loss and the correct ...Ng4 answers.
- notes/white-taimanov-qd2-f4.md - T49R3: the Qd2/f4/e5/exf6 plan, the Qxd8+?? Bf6 miss and the two-rooks-v-queen draw.
