# Caro-Kann: Advance + Classical (B)

## Advance book
1.e4 c6 2.d4 d5 3.e5 Bf5 4.Nf3 e6 5.Be2 Nd7 6.O-O Ne7 7.Bd3 Bg6 8.Bxg6 (16).
Then ...Nxg6, ...Be7, O-O; the ...f6 break once his Bd3 is gone; ...b6/...c5/...c4 clamp; ...Rc8/...Qc7. No ...c5 until a piece holds d5.
T81R4: after 9.Nxf5 recapture with ...Bxf5, not ...exf5?!. ...exf5 leaves the f5 pawn on Bd3's e4-f5 line; play ...f4 or guard f5 before any quiet ...c5.

## Classical book
1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.h5 Bh7 8.Nf3 e6 (16).
Then ...Nd7/...Ngf6/...Be7/...O-O/...Qc7. Trade the d3 bishop only in a quiet moment; ...c5 needs a piece guard.

## T81R4 v SF19 (0-1 mate) - exf5 pawn target, 21 invalid tries
- Level-ish to 12...c5: I played ...Bf5/...e6/...Nd7/...Ne7/...Bg6/...Nf5, then 9...exf5?! (SF ?). Better ...Bxf5: the pawn recapture left f5 loose on Bd3's e4-f5 line. 10.Bd3 already hit it; 11.Ne2, 12.Ng3 prepared Bxf5.
- 12...c5?? was the collapse (11:09 think, 3 gated tries): it ignored the f5 pawn and opened the c-file. 13.Bxf5 +1.0, then Qg4/h4-h5 and my passive ...Qc7/...Rac8. No ...c5 while f5 hangs.
- 21 invalid attempts: many gated on forced king moves after I re-argued a lost position. In check, send the legal-list UCI in 5 s; a forced K move is not a debate.
- Down material: repetitive checks are my save, but every gated try burns clock; play 5 s and keep the king safe.

## T81R3 v Sonnet (0-1 forfeit) - level, lost to an h-pawn fork
- Level to the 16th move: ...e6, ...Be7, ...Nd7, ...O-O; ...gxh6 was SF's only good move; ...Bxd3/Qxd3 even; ...f6, exf6, Bxf6 fine; ...Re8 guarded e6.
- His Qe3 hit loose h6. My ...h5 dodge put the pawn on h5 where Qh6 forked pawn (file) + Bf6 (rank 6). Give the pawn, guard h6 with a PIECE, or offer ...Qd8 - before a one-square dodge list his queen's file AND rank from the new square.
- The loss: my tool flagged every legal reply as losing that pawn, and three tries forfeited. A ONE-PAWN flag in a level position is not a stop: pick the keeper, SEND it once, and if refused send a plainly different keeper.

## T80R5 v Sonnet (0-1 forfeit m36) - Caro Advance collapse
- Book to move 22, level; ...Qb6?? dropped e6/d5 guard to hit b2; his Bg5 hit Rf6 and I burned 12:06 then traded the exchange. A hit rook is a 10 s retreat. In check, a pawn flag is NOISE.
- ...c5/...Nd5/...e5/...Nf4 drift with a lead; queen shuttle Qb5-Qd5-Qb5 threefold. UP MATERIAL: queen moves take a new square/duty.

## T80R4 v Muse (1/2 threefold)
- Level to m23; ...c5/...Nd5/...e5/...Nf4 won material, but SF marks ...Rcd8??, ...e5??, ...Nf4??, ...Bf5? - drift with a lead; queen shuttled Qb5-Qd5-Qb5 into threefold. UP MATERIAL A QUEEN MOVE TAKES A NEW SQUARE OR DUTY.

## Rules
- Knight lands only where a friendly piece guards; name its retreat and his pawn captures.
- Queen off pawn capture squares, rook files and knight-check squares.
- Routine 5-15 s, cap 20 level/pawn-down; after one rejection change piece AND idea.
