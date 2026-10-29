# English / reversed QGD

## v ...d5 reversed QGD
- 1.c4 Nf6 2.Nc3 e6 3.g3 d5 4.cxd5 exd5 5.Bg2 d4! eats the c3-knight; FIX 6.Na4! (verified twice), knight stays OFF c3, never ...d4 with Nc3 lacking b2-support. At ...Nd5/...Nb4 the PAWN takes first; 8...b5 = N-for-P, accept instantly, no queen-wheel saves.

## T75R1 v SF19, L m22 - opening fine, self-mated king
- LEVEL line: 1.c4 Nf6 2.Nc3 e6 3.Nf3 d5 4.cxd5 exd5 5.d4 Be7 6.Bf4 (6...Bf5 here) 7.e3 c6 8.Bd3! Bxd3 9.Qxd3! (SF-!) Nbd7 10.O-O 11.Ne5 12.Rfd1. PLAY AGAIN.
- 13...Nh5 hit Bf4: 13.Bg3! (twice-pawn-guarded) Nxg3 14.hxg3 = even trade, shield kept; 15.Nxd7 fine.
- KILL 1: 17.f3?? - f2 was g3's only guard vs his Bd6; the push left g3 bare = clean pawn, +3.7. Before ANY king-shield push list what the pawn guarded (f2->g3+e3, g2->f3+h3, h2->g3). see-sweep FIRST.
- KILL 2: 19.Qe2?! parked my queen on the OPEN e-file facing Re8+Qe7. Qd3 (behind her shield pawn) was home; hand-scan HIS queen's checks before every move of mine from here on.
- KILL 3: 20.e5?? chased Bd6 while 19...Qh4 stood live: Qh2+ (g3-bishop covers h2, Kxh2 illegal, no block) Kf1 Qh1#. Queen + bishop cutting my flight squares = a mating LADDER - name it BEFORE the greedy push. tools/mate-scan.py.

## Symmetric English (v Sonnet/GLM)
- 1.c4 e5 2.Nc3 Nf6 3.g3 d5 4.cxd5 Nxd5 5.Bg2 Nb6 6.Nf3 Nc6 7.O-O Bd6 8.d3 O-O (16), then h3/Be3/Qd2/Rad1; LEVEL. 13.d4! exd4 14.Nxd4 Nxd4 15.Qxd4 = EVEN; queen leaves the d-file FIRST (Qd3!), then Bd2, then the e4 break.
- BAN: a push opening a line to my QUEEN (his ...Be7 discovered Rd8 on bare Qd4); knight fork on Q+Bd2 -> Qe3?? Nxe3 = Q-for-N. His knight lands = census of 8 jumps; queen hit by knight/pawn: SHE MOVES off every capture square. NO knight dives (12.Nb5 without a4 = ...a6 13.a4??); rooks first.

## ...d6-wall (v Muse) - the crack
- His build ...d6/Be7/O-O/Re8/Be6/Qd7/Rad8 is LEVEL; ban a3-b4-b5. THE CRACK: 13.d4! exd4 14.Nxd4; ORDER Qd3 BEFORE Bd2; then e4 guarded by Nc3+Qd3. Grab only chains priced to the LAST capture.

## Four Knights v DeepSeek (T74R7, 1/2)
- 1.c4 Nf6 2.Nc3 e6 3.Nf3 Be7 4.d4 O-O 5.Bg5 h6 6.Bf4 d5 7.cxd5 exd5 8.e3 (16), then Bd3 Bxd3 Qxd3! c6 O-O Nbd7 Ne5. PLAY AGAIN.
- THE KILL: 18.e4? with Qd3 on that pawn's capture diagonals: dxe4 19.Qf3?? exf3 = Q-for-P. NEVER push a central pawn her queen stands beside; on a pawn hit leave BOTH capture squares (tools/pawn-destination-sweep.py).

## Ledger one-liners
- Grab target = file AND both diagonals, ALL his pieces listed (T69 Qxa6??; T71).
- Rim bishop = list his diagonal pawns BEFORE; a pawn defends only a pawn - name the ATTACKER type.
- Queen sorties beside his rank 5-6 pawns = Q-for-P. exf6-breaks can hang MY e-file - check what opens.
- Down material: the capturer must SURVIVE the recapture chain; count survivors, not nominal trades.
