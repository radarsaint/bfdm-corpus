| Scenario | Step | Outcome | Engine read the line as | Rejections | Degraded | Time (s) | Auto flags |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V1 | 0 | committed | opening | 0 |  | 3.5 |  |
| V1 | 1 | committed | social | 0 |  | 50.5 |  |
| V1 | 2 | committed | social | 0 |  | 24.0 |  |
| V1 | 3 | abandoned_after_rejections | abandoned_after_rejections | 4 |  | 82.5 |  |
| V1 | 4 | abandoned_after_rejections | abandoned_after_rejections | 4 |  | 92.6 |  |
| V2 | 0 | committed | opening | 0 |  | 15.5 |  |
| V2 | 1 | committed | social | 0 |  | 14.5 |  |
| V2 | 2 | committed | toll_pay | 1 |  | 33.3 |  |
| V2 | 3 | committed | observe | 1 |  | 39.3 |  |
| V2 | 4 | committed | social | 3 | yes | 48.5 |  |
| V3 | 0 | committed | opening | 0 |  | 7.5 |  |
| V3 | 1 | committed | social | 0 |  | 15.5 |  |
| V3 | 2 | committed | social | 0 |  | 24.0 |  |
| V3 | 3 | committed | toll_refuse | 0 |  | 16.5 |  |
| V3 | 4 | committed | social | 1 |  | 26.8 |  |
| V4 | 0 | committed | opening | 0 |  | 7.0 |  |
| V4 | 1 | committed | social | 2 | yes | 36.6 |  |
| V4 | 2 | committed | check | 1 |  | 22.8 |  |
| V4 | 3 | committed | social | 2 | yes | 42.6 |  |
| V4 | 4 | committed | social | 0 |  | 15.0 |  |
| V5 | 0 | committed | opening | 0 |  | 6.5 |  |
| V5 | 1 | committed | card_watch | 0 |  | 13.5 |  |
| V5 | 2 | committed | card_offer | 0 |  | 16.5 |  |
| V5 | 3 | committed | check | 0 |  | 15.5 |  |
| V5 | 4 | committed | social | 0 |  | 14.5 |  |
| V6 | 0 | committed | opening | 0 |  | 7.5 |  |
| V6 | 1 | committed | social | 1 |  | 22.8 |  |
| V6 | 2 | pending_ruling | physical action refused | 0 |  | 0.1 |  |
| V6 | 3 | committed | social | 1 |  | 25.8 |  |
| V7 | 0 | committed | opening | 0 |  | 7.0 |  |
| V7 | 1 | committed | exit | 1 |  | 23.3 | no handoff question |
| V7 | 2 | pending_ruling | left the room (slice ends) | 0 |  | 0.1 |  |
| V7 | 3 | pending_ruling | left the room (slice ends) | 0 |  | 0.1 |  |
| V7 | 4 | pending_ruling | left the room (slice ends) | 0 |  | 0.1 |  |
| V8 | 0 | committed | opening | 0 |  | 10.5 |  |
| V8 | 1 | committed | social | 0 |  | 16.0 |  |
| V8 | 2 | committed | card_offer | 0 |  | 14.0 |  |
| V8 | 3 | committed | card_mode_play | 0 |  | 13.5 |  |
| V8 | 4 | committed | social | 0 |  | 12.5 |  |
| V9 | 0 | committed | opening | 0 |  | 6.5 |  |
| V9 | 1 | pending_ruling | combat stall | 0 |  | 0.1 |  |
| V9 | 2 | pending_ruling | combat stall | 0 |  | 0.1 |  |
| V9 | 3 | committed | social | 0 |  | 9.5 |  |
| V9 | 4 | committed | social | 1 |  | 20.8 |  |
| V10 | 0 | committed | opening | 0 |  | 7.0 |  |
| V10 | 1 | committed | social | 0 |  | 14.0 |  |
| V10 | 2 | committed | social | 0 |  | 15.0 |  |
| V10 | 3 | committed | social | 0 |  | 15.5 |  |
| V10 | 4 | pending_ruling | combat stall | 0 |  | 0.1 |  |
| V11 | 0 | committed | opening | 0 |  | 7.0 |  |
| V11 | 1 | committed | social | 0 |  | 14.5 |  |
| V11 | 2 | committed | social | 1 |  | 21.8 |  |
| V11 | 3 | committed | social | 0 |  | 8.5 |  |
| V11 | 4 | pending_ruling | combat stall | 0 |  | 0.1 |  |

| Latency (committed player turns) | n | median (s) | max (s) |
| --- | --- | --- | --- |
| player_turn_total | 33 | 16.5 | 50.5 |
| engine_only | 33 | 0.3 | 0.6 |
| dm_model | 33 | 16.2 | 50.2 |
