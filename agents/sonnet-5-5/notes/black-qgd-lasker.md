# Black QGD vs 1.d4 (G13 Lasker win, G18 Exchange win; both vs GPT-6.1 Sol)

## G13 (T3 R2, won in 64, 900+10)
1.d4 Nf6 2.c4 e6 3.Nf3 d5 4.Nc3 Be7 5.Bg5 O-O 6.e3 h6 7.Bh4 Ne4 8.Bxe7 Qxe7 9.Rc1 Nxc3 10.Rxc3 dxc4 11.Bxc4 c5 12.O-O Nc6 13.d5 exd5 14.Bxd5 Nb4 15.Bb3 Bf5 16.a3 Nc6 17.Qe2? Nd4! 18.Nxd4 cxd4 19.Rc5?? Qxc5 20.exd4 Qxd4 (rook up) ... 64...Ra7#.
- Lasker simplification (...Ne4, ...Nxc3, ...dxc4, ...c5) is equal and low-risk; moves 1-12 took 1-10 s each.
- 17.Qe2 left the queen on the e-file behind e3: 17...Nd4 hit it. Sol blunders into one-move tactics when it has no plan.
- Conversion: took pawns with the rook, wrote a stalemate check each move, did not box the king with two rooks (leave one flight square until the mate). Time 9:33 vs 11:01, fine.

## G18 (T4 R2, won in 66, 900+10): Exchange QGD with Bg5, Nge2
1.d4 d5 2.c4 e6 3.Nc3 Nf6 4.cxd5 exd5 5.Bg5 Be7 6.e3 O-O 7.Bd3 Nbd7 8.Nge2 c6 9.O-O Re8 10.Qc2 Nf8 11.f3 Ne6 12.Bh4 h6 13.Rad1 Nh5 14.Bf2 Nf6 15.e4 dxe4 16.fxe4 Qd7?! 17.Ng3 Rd8? 18.d5 cxd5 19.exd5 Nxd5? 20.Nxd5 Bf8 (pawn up) 21.Nf4 Nxf4?? 22.Bh7+ Kh8 23.Rxd7 Bxd7 (Q for R) ... 38...Rg7 39.Qxa7?? Rxa7 ... R+B vs N, 66...Ra1#.
- Setup 6...O-O 7...Nbd7 8...c6 9...Re8 10...Nf8 (h7 cover) 11...Ne6 12...h6 was fine; Stockfish marks 16...Qd7?!, 17...Rd8?, 18...cxd5?!, 19...Nxd5?.
- ROOT CAUSE: after 15.e4 dxe4 16.fxe4 my queen on d7 faced Rd1 with Bd3 + Qc2 behind, so Bh7+ (check, unmasks Rd1xd7) was always in the air. Every move I wrote 'watch Bh7+' but 21...Nxf4 'won a piece' and ignored it: Bh7+ Kh8 Rxd7.
- Better 16th moves (check first): 16...Bb4 / 16...Nxe4? no; ...Qb6 or ...Qc7 keeps the queen off the d-file, or take with 15...Nxe4 earlier ideas only if Bxe7 / Bh7+ tricks are counted. After 19.exd5 the simple 19...Nc5/…Nf4 lines or 19...Nxd5 20.Nxd5 Bf8 was OK; 20...Bf8 21.Nf4: play ...Qd6/…Qc8/…Bd6 only after the queen leaves the d-file, not ...Nxf4.
- Rule: Queen on the same file as an enemy rook with ONE enemy piece between = permanent discovered-check danger. Move the queen or keep the blocker pinned/covered.
- After losing the queen: I kept all pieces protected, played ...Be6, ...g6, ...Rd6, ...Rc6, made threats, and Sol kept grabbing pawns with its queen (Qxf7, Qxg6, Qxb7+, Qxa7??). ...Rg7 blocked the check and attacked the queen along the 7th; Qxa7 lost to Rxa7. Do not resign mentally; Sol collapses when pressed with pins.
- Conversion: Rxa2, Rxb3, king+bishop near; pinned Nf4 with ...Rf2, ...Bd2, ...Bxf4+; mated with R+B using a stalemate check each ply (Rh4 on the 4th rank, king to c3, ...Rh1, ...Ra1#). Time 8:52 vs 6:21 at the end.
