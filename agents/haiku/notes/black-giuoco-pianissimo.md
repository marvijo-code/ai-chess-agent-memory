# Black Giuoco Pianissimo v DeepSeek V4.1 Flash (T44R3 W forfeit m14; T45R3 I won, W flag m48) and v GLM 5.3 Flash (T45R1, L m34)

## v DeepSeek
Setup that worked twice (move names, not a stored line):
- ...Nc6, ...Nf6 (hits e4, guarded by d3), ...Bc5, ...O-O, ...d6, then ...Be6 or ...Bg4 as White plays d3/c3/Bb3/Nbd2/h3.
- T44R3: ...Be6 blocked Bb3's f7 diagonal; ...Bxb3 Nxb3 Bb6 kept the bishop safe; ...Re8, ...Qe7 after Bxe3 fxe3, ...h6 luft. White's knight jumps to b4, d4 and a5 lost to c3 or Nb3.
- T45R3: ...Bg4 after Nbd2, ...Bxf3 Nxf3 h6 for luft, Bb3 Bb6, Re1 Qe7, Nh4 Qd7. After Nf5 the answer was ...h5 (stops Bxh6). Then 14.Bf4?? exf4: the e5 pawn captured the bishop. White's g3 grab gave the pawn back, and queens came off a piece up.
- Why it worked: ...Nf6 with d3 guarding e4; ...Be6/...Bb6 kept my bishops off White's active pieces; the e5 pawn guards f4 and d4.

Errors to avoid (T45R3, both rook grabs):
- 31...Rexe4? took a pawn guarded by Bc2 once 30.d4 had opened c2-d3-e4. 32.Bxe4 took my rook, and I answered 32...Rg4+?? instead of Rf4xe4. Recapture first.
- 35...Rxd4?? took a pawn guarded by the c3 pawn. 36.cxd4 won the rook.

Checks next time:
- Before any rook grab, name each pawn whose diagonal reaches the square (c3 hits d4) and any bishop line a pawn move just opened.
- After his capture, name my recapture before any check or other move.
- Before a ...Nb4, ...Nd4 or ...Na5 jump, name the c3 pawn and the Nb3 captures.
- Keep my own moves to verified legal squares; DeepSeek's illegal tries came in pawn moves through its own pieces.
- DeepSeek burns 3-10 min on quiet moves; keep my clock calm and convert with simple, checked moves.

## v GLM (T45R1, L m34 Qe6#)
Played (16 plies): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Bc5 4.c3 Nf6 5.d3 O-O 6.O-O d6 7.Nbd2 Bg4 8.h3 Bxf3

Then: 9.Qxf3 h6 10.a4 (GLM's Nf1 try was illegal) a5 11.Re1 Bb6 12.Bb3 Qe7 13.Nc4 Bc5 14.Rb1 Bb6 (SF ?!: the bishop could go elsewhere). 15.Ne3 Bxe3 16.Bxe3 Rae8 17.d4 exd4 18.cxd4 Nxe4 (+1 pawn for Black) 19.d5 Ne5?? 20.Qxe4 (the knight on e5 blocked Qe7's guard of e4 along the e-file). 20...Qf6 21.f4 hit Ne5 and g5. 21...Qg5?? 22.fxg5 hxg5 23.Bxg5: queen lost.

What went wrong:
- 19...Ne5 cut my own queen's defence of e4. A knight on the defending line is a screen, not a move.
- 21...Qg5 walked onto the square f4 attacks. The f4 push had just hit e5 and g5 together; I checked the knight's square but not the pawn's new attack.

Checks next time (unverified):
- After 19.d5, the knight on e4 needs a retreat that keeps the e-file open: ...Nc5 (Ng5 hangs to Bxg5).
- Before a knight move, name the line each of my guards travels along, and write the square the knight will sit on.
- After 21.f4, ...Nc6, ...Nd7 or ...Ng6 keep material. Never put the queen on a square a fresh pawn push covers.
- Against GLM's Giuoco setup (c3, d3, Nbd2, h3, Re1, Nc4, d4 break), the middlegame is level; trade pieces and keep the e-file calculation simple.
