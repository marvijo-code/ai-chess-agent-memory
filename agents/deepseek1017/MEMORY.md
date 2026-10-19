# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries on ONE move forfeit. T47R1 had 3 invalid attempts and burned minutes. T48R1 had 2 invalid tries on king moves. T49R1 wasted one on O-O with my Ng8 still at home. T49 Final had 3 separate invalid tries. T50R2 had one illegal try on 8.Be3 (a 2-second book move). Before sending, list the piece's CURRENT square, destination and path; before CASTLING check king and rook unmoved and the two squares empty. After ONE rejection redraw, pick a DIFFERENT move, never resend.
- A CAPTURE THAT LEAVES HIM A PIECE AHEAD IS A SAC, NOT A TRADE. T50R2 11.Nxd5?? - I wrote 'knight-for-knight and a clean pawn', but d5 was guarded by Nf6: 11...Nxd5 took my knight, HIS knight stayed on d5, and 12.Bf3 only attacked it (defended, it retreats or trades on its terms). ATTACKING A DEFENDED PIECE WINS NOTHING. After every capture chain write 'W pieces / B pieces' from the board; never NxP on a defended square unless a named recapture wins the piece back.
- QUEEN NEVER LANDS ON A PAWN'S CAPTURE SQUARE. T49R4 21.Qd3?? cxd3! won my queen for a pawn. T50R2 16.Qh6?? gxh6 - the g7-pawn's capture squares are f6 and h6; I counted 'a second attacker on g7' and never asked whether g7 simply takes h6. Before every queen move write every enemy pawn's two capture squares FROM THE BOARD; a pawn 'defender' does not make the square safe, the pawn is taken.
- THE PIECE I MOVE MAY BE g7's ONLY GUARD. T49R1 (Taimanov B v SF): my king on e8, his Qg3+Ne4 aimed at g7, and Bf8 was the ONLY guard; 10...Be7? stepped it off - 11.Qxg7 Bf8 12.Qxh8 won a whole ROOK. An UNCASTLED king never guards g7, and ...h6 is luft only for a king on g8. Before any ...Be7/...Bd6/...Bf8 step with his queen near g3 write 'what guards g7 after this?' - or castle.
- A WARNING I WRITE IN MY NOTES IS AN ORDER FOR THE NEXT MOVE. T49R1 my own comment said 'watch that Nf6+ jump and my uncastled king', and I played ...Nb4?? anyway. Re-read the last comment before choosing.
- COUNT EVERY DEFENDER BEFORE ANY CAPTURE - FULL DIAGONALS BOTH WAYS. T49R2 (Dragon): 10.Qxg4?? took an 'undefended' Ng4, but his Bc8 guarded g4 through d7-e6-f5; 10...Bxg4 won my QUEEN for a knight. 'Undefended' is a count of NAMED pieces, never a word; sweep his queen's and BOTH bishops' diagonals to the landing square plus every pawn/knight.
- A PAWN-ATTACKED PIECE MUST MOVE; DEFENDING IT DOES NOT SAVE IT. T49R3 12.exf6! won a knight for a pawn - his Nf6 was 'defended twice' (Be7 and g7) and still lost, because a pawn capture of a piece is material whatever recaptures. Mirror image: when HIS pawn attacks my piece, move it; when MY pawn attacks his, take it.
- QUEEN OR ROOK LANDING ON HIS BACK RANK: WALK BOTH HIS BISHOPS' DIAGONALS AND EVERY SLIDER TO THE SQUARE. T49R3 18.Qxd8+?? - his Bf6 covered d8; 18...Bxd8. A check is not a forcing win; UP MATERIAL THERE IS NO QUEEN GRAB.
- Qg3 + HIS BISHOP REACHING e5/f6 = Qxg7#. T48 Final: 13...dxe5?? 14.Bxe5 15.Qxg7#. With his queen on g3 and a bishop on f4/h6/c1, before any central break write which diagonal covers g7; put a PIECE on g7 or decline the break.
- A QUICK MOVE STILL GETS THE SCAN. T48 Final was 5-20 s a move, 0 illegal, and lost to a skipped g7 audit. T50R2 was 1-2 s book moves with one illegal try. Speed is fine only if the per-move list is written.
- A LANDING SQUARE IS A CAPTURE SQUARE. 16.Nd6?? Bxd6; T49R1 12...Nd5?! into Nc3. Before a knight jump list every enemy piece that captures the arrival square and whether the exchange helps me.
- CHECKED? List block/capture squares and which of my pieces sit on the checker's diagonal. A king step that keeps a piece attacking his queen is ideal.
- QUEEN TRADE = RECAPTURE CHAIN ON MY CENTRAL KNIGHT. T48R1 11.Qd2?? met ...Qxd2+ then ...Nxd4/...Bxd4 won a bishop. Block with a guarded piece (Bd2/c3) or keep queens.
- DOWN A QUEEN OR PIECE v SF: no rescue, guard every unit, 5-10 s moves - it mates within ~15 moves. v the MIRROR DeepSeek it converts a piece-up position cleanly too: trade nothing into its attack, take only free units, and check the rank-1 mate every move.

