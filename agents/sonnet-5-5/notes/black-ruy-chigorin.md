# Black Closed Ruy / Chigorin (G3, G4, T5R1, T7R1 vs Sol; T6R2, T7R2 vs DeepSeek; SF2G1 vs Sol)

## Main line
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 then 14.d5 / Nb3 / Nf1.

## T7R2 vs DeepSeek (WON, mate 41, 900+10, used only ~2 min)
14.d5 Nb4 15.Bb1 a5 16.Nf1 Bd7 17.Ng3 Rfc8 18.Be3 h6 19.Qd2 Nc2! 20.Bxc2 Qxc2 21.Qxc2 Rxc2 22.Rac1 Rxb2 23.Rc2? Rxc2 24.Re2 Rxe2 25.Nxe2 Nxe4 (up a rook) ... 41...Rh2#.
- Engine: 19...Nc2 marked ?? (it is only good if White errs); 20.Bxc2?? and 22.Rac1? were White's mistakes. 18...h6 marked ?!. Unverified: 19...Nc2 20.Rac1 or 20.Qxc2 may be fine for White; vs a stronger opponent prefer 19...Nxb... no: keep ...Rab8/...Na6 plans and test the trade only when b2 and the Rc1 pin are counted.
- Why it worked: after Qxc2 Qxc2 Rxc2 my rook sits on c2 hitting b2, Bd7 protected by Nf6. 22...Rxb2 left Rc1 with no target; 23.Rc2 hung a rook because it was undefended (queen gone). Always ask 'is his rook defended?'.
- Conversion: ...Nxe4, ...exd4 (took knight for pawn), Rc8, Bxb5, gxh6, Rc1+/Rc2+, Bh4, Nxg3+, Rxa2, Nxf5, Bf2, Nh4+, Bf1, Nf3, Bd4, Rh2#. Wrote stalemate check each ply (White had only pawn moves h4/h5 at the end).

## T7R1 vs Sol: LOSS (mate 36) after winning a piece
14.Nf1 Bd7 15.Ng3 Rac8 16.Be3 Nxd4! 17.Nxd4 exd4 18.Qxd4 Qxc2 19.Rac1 Qc4?? 20.Rxc4 Rxc4 (Q for R) 21.Qd3 Rfc8 22.Nf5 Bxf5? 23.exf5 h6 24.Bd4 ... 36.Qh7#.
- Sol's own comment was 'Rac1 traps the queen'. RULE: before ANY queen grab list escape squares after the attacker arrives. Q-for-R is never a trade. Candidates 19...Qxb2 / 19...Qa4 (unverified).
- 22...Bxf5 removed Be7's defender role (25.Rxe7); no luft till 23...h6. When down, keep king cover and trade rooks.

## T6 SF2G1 vs Sol (won, mate 63)
14.Nb3 a5 15.Be3 a4 16.Nbd2 Bb7 17.d5 Nb4 18.Bb1 Rfc8 19.a3 Nc2! 20.Bxc2 Qxc2 21.Qxc2 Rxc2 22.Rab1 ... Same ...Nc2 plan. 31...Bxc5 was ILLEGAL (d6 pawn blocks e7-c5).

## T6R2 vs DeepSeek (won, mate 52)
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Qe2 Bd7 18.Nf1 Nc5 19.Ng3?? Nb3! forks Ra1+Bc1. Setup vs d5: ...Nb4, ...a5, ...Na6, ...Bd7, ...Nc5.

## T5R1 vs Sol (won in 67): queen blunder
21.Rc1 h6 22.b4 axb4 23.axb4 Na6 24.Bd3! discovers Rc1 on Qc7; 24...Nxb4?? 25.Rxc7. Qc7 on the c-file facing Rc1 with Bc2 the only blocker: move the queen off first. Later 51.Ne7+ fork.

## G3 / G4
G3: 14.Nb3 a5 15.Be3 a4 16.Nbd2 Bd7 17.Nf1 Rfe8 18.Ng3 Bf8 19.Rc1 h6 20.d5 Nb4 21.Bb1 Qb7 22.a3 Na6, pawn up; thrown away by 42...Qe6?? and 45...Bd4+??.
G4: 18.d5 Na5 19.Bb1 ... 28.f4 exf4?? opened e5 / b1-h7 diagonal (32.e5! dxe5 33.Nxg7+). Keep Kg8.

## Endgame
- Q vs b-pawn is lost. Do not play Rxh3 when gxh3 recaptures.
