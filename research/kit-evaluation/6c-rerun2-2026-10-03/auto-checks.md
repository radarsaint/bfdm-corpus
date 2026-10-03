| Scenario | Step | Outcome | Engine read the line as | Rejections | Degraded | Time (s) | Auto flags |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V1 | 0 | committed | opening | 0 |  | 14.1 |  |
| V1 | 1 | committed | social | 0 |  | 44.1 |  |
| V1 | 2 | committed | toll_appeal | 0 |  | 9.0 |  |
| V1 | 3 | committed | social_check | 2 | yes | 159.7 |  |
| V1 | 4 | committed | card_offer | 0 |  | 24.5 |  |
| V2 | 0 | committed | opening | 0 |  | 8.5 |  |
| V2 | 1 | committed | social | 0 |  | 3.0 |  |
| V2 | 2 | committed | toll_threaten | 0 |  | 9.5 |  |
| V2 | 3 | committed | physical_act | 0 |  | 3.0 |  |
| V2 | 4 | committed | combat_round | 0 |  | 51.6 | no handoff question |
| V3 | 0 | committed | opening | 0 |  | 7.6 |  |
| V3 | 1 | committed | social | 0 |  | 3.1 |  |
| V3 | 2 | committed | check | 0 |  | 23.5 |  |
| V3 | 3 | committed | toll_appeal | 0 |  | 7.0 |  |
| V3 | 4 | committed | social | 0 |  | 3.5 |  |
| V4 | 0 | committed | opening | 0 |  | 3.0 |  |
| V4 | 1 | committed | social | 0 |  | 3.5 |  |
| V4 | 2 | committed | check | 0 |  | 3.0 |  |
| V4 | 3 | committed | inspect_tub | 0 |  | 3.5 |  |
| V4 | 4 | committed | social | 0 |  | 3.5 |  |
| V5 | 0 | committed | opening | 0 |  | 3.0 |  |
| V5 | 1 | committed | card_watch | 0 |  | 3.0 |  |
| V5 | 2 | committed | card_accuse | 0 |  | 3.5 |  |
| V5 | 3 | committed | check | 0 |  | 44.5 |  |
| V5 | 4 | committed | combat_round | 0 |  | 15.0 | refreshment?:meat; no handoff question |
| V6 | 0 | committed | opening | 0 |  | 8.0 |  |
| V6 | 1 | committed | social | 0 |  | 36.0 |  |
| V6 | 2 | committed | observe | 0 |  | 9.0 |  |
| V6 | 3 | committed | social | 0 |  | 3.5 |  |
| V7 | 0 | committed | opening | 0 |  | 3.0 |  |
| V7 | 1 | committed | social | 0 |  | 3.5 |  |
| V7 | 2 | committed | toll_haggle | 0 |  | 3.5 |  |
| V7 | 3 | committed | toll_refuse | 0 |  | 3.0 |  |
| V7 | 4 | committed | card_offer | 0 |  | 3.5 |  |
| V8 | 0 | committed | opening | 0 |  | 3.0 |  |
| V8 | 1 | committed | social | 0 |  | 3.5 |  |
| V8 | 2 | committed | card_offer | 0 |  | 3.5 |  |
| V8 | 3 | committed | card_mode_play | 0 |  | 12.5 |  |
| V8 | 4 | committed | card_mode_check | 0 |  | 23.5 |  |
| V9 | 0 | committed | opening | 0 |  | 7.0 |  |
| V9 | 1 | committed | combat_round | 0 |  | 11.0 | no handoff question |
| V9 | 2 | committed | combat_round | 0 |  | 15.5 | no handoff question |
| V9 | 3 | committed | combat_round | 0 |  | 16.5 |  |
| V9 | 4 | committed | observe | 0 |  | 16.0 |  |
| V10 | 0 | committed | opening | 0 |  | 7.5 |  |
| V10 | 1 | committed | social | 0 |  | 3.5 |  |
| V10 | 2 | committed | physical_act | 0 |  | 3.0 |  |
| V10 | 3 | committed | combat_round | 0 |  | 3.5 | no handoff question |
| V10 | 4 | committed | combat_round | 0 |  | 10.5 | no handoff question |
| V11 | 0 | committed | opening | 0 |  | 7.5 |  |
| V11 | 1 | committed | physical_act | 0 |  | 3.0 |  |
| V11 | 2 | committed | social | 0 |  | 3.5 |  |
| V11 | 3 | pending_ruling | Roll the attack for your stomp in Avrae, with its damage. No | 0 |  | 0.1 |  |
| V11 | 4 | committed | combat_round | 0 |  | 21.5 | no handoff question |

| Latency (committed player turns) | n | median (s) | max (s) |
| --- | --- | --- | --- |
| player_turn_total | 42 | 3.5 | 159.7 |
| engine_only | 42 | 0.3 | 0.6 |
| dm_model | 42 | 3.2 | 159.2 |