## Endings and king safety
- KING ON h1 + HIS QUEEN ON g3 = HIS ROOK ON e1 IS MATE. T50R2 30...Re1#: my own h3/g3 were no luft because Qg3 covers h2 and g2. After my king goes to h1 with his queen near g3, name the rank-1 squares his rooks reach and keep a rook or pawn on e1/e2.
- TWO ROOKS (or R+R+N) v QUEEN: draw by blockade, not by raids. T49R3 held it: one rook on the f-file, one on d1 covering e1, knight on c3 shielding b2/a2. T49R4 with 2R+N v Q+pawns: keep one rook on d1 vs the passed d-pawn, the other active (Rc7), take the bishop when loose.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. My losses are scan misses, not the clock. T49R1: opponent burned 6:07 on one move, I used 1-8 s and had 61:36 left. T49R3: ~46 min left at the end. T49R4: ~55 min, GLM flagged at 0:46. T50R2: ~53 min left at mate while the mirror spent 1:04-8:23 a move. Never a time problem - long thinks and bad moves are.

## Opening: Open Sicilian Taimanov (both colours)
- 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- T49R3 WHITE plan that worked: 9.Qd2 b5 10.f4 Bb7 11.e5 Qc7 12.exf6! (8 plies) 12...Bxf6 13.Nxc6 dxc6 14.Rad1 - a clean piece up by move 13. BAN premature f4-f5 (12.f5? met ...exf5).
- T50R2 WHITE, the ...d5 answer: 9.Qd2 d5 10.exd5 exd5 and then d5 is guarded by Nf6 AND Qd8 - hit it with Nxc6/Bd3/Nb3 or trade the f6-knight FIRST; NEVER 11.Nxd5?? (Nf6xd5 = knight for a pawn; I went -2 and lost).
- T49R4 (same plan v GLM): 12.Nxc6! worked because after ...Nxe4?? the in-between 13.Nxe7+ Qxe7 keeps c6 and then 14.Nxe4 wins a piece. When HIS knight takes a pawn and hits my queen, a check or capture of a bigger unit beats resolving the queen attack.
- As BLACK v 9.f4/10.Qd2: 10...Nxd4 11.Bxd4 b5 then ...Bb7/...Rfc8 is sound; ...Qc7 covers c6 and eyes e5. Do NOT jump ...Nd5 into his Nc3 unless the recapture structure favours me.

## Opening: Open Sicilian Dragon (me White)
- Played T49R2: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Bc4 d6 8.Bb3 Ng4 (16 plies). The knight on g4 is GUARDED BY Bc8 (d7-e6-f5). Answer ...Ng4 with h3 or 9.Nxc6 bxc6 10.Bg5/h3; NEVER Qxg4.
- T48R1 Dragon ...d5: 8.exd5 Nxd5 9.Nxd5 Qxd5! 10.Bf3 Qa5+ - do NOT block with Qd2?? (...Qxd2+ Kxd2 ...Nxd4 Bxd4 Bxd4 wins a bishop). Use a guarded block (Bd2/c3).

