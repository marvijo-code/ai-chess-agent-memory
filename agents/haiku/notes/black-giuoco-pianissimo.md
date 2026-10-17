# Black Giuoco Pianissimo v DeepSeek V4.1 Flash (T44R3, W forfeit m14) and v GLM 5.3 Flash (T45R1, L m34)

## v DeepSeek (T44R3, W forfeit)
Played (14 plies): 1.e4 e5 2.Nf3 Nc6 3.Bc4 Nf6 4.d3 Bc5 5.c3 O-O 6.O-O d6 7.Bb3 Be6

Then: 8.Nbd2 Bxb3 9.Nxb3 Bb6 (Nb3 attacked c5, so the bishop retreated to b6, where nothing hit it). 10.h3 Re8 (h3 stops ...Bg4; ...Nd4 would lose to cxd4). 11.Be3 Bxe3 12.fxe3 Qe7 (queen and rooks connected; knight jumps to b4, d4 and a5 lose to c3 or Nb3). 13.Qd2 h6 (luft, and it takes g5 from Nf3).

Why it worked:
- ...Nf6 hits e4, and after d3 the pawn is guarded, so Nxe4 is not a threat for White.
- ...Be6 blocks Bb3's diagonal toward f7, and f7 guards e6.
- The ...Bxb3 trade removes White's active bishop. Nxb3 gains a tempo on Bc5, so ...Bb6 is the retreat.
- Rook on e8 behind e5 is the e-file rook; h3 prevents ...Bg4.

Checks for next time (unverified against stronger opponents):
- After Bxe3 fxe3, the f-file opens for White's rook. Check Rf1 and Qd2 pressure on f7 before any queen move.
- Before a ...Nb4, ...Nd4 or ...Na5 jump, name the c3 pawn and the Nb3 captures.
- Play ...h6 luft once queens are on the board. Keep the king guarded by f7, g7, h6.
- Opponent-specific: DeepSeek's illegal tries came in pawn moves through its own pieces (b4 through Nb3). Keep my own moves to verified legal squares; do not exploit by pace.

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
