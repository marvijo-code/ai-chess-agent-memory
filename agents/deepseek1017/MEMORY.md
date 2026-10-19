# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries forfeit. T47R1 had 3 invalid attempts (two on 12.f5, two on 13.Nxf5) and burned minutes. T48R1 had 2 invalid tries on king moves (46.Kc4, 47.Kb5/Kxa5). T49R1 wasted one on O-O with my Ng8 still at home. Before sending a king move, list its legal squares and flights; before CASTLING check the three squares are as required - king and rook unmoved, and for O-O f8 AND g8 empty (f1 AND g1 as White). After ONE rejection redraw and pick a different move, never resend.
- Qg3 + HIS BISHOP REACHING e5/f6 = Qxg7#. T48 Final: my Kg8 had g7 guarded by the king ALONE; 13...dxe5?? opened f4-e5, 14.Bxe5 put queen and bishop on g7, 14...Qd8?? 15.Qxg7#. With his queen on g3 and a bishop on f4/h6/c1, before every central capture or push write which diagonal lets a bishop cover g7; put a PIECE on g7 (get a bishop to f6/d6 geometry) or decline the break. A loose central pawn is never worth a mate net on g7.
- A QUICK MOVE STILL GETS THE SCAN. T48 Final was played at 5-20 s a move, 59:49 left, 0 illegal; the mate came from a skipped g7 audit, not the clock. Speed is fine only if the per-move list is still written.
- A LANDING SQUARE IS A CAPTURE SQUARE. 16.Nd6?? walked into ...Bxd6; and T49R1 12...Nd5?! put my knight where his Nc3 recaptured: Nxd5 exd5 only fixed HIS e5 pawn. Before a knight jump list every enemy piece that captures the arrival square and whether the exchange helps me or him.
- TEMPO ATTACKS NEED A CHECK SCAN. 14.Bf4? hit Qc7 but ...Bc5+ came with tempo, forcing Kh1 and ...Qd8. Attacking a queen only gains time if he has no check or counter-capture.
- CHECKED? List block/capture squares and which of my pieces sit on the checker's diagonal; T47R1 14...Bc5+ was answered correctly only by 15.Kh1 (Qe3?? and Nd4?? lose material). A king step that keeps my bishop attacking his queen is ideal.
- COUNT ATTACKERS v DEFENDERS, not the word 'defended'. 19.Nxe4 won a whole knight: Qe3 and Nc3 both hit e4, only Nc6 defended.
- QUEEN TRADE = RECAPTURE CHAIN ON MY CENTRAL KNIGHT. T48R1 11.Qd2?? blocked ...Qa5+ but met ...Qxd2+; after Kxd2, ...Nxd4 Bxd4 Bxd4 won a bishop. Block with a guarded piece (Bd2/c3) or keep queens; verify the block and the whole chain.
- UP MATERIAL: simplify only when it removes his counterplay; otherwise keep active pieces and pick up free units.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. T47R1 spent 2:45 on 12.f5 and 3:45 on 14.Bf4 without finding anything; 2-4 min thinks are a diagnosed loss mode. My losses are scan misses, not the clock; keep the pace, never skip the audit. T49R1: opponent burned 6:07 on 12.e5, I used 1-8 s a move and had 61:36 left.

## Opening: Open Sicilian Taimanov (both colours)
- Same structure either way: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nc6 5.Nc3 a6 6.Be2 Be7 7.O-O Nf6 8.Be3 O-O then f4/Qd2/Rad1 (White) or ...Qc7/...b5/...Bb7/...Rfc8 (Black).
- As WHITE BAN premature f4-f5: 12.f5? met ...exf5, opening the e-file for his Re8 and leaving e4 hit twice. Keep the tension with Qe1/Qg3, Rf3; push f5 only with e4 double-guarded. Watch ...Bb4, ...Nxd4 (recapture with B), ...d5, ...b5.
- As BLACK v 9.f4/10.Qd2 (T49R1): 10...Nxd4 11.Bxd4 b5 then ...Bb7/...Rfc8 is sound; ...Qc7 covers c6 and eyes e5. Do NOT jump ...Nd5 into his Nc3 (12...Nd5?! Nxd5) unless the pawn structure after the recapture favours me - here it only fixed his e5 pawn. Prefer ...Bb7/...d6/...Rfc8 first. His 12.e5 gain of space is answered by hitting e5, not by trading into his plan.

## Opening: Taimanov as BLACK v Stockfish
- Played: 1.e4 c5 2.Nf3 Nc6 3.Nc3 e6 4.d4 cxd4 5.Nxd4 Nf6 6.Nxc6 bxc6 7.e5 Nd5 8.Qf3 Nxc3 (16 plies); then 9.bxc3 Be7 10.Be2 O-O 11.O-O Qc7 12.Bf4 d6. Level to move 12.
- 8...Nxc3 9.bxc3 handed White the big centre (+0.20 -> +0.47) and the d5-knight was not really attacked: take that exchange only for a concrete reason, ...Be7/...Qc7 first.
- After 13.Qg3 do not take ...dxe5 (g7 mate net, T48 Final). Cover g7 with a piece first.

## Opening: Open Sicilian vs Stockfish Dragon ...g6
- Played: 1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.Nc3 Bg7 6.Be3 Nf6 7.Be2 d5 8.exd5 Nxd5 (16 plies). Then 9.Nxd5 Qxd5! 10.Bf3 Qa5+ : do NOT block with 11.Qd2?? (...Qxd2+ Kxd2 ...Nxd4 Bxd4 Bxd4 wins a bishop). Consider a guarded block (Bd2/c3) or keep queens.

## Opponents
- Stockfish 19 (depth 4): instant, no second chances. As White v my Taimanov: 6.Nxc6, 7.e5, 8.Qf3, Bf4 then Qg3 - it pounces on any capture that opens a bishop to g7. As Black vs my Open Sicilian it played Dragon ...g6/...Bg7/...d5, met Bf3 with Qa5+, and traded queens into ...Nxd4/...Bxd4.
- DeepSeek V4.1 Flash (other instance, T49R1): long single thinks (6:07 on 12.e5) then engine failure; forfeits readily. Its play is a mirror of mine: castled Taimanov, f4/Qd2, tries to gain space with e5. Plan: guard every unit, take free captures, 10-15 s sound moves and let its clock run.
- GLM 5.3 Flash: slow multi-minute thinks, illegal tries, forfeits readily; grabs pawns when lost. 10-15 s sound moves, guard everything.

## Record
- T47R1 White v GLM: 1-0 by forfeit (3 invalid replies), one piece up after 19.Nxe4.
- T48R1 White v Stockfish 19: 0-1 checkmate. 11.Qd2?? lost a bishop after the queen trade; two invalid king tries.
- T48 Final Black v Stockfish 19: 0-1 (Qxg7# m15). 13...dxe5?? and 14...Qd8??; level to move 12.
- T49R1 Black v DeepSeek V4.1 Flash: 0-1 win by forfeit at move 13 (opponent engine failure); 1 illegal try (O-O with Ng8 home); 61:36 left.

Note files:
- notes/stockfish-dragon-queen-trade.md - SF19 Dragon ...d5, the Qd2?? queen trade and king-move legality.
- notes/taimanov-black-g7-battery.md - SF19 as White in the Taimanov, the dxe5/Bxe5/Qxg7 mate and the g7 audit.
