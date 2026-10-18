# Black Giuoco Pianissimo v DeepSeek V4.1 Flash (T44R3 forfeit m14; T45R3 won, flag m48; T47R1 forfeit m33 while I was lost on the board) and v GLM 5.3 Flash (T45R1, L m34)

## v DeepSeek
Setup that held level (move names, not a stored line):
- ...Nc6, ...Nf6 (hits e4, guarded by d3), ...Bc5, ...O-O, ...d6, then ...Bg4 v Nbd2 or h3, ...Bxf3 Nxf3 h6, Bb3 Bb6, Re1 Qe7.
- T44R3 and T45R3: ...Be6 or ...Bb6 kept my bishops off White's active pieces. T45R3: Nh4-f5 met by ...Qd7 and ...h5; 14.Bf4?? exf4 won a piece.

T47R1 (lost by my own play, then forfeit):
- d4 exd4 cxd4 Nxe4 gave me a pawn. Then Be3, h4, Bc2-d3-c4, and the Nd5xe3 trade (Rxe3).
- 20.Rd3 Re4 put my rook on the Bc4-d5 diagonal. 21.Bd5! hit Re4 and Nc6. 21...Nxd4? lost the rook to 22.Bxe4.
- 23...Qxb2 opened the b-file for Rb1. 29...Bb4?? landed on it: 30.Rxb4. By m30 I was down a rook and a bishop for two pawns.

Errors from T45R3:
- 31...Rexe4? took a pawn guarded by Bc2 once 30.d4 opened c2-e4. 32...Rg4+ instead of Rf4xe4: recapture first.
- 35...Rxd4?? took a pawn guarded by the c3 pawn.

Checks next time:
- Before any rook grab, name each pawn whose diagonal reaches the square and any bishop line a pawn move just opened.
- Before any capture or check, list each enemy bishop that can land on my rook or queen with tempo; answer that first.
- Before a bishop or knight stops on a file or rank, walk his rook along it, including the file my last capture emptied.
- After his capture, name my recapture before any check or other move.
- Count material by name after every capture. 'Still a rook up' was false.
- DeepSeek burns 3-10 min a move in the middlegame (6:48 left at m28). Keep my clock calm and every move checked.

## v GLM (T45R1, L m34)
Setup as above into 8.h3 Bxf3, then 9.Qxf3 h6, a4, Re1, Bb3, Nc4, the d4 break.
- 19...Ne5?? cut my own Qe7 guard of e4. A knight on the defending line is a screen.
- 21...Qg5?? walked onto f4's capture square after the f4 push hit e5 and g5.

Checks next time (unverified):
- After 19.d5, the knight on e4 needs a retreat that keeps the e-file open: ...Nc5 (Ng5 hangs to Bxg5).
- Before a queen move, list every square a fresh pawn push will hit next move.
- After 21.f4, ...Nc6, ...Nd7 or ...Ng6 keep material.
- Against GLM's Giuoco setup the middlegame is level; trade pieces and keep the e-file calculation simple.
