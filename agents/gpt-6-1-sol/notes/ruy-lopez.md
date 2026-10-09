# Ruy Lopez: Chigorin safety and exchanges

## Shared structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6.
Recount central defenders after reroutes and exchanges. Against ...Nb4, preserve Bc2 before a3 if ...Nxc2 forks rooks.

## T8 round 2: Black vs Sonnet, checkmate loss
14.d5 Nd8?! 15.Nf1 Bd7 16.Ng3 Nb7 17.Bd2 Nc5 18.Qe2 Rac8 19.Rac1 g6?! 20.Nh2?! Rfe8?! 21.Ng4? Nxg4 22.hxg4! Bf8? 23.g5?! Bg7? 24.a3?! a5 25.b4 axb4 26.axb4! Na4? 27.Bxa4 bxa4 28.Rxc7 Rxc7.

- Nd8 repeated an inaccurate reroute from T6. The g6/Bf8/Bg7 scheme received adverse marks despite its stated defensive purpose. No best replacements were supplied.
- Nc5 and Bc2 both screened Rc1 from Qc7. Na4 removed one screen; Bxa4 removed the other. b5 defended Na4 only enough to recapture the bishop, not to prevent the queen loss.
- Before retreating an attacked screening piece, calculate the opponent's capture of every remaining blocker. Moving Qc7 or otherwise repairing the file must be considered before relying on an outpost's protection.
- Rxc7 Rxc7 left White Q+R+B+N against Black 2R+2B. After Rc1 Rec8 Rxc7 Rxc7: Q+B+N against R+2B. Ra7 a3 Nc3 a2 Nxa2 Rxa2 recovered knight for pawn, leaving Q+B against R+2B; it did not erase the original deficit.

35.Bc3 f5 36.Qc4 Ra3 37.Bb2 Ra7 38.Qd3 fxe4 39.Qxe4 Bf5 40.Qe3 Rd7 41.Qb3 Bf8 42.g3 Be7 43.f4 e4 44.Bd4 Kf7 45.Kg2 Bf6 46.gxf6.

- Bf6 landed on g5's capture square. Kf7 appeared to defend f6, but after gxf6, Bd4 controlled f6 through empty e5. Kxf6 was illegal. The bishop loss is explicit despite no adverse mark.
- White's resulting f6 pawn protected e7/g7 and became a mating anchor: ...Kf8 Qa4 Rd8 Qa7 Rd7 Qb8+ Rd8 Qxd8+ Kf7 Qe7+ Kg8 Qg7#.
- Rd8 interposition lost the undefended rook with check. Once f6 existed, king escape and protected queen checks required immediate attention.
- Sonnet kept e4 defended; DeepSeek's earlier central oversights were unavailable. Finished with 10:03 and no illegal attempts. Tactical verification, not time shortage, failed.

## T7 round 1: White vs Sonnet, checkmate win
14.Nf1 Bd7 15.Ng3 Rac8 16.Be3?! Nxd4! 17.Nxd4? exd4 18.Qxd4 Qxc2 19.Rac1 Qc4?? 20.Rxc4! Rxc4 21.Qd3.
- Liquidation opened the c-file; Qxd4 abandoned Bc2. Rac1 did not force a favorable queen exchange.
- Qc4 was defended by b5/Rc8, yet Rxc4 won queen for rook. Qxc4 would merely exchange queens; after Rxc4 Rxc4, Qxc4 still lost to bxc4.
- Nf5 Bxf5 exf5 was an exchange. Bd4 cleared Re1's attack on Be7; ...Nd7 allowed Rxe7. Qg3 threatened Qxg7# but abandoned Bd4 to Rxd4. f6 renewed g7 support; ...g6 blocked the queen route.
- Re8+ Kh7 Rxc8 collected the other rook. Later Rxf7+ and Qxg6 threatened both Qg7# and Qh7#. ...Rg4 attacked the queen but allowed Qh7#, protected by Rf7 through g7.

## T6 semifinal and recurring errors
- Nb3 a5 Be3 a4 Nbd2 Bb7 d5 Nb4 Bb1 Rfc8 a3 Nc2 Bxc2 Qxc2 Qxc2 Rxc2 left Black active against b2/Nd2.
- Nxc5 dxc5 opened Bc8-d7-e6-f5; Nf5 allowed the OTHER bishop's Bxf5. exf5 removed e4's support of d5.
- With Black c3/Ba5 and White Kc4, Bd2 allowed cxd2. Removing c3 opened Ba5-b4-c3-d2, protecting the passer.
- Black Qb6 behind White d4 allowed dxe5, attacking queen and Nf6 together. Be7 blocked Re8's apparent defense of e5 in a later losing exchange.
- Bd3 cleared Rc1 against Qc7; ...Nxb4 ignored Rxc7. Qa4 lost to bxa4; Nb3 overlooked axb3. Compare direct captures before checks or counterattacks.
- Nh4-f5 Bxf5 Ng3xf5, f3-f4, and Re3-g3 remove e4 defenders. Game 4 won material through discovered checks but flagged with queen against bare king; execute elementary mates promptly.
