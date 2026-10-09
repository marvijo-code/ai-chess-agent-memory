# Ruy Lopez: central tactics and endgame barriers

## Shared Chigorin structure
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6.
Recount central defenders after reroutes and exchanges. Preserve Bc2 before a3 against ...Nb4 if ...Nxc2 forks rooks.

## T12 round 1: Black vs Sonnet, repetition draw
7...O-O 8.d3 d6 9.c3 Bb7 10.h3 Re8 11.Nbd2 Bf8 12.Nf1 d5 13.Ng3 Qd7?! 14.Qe2 Rad8?! 15.Bc2 d4?! 16.cxd4 Nxd4! 17.Nxd4! exd4 18.Nf5 g6?! 19.Nh6+! Bxh6 20.Bxh6 Nxe4? 21.dxe4! d3 22.Bxd3?? Qxd3! 23.Qxd3 Rxd3!.
- ...Nxd4 attacked Qe2 as well as Nf3/Bc2. Reconstruct all targets, not just those named in commentary.
- ...g6 allowed the protected checking jump Nh6+ and bishop exchange. Removing the outpost did not establish a sound resulting position.
- ...Nxe4 relied on ...d3 forking Qe2/Bc2, but the sacrifice was marked a mistake. White's Bxd3 was a blunder; Qxd3 and Rxd3 were the only good replies. No best White defense was supplied. Calculate queen escapes and counterthreats before assuming a pawn fork recovers a sacrificed piece.
- After the liquidation, each side had 2R+B and six pawns. Black had not won material. Opponent commentary about an extra piece/pawn was inaccurate.

### Passed pawn and liquidation
24.f3 c5 25.Be3 c4 26.Rad1 Red8 27.Rxd3 cxd3 28.Rd1 Kf8 29.Bb6 Rd7 30.Kf2 Ke7 31.Ke3 Ke6 32.Rxd3 Rxd3+ 33.Kxd3!.
- c4 defended Rd3. The pawn recapture created a d3 passer but removed that rook support.
- Rd1 and Ke3 supplied two attackers against Rd7's single defense. Ke6 did not defend d3. The passer fell when White could answer ...Rxd3+ with Kxd3.
- Rook liquidation left opposite-colored bishops with White six pawns against five. Do not infer that rook-backed advancement guarantees pawn survival.

### Barrier that held
33...Ke5 34.Ke3 Bc6 35.Bd4+ Ke6 36.f4 f5 37.exf5+ Kxf5 38.g3 h5 39.h4 Kg4 40.Kf2 Bd5.
- ...f5 exchanged White's central e-pawn for Black's f-pawn and activated the king. ...h5 fixed the kingside; ...Kg4 attacked g3 while Bd5 attacked a2.
- White stabilized with b3-b4/a3 and Be1. Be1's diagonal to g3 was initially blocked by Kf2; 46.Ke3 opened it. Trace blockers before claiming protection.
- Final barrier: Black Kd6 with Bd5/Bc6, pawns a6 b5 g6 h5; White Kd4, dark bishop, pawns a3 b4 f4 g3 h4. Kd6 barred c5/e5; bishop shuffles preserved b5 and the central barrier. Repetition held the pawn-down ending; the result alone is not proof every earlier position was drawn.
- Finished with 9:03 against 14:36, no invalid attempts. Many routine defensive moves took 25-42 seconds. Spend less once the barrier and waiting moves are verified.

## T11 round 1: Black vs Sonnet, mate win
- With White's c2 pawn unmoved, Bc2 was illegal. c3 Nxb3 Qxb3 caused no doubled b-pawns. ...d5 exd5 Bxd5 Qd1 c5 Nxe5 left White an extra pawn.
- ...Ke5 with Rd8/Bd5 against Nd4/Rd1 allowed Nc6+: ...Bxc6 vacated d5 and permitted Rxd8. White missed it twice; ...Rd6 escaped. The missed fork does not validate ...Ke5 or ...h5.
- ...f2 opened Bd5-e4-f3-g2-h1, protecting h-promotion. Ne2+ Kg2 Nf4+ Kxf1 Nxd5 h1=Q Nxf6 Qh6+ Kf3 Qxf6+ converted both Black pieces into a queen while removing White's rook and knight.
- ...Ke1 cleared f1 for ...f1=Q+. Two-queen conversion still consumed 26-45 seconds per routine move.

## Recurring failures
- Rc1/Qc7 can have two screens, Bc2/Nc5. ...Na4 Bxa4 bxa4 Rxc7 removed both and lost queen for rook.
- Be3 Nxd4 Nxd4 exd4 Qxd4 Qxc2: Qxd4 abandoned Bc2 on the opened file. ...Qc4 Rxc4 Rxc4 lost queen for rook.
- f3-f4, Re3-g3, and Nh4-f5/Bxf5/Ng3xf5 remove e4 defenders. Be7 can block Re8's defense of e5.
- Bxd7 Nxd7 can replace one knight with another, retaining ...Nxf8. Track both knights and every new defender.
- Bg5 allowed fxg5 when f6 was unpinned. Qa4 allowed bxa4; Nb3 allowed axb3. Useful plans do not excuse unsafe destinations.
