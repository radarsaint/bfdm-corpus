| Scenario | Step | Outcome | Engine read the line as | Rejections | Degraded | Time (s) | Auto flags |
| --- | --- | --- | --- | --- | --- | --- | --- |
| V1 | 0 | committed | opening | 0 |  | 3.5 |  |
| V1 | 1 | committed | social | 0 |  | 18.0 |  |
| V1 | 2 | committed | toll_appeal | 1 |  | 27.3 |  |
| V1 | 3 | committed | social | 1 |  | 39.3 |  |
| V1 | 4 | committed | card_offer | 0 |  | 11.5 |  |
| V2 | 0 | committed | opening | 0 |  | 6.5 |  |
| V2 | 1 | committed | social | 0 |  | 11.5 |  |
| V2 | 2 | committed | toll_threaten | 1 |  | 28.4 |  |
| V2 | 3 | committed | physical_act | 1 |  | 26.3 |  |
| V2 | 4 | committed | combat_round | 2 | yes | 49.2 | no handoff question |
| V3 | 0 | committed | opening | 0 |  | 7.0 |  |
| V3 | 1 | committed | social | 0 |  | 18.0 |  |
| V3 | 2 | committed | social | 0 |  | 14.0 |  |
| V3 | 3 | committed | toll_appeal | 0 |  | 13.0 |  |
| V3 | 4 | committed | social | 2 | yes | 54.7 |  |
| V4 | 0 | committed | opening | 0 |  | 6.5 |  |
| V4 | 1 | committed | social | 0 |  | 23.5 |  |
| V4 | 2 | committed | check | 0 |  | 13.5 |  |
| V4 | 3 | committed | inspect_tub | 1 |  | 30.3 |  |
| V4 | 4 | committed | social | 0 |  | 12.5 |  |
| V5 | 0 | committed | opening | 0 |  | 6.5 |  |
| V5 | 1 | committed | card_watch | 0 |  | 12.0 |  |
| V5 | 2 | committed | card_accuse | 0 |  | 14.0 |  |
| V5 | 3 | committed | card_offer | 0 |  | 13.0 |  |
| V5 | 4 | committed | combat_round | 1 |  | 19.9 | refreshment?:meat; no handoff question |
| V6 | 0 | committed | opening | 0 |  | 7.5 |  |
| V6 | 1 | committed | social | 2 | yes | 42.6 |  |
| V6 | 2 | committed | observe | 0 |  | 13.5 |  |
| V6 | 3 | committed | social | 0 |  | 12.5 |  |
| V7 | 0 | committed | opening | 0 |  | 6.5 |  |
| V7 | 1 | committed | social | 0 |  | 12.0 |  |
| V7 | 2 | committed | toll_haggle | 0 |  | 11.0 |  |
| V7 | 3 | committed | toll_refuse | 0 |  | 12.0 |  |
| V7 | 4 | committed | card_offer | 0 |  | 11.0 |  |
| V8 | 0 | committed | opening | 0 |  | 6.5 |  |
| V8 | 1 | committed | social | 0 |  | 11.5 |  |
| V8 | 2 | committed | card_offer | 2 | yes | 26.7 |  |
| V8 | 3 | committed | card_mode_play | 1 |  | 20.3 |  |
| V8 | 4 | committed | card_mode_check | 1 |  | 21.3 |  |
| V9 | 0 | committed | opening | 0 |  | 6.0 |  |
| V9 | 1 | pending_ruling | Roll the Fireball damage in Avrae. No turn was committed. | 0 |  | 0.1 |  |
| V9 | 2 | pending_ruling | Nobody here is fighting you, so there is no initiative to ro | 0 |  | 0.1 |  |
| V9 | 3 | committed | combat_round | 1 |  | 29.3 | no handoff question |
| V9 | 4 | committed | observe | 0 |  | 12.5 | no handoff question |
| V10 | 0 | committed | opening | 0 |  | 7.5 |  |
| V10 | 1 | committed | social | 0 |  | 12.5 |  |
| V10 | 2 | committed | physical_act | 0 |  | 13.0 |  |
| V10 | 3 | committed | combat_round | 0 |  | 12.0 | no handoff question |
| V10 | 4 | committed | combat_round | 0 |  | 15.0 | no handoff question |
| V11 | 0 | committed | opening | 0 |  | 6.5 |  |
| V11 | 1 | committed | physical_act | 0 |  | 14.0 |  |
| V11 | 2 | committed | social | 0 |  | 12.5 |  |
| V11 | 3 | pending_ruling | Roll the attack for your stomp in Avrae, with its damage. No | 0 |  | 0.1 |  |
| V11 | 4 | committed | combat_round | 1 |  | 32.4 | no handoff question |

| Latency (committed player turns) | n | median (s) | max (s) |
| --- | --- | --- | --- |
| player_turn_total | 40 | 14.0 | 54.7 |
| engine_only | 40 | 0.3 | 0.6 |
| dm_model | 40 | 13.7 | 54.1 |
