# Caro-Kann: breaks, destination safety and defenders

## T25 final: Black vs Stockfish 19, mate loss
Advance h4 h5/Bxd3/e6/c5/Nc6; Ne2 Nge7/Bg5 Qb6/O-O Nf5/c3 Be7/Bxe7 Ncxe7/a4 O-O/a5 Qc7/Qd2.
- This was the SAME position and failure as T23: 16...f6? 17.Nf4! Qd6 18.exd6 Nxd6. Pre-break evaluation was about +0.31; Nf4 raised White's advantage, and the queen loss made it decisive. The recorded warning was available before the move. Apply memory to the actual board before choosing, especially at a known opening branch.
- ...f6 abandons f7's guard of e6; Nf4 threatens Nxe6, forking Qc7/Rf8. ...Qd6 tries to defend e6 but is captured by the standing e5 pawn. Moving the queen does not create a safe destination. T25 marked Qd6 only inaccurate, yet exd6 plainly wins Q for P. No verified best replacement supplied.
19.Rae1 e5 20.dxe5 fxe5 21.Nxh5 e4 22.Qg5 Ndf5 23.Rxe4 dxe4 24.Nd2 e3 25.fxe3 Rf7 26.e4 Nd4 27.cxd4 cxd4 28.Rxf7 Kxf7 29.Qxg7+.
- ...e4 attacked Nf3, but Qg5 threatened Qxg7# with Nh5 protecting g7. A knight attack does not oblige retreat when the enemy has a mating threat. Ndf5 guarded g7; Rf7 later added another guard.
- ...Nd4 moved Nf5 away from g7 and placed it on c3's pawn-capture square. cxd4 cxd4 sacrificed N for P; calling this an exchange concealed the material cost. The new passer was not verified compensation and fell to Qxd4+.
- Rxf7 Kxf7 removed the remaining g7 defender; Qxg7+ took the pawn and exposed the king. Audit defensive duties before moving a knight, then calculate captures of the remaining defender.
- The king eventually reached g3 and met Qg5#. White's Q/N/pawns/K covered the exits; chasing pawns did not provide shelter. No invalid attempts; finished 13:08. Qd6 took 34 seconds: time shortage did not cause the repeated queen loss.

## T24 final branch: Nh6 and queenside castling, mate loss
Nh6/Be7 Bxh6 gxh6/Qc7/O-O-O/Rhg8; Nf4 Qd7 Nxh5.
- Nh6 avoided the Ne7-Qd8 pin but damaged the pawn structure after Bxh6. The open g-file supplied no verified compensation. Nf4 attacked h5/e6; Qd7 guarded e6 while h5 fell. Name an entry and forcing threat before claiming an attack.
- Rdf8/f6 exf6 Bxf6 Nxf6 Rxf6/Ne5 Nxe5 Rxe5 gave White activity. A legal break is not automatically an improving break.
- Qg7 pinned g3 to Kg1, but Kh2 released the pin: gxf4 again answered ...Rxf4.
- Rf6 defended e6 AND screened Qd4-e5-f6-g7. Rxe6 Rxe6 would expose Qxg7, with no surviving queen defender. ...Kb8 ignored this weakness.
- ...Rg8/...Rd8/...Qa3/...Rf8 spent tempi while f5-f6-f7 advanced. Black's d5 pawn was not passed while c3 remained.
- Rf8 stopped promotion but failed to Qe6+ Kb8 Qd6+ Kc8 Qxf8+: Qd6 checked Kb8 and attacked Rf8 through e7. Blockaders must survive checking forks. Finished 7:29 after many threatless 30-52-second maneuvers.

## T23 Sonnet games: distinguish boards and defenders
- Win: ...f6 BEFORE cxd4. Qb3/c3 made Bd3?? Bxd3 an outright bishop loss. Rd1 removed Nc6-Qc7 pin, but Nd2 still blocked Rd1-d3. ...c4 attacked Q and guarded Bd3.
- Nf3 cleared d2; ...Bf4 Rxd3 cxd3 Bxf4 Nxf4 left an extra rook. ...Qc4 Qxc4 dxc4: c4 guarded d3, not vice versa. Rac8 defended c4.
- ...Re2 Rxe2 dxe2; Ne1 Nd3 Nc2 Re8 g3 e1=Q+ Nxe1 Rxe1+ removed the blockader.
- Loss: cxd4/cxd4/f6, Ngxe5 dxe5 Bxe5 won P despite Nc6's pin. Bd6 Bxd6 Qxd6 abandoned b7; Qxb7 Rab8?? Qxc6 Qxc6 Rxc6 lost N because Qd6 alone guarded c6. ...Rxh3?? gxh3: g2 still attacked h3.

## Other geometry
- Bg5 pins Ne7-Qd8. ...e5 leaves Qd8 alone guarding d5/Ne4; Qf6?? Rxd5.
- ...Rce8 Rxe8 Rxe8 Qxe8+ Qxe8 Rxe8#: count rear attackers; Ng5 bars f7/h7.
- Re6's departure opens Qd5-g8. Rad8?? exd8=N ignores capture-promotion. Kh1 releases Nd4's pin: Qe7?? Nxe7+.
