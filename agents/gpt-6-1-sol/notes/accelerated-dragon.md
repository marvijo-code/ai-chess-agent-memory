# Accelerated Dragon: capture checks before conversion

## T10 semifinal 2, game 1: Black vs Stockfish 19, repetition draw
1.e4 c5 2.Nf3 Nc6 3.Nc3 g6 4.d4 cxd4! 5.Nxd4 Bg7 6.Be3 Nf6 7.Bc4 O-O 8.O-O Nxe4 9.Nxc6 bxc6 10.Nxe4 d5! 11.Bd3 dxe4! 12.Bxe4.
- The central fork recovered the sacrificed knight. Both sides lost both knights and two pawns; material was equal. Preserve the d-pawn until the fork and calculate the complete liquidation.
- 12...Qc7 13.c3 Rd8 14.Bf4 Qb6?! 15.Qb3 Be6 16.Qxb6 axb6! opened the a-file but created a vulnerable b6 pawn. Qb6 was inaccurate; no best replacement was supplied.

## Back-rank tactic and changing geometry
17.a4 Bd5 18.Rfe1 e6 19.Bc7 Rd7 20.Bxb6 Rb7! 21.a5?? Bxe4! 22.Rxe4 Rxb6.
- After 22...Rxb6, 23.axb6? Rxa1+ 24.Re1 Rxe1# explains why the pawn could not immediately recover the rook. White's king was enclosed by f2/g2/h2.
- Black obtained an extra bishop. After 23.b4 Rba6 24.Rd1 Bxc3 25.Rd3 Bg7 26.Rc4 Rb8 27.Rd6 Rbb6, White had relocated BOTH rooks. Recalculate the back-rank sequence; its earlier force cannot be assumed to persist.
- 28.Rd8+ Bf8 29.Rcd4 left Black Kg8/Ra6/Rb6/Bf8, pawns c6/e6/f7/g6/h7; White Kg1/Rd8/Rd4, pawns a5/b4/f2/g2/h2. The a5 pawn directly attacked Rb6.
- 29...Kg7?? 30.axb6! Rxb6! lost a rook for a pawn. Black now had R+B against 2R and one extra pawn. Unpinning Bf8 was a local purpose, not sufficient justification. No engine-best replacement was supplied.

## Doubled-rook forcing captures
31.R8d7 c5? 32.Rf4! cxb4 33.Rdxf7+ Kg8 34.Rxf8+ Kg7.
- c5 attacked Rd4 and b4, but White relocated the attacked rook to f4, supporting the other rook's invasion.
- Rd7xf7 removed f7 with check. Rf7xf8 then captured Bf8 with check; Rf4 protected f8 along the clear file, so Kxf8 was illegal despite Kg8's apparent protection of the bishop.
- Black was left with one rook against two. Winning b4 and creating a passer did not compensate for losing the bishop. Inspect checks and doubled-rook captures before advancing pawns.

## Practical resistance is not equality
- ...b3/...b2 tied a rook to promotion defense, but 46.Rcxb2 removed the passer. ...h3+ merely lost h3 to Kxh3; a checking pawn push requires a concrete follow-up.
- The e-pawn reached e2: 57.Rxe2+ Kxe2 58.Rxf3 Kxf3 removed all rooks. White retained king and g/h pawns against a bare king. This liquidation did not establish a draw.
- White eventually had g6/h6 while Black shuffled Kg8/Kh8. White's king retreated to h4/g3 and repeated. The depth-4 opponent failed to convert; this was not a theoretical rook-pawn draw, because White still had the g-pawn.
- Clock: 12:15 after move 21, 10:49 after the decisive Kg7, 6:45 after move 47, 3:04 at the finish. Many routine choices consumed 25-50 seconds. Direct capture omissions caused the material losses with ample time; avoid spending similarly long on forced checks and corner shuffles.
