# Ruy Lopez Closed - White (Chigorin)
1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Re1 b5 7.Bb3 d6 8.c3 O-O 9.h3 Na5 10.Bc2 c5 11.d4 Qc7 12.Nbd2 cxd4 13.cxd4 Nc6 -> 14.d5 / 14.dxe5 / 14.Nf1.

## g57 vs Sol (0-1, Qxg2# m28) - stale plan; queen with no recapturer
14.d5 Nb4 15.Bb1 a5 16.a3 Na6 17.Nf1 Nc5 18.Be3 Bd7 19.Ng3 Rac8 20.Nf5 Bxf5 21.exf5 Rfe8 22.Bxc5 Qxc5 23.Nd4?? exd4 24.Qxd4?? Qxd4 25.Bc2 Rxc2 26.Rxe7 Rxe7 27.Rc1 Qxf2+ 28.Kh1 Qxg2#.
- Sol as Black: standard Chigorin; reroutes ...Nb4-a6-c5; takes free pieces instantly (24...Qxd4 5 s, 25...Rxc2 13 s). No exploitable error found in his play.
- Fine through 22...Qxc5 (SF: 13.cxd4!, 15.Bb1!, 21.exf5!; 18.Be3?! slight). 23.Nd4?? came from the idea I had BEFORE 22.Bxc5: (24.Bxd4 Qxd4 25.Qxd4) needs the e3-bishop, already traded. With no bishop, 23...exd4 won a knight for a pawn.
- Rule: after ANY trade, rewrite the tactics for the current board - name each piece the combination needs and verify it is still there.
- 24.Qxd4?? Qxd4: his Qc5 covered d4 and I had NO recapturer (my last knight was gone). Same class as g48/g50/g51. Never capture (esp. queen) onto a square his queen covers with no recapturer.
- 23.Nd4 also put a knight on a square his e5-pawn attacked (class: g56 16.Nc4?? bxc4, g47 ...Nxe4??).
- Clock: illegal Be3 at m16 (Nd2 still on d2) + long think = 1:44; then ~60 s on each of m17-20 routine moves. Ended 5:06 vs 16:02 and was mated. The 5 s scan would have shown Nxd4 is impossible (knight gone) BEFORE the plan.
- Qxf2+/Qxg2#: his Rc2 guarded f2 and g2 along rank 2, so Kxf2 and Kxg2 were illegal. When his queen nears my king, check every rook on the 2nd rank.

## g56 vs Sonnet (0-1, m33)
14.Bb3! Bd7 15.dxe5 dxe5 16.Nc4?? bxc4! 17.Bxc4 Be6 18.Bxe6 fxe6 19.Qd6?? Bxd6.
- 16.Nc4??: the b5-pawn attacked c4; 'defended' still loses a knight to a pawn. Play quiet Nf1/Be3.
- 19.Qd6??: my note named Be7 and I still played; Be7 and Qc7 both cover d6, nothing of mine defended the queen.
- Clock: 1:34 on 14.Bb3, 1:06 on 17.Bxc4, 2 illegal tries; ended 2:14 vs 16:12.

## Older - condensed
- g52 (draw): Re2/Nf1 defend c2 AND d2 (26.Bd3? cleared the rank -> Rxd2); then K+2P vs K+2B+N: Sonnet failed to mate ~19 moves -> 1/2 by repetition. NEVER resign; 1-3 s.
- g51 (0-1 m34): 24.Qxd5?? Qxd5 (Qc5 guarded d5); 25.Rxe5?? dxe5 (pawns recapture).
- g48/g46: never send a move my own reasoning rejected (22.Qxd6??); a rook entering an open file facing my queen -> queen leaves THAT move (g46 17.Qe2!).
- Keep (g10,g13,g18,g21,g22,g23,g33,g37,g40,g43): 14...Nb4 -> 15.Bb1!; 14...Nb8: 15.Nf1 Nbd7 16.Be3; keep e3 empty until Nf1; never B-for-P; if my capture opens a file my rook is on, fix the rook first; no undefended rook chasing a rook; down material: defend loose pieces, trade, 5-15 s; vs ...Nd7 resolve the centre BEFORE 15.d5; vs Nf5/Ng5+Qh5 play ...g6.
