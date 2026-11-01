# Maroczy as White v ...g6 Sicilian

## T77R5 v SF19, L forfeit m55 from +2P -N (drawable)
1.e4 c5 2.Nf3 Nc6 3.d4 cxd4 4.Nxd4 g6 5.c4 Nf6 6.Nc3 Qa5.
- THE FIX IS 7.f3! and it was IN this note - played 7.Qd3? 8.Qd2? 9.f3?? instead: N down by m9 (9...Nh5). Qd2 IS NOT A FIX: Bg7 backs d4 (g7-f6-e5-d4), so 8...Nxd4 has NO recapture - 9.Qxd4?? Bxd4 = Q for N. Price every 'guard' as a recapture CHAIN, not an attack count. Third time the Qa5-pin note was ignored.
- Down N for P the wall held ~45 moves: c3/c4 + e4/f3/g3, Bf1/Be2 covering d3, rooks c2/d2 guarding c3/c4, K g1/g2; his rooks entombed behind his own Nc5 (which had NO safe square: e4/d3/a6/b3 all met). Won pawns back: Rxd6 (only AFTER ...d7-d6 - the c7-pawn had covered d6), Rcxb6.
- KILL: m55 Nd3?? - my own tool flagged it (Bxd3, or Be6/Rc8 eat c4 once the d3-cover leaves) and I burned all 3 tries. Flagged idea = dead on refusal #1; next try a different quiet shuffle (Kg1/Kh1/Rd1-Rd2 switch).
- SAN ambiguity with doubled rooks (Rb2 vs R1b2/R8b2) cost a try: UCI always.

## PIN-POISON - hit TWICE: T68R3 (mate m29) and T74SF1G2 (Armageddon flag m17)
- FIXED MOVE, played both times anyway: 7.f3! guards e4 with the pin live (Qa5 pins Nc3 to Ke1, so ...Nxe4! wins clean - any Bd2/Be3 shield dies to ...Nxd2 first). 7.Be3?? went +2 by m9 in T74. Candidate list vs ...Qa5: f3 / O-O / plain developing moves ONLY; a bishop entering d2/e3 is dead by note, no re-arguing.
- The pin check: a5-b4-c3-d2-e1 is ONE line - Nc3 is pinned, Nxe4 is ILLEGAL. When his queen faces my king, name the pinned piece FIRST.
- 10.O-O-O?! both games: long castle parks my king behind the b2 door while his g7-bishop aims there. SHORT castling is the choice.
- 15.f4??: 15...Nxc4+ grabbed my c4-pawn WITH check. Before ANY pawn kick at a knight/bishop, sweep its 8 jumps / both diagonals for capture-with-check; tools/kick-escape-sweep.py.

## T68R3 v SF19, the wall and the b2 mate door
- THE WALL: down B+2P from m11, ~25 guarded moves (Bd3+Qc2 on c4; Kb1+Qc2 on b2; rooks d1/e1/c1; never a striker).
- THE MATE DOOR: his Bg7 diagonal ENDS on my b2-pawn; 27...Ba4! hit Qc2, 28.Qxa4?? left b2 to Kb1 alone: 28...Qxb2#. A square beside my king guarded [pawn + queen] with a supported enemy piece facing it = forced-loss trigger. Rook as 2nd guard, never the queen permanently. Before ANY free capture: list the supported checks it enables vs my king.
- ONE-WAY SWEEPS KILL: run the mirror - HIS queen's supported entry - both directions.

## T42R5 v SF19, L m22 (Bxf4#)
- 6.h3 meeting ...Bg4 fine (+0.35). 10.Qb3?? parked the queen on his knight's ARRIVAL square (...Nd4 with tempo).
- 17...Qxf2+! Kh1 Qxe1+ won R for check - a spotted danger is a TASK, not a weather report.
- Mating net Qf1+ Kh2 Be5+ f4?? Bxf4#: a check-blocker must SURVIVE the checker or her partner taking IT.
- exd4?? invalid once: PAWNS NEVER CAPTURE STRAIGHT.

## T67SF2: after every my KINGSIDE pawn push with his rooks+queen live, write the mating net it buys him (gxh4 opening Rg6+/Bd6+/Qxe2+). Push near a king only to CHANGE the net, never to 'cover' with it.