## Opening: Taimanov as BLACK v Stockfish
- Played: 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies); then 9.bxc3 Be7 10.Be2 O-O 11.O-O Qc7 12.Bf4 d6. Level to move 12.
- 8...Nxc3 9.bxc3 handed White the big centre (+0.20 -> +0.47): take that exchange only for a concrete reason. After 13.Qg3 never ...dxe5 (g7 mate net).
- T49R1, same line with 8...Qc7 9.Qg3 h6 10.Ne4 (6 plies): my king still on e8, so ONLY Bf8 guarded g7. 10...Be7? - 11.Qxg7 Bf8 12.Qxh8 won a ROOK. ...h6 is luft only for a king on g8; ...O-O or Bf8 staying home was the move.
- Down a whole rook (12.Qxh8): 12...Nb4?? after 5:28 lost to 13.Nf6+ 14.Qxf8#. No counterplay grabs down material; audit his knight landings for check+mate.
- T49 Final, same ...bxc6 Taimanov: 11...O-O? was the losing slip. 12.Bxc6! won my a8 rook: after ...bxc6 the c6 pawn has no recapturer (b7 empty, Bc8 and Qd8 miss c6). Guard c6 with ...Qc7 BEFORE castling; then Bxc6 is met by ...Qxc6.

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. Punishes any piece I call 'undefended' or 'loose' - it has a hidden defender (T49R2 Bc8-g4). As White v my Taimanov: 6.Nxc6, 7.e5, 8.Qf3, Bf4 then Qg3, pouncing on any capture that opens a bishop to g7; Bxc6! hits the a8 rook when c6 is unguarded (T49 Final). As Black vs my Open Sicilian: Dragon ...g6/...Bg7/...d6/...Ng4, and vs ...d5 lines Qa5+ with a queen trade. Once a queen up it mates cleanly.
- DeepSeek V4.1 Flash (the mirror, T49R1 and T50R2): as Black it plays the Taimanov solidly, thinks 1:04-8:23 a move but uses the time well, converts a piece-up position without gifts (T50R2 11...Nxd5 12...Nxd4 13...Be6 14...Qd7, then 30...Re1#), and keeps every unit guarded - unlike the other DeepSeek instance it does not forfeit. Treat it as strong opposition: my losses to it were my own blunders (T50R2 Nxd5??, Qh6??), so win on the checklist, not on its clock.
- GLM 5.3 Flash: slow multi-minute thinks that burn its clock to seconds while I keep 40-55 min; illegal tries; takes free material when offered. It calls a piece 'undefended' without checking an in-between check (T49R4 12...Nxe4?? allowed 13.Nxe7+). Play 10-15 s sound moves, guard every unit, take free captures, let its clock run.

## Record
- T47R1 White v GLM: 1-0 by forfeit (3 invalid replies), one piece up after 19.Nxe4.
- T48R1 White v Stockfish 19: 0-1 checkmate. 11.Qd2?? lost a bishop after the queen trade; two invalid king tries.
- T48 Final Black v Stockfish 19: 0-1 (Qxg7# m15). 13...dxe5??; level to move 12.
- T49R1 Black v DeepSeek V4.1 Flash: win by forfeit at move 13 (opponent engine failure); 1 illegal try (O-O with Ng8 home).
- T49R2 White v Stockfish 19: 0-1 checkmate m28. 10.Qxg4?? lost my queen to ...Bxg4 (Bc8 defended g4).
- T49R3 White v GLM 5.3 Flash: 1/2 threefold. +piece after 12.exf6!; 18.Qxd8+?? Bxd8 gave queen for rook; then held two rooks v queen.
- T49R4 White v GLM 5.3 Flash: 1-0 on time. +piece after 12.Nxc6 13.Nxe7+ 14.Nxe4; 21.Qd3?? cxd3! threw back a queen; GLM flagged at 0:46.
- T49 Final Black v Stockfish 19: 0-1 checkmate. 11...O-O? allowed 12.Bxc6! winning the a8 rook; ...Qc7 guarded c6.
- T50R1 Black v Stockfish 19: 0-1 checkmate m14. 10...Be7? left g7 unguarded (king on e8), 11.Qxg7 Bf8 12.Qxh8 won a rook; 12...Nb4?? lost to 13.Nf6+ 14.Qxf8#.
- T50R2 White v DeepSeek V4.1 Flash (mirror): 0-1 checkmate m30. 11.Nxd5?? = knight for a pawn (Nf6 recaptured and stayed); 16.Qh6?? gxh6 lost my queen; 30...Re1# (Kh1, his Qg3 covers h2/g2). 1 illegal try, ~53 min left.

Note files:
- notes/stockfish-dragon-queen-trade.md - SF19 Dragon ...d5, the Qd2?? queen trade and king-move legality.
- notes/taimanov-black-g7-battery.md - SF19 as White in the Taimanov, the dxe5/Bxe5/Qxg7 mate and the g7 audit.
- notes/white-dragon-yugoslav.md - T49R2: the Ng4/Bc8 trap and the correct ...Ng4 answers.
- notes/white-taimanov-qd2-f4.md - T49R3: the Qd2/f4/e5/exf6 plan and the two-rooks-v-queen draw.
- notes/white-taimanov-glm-t49r4.md - T49R4: the Nxe7+ intermezzo, the Qd3?? cxd3 loss, GLM's clock.
- notes/black-taimanov-c6-guard.md - T49 Final: ...O-O? before ...Qc7, Bxc6 wins a8.
- notes/black-taimanov-g7-guard.md - T50R1: uncastled king, Bf8 the only g7 guard, ...Be7? loses a rook.
- notes/white-taimanov-mirror-t50r2.md - T50R2: the Nxd5?? sac, the Qh6?? gxh6 queen loss and the Re1# back-rank net.
