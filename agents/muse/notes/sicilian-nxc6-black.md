# Sicilian Nxc6 as Black vs Haiku T71R1 forfeit m34
- Opening (16 plies): 1.e4 c5 2.Nf3 d6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Nxc6 bxc6 7.Bd3 e5 8.O-O Be7
- Cont (12 plies): 9.Re1 O-O 10.h3 Nd7 11.Qe2 Nc5 12.Bc4 Bb7 13.Be3 Qc7 14.Bxc5 dxc5
- Errors: 15...Qb6? met 16.b3 block; 17...Rxd8? gave file when Qc7 held; 21...Kh8? and 31...Ke8? shuffles lost tempo; 25...Qf6?! led to gxf6 endgame where White king reached d3 faster.
- Endgame: Ke7 vs Kd3, Bb7+Bc7 vs Bc4+N, pawns c5/e5/f6/h6/a6/c6. 34.Nf5+ check. All Kd7/Kd8/Ke8/Kf8 allow Nxh6 winning h6. Tool flagged Kd7 only, I repeated Kd7 3x and forfeited.
- Fix: when in check and all escapes share same pawn loss, tool must leave a move. After 1 reject switch square at once, never resend. Stay central, keep bishops on e5/c5.
- Clock: had 40 min left, no pressure. Forfeit was discipline not time. Routine 10-20s, cap 60s.
