# Chess memory - DeepSeek V4.1 Flash 1017

## Move discipline (check every move)
- LEGALITY FIRST: 3 rejected tries forfeit. T47R1 had 3 invalid attempts (two on 12.f5, two on 13.Nxf5) and burned minutes. Before sending, name the piece's current square, the destination's occupant, and the path; after ONE rejection choose a different move, never resend.
- A LANDING SQUARE IS A CAPTURE SQUARE. 16.Nd6?? walked into ...Bxd6; the 'fork' on Bb7/Re8 bought only a bishop pair, and ...Nxe4 followed. Before a knight jump list every enemy piece that captures the arrival square (Bxd6, Nxd6) and whether each target is really defended.
- TEMPO ATTACKS NEED A CHECK SCAN. 14.Bf4? hit Qc7 but ...Bc5+ came with tempo, forcing Kh1 and ...Qd8. Attacking a queen only gains time if he has no check or counter-capture.
- CHECKED? List block/capture squares and which of my pieces sit on the checker's diagonal; T47R1 14...Bc5+ was answered correctly only by 15.Kh1 (Qe3?? and Nd4?? lose material). A king step that keeps my bishop attacking his queen is ideal.
- COUNT ATTACKERS v DEFENDERS, not the word 'defended'. 19.Nxe4 won a whole knight: Qe3 and Nc3 both hit e4, only Nc6 defended.
- UP MATERIAL: simplify only when it removes his counterplay; otherwise keep active pieces and pick up free units. 20.Qa3 (offering the trade while a piece up) was marked inaccurate though still winning.

## Clock
- Hard cap 60 s. Routine 5-15 s; captures/checks/pawn breaks 20-40 s. T47R1 spent 2:45 on 12.f5, 1:54 on 13.Nxf5, 3:45 on 14.Bf4 without finding anything; 2-4 min thinks are a diagnosed loss mode for me.

## Opening: Open Sicilian Taimanov as White
- Played: 1.e4 c5 2.Nf3 e6 3.d4 cxd4 4.Nxd4 Nf6 5.Nc3 Nc6 6.Be2 a6 7.O-O Be7 8.Be3 O-O (16 plies), then f4/Qd2/Rad1. Fine through move 11; Rad1 was only a slight inaccuracy.
- BAN premature f4-f5: 12.f5? met ...exf5, opening the e-file for his Re8 and leaving e4 hit twice (Nc6, f5-pawn) with only Nc3 guarding; his ...g6 later kicks the f5 knight. Keep the tension with Qe1/Qg3, Rf3/Rf1-f3; push f5 only with e4 double-guarded and his rook denied the e-file.
- Watch ...Bb4, ...Nxd4 (recapture with B), ...d5, ...b5. After ...b5/...Bb7 his b7-bishop blocks the long diagonal, so Ndb5 tricks are off; answer a Nc3 pin with Be2 kept flexible.

## Opponents
- GLM 5.3 Flash: slow multi-minute thinks (2:36 on ...b5, 8:16 on ...Bc5+), 1 illegal here, 3 in another game, forfeits readily. When lost it grabs pawns (19...Qxa2) and defends stubbornly. Plan: guard every unit, take free captures, play 10-15 s sound moves and let its clock run.

## Record
- T47R1 White v GLM: 1-0 by forfeit (3 invalid replies), one piece up at the end after 19.Nxe4.

Note files: none yet.
