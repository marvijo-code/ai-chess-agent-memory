# Chess memory

## Move discipline
- Start with the enemy's last move: changed attacks, pawn controls and opened lines. Scan checks, captures, forks, promotions and mates; repeat on the proposed final board.
- Before Q/R moves or captures, scan enemy pawn/knight captures and EVERY bishop ray. Check, attack and pin do not establish destination safety.
- Name exact defenders, screens and LEGAL recapturers; trace through OWN pieces. Simulate the enemy capture and full exchange, including KING recaptures and rear attackers. Queen-only defense can fail to Qx Qx followed by another recapture.
- Refresh pins after either endpoint moves. Leaving one ray may enter another behind the SAME screen. Relative pins permit moves that lose Q/R.
- Before moving a screen, name BOTH endpoints and exposed targets. Attacking the pinning piece does not prevent capture. A checking piece can block my own rook's protection.
- Track pawn squares and forward AND capture-promotions. Blocked pawns attack diagonally; advances abandon guards. Verify replacement defenders on the final board; g2 still captures h3 until it moves.
- After EVERY capture, refresh the capturer's attacks and vacated lines. Before pawn grabs, test enemy breaks that fork the capturer and another piece.
- When forked, save the higher-value target and compare moves defending both. Before king/Q moves, list guards and screens LOST.
- Before forks/discovered attacks, test enemy checks FIRST. A central knight may screen a mating rook entry. Test captures of EVERY checking/supporting piece before claiming a forced retreat.
- If my calculation rejects a move, do not play it without resolving the named refutation. Sparse marks and a win do not validate every move.

## Clock and conversion
- Deadline INCLUDING output: book/forced 1-5 seconds; quiet 10-15; critical 20-40. Below 5 minutes cap 15; below 90 seconds use 1-3.
- Long thinks do not replace reply calculation. Name a target or break before shuffling; shorten routine endgame maneuvers.
- Ahead: restrain counterplay, simplify safely, preserve mating material. Worse or Black with draw odds: seek activity/repetition. Sacrifice an active rook only for verified promotion or mate.
- Escort passers; count races, captures and blockaders. Minor endings need a target, entry or break. Opposite bishops: count separated passers, blockades and king routes; defend the blocker.
- Use protected checks and restricted exits. Check stalemate after quiet moves/captures; preserve pawn tempi against an immobilized king.

## White openings
- T23 Ruy vs SF: Qb1 Bxf3 gxf3 weakened shelter; doubled g-rooks alone gave no attack. ...g5 supports Nf4: h4 threatens it, h5 abandons capture. Qd4 c6 Qxc4 cxd5 forks Qc4/Be4: Bd3?? dxc4 loses Q.
- T23 Sicilian: Be2/O-O/Be3/f4; ...Nxd4 Bxd4 e5 fxe5 dxe5 Bxe5 wins P. ...Bd6?? Qxd6 Qxd6 Bxd6 wins B. Nf6+ screened Rf1-f7, permitting Kxf7; Nxe8+ restored check. Count liquidation, not imagined mate.
- d3 Ruy: ...Nb4 Bb1 d5 e5 clears Bb1-h7; Qd3 threatens Qh7#, ...g6 answers. ...Bxf3 Rxd8 Rxd8 gxf3 keeps Re1 guarding e5. ...Rd5 f4 Nd4 Be4 saves B with tempo; Bxd4 permits rook activity. Bd5 guards a2; e7 clears Ba2-f7 before promotion.
- Ruy traps: Bh5/Qe2 still share Nf3's screen: Ne5?? Bxe2. Ne5 screens Re6-e1: Nxf7?? Re1#. OWN d4 blocks Qd1-d5: Rxd5?? Qxd5. Ng5 g6 Ne4 Qxe4 Qxe4 Rxe4 loses N to the rear rook.
- Chigorin Bb1/e5 clears b1-h7; Qe4-h7 vacates its own screen. ...dxe5 allowed Qh7+ Kf8 Qh8#; no earlier forced win established.

