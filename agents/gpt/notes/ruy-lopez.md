# Ruy Lopez / Italian: blockers and conversion

## Shared Chigorin structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6.
Preserve Bc2 against ...Nb4/...Nxc2. Recount defenders and trace every recapture through blockers.

## T14 round 2: Black vs DeepSeek, mate win
14.d5 Nb4 15.Bb1! a5! 16.a3 Na6! 17.Nf1 Nc5 18.Be3?! Bd7?! 19.Ng3 Rac8 20.Nf5 Bxf5 21.exf5! Rfe8 22.Bxc5 Qxc5.
- ...a5 vacated a6 for the attacked knight; ...Na6 preserved it and enabled ...Nc5. Both moves were marked only good. ...Bd7 was inaccurate; no best replacement supplied. Do not certify the whole setup from the win.
- ...Qxc5 retained d6 as a blockade of d5. The knight exchange removed Nc5, clearing Rc8's file after the queen moved away.
23.Nd4?? exd4 24.Qxd4 Qxd4 25.Bc2 Rxc2 26.Rxe7 Rxe7 27.Rc1 Qxf2+ 28.Kh1 Qxg2#.
- Nd4 was captured by e5. White's claimed Bxd4 resource was imaginary: its e3 bishop had already exchanged on c5, and Bb1 could not capture d4.
- Qxd4 offered an undefended queen, not a queen trade: after ...Qxd4 no White piece could recapture. Verify the opponent's recapturer before declining an apparent exchange.
- ...exd4 vacated e5 and opened Re1's attack on Be7, but Re8 could recapture on e7. White's Rxe7 therefore lost rook for bishop; the newly opened line did not refute ...exd4.
- After ...Qxd4, c7-c3 were empty. Bc2 landed directly on Rc8's file and ...Rxc2 won it.
- Rc1 attacked Rc2, but ...Qxf2+ answered with check. After Kh1, ...Qxg2# was protected by Rc2 through d2/e2/f2. A rook attack need not force retreat when a forcing mate exists. Do not assume Kh1 was White's only legal king move.
- No invalid attempts; about 16 minutes remained. Book moves gained clock; the critical ...exd4 calculation took 29 seconds.

## T13 round 2: Black vs Sonnet, mate win
After 14.d5 Nb8, ...Nbd7/...Bb7/...b4/...a5 secured c5. 22.Nxf6+ Bxf6! preserved the pawn shield.
- 23.Bd3?? Nxd3 won a bishop: Bd2 blocked Qd1-d2-d3. ...Nxb2 then attacked Qd1; ...Nc4 was guarded by Qc7 through c6/c5.
- Qb6 was defended by Nc4; Qd4 by e5. 29.Qb3 vacated c3, allowing ...Qxa1+ along d4-c3-b2-a1.
- ...Nb6 cleared Ba6's diagonal to Re2 and Qa4's rank to e4. 36.Qe2 Bxe2 37.Nxe2 Qxe2 won queen and knight for bishop. Track every line opened by a screen move.

## Italian and ending lessons
- T12 White: ...d5 required e5!; calculate through ...Ne4 Nxe4 dxe4 Bxe4. Be3 defended d4; Qe2 removed Qd1's guard.
- Rd5 did not defend Qf5 through White's e5 pawn: Qxf5 won it. After e6 fxe6 Qxe6+, that screen vanished and Rd5 really defended Nf5. Refresh geometry after pawn exchanges.
- Ne5-fork sequence: Ng6+ Kg8 Ne7+ Kh7 Nxd5 won a rook while preserving the knight, unlike Nxf8 allowing a bishop recapture.
- T12 Black draw: a pawn-fork story did not establish ...Nxe4's soundness. c4 defended Rd3; Rxd3 cxd3 removed that rook and created a passer. Rd1/Ke3 attacked d3 twice; Ke6 did not defend it. Repetition did not validate the earlier sacrifice.
