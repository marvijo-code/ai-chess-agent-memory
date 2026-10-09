# Black vs 1.e4 e5 2.Nf3 Nc6 3.Nc3 (SF plays this as White every time)

PLAN: 3...Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4! 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 (SF chose Bc4, not Bxc6). Played fine to move 10 (eval ~+0.1). 3...Bc5 failed twice (G7, T10R1).

## T10 Final Armageddon (Black, draw wins): DRAW by repetition at -12
1.e4 e5 2.Nf3 Nc6 3.Nc3 Nf6 4.Bb5 Bb4 5.O-O O-O 6.Nd5 Nxd5 7.exd5 e4 8.dxc6 exf3 9.Qxf3 dxc6 10.Bc4 Qd4 11.d3 Qd6?! 12.c3 Bc5 13.d4 Bb6 14.a4 Be6 15.b3 Bxc4?! 16.bxc4 Rad8 17.c5! (forks Qd6+Bb6, +5.6) Bxc5 18.dxc5 Qxc5 19.Ba3 Qe5 20.Rae1 Qxc3?? 21.Qxc3 (Qf3 guarded c3 along the 3rd rank) ... 42...Kg7 threefold: Qd7+ Kg6 Qe8+ Kg7.
- Errors: 11...Qd6 let c3 and d4 come with tempo on Bb4/Bc5/Bb6. Candidates (unverified, calculate): 11...Bxc3 12.bxc3 Qxc3 (pawn back; check Bd2/Rab1), or 11...Bd6.
- 15...Bxc4 16.bxc4 gave a pawn on c4 -> c5 fork of Qd6+Bb6. Rule: Q and B on d6/b6 (or any two pieces a pawn push apart) get forked by a pawn; before recapturing options, list his pawn pushes. Better 15...Bd5 or move the queen off d6 earlier (Qe7/Qc... ) and keep Bb6 defended by a5/c5.
- 20...Qxc3??: queen grab where the square was guarded by his queen on f3 (rank). ALWAYS list his queen's lines (ranks too) before any queen capture. At 19...Qe5 20.Rae1 I was already -7, but 20...Qd6/Qh5 kept more.
- LIFELINE WORKED: SF (depth 4) just checks in a loop even at +12. Keep king shuffling between two squares where each check has only one reply (Kg6/Kg7 vs Qd7+/Qe8+, with ...f6 played and pieces protected); do not wander. Repeat the moves exactly; it takes 3 repeats.
- Time: fine (used only ~2:30 of 7:30); spend extra at moves 11-16.

## T10R1 (3...Bc5, draw by repetition a piece down)
3...Bc5 4.Nxe5 Nxe5 5.d4 Bd6 6.dxe5 Bxe5 7.Bd3 Nf6 8.Ne2 O-O 9.f4 Bd6? 10.e5 forks B+N. Be5 has no retreat vs f4. Verify every written fix against pawn forks. Avoid 3...Bc5.

## Older 3...Nf6 4.Bb5 Bb4 losses (T9R3, G6): improvised after 6.Nd5
T9R3: 7...Ne7? 8.Nxe5 Nxd5 ... Ne8 blocked back rank, Qxe8#. G6: 7...e4 8.dxc6 exf3 9.Qxf3 bxc6? 10.d4 ... Rxf8#. Recapture 9...dxc6, not bxc6.
- 6.d3 Bxc3 7.bxc3 d6 (unverified, solid).

## 4...Nd4?! (T6, T8R3 lost/drew): never
5.Nxe5 Qe7 6.f4 Nxb5 7.Nxb5; 6...d6 illegal (pin). Down exchange+2P fortress drew twice. Don't play 8...Nxe4 into Qe2/Nc7+.

## G11 Caro-Kann Advance lost (7...Nbc6?? 8.Nb5). Skip Caro; play 1...e5.

## General
- Keep king pawns intact; bishop safety before ...d6.
- Use time at moves 6-16 on 'his best reply: pawn pushes, forks, queen lines'.