## Black openings
- T23 SF2 Sonnet Advance: same Bf5/e6/c5/Nc6/Nge7-g6/Be7/Qc7/O-O setup, then ...f6 BEFORE cxd4. c3 screens Qb3-d3: Bd3?? Bxd3 wins B. Rd1 removes Rc1's Nc6-Qc7 pin; OWN Nd2 blocks Rd1-d3. ...c4 attacks Q and guards Bd3. Retaining tension worked here, not a proven opening advantage.
- T23 R3 Advance: Rc1 pins Nc6-Qc7, but Ngxe5 dxe5 Bxe5 wins P. Rfe8 Nf3 Bd6 Bxd6 Qxd6 abandons b7. Qxb7 attacks Ra8/Nc6; Rab8?? Qxc6 Qxc6 Rxc6 loses N: Qd6 alone guarded it. Address loose defenders before chasing Q. ...Rxh3?? gxh3 loses R.
- Caro Classical: dxe4 Nxe4 Bf5 Ng3 Bg6 h4 h6 h5 Bh7; Bd3 Bxd3 Qxd3 e6, Nd7/Ngf6/Be7. h6 supplies h7 and controls g5.
- T22 Sonnet: c5 Bxf6 Bxf6 dxc5 Qc7 b4 a5 a3?? axb4 axb4 Ra1#. dxc5 clears d4; b4 clears b2: Bf6 guards a1/covers b2. Scan FINAL recapture board for mate.
- Advance: develop Bf5 outside chain, challenge with c5/f6. Bg5 pins Ne7-Qd8: Nf5?? Bxd8. ...e5 can leave Qd8 alone guarding d5/Ne4: Qf6?? Rxd5. ...Nxc3 Rxe5 Qd6 bxc3 loses N despite Rc8: Qe3 guards c3.
- ...Rce8 Rxe8 Rxe8 Qxe8+ Qxe8 Rxe8#: count ALL rear attackers; Ng5 bars f7/h7. Qe8 guarded Be7 AND b8; Qf7?? Rb8+ Bf8 pins B. Qxf4?? g3xf4 loses Q.
- QGD: h6/b6/Bb7/Nbd7/c5, cxd5 exd5; Ne5 Nxe5 Bxe5 Bd6 Bxd6 Qxd6; dxc5 bxc5. Bf5 hits Rc8: Rcd8. ...Nxe4 Nxe4 dxe4 clears d5; Qd5+ Qxd5 wins Q without recapturer. ...e3 clears Bb7-g2 for Qxg2#.

## Recurring geometry
- Rbg7+ Bxg7 Rxg7+ Kxg7 gives BOTH rooks for B. Qa7/Nd6 cages Kd8: preserve pawn tempi, Ke5-e6 then Qd7#.
- Benoni Nc3 screens BOTH Qa5-e1 and Rc5-c2; Ne4 exposes both rooks. Bxc5 Rxc5 also clears Be3 from Bh6-Rc1.
- Uncastled Rh8/h5: Bh6 Bxh6 Qxh6 Rxh6 loses Q.
- Passer conversion: ...Re2 Rxe2 dxe2, ...Nd3/Re8, e1=Q+ Nxe1 Rxe1+ removes the blockader. Rf2/Ng4/Kf4 against Kh3: Rh2#; verify the rook's guard and all flights.

## Note files
- notes/accelerated-dragon.md - Rook captures and g-file mate.
- notes/berlin-endgame.md - d3 Ruy, bishop tempi and promotion guards.
- notes/caro-kann-advance.md - Central tension, defenders and passer conversion.
- notes/deepseek.md - Sicilian exchanges, rook screens and conversion.
- notes/four-knights.md - Double attacks, screens and clocks.
- notes/qgd-exchange.md - Benoni screens and defenders.
- notes/ruy-lopez.md - Pawn forks, relative pins and king attacks.
- notes/sicilian-maroczy.md - Recapture guards and promotions.
