# Homebrew player-option inventory

Authority: `main` at `6795362e967e89230086afc28c04450cc7d0cce4`. This file is a research index. It is not a rules replacement and not a legal-rights finding.

The machine-readable copy of every field is [options.jsonl](options.jsonl). One JSON object per line. Open that file for a single option rather than searching the whole corpus again.

Discord evidence is counts, channel names, and message ids in [discord-mentions.jsonl](discord-mentions.jsonl). Message text is not copied. `play_observed` is `NOT_ESTABLISHED` on every record. A published page is not play. A name in a channel is not play.

## Counts

Option records: **159**.

| Type | Count |
|---|---|
| background | 25 |
| character_creation_system | 5 |
| class | 2 |
| class_archetype_name | 48 |
| class_feature_table | 1 |
| event_adaptation | 1 |
| life_path | 3 |
| race | 11 |
| race_reskin | 25 |
| spell | 12 |
| subclass | 17 |
| subrace | 9 |

| Design relation | Count |
|---|---|
| BESPOKE | 65 |
| BESPOKE_ALSO_PRESENTED_AS_RESKIN | 11 |
| BESPOKE_FRAMEWORK | 4 |
| EVENT_ADAPTATION_OF_PUBLISHED_CHASSIS | 1 |
| EXTERNAL_ALLOWLIST | 1 |
| NAME_ONLY | 50 |
| RESKIN | 25 |
| UNRESOLVED | 2 |

Published (a player-facing Site or equivalent published capture): 64. Not published: 95.

Status fields are separate. `status_published` means a player-facing published capture contains the option. `status_offered` means a character-creation text or event text offers it. `status_draft` means a draft or edit document contains it. An option can be more than one. `play_observed` is not inferred from either.

## Do not collapse these conflicts

- Char-gen approved-homebrew lines map several peoples onto published species. The homebrew-races page also prints bespoke trait blocks. Records use `BESPOKE_ALSO_PRESENTED_AS_RESKIN`. The map is not a finding that the traits are unchanged.
- Seraph is mapped from both Aasimar and Tiefling on char-gen.
- Tatankan / Tatakan. Palomino / Palamino. Lumber Jacked / Lumberjacked. Mischievous / Mischiveous. Gritgiblin / Gritgiblins. Gun Fu / Gunfu / Gun-Fu.
- Savage Fertility (heading) versus Frontier's Blessing (prose and changelog).
- Mississippi Mudskipper (heading) versus Mississippi Catfish (age and social lines) versus Locathah / Locatha.
- Peach Punk Gnomes versus char-gen's Gnorgian Peachpunk. Bullygrung is named on char-gen and has no trait block on the race page.
- Way of Gun Fu: published site does not contain 'short or long rest'. PDF BCS-000114 limits Focused Beatdown to a short or long rest. Changelog says the published feature has no usage limit.
- Combat Field Scholar is a background. BCS-000085's Order of Saint George block does not contain the reaction feature.
- Pigeon Lord v2 spells Coo Tounge and Coo Tongue. Draft BCS-000148 is not v2. Flock of the Lame is not equated with the draft heading The Ridonculous Flock.
- Isekai file BCS-000189 is reskin-only. Mapped names Geppetin and Geleton are printed as-is.
- Wellspring archetype names have role briefs only. Section V of BCS-000066 says to brainstorm signature abilities. None were invented here.
- Clerrook is not in the corpus.

## Index

| ID | Name | Type | Relation | Published | Primary |
|---|---|---|---|---|---|
| `awe-wellsprings` | Four Wellsprings and class archetypes | character_creation_system | BESPOKE_FRAMEWORK | no | `sources/at-wars-end/BCS-000066/source.md:394` |
| `bar-char-gen` | Bastion and Redoubt character creation | character_creation_system | BESPOKE_FRAMEWORK | no | `sources/bastion-redoubt/BCS-000058/source.md:20` |
| `bg-cfs` | Combat Field Scholar | background | BESPOKE | no | `sources/later-play/BCS-000191/source.md:77` |
| `bg-s3-george` | The Order of Saint George the Dragon Slayer | background | BESPOKE | no | `sources/roanoke/BCS-000085/source.md:51` |
| `bg-s3-groundlings` | The Groundlings of the Globe | background | BESPOKE | no | `sources/roanoke/BCS-000085/source.md:294` |
| `bg-s3-highgate` | The Highgate Hunting Club | background | BESPOKE | no | `sources/roanoke/BCS-000085/source.md:401` |
| `bg-s3-lazarus` | The Lazurian Oath | background | BESPOKE | no | `sources/roanoke/BCS-000085/source.md:101` |
| `bg-s3-vigil` | The Vigil of Siege Perilous | background | BESPOKE | no | `sources/roanoke/BCS-000085/source.md:206` |
| `bg-s4-barber` | Barber | background | BESPOKE | no | `sources/empire-city/BCS-000184/source.md:8` |
| `bg-s4-bootlegger` | Bootlegger | background | BESPOKE | no | `sources/empire-city/BCS-000184/source.md:23` |
| `bg-s4-mechanic` | Black Thumb Mechanic | background | BESPOKE | no | `sources/empire-city/BCS-000184/source.md:48` |
| `bg-s4-minuteman` | Minuteman | background | BESPOKE | no | `sources/empire-city/BCS-000184/source.md:56` |
| `bg-s4-thespian` | Broadway Thespian | background | BESPOKE | no | `sources/empire-city/BCS-000184/source.md:38` |
| `bg-s4-todo-panhandler` | Panhandler | background | NAME_ONLY | no | `sources/empire-city/BCS-000184/source.md:71` |
| `bg-s4-todo-reporter` | Reporter | background | NAME_ONLY | no | `sources/empire-city/BCS-000184/source.md:71` |
| `bg-s5-crypto` | Cryptozoologist | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:125` |
| `bg-s5-illuminated` | Illuminated Scholar | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:243` |
| `bg-s5-pioneer` | Pioneer | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:331` |
| `bg-s5-rainier` | Guardian of Mount Rainier | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:271` |
| `bg-s5-raven` | Raven Herald | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:151` |
| `bg-s5-rockefeller` | Baron Rockefeller's Enforcers | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:73` |
| `bg-s5-scholar` | Scholar of the Ivory Tower | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:213` |
| `bg-s5-shadow` | Shadow Sentinel | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:99` |
| `bg-s5-slicker` | Empire City Slicker | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:47` |
| `bg-s5-steamboat` | Steamboat Captain | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:303` |
| `bg-s5-vanderbilt` | Baron Vanderbilt's Guardians | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:19` |
| `bg-s5-verdant` | Verdantreach Explorer | background | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md:187` |
| `ec-class-pigeon-lord` | Pigeon Lord | class | BESPOKE | no | `sources/empire-city/BCS-000175/source.md:112` |
| `ec-sub-flock-of-names` | The Flock of Names | subclass | BESPOKE | no | `sources/empire-city/BCS-000175/source.md:136` |
| `ec-sub-flock-of-the-lame` | The Flock of the Lame | subclass | BESPOKE | no | `sources/empire-city/BCS-000175/source.md:172` |
| `event-bowling` | Bowling event class adaptations | event_adaptation | EVENT_ADAPTATION_OF_PUBLISHED_CHASSIS | no | `sources/bowling-event/BCS-000182/source.md:92` |
| `gap-bullygrung` | Bullygrung | race | UNRESOLVED | yes | `sources/roanoke-s5-legends/google-sites/char-gen/pages/home.md:199` |
| `gap-clerrook` | Clerrook | subclass | UNRESOLVED | no | `research/source-leads/homebrew-mechanics-worldbuilding.md:51` |
| `isekai-01-asari-mass-effect` | Asari (Mass Effect) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:16` |
| `isekai-02-yautja-predator` | Yautja (Predator) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:47` |
| `isekai-03-time-bandits` | Time Bandits | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:75` |
| `isekai-04-themyscirian-wonderwomen` | Themyscirian (Wonderwomen) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:106` |
| `isekai-05-na-vi-pandorian` | Na'vi (Pandorian) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:134` |
| `isekai-06-gelfling` | Gelfling | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:171` |
| `isekai-07-marooned-grays` | Marooned Grays | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:202` |
| `isekai-08-space-marines` | Space Marines | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:230` |
| `isekai-09-care-bears` | Care Bears | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:258` |
| `isekai-10-paleborn` | Paleborn | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:289` |
| `isekai-11-gargoyles` | Gargoyles | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:314` |
| `isekai-12-symbiote` | Symbiote | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:339` |
| `isekai-13-thundarian-thundercats` | Thundarian (Thundercats) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:367` |
| `isekai-14-programs` | Programs | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:395` |
| `isekai-15-the-silence-doctor-who` | The Silence (Doctor Who) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:423` |
| `isekai-16-my-little-pony` | My Little Pony | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:457` |
| `isekai-17-furby` | Furby | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:485` |
| `isekai-18-gary-clones` | Gary Clones | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:513` |
| `isekai-19-wookiees` | Wookiees | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:530` |
| `isekai-20-mutants-tmnt` | Mutants (TMNT) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:550` |
| `isekai-21-brownies-willow` | Brownies (Willow) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:576` |
| `isekai-22-adam-addict-rapture` | Adam Addict (Rapture) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:598` |
| `isekai-23-mogwai-gremlins` | Mogwai (Gremlins) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:608` |
| `isekai-24-moogles-ff6` | Moogles (FF6) | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:630` |
| `isekai-25-gummi-bears` | Gummi Bears | race_reskin | RESKIN | no | `sources/later-play/BCS-000189/source.md:652` |
| `later-allow-lists` | External content allow-lists | character_creation_system | EXTERNAL_ALLOWLIST | no | `sources/later-play/BCS-000192/source.md:8` |
| `s5-char-gen` | Season 5 character creation | character_creation_system | BESPOKE_FRAMEWORK | yes | `sources/roanoke-s5-legends/google-sites/char-gen/pages/home.md:15` |
| `s5-class-harbinger` | Harbinger | class | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/harbingers5/pages/home.md:93` |
| `s5-downtime-training` | Season 5 downtime training | character_creation_system | BESPOKE_FRAMEWORK | yes | `sources/roanoke-s5-legends/google-sites/s5-training/pages/home.md:17` |
| `s5-enforcer-improvised-table` | Enforcer improvised-weapon tables | class_feature_table | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/improvised-weapon-for-enforcer/pages/home.md:1` |
| `s5-life-gambler` | Gambler | life_path | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/lifepathgambler/pages/home.md:1` |
| `s5-life-miner` | Miner | life_path | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5mining/pages/home.md:15` |
| `s5-life-rancher` | Rancher | life_path | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/lifepathrancher/pages/home.md:1` |
| `s5-race-bigfoot` | Bigfoot | race | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:705` |
| `s5-race-brunelock` | Brunelock | race | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:753` |
| `s5-race-chinnokin` | Chinnokin | race | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:157` |
| `s5-race-halfwudgie` | Halfwudgie | race | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:853` |
| `s5-race-jackalope` | Jackalope | race | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:21` |
| `s5-race-peach-punk` | Peach Punk Gnomes | race | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:665` |
| `s5-race-puffkin` | Puffkin | race | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:585` |
| `s5-race-seraph` | Seraph | race | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:271` |
| `s5-race-tatankan` | Tatankan | race | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:83` |
| `s5-sub-codebound` | Oath of the Codebound | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5-codebound/pages/home.md:15` |
| `s5-sub-drifter` | Oath of the Drifter | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/oath-of-the-drifter/pages/home.md:55` |
| `s5-sub-enforcer` | Enforcer | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5rogueoptions/pages/home.md:21` |
| `s5-sub-gunfu` | Way of Gun Fu | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/arcanian-monk-options/pages/home.md:15` |
| `s5-sub-harbinger-bonds` | Harbinger of Fated Bonds | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/harbingers5/pages/home.md:283` |
| `s5-sub-harbinger-endings` | Harbinger of Endings | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/harbingers5/pages/home.md:237` |
| `s5-sub-harbinger-veils` | Harbinger of Veils | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/harbingers5/pages/home.md:315` |
| `s5-sub-joybringer` | Joybringer Domain | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5homebrewclericoptions/pages/home.md:43` |
| `s5-sub-lumberjacked` | Path of the Lumber Jacked | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/path-of-the-lumber-jacked/pages/home.md:1` |
| `s5-sub-rail-baron` | Rail Baron Pact | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5warlockoptions/pages/home.md:17` |
| `s5-sub-savage-fertility` | Domain of Savage Fertility | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5homebrewclericoptions/pages/home.md:95` |
| `s5-sub-spellshot` | Spellshot | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/spellshotwizard/pages/home.md:1` |
| `s5-sub-trail` | College of the Trail | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5bardcolleges/pages/home.md:15` |
| `s5-sub-whims` | Domain of Mischievous Whims | subclass | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/s5homebrewclericoptions/pages/home.md:167` |
| `s5-subrace-bobcat` | Appalachian Bobcat | subrace | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:411` |
| `s5-subrace-gritgiblin` | Gritgiblin | subrace | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:311` |
| `s5-subrace-klondike` | Klondike Goliath | subrace | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:523` |
| `s5-subrace-mudskipper` | Mississippi Mudskipper | subrace | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:371` |
| `s5-subrace-palomino` | Palomino Centaur | subrace | BESPOKE_ALSO_PRESENTED_AS_RESKIN | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:475` |
| `s5-subrace-plainsguard` | Plainsguard | subrace | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:133` |
| `s5-subrace-spiritspeaker` | Spiritspeaker | subrace | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:145` |
| `s5-subrace-sunrise-puffkin` | Sunrise Puffkin | subrace | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:609` |
| `s5-subrace-sunset-puffkin` | Sunset Puffkin | subrace | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md:633` |
| `spell-amnesty` | Amnesty | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:171` |
| `spell-bliss` | Bliss | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:95` |
| `spell-boldness` | Boldness | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:139` |
| `spell-cringe` | Cringe | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:15` |
| `spell-defiance` | Defiance | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:211` |
| `spell-desolation` | Desolation | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:391` |
| `spell-despair` | Contagious Despair | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:433` |
| `spell-dread` | Dread | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:37` |
| `spell-dumb-ways` | Dumb Ways to Die | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:243` |
| `spell-frustration` | Frustration | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:65` |
| `spell-pursuit` | Terrifying Pursuit | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:349` |
| `spell-shame` | Shame | spell | BESPOKE | yes | `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md:313` |
| `uru-urucokra` | Urucokra | race | BESPOKE | no | `sources/roanoke/BCS-000120/source.md:37` |

At War's End class-archetype names are a table at the end. Their rules are the role brief only.

## Entries

### Four Wellsprings and class archetypes

- **ID:** `awe-wellsprings`
- **Type:** character_creation_system
- **Setting:** At War's End
- **Design relation:** BESPOKE_FRAMEWORK
- **Completeness:** NAMES_AND_ROLE_BRIEFS_ONLY
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000066
- **Source:** `sources/at-wars-end/BCS-000066/source.md` line 394. (no URL; Drive or repo text)
- **Anchor:** ## **IV. Four Wellsprings & Their Class Archetypes** Below, each Primal Wellspring is paired with every Focus to form a specific “class” name and role. Think of these as the *first tier* of Confluences—how raw Wellspring current + Focus anatomy/psyche produce a distinctive archet
- **Overview:** A character-building framework. Two focus types (Corporea and Essentia), six named foci in each, and four wellsprings (Divine, Eldritch Shadow, Arcane, Valor). Crossing a focus with a wellspring names a class archetype and gives a one-line role. Section V tells the reader to brainstorm signature abilities. This inventory does not treat those names as written classes.
- **Discord phrase hits (not play):** empire-city: Wellspring 1
- **Sample message ids:** 869422759229390899 (empire-city, dead-chat👻, 2021-07-27)
- **Note:** Child records are the named archetypes. They have no level table in this source.

### Bastion and Redoubt character creation

- **ID:** `bar-char-gen`
- **Type:** character_creation_system
- **Setting:** Bastion and Redoubt
- **Design relation:** BESPOKE_FRAMEWORK
- **Completeness:** ORIENTATION_ONLY
- **Draft / published / offered / play-observed:** False / False / True / NOT_ESTABLISHED
- **Corpus:** BCS-000058
- **Source:** `sources/bastion-redoubt/BCS-000058/source.md` line 20. (no URL; Drive or repo text)
- **Anchor:** \- **Point Buy System:** We will be using the point buy system for character creation. This ensures a balanced and fair starting point for all characters.
- **Overview:** Orientation for Bastion and Redoubt. Point buy. All player characters are city guards. Custom backgrounds are encouraged. Each character receives a custom growth item that evolves, and may requisition special items for a session. The captured text does not list homebrew races, classes, or feats.
- **Note:** Offered means the captured guide offers this procedure to players. It is not a Season 5 Google Site.

### Combat Field Scholar

- **ID:** `bg-cfs`
- **Type:** background
- **Also printed as:** Order of Saint George, CFS
- **Setting:** Captured PDF BCS-000191. Related to the Roanoke Season 3 Order of Saint George background in BCS-000085. Not a class.
- **Design relation:** BESPOKE
- **Completeness:** PDF_TEXT_EXTRACT
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000191, BCS-000085
- **Source:** `sources/later-play/BCS-000191/source.md` line 77. (no URL; Drive or repo text)
- **Anchor:** Feature: The Meek shall Inherit Your time spent learning how to squire, scholar and scrub
- **Overview:** Background. Skill proficiencies: Persuasion and history or religion. Tool: Dragon chess (the extract spells 'Tool Proficirncies'). Language: Draconic. Feature: The Meek shall Inherit. As a reaction, retry a Charisma-based skill check that another player has failed. The same Order of Saint George fiction appears in BCS-000085, where the Feature label has no following feature sentence before the tool line.
- **Mechanics:**
  - The Meek shall Inherit. As a reaction, you may retry a Charisma based skill check that another player has failed.
- **Conflicts:**
  - BCS-000191 gives the reaction feature The Meek shall Inherit. BCS-000085's Order of Saint George block labels 'Feature:' and then lists the tool and equipment, with no feature sentence.
  - BCS-000191 spells 'Tool Proficirncies' and 'Lazaurian' is a different background. Do not merge Combat Field Scholar into a class chassis.
- **Lineage:**
  - BCS-000085: Season 3 public backgrounds. Same order, feature label without this reaction rule in the captured text.
- **Discord phrase hits (not play):** roanoke-season-3: Field Scholar 1
- **Sample message ids:** 734220005062869012 (roanoke-season-3, 🌁-london, 2020-07-19)
- **Note:** A Discord phrase search for 'Combat Field Scholar' was not the same as 'Field Scholar'. 'Field Scholar' had 1 hit in Roanoke Season 3 channel london. That hit is not play evidence for this feature. Discord counts for a common word are phrase hits, not a census of characters.

### The Order of Saint George the Dragon Slayer

- **ID:** `bg-s3-george`
- **Type:** background
- **Setting:** Roanoke Season 3 public backgrounds document
- **Design relation:** BESPOKE
- **Completeness:** DRAFT_OR_PUBLIC_DOC_PARTIAL
- **Draft / published / offered / play-observed:** True / False / True / NOT_ESTABLISHED
- **Corpus:** BCS-000085
- **Source:** `sources/roanoke/BCS-000085/source.md` line 51. (no URL; Drive or repo text)
- **Anchor:** The Order of Saint George the Dragon Slayer. (PDF) You have spent your days in service of the Order of St. George. The Order is descended from the group of adventurers who famously slayed the Ancient Green Dragon of Wales, Bwytawr ffwl (Fool Eater). Bwytawr ffwl was a tyrant who ruled Wales through deceit and guile. Sa
- **Overview:** Persuasion and history or religion; dragon chess; Draconic. The feature label is empty in this capture. See Combat Field Scholar for a later feature on the same fiction.
- **Note:** BCS-000085 also names, without full blocks, The Gamesmen and Falconers and The Royal Academy of Naturalistic studies. Those two are name stubs only and are not given option records.

### The Groundlings of the Globe

- **ID:** `bg-s3-groundlings`
- **Type:** background
- **Setting:** Roanoke Season 3 public backgrounds document
- **Design relation:** BESPOKE
- **Completeness:** BACKGROUND_BLOCK
- **Draft / published / offered / play-observed:** True / False / True / NOT_ESTABLISHED
- **Corpus:** BCS-000085
- **Source:** `sources/roanoke/BCS-000085/source.md` line 294. (no URL; Drive or repo text)
- **Anchor:** The Groundlings of the Globe. You are one of the few, one of the dedicated suffering artists who is as likely to be paid in stew and ale for his art as he is to play for precious gems and sacks of gold from royalty. The Globe may be burnt to the ground, but the Groundlings of the Globe still live on in every audience m
- **Overview:** Feature: Scribbles for nibbles. Patronage in exchange for art. Skills Performance and Sleight of Hand. Any instrument.
- **Note:** BCS-000085 also names, without full blocks, The Gamesmen and Falconers and The Royal Academy of Naturalistic studies. Those two are name stubs only and are not given option records.

### The Highgate Hunting Club

- **ID:** `bg-s3-highgate`
- **Type:** background
- **Setting:** Roanoke Season 3 public backgrounds document
- **Design relation:** BESPOKE
- **Completeness:** BACKGROUND_BLOCK
- **Draft / published / offered / play-observed:** True / False / True / NOT_ESTABLISHED
- **Corpus:** BCS-000085
- **Source:** `sources/roanoke/BCS-000085/source.md` line 401. (no URL; Drive or repo text)
- **Anchor:** The Highgate Hunting Club Highgate Cemetery is known as one the Magnificent Seven Cemeteries of London. It is from these majestic hallowed grounds that The Highgate Club takes its name.This well funded group of monster hunters is known through their tales as told in the Strand Magazine, a publication well known for its
- **Overview:** Feature: Ear to the Ground. A contact in any city who can provide advantage on checks to find specific kinds of non-humanoid monsters. The page mentions vampires and werewolves as an example of Old World cryptid themes inside the club's fiction. That sentence is the source's example, not a player species in this inventory.
- **Note:** BCS-000085 also names, without full blocks, The Gamesmen and Falconers and The Royal Academy of Naturalistic studies. Those two are name stubs only and are not given option records.

### The Lazurian Oath

- **ID:** `bg-s3-lazarus`
- **Type:** background
- **Setting:** Roanoke Season 3 public backgrounds document
- **Design relation:** BESPOKE
- **Completeness:** DRAFT_OR_PUBLIC_DOC_PARTIAL
- **Draft / published / offered / play-observed:** True / False / True / NOT_ESTABLISHED
- **Corpus:** BCS-000085
- **Source:** `sources/roanoke/BCS-000085/source.md` line 101. (no URL; Drive or repo text)
- **Anchor:** The Lazurian Oath “And verily, the Lord of our order said: "Health is the greatest gain." He also said: "He who would minister to me should minister unto the sick."
- **Overview:** Also spelled Lazaurian in the next heading. Members call themselves the Afflicted. Specialties: Diagnostics, Apothecary, Surgery, Bone Setting, Therapy, Research. Skills Medicine and Insight. Feature label: Burden of Life. No rules sentence follows that label before Traits in the capture.
- **Conflicts:**
  - Lazurian versus Lazaurian spelling.
- **Note:** BCS-000085 also names, without full blocks, The Gamesmen and Falconers and The Royal Academy of Naturalistic studies. Those two are name stubs only and are not given option records.

### The Vigil of Siege Perilous

- **ID:** `bg-s3-vigil`
- **Type:** background
- **Setting:** Roanoke Season 3 public backgrounds document
- **Design relation:** BESPOKE
- **Completeness:** BACKGROUND_BLOCK
- **Draft / published / offered / play-observed:** True / False / True / NOT_ESTABLISHED
- **Corpus:** BCS-000085
- **Source:** `sources/roanoke/BCS-000085/source.md` line 206. (no URL; Drive or repo text)
- **Anchor:** The Vigil of Siege Perilous Before there was England there was the throne. Before the first of the angler tribe departed the main land of the Old World, there was the throne. At the dawning of the dragons, the green and the red, the white and the black laid claim to all of the land. A single gold dragon looked on the i
- **Overview:** Choose a virtue and a vice with the DM. Feature: Arbiter. Minor disputes, traditional payment 5 gold. Skills Intimidation and Insight. Calligraphy set and a viol. Language Dwarvish.
- **Note:** BCS-000085 also names, without full blocks, The Gamesmen and Falconers and The Royal Academy of Naturalistic studies. Those two are name stubs only and are not given option records.

### Barber

- **ID:** `bg-s4-barber`
- **Type:** background
- **Setting:** Empire City / Season 4 homebrew backgrounds
- **Design relation:** BESPOKE
- **Completeness:** BACKGROUND_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000184
- **Source:** `sources/empire-city/BCS-000184/source.md` line 8. (no URL; Drive or repo text)
- **Anchor:** Barber Working with hair is not your only ability as a barber. You have spent your years of cutting hair being asked to do odd jobs around the body of many humanoids. Jobs include pulling teeth, sewing arms back on, or chopping off gangrenous limbs. The unwanted expectations of others have made you competent in the blo
- **Overview:** Medicine, Deception. Herbalism and poisoner's kit. Feature: The barber's assurance. +2 to persuasion when asking for a small knife or scissors.
- **Note:** The same document ends with 'Todo: minuteman, reporter, panhandler' even though a Minuteman block is present above that line. Reporter and panhandler are names in the todo only. No rules were written for them here.

### Bootlegger

- **ID:** `bg-s4-bootlegger`
- **Type:** background
- **Setting:** Empire City / Season 4 homebrew backgrounds
- **Design relation:** BESPOKE
- **Completeness:** BACKGROUND_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000184
- **Source:** `sources/empire-city/BCS-000184/source.md` line 23. (no URL; Drive or repo text)
- **Anchor:** Bootlegger: Everyone needs something and bootleggers know how to get things past the redcoats and the minutemen. While others rely on stealth and guile, you have built hiding places and dead drops.
- **Overview:** Deception, Survival. Land vehicles, brewing. Feature: Give em the slip. Opposed Survival versus Perception to get away with what you are carrying.
- **Note:** The same document ends with 'Todo: minuteman, reporter, panhandler' even though a Minuteman block is present above that line. Reporter and panhandler are names in the todo only. No rules were written for them here.

### Black Thumb Mechanic

- **ID:** `bg-s4-mechanic`
- **Type:** background
- **Setting:** Empire City / Season 4 homebrew backgrounds
- **Design relation:** BESPOKE
- **Completeness:** BACKGROUND_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000184
- **Source:** `sources/empire-city/BCS-000184/source.md` line 48. (no URL; Drive or repo text)
- **Anchor:** Black Thumb Mechanic: Your thumbs are black, and you smell like grease. But these are a mark of pride. The Empire City Blackthumbs has certified you to work on all manner of vehicles.
- **Overview:** Air, land, and water vehicles. Feature text begins 'An engineer is always welcome on any vehicle with room to spare' and waives tickets in exchange for repairs, without a separate feature name.
- **Note:** The same document ends with 'Todo: minuteman, reporter, panhandler' even though a Minuteman block is present above that line. Reporter and panhandler are names in the todo only. No rules were written for them here.

### Minuteman

- **ID:** `bg-s4-minuteman`
- **Type:** background
- **Setting:** Empire City / Season 4 homebrew backgrounds
- **Design relation:** BESPOKE
- **Completeness:** BACKGROUND_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000184
- **Source:** `sources/empire-city/BCS-000184/source.md` line 56. (no URL; Drive or repo text)
- **Anchor:** Minuteman: “Ready within a minute’s notice” you have been trained in the techniques of rapidly being ready for combat, as well as military tactics, including hit and run and guerilla fighting.
- **Overview:** Stealth, Survival. Navigator's tools. Feature: Guerilla Tactics. +5 initiative if enemies have not detected you. Net restraint Strength DC becomes 15.
- **Conflicts:**
  - Todo line still lists minuteman after a Minuteman block exists.
- **Note:** The same document ends with 'Todo: minuteman, reporter, panhandler' even though a Minuteman block is present above that line. Reporter and panhandler are names in the todo only. No rules were written for them here.

### Broadway Thespian

- **ID:** `bg-s4-thespian`
- **Type:** background
- **Setting:** Empire City / Season 4 homebrew backgrounds
- **Design relation:** BESPOKE
- **Completeness:** BACKGROUND_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000184
- **Source:** `sources/empire-city/BCS-000184/source.md` line 38. (no URL; Drive or repo text)
- **Anchor:** Broadway Thespian: The bright lights of Broadway cast many shadows. You have spent your life dreaming of the spotlight. Tryout after tryout has made you numb to being told you aren’t right for the part. You're emotionally resilient. Choose from the following professions: life coach, assistant to the assistant stage man
- **Overview:** Perception, Insight. Disguise and forgery kits. Feature: Waiter, waitress or server. Union card, one gold per day for an 8 hour shift.
- **Note:** The same document ends with 'Todo: minuteman, reporter, panhandler' even though a Minuteman block is present above that line. Reporter and panhandler are names in the todo only. No rules were written for them here.

### Panhandler

- **ID:** `bg-s4-todo-panhandler`
- **Type:** background
- **Setting:** Named only in the todo line of BCS-000184
- **Design relation:** NAME_ONLY
- **Completeness:** NAME_ONLY
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000184
- **Source:** `sources/empire-city/BCS-000184/source.md` line 71. (no URL; Drive or repo text)
- **Anchor:** Todo: minuteman, reporter, panhandler
- **Overview:** Name only. No proficiencies or feature were written in this document.

### Reporter

- **ID:** `bg-s4-todo-reporter`
- **Type:** background
- **Setting:** Named only in the todo line of BCS-000184
- **Design relation:** NAME_ONLY
- **Completeness:** NAME_ONLY
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000184
- **Source:** `sources/empire-city/BCS-000184/source.md` line 71. (no URL; Drive or repo text)
- **Anchor:** Todo: minuteman, reporter, panhandler
- **Overview:** Name only. No proficiencies or feature were written in this document.

### Cryptozoologist

- **ID:** `bg-s5-crypto`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 125. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Background: Cryptozoologist You are a seasoned Cryptozoologist, a dedicated researcher and explorer of the hidden and elusive creatures that dwell in the untamed wilderness of the Old West. With a deep passion for the unknown, you have honed your skills in observation, tracking, and deciphering the 
- **Overview:** Feature heading: Cryptid Knowledge. Read the proficiency lines at the anchor. Language Sequian is on the page.

### Illuminated Scholar

- **ID:** `bg-s5-illuminated`
- **Type:** background
- **Parent:** `bg-s5-scholar`
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 243. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Variant: Illuminated Scholar Within the prestigious ranks of the Ivory Tower, some scholars have delved into the hidden world of secret societies and esoteric knowledge. These Illuminated Scholars have formed a connection to the enigmatic Illuminati, uncovering arcane secrets and gaining insights in
- **Overview:** Presented as a variant of Scholar of the Ivory Tower, not a second full background. Adds Arcana, alchemist's supplies or herbalism, one language. Feature: Illuminati Insight. Illuminati Magic says at 1st level you learn Detect Magic and can cast it as a ritual, plus advantage on saves against spells.
- **Conflicts:**
  - Illuminati Magic is worded 'At 1st level' inside a background variant.
- **Note:** Scholar of the Ivory Tower is one background. Illuminated Scholar is its printed variant.

### Pioneer

- **ID:** `bg-s5-pioneer`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 331. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Background: Pioneer Point Defiance, a remote outpost on the edge of the untamed frontier, stands as a bastion of civilization amidst the wilderness. As a Pioneer, you have embraced the spirit of exploration and resilience, venturing into the untamed landscapes that stretch beyond the settlement. Cla
- **Overview:** The heading 'Background: Pioneer' occurs twice in a row. Skills under the second heading: Survival, History. Navigator's tools. Feature: Trailblazer. Treat as one background with a duplicated heading, not two backgrounds.
- **Conflicts:**
  - Heading 'Background: Pioneer' is printed twice.

### Guardian of Mount Rainier

- **ID:** `bg-s5-rainier`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 271. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Background: Guardian of Mount Rainier For generations, your family has been entrusted with the sacred duty of safeguarding the majestic Mount Rainier and its surrounding lands. As a Guardian of Mount Rainier, you have dedicated your life to studying the mountain's diverse flora and fauna, as well as
- **Overview:** Feature: Protector's Vigil. Herbalism kit is in the proficiency block. Read the anchor for the rest.

### Raven Herald

- **ID:** `bg-s5-raven`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 151. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Background: Raven Herald As a Raven Herald, you are part of an ancient and secretive order known as the Golden Ravens, chosen by the mysterious forces that govern the threads of fate. Steeped in the lore of Odin's Ravens, you have inherited a connection to these enigmatic avian messengers, granting 
- **Overview:** Feature: Raven's Insight. Advantage on Perception or History checks related to secrets, ancient texts, or symbols tied to Odin's Ravens, as the feature states.

### Baron Rockefeller's Enforcers

- **ID:** `bg-s5-rockefeller`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 73. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Baron Rockefeller's Enforcers You come from a group known as Baron Rockefeller's Enforcers, a select few who have pledged their loyalty and service to the powerful and influential Baron John D. Rockefeller. As a member of this background, you have been entrusted with maintaining order, protecting th
- **Overview:** Intimidation, Persuasion. Artisan's tools and land vehicles. Language Transcontinental. Feature: Authority of Baron Rockefeller. Trading posts are inside that influence.

### Scholar of the Ivory Tower

- **ID:** `bg-s5-scholar`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 213. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Scholar of the Ivory Tower You have dedicated your life to the pursuit of knowledge and intellectual mastery within the hallowed halls of the Ivory Tower, a prestigious institution built by the visionary scholar known as Harvard. As a Scholar of the Ivory Tower, you have honed your mind and academic
- **Overview:** Arcana, History. Feature: Scholar's Expertise doubles proficiency on the chosen expertise check. The same block then gives Harvard's Guidance, worded 'At 1st level', one hour of study for advantage on one Intelligence check, once per long rest.
- **Conflicts:**
  - Harvard's Guidance is worded as a 1st-level feature inside a background.
- **Note:** Scholar of the Ivory Tower is one background. Illuminated Scholar is its printed variant.

### Shadow Sentinel

- **ID:** `bg-s5-shadow`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 99. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Background: Shadow Sentinel You are a member of the Shadows of the Sequoia, a secretive organization that operates within the ancient Redwood forests, protecting its secrets and defending the balance between the natural world and the forces of darkness. As a Shadow Sentinel, you have undergone rigor
- **Overview:** Stealth, Arcana. Herbalism kit and artisan's tools. Language Sequian. Feature: Guardian of the Redwoods.

### Empire City Slicker

- **ID:** `bg-s5-slicker`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 47. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Empire City Slicker You come from the sprawling metropolis known as Empire City, a bastion of advanced technology and potent magic. As an Empire City Slicker, you have ventured from the urban wonders of Empire City to the untamed frontiers of the Old West, bringing with you a unique set of skills an
- **Overview:** Arcana, Persuasion. One artisan's tools. The page spells a language line 'Costal Arcanian. Morse' code.' Feature: Urban Ingenuity.
- **Conflicts:**
  - The page spells 'Costal Arcanian'.

### Steamboat Captain

- **ID:** `bg-s5-steamboat`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 303. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Background: Steamboat Captain Born and raised in the bustling city of Emerald, you developed a deep fascination for the steamboats that traversed the picturesque waters of Puget Sound. From an early age, you honed your skills in navigation, ship handling, and understanding the ever-changing currents
- **Overview:** Athletics, Perception. Navigator's tools. Feature name is split across a line break as 'Feature' then 'Nautical Expertise'. Advantage to navigate and pilot steamboats or other water vessels, plus discounted or free passage.

### Baron Vanderbilt's Guardians

- **ID:** `bg-s5-vanderbilt`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 19. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Baron Vanderbilt's Guardians You hail from a group known as Baron Vanderbilt's Guardians, a select few who have sworn their allegiance and service to the influential Baron Cornelius Vanderbilt. As a member of this background, you are entrusted with protecting the Baron's interests, maintaining order
- **Overview:** Athletics, Insight. Gaming set and water vehicles. Language Transcontinental. Feature: Authority of Baron Vanderbilt. Cooperation and basic supplies inside the Baron's influence, including gambling halls.

### Verdantreach Explorer

- **ID:** `bg-s5-verdant`
- **Type:** background
- **Setting:** Arcania / Roanoke Season 5 published backgrounds site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_BACKGROUND
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000088
- **Source:** `sources/roanoke-s5-legends/google-sites/s5backgrounds/pages/home.md` line 187. https://sites.google.com/view/s5backgrounds/home
- **Anchor:** Verdantreach Explorer You come from the picturesque state of Verdantreach, nestled in the heart of the North East region of Arcania. This land of sprawling forests, scenic mountains, and vibrant cities has shaped your upbringing and instilled in you a sense of exploration and resilience. As a Verdan
- **Overview:** Region block under Columbia. Survival, Nature. Navigator's tools and artisan's tools. Feature: Wilderness Lore. Guidance in Arcania wilderness. Not a separate background from the duplicate Pioneer problem.

### Pigeon Lord

- **ID:** `ec-class-pigeon-lord`
- **Type:** class
- **Also printed as:** Pigeon lord
- **Setting:** Empire City / Roanoke Season 4 lineage. Draft BCS-000148 and v2 BCS-000175.
- **Design relation:** BESPOKE
- **Completeness:** DRAFT_V2_CLASS
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000175, BCS-000148
- **Source:** `sources/empire-city/BCS-000175/source.md` line 112. (no URL; Drive or repo text)
- **Anchor:** Coo Tounge Through years of isolation and living with your pigeons you have learned their hidden language. An outlandish unimaginable combination of coo’s and chirps that allow you to ask them for the spells and abilities they grant you. Only other pigeon lords or pigeons can understand you while in conversation.
- **Overview:** Full class in Pigeon Lord v2. Hit die 1d6. Spellcasting uses a resource the table headers call Bread. 1st level: Spellcasting and Coo Tongue (the feature heading is spelled 'Coo Tounge'). 7th: Fresh Batch, regenerate up to half the bread pool on a short rest. 11th: Tethered flight and Flock of burden. Ability Score Increase at 4th, 8th, 12th, 16th, and 19th. Two subclasses: The Flock of Names and The Flock of the Lame. BCS-000148 is an earlier draft and is not the same text.
- **Mechanics:**
  - level 1: Hit die and Coo Tongue. 1d6 per pigeon lord level. Coo Tongue is a language of coos and chirps used to ask pigeons for spells. The heading spells it 'Coo Tounge'.
  - level 7: Fresh Batch. At level 7, regenerate up to half of the bread pool with a short rest.
  - level 11: Tethered flight. Summon pigeons to move you or a creature you can see. Unwilling targets make a Constitution save against your spell save DC. Flying speed 10 feet. Uses per day equal to Constitution modifier, minimum 1.
  - level 11: Flock of burden. 10 minutes to summon a rolling flock that holds up to 500 pounds for 1 hour. More weight kills the pigeons. Uses per day equal to Constitution modifier, minimum 1.
- **Conflicts:**
  - Feature heading spells 'Coo Tounge'. The level table spells 'Coo Tongue'.
  - v2 is not the Season 5 Google Sites layer. Do not treat it as published player-facing Season 5 text.
- **Lineage:**
  - BCS-000148: earlier draft titled Pigeon Lord- draft
- **Discord phrase hits (not play):** empire-city: Pigeon Lord 16; empire-city-dev: Pigeon Lord 10
- **Sample message ids:** 851700412629516348 (empire-city, market, 2021-06-08), 863676363038261259 (empire-city, the-bon, 2021-07-11), 747509845045018625 (empire-city-dev, pigeon-lord, 2020-08-24), 748385678886436947 (empire-city-dev, dm-chat, 2020-08-27)
- **Note:** Discord has a pigeon-lord channel in Empire City Dev and name hits in Empire City. That is not recorded as observed play of these rules.

### The Flock of Names

- **ID:** `ec-sub-flock-of-names`
- **Type:** subclass
- **Parent:** `ec-class-pigeon-lord`
- **Setting:** Empire City, Pigeon Lord v2
- **Design relation:** BESPOKE
- **Completeness:** DRAFT_V2_SUBCLASS
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000175, BCS-000148
- **Source:** `sources/empire-city/BCS-000175/source.md` line 136. (no URL; Drive or repo text)
- **Anchor:** Sub Classes: The Flock of Names Me and a Pigeon named Steve.
- **Overview:** 3rd: Me and a Pigeon named Steve. 6th: Me and a Pigeon named Marv, costing 2 bread. 10th: Me and Bad Bertha, costing 3 bread. 14th: Gunther's Wall of pigeons, a nonmagical wall of pigeons, 5 feet thick, 10 feet high, up to 80 feet long.
- **Conflicts:**
  - Draft BCS-000148 also uses The Flock of Names. Compare the two texts before treating a draft sentence as v2.
- **Lineage:**
  - BCS-000148: draft also contains The Flock of Names, including Steve, Marv, and Bad Bertha

### The Flock of the Lame

- **ID:** `ec-sub-flock-of-the-lame`
- **Type:** subclass
- **Parent:** `ec-class-pigeon-lord`
- **Setting:** Empire City, Pigeon Lord v2
- **Design relation:** BESPOKE
- **Completeness:** DRAFT_V2_SUBCLASS
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000175
- **Source:** `sources/empire-city/BCS-000175/source.md` line 172. (no URL; Drive or repo text)
- **Anchor:** Sub Class: The Flock of the Lame: By 3rd level, the hivemind of cranium pigeons has taken pity on you. Knowing that you cannot do everything for yourself, not only will they help you cast, but they will help you fight too. Beginning at level 3, by expending one use of your bread, a flock of pigeons (one for each level 
- **Overview:** Second subclass in v2. 3rd: expend 1 bread; a flock carries a shield for +2 AC for 1 minute. 6th: a flock carries and attacks with a one-handed weapon. 10th: a mutant pigeon carries a two-handed weapon. 14th: an extraordinarily beautiful pigeon that follows familiar rules and can attune one extra item. The draft BCS-000148 has a heading 'The Ridonculous Flock' which is not equated with this name.
- **Mechanics:**
  - level 3: Shield flock. Expend one bread. One pigeon per pigeon-lord level, 4 HP, AC 14, carries a shield for +2 AC for one minute.
  - level 6: One-handed weapon flock. Expend one bread. The flock attacks with a one-handed weapon inside a 15-foot cube. The text calls this an extra attack.
  - level 10: Mutant pigeon. A massive mutant pigeon, HP 30, AC 14, carries a two-handed weapon.
  - level 14: Attuning pigeon. An extraordinarily beautiful pigeon, HP 20, AC 16, familiar rules, can attune one extra item.
- **Conflicts:**
  - Draft name 'The Ridonculous Flock' (BCS-000148) versus v2 name 'The Flock of the Lame' (BCS-000175). Not silently merged.
- **Lineage:**
  - BCS-000148: draft heading 'The Ridonculous Flock' may be an earlier path. Not equated here.

### Bowling event class adaptations

- **ID:** `event-bowling`
- **Type:** event_adaptation
- **Setting:** Bowling event. One-session rules layered on published subclass names.
- **Design relation:** EVENT_ADAPTATION_OF_PUBLISHED_CHASSIS
- **Completeness:** EVENT_RULES
- **Draft / published / offered / play-observed:** True / False / True / NOT_ESTABLISHED
- **Corpus:** BCS-000182
- **Source:** `sources/bowling-event/BCS-000182/source.md` line 92. (no URL; Drive or repo text)
- **Anchor:** Class Features may be used only once per encounter. Dwarf Battlerager Barbarian
- **Overview:** Six pregenerated characters use published subclass names and bowling-specific features. Class features may be used only once per encounter. This is not an Arcanian class and not evidence those published subclasses were redesigned. Names and event features: Dwarf Battlerager (Rage; Gutter ball rage), Aasimar Life cleric (Aura of Healing; Aura of Restoration), Half-elf Arcane Trickster (Magical Ambush; Scavenge), Human Oath of Redemption (Aura of the Guardian; Never Fear, I am here), Genasi giant-soul sorcerer (Arcane Edge; Enlarge), Tiefling Great Old One warlock (Mage hand; Fireball). The warlock heading also says Pact of the Blade.
- **Mechanics:**
  - Limit. Class features may be used only once per encounter.
- **Note:** Offered for that event's players in the document. Not Season 5 publication.

### Bullygrung

- **ID:** `gap-bullygrung`
- **Type:** race
- **Also printed as:** Grung
- **Setting:** Named on Season 5 char-gen as an approved homebrew map from Grung. No trait block was found on the homebrew-races page.
- **Design relation:** UNRESOLVED
- **Completeness:** NAME_ONLY
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000109
- **Source:** `sources/roanoke-s5-legends/google-sites/char-gen/pages/home.md` line 199. https://sites.google.com/view/char-gen/home
- **Anchor:** -Bullygrung Locathah Mississippi Mudskipper
- **Overview:** Char-gen line pairs Grung with Bullygrung under Approved Homebrew. The homebrew-races capture does not contain the string Bullygrung. No original trait block was found in the searched containers. Do not invent traits. Do not assume it is only a rename of Grung; the page does not say the mechanics are unchanged.
- **Conflicts:**
  - Named as approved homebrew, but no accompanying trait page is in the captured Season 5 race site.

### Clerrook

- **ID:** `gap-clerrook`
- **Type:** subclass
- **Setting:** Named only in a research lead. Not a BCS container on this main.
- **Design relation:** UNRESOLVED
- **Completeness:** ABSENT_FROM_CORPUS
- **Draft / published / offered / play-observed:** False / False / False / NOT_ESTABLISHED
- **Corpus:** none on main
- **Source:** `research/source-leads/homebrew-mechanics-worldbuilding.md` line 51. (no URL; Drive or repo text)
- **Anchor:** ### Clerrook Subclass - Drive ID: `1A0TDh8s4QRhji1b6kFlUOm8b-L47rQ88memK6S5vN8E`
- **Overview:** The source-lead file names a Drive document and describes a cooking-themed cleric treatment. That Drive file is not a BCS source container on current main. Document full-text search for clerrook returned zero containers. Discord phrase search for Clerrook returned zero messages in all three hydrated harvests. No rules are copied here because the canonical body is not in the repository.
- **Note:** Archive gap. The research lead is not source truth. Do not reconstruct the subclass from the lead's paraphrase.

### Asari (Mass Effect)

- **ID:** `isekai-01-asari-mass-effect`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 16. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Aasimar
- **Overview:** Cosmetic reskin. Mapped race: Aasimar. Mapped subrace: Protector. Reskin line: Divine features present as biotic energy and neural projection. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Aasimar / Protector
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Yautja (Predator)

- **ID:** `isekai-02-yautja-predator`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 47. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Half-Orc
- **Overview:** Cosmetic reskin. Mapped race: Half-Orc. Mapped subrace: None. Reskin line: All features represent advanced hunting physiology and wargear. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Half-Orc / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Time Bandits

- **ID:** `isekai-03-time-bandits`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 75. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Halfling
- **Overview:** Cosmetic reskin. Mapped race: Halfling. Mapped subrace: Lightfoot. Reskin line: Luck and stealth represent temporal misalignment and opportunistic movement. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Halfling / Lightfoot
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Themyscirian (Wonderwomen)

- **ID:** `isekai-04-themyscirian-wonderwomen`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 106. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Human
- **Overview:** Cosmetic reskin. Mapped race: Human. Mapped subrace: Variant. Reskin line: Feats and adaptability represent divine blessing and warrior training. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Human / Variant
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Na'vi (Pandorian)

- **ID:** `isekai-05-na-vi-pandorian`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 134. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Elf
- **Overview:** Cosmetic reskin. Mapped race: Elf. Mapped subrace: Wood Elf. Reskin line: Elven traits represent deep ecological and neural connection to Pandora. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Elf / Wood Elf
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Gelfling

- **ID:** `isekai-06-gelfling`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 171. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Gnome
- **Overview:** Cosmetic reskin. Mapped race: Gnome. Mapped subrace: Forest Gnome. Reskin line: Gnomish traits represent dream-sharing and natural attunement. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Gnome / Forest Gnome
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Marooned Grays

- **ID:** `isekai-07-marooned-grays`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 202. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Githyanki
- **Overview:** Cosmetic reskin. Mapped race: Githyanki. Mapped subrace: None. Reskin line: Psionic traits represent invasive telepathic experimentation. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Githyanki / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Space Marines

- **ID:** `isekai-08-space-marines`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 230. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Goliath
- **Overview:** Cosmetic reskin. Mapped race: Goliath. Mapped subrace: None. Reskin line: Physical traits represent gene-forged physiology and power armor resilience. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Goliath / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Care Bears

- **ID:** `isekai-09-care-bears`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 258. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Halfling
- **Overview:** Cosmetic reskin. Mapped race: Halfling. Mapped subrace: Stout. Reskin line: Resilience and luck represent emotional strength and positivity. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Halfling / Stout
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Paleborn

- **ID:** `isekai-10-paleborn`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 289. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Reborn
- **Overview:** Cosmetic reskin. Mapped race: Reborn. Mapped subrace: None. Reskin line: Undead traits represent detachment from memory and reality. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Reborn / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Gargoyles

- **ID:** `isekai-11-gargoyles`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 314. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Aarakocra
- **Overview:** Cosmetic reskin. Mapped race: Aarakocra. Mapped subrace: None. Reskin line: Flight and form represent winged stone guardians. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Aarakocra / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Symbiote

- **ID:** `isekai-12-symbiote`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 339. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Dhampir
- **Overview:** Cosmetic reskin. Mapped race: Dhampir. Mapped subrace: None. Reskin line: Vampiric traits represent parasitic bonding and predation. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Dhampir / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Thundarian (Thundercats)

- **ID:** `isekai-13-thundarian-thundercats`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 367. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Tabaxi
- **Overview:** Cosmetic reskin. Mapped race: Tabaxi. Mapped subrace: None. Reskin line: Feline agility and traits represent warrior heritage and survival instinct. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Tabaxi / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Programs

- **ID:** `isekai-14-programs`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 395. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Warforged
- **Overview:** Cosmetic reskin. Mapped race: Warforged. Mapped subrace: None. Reskin line: Construct traits represent digital existence and light-based form. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Warforged / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### The Silence (Doctor Who)

- **ID:** `isekai-15-the-silence-doctor-who`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 423. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Bugbear
- **Overview:** Cosmetic reskin. Mapped race: Bugbear. Mapped subrace: None. Reskin line: Stealth and ambush traits present as gaps in attention and untracked movement rather than physical hiding. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Bugbear / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### My Little Pony

- **ID:** `isekai-16-my-little-pony`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 457. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Centaur
- **Overview:** Cosmetic reskin. Mapped race: Centaur. Mapped subrace: None. Reskin line: All features present as compact, expressive equine physiology with identity marks. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Centaur / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Furby

- **ID:** `isekai-17-furby`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 485. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Changeling
- **Overview:** Cosmetic reskin. Mapped race: Changeling. Mapped subrace: None. Reskin line: Shapeshifting manifests as adaptive mimicry—voice, expression, and form adjust based on observed behavior rather than fixed identity. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Changeling / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Gary Clones

- **ID:** `isekai-18-gary-clones`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 513. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Kenku
- **Overview:** Cosmetic reskin. Mapped race: Kenku. Mapped subrace: None. Reskin line: Mimicry is involuntary echoing—speech and behavior are reproduced from memory fragments and recent input rather than original expression. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Kenku / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Wookiees

- **ID:** `isekai-19-wookiees`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 530. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Firbolg
- **Overview:** Cosmetic reskin. Mapped race: Firbolg. Mapped subrace: None. Reskin line: Natural magic and speech are expressed through physical presence, vocal tone, and an instinctive connection to forest environments rather than overt spellcasting or hidden illusion. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Firbolg / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Mutants (TMNT)

- **ID:** `isekai-20-mutants-tmnt`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 550. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Giff
- **Overview:** Cosmetic reskin. Mapped race: Giff. Mapped subrace: None. Reskin line: All traits represent exaggerated mutant physiology—durability, brute force, and instinct-driven combat capability. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Giff / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Brownies (Willow)

- **ID:** `isekai-21-brownies-willow`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 576. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Fairy
- **Overview:** Cosmetic reskin. Mapped race: Fairy. Mapped subrace: None. Reskin line: All features present as erratic movement, exaggerated personality, and small-scale forest survival rather than graceful or magical demeanor. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Fairy / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Adam Addict (Rapture)

- **ID:** `isekai-22-adam-addict-rapture`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK_INCOMPLETE
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 598. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Simic Hybrid
- **Overview:** Cosmetic reskin. Mapped race: Simic Hybrid. Mapped subrace: None. Reskin line: no reskin sentence in the captured block. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Simic Hybrid / None
- **Conflicts:**
  - No reskin sentence was captured between this Mapped Race line and the next block.
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Mogwai (Gremlins)

- **ID:** `isekai-23-mogwai-gremlins`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 608. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Goblin
- **Overview:** Cosmetic reskin. Mapped race: Goblin. Mapped subrace: None. Reskin line: All features present as reactive learning, environmental adaptation, and impulsive behavior rather than malice or cruelty. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Goblin / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Moogles (FF6)

- **ID:** `isekai-24-moogles-ff6`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 630. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Geppetin
- **Overview:** Cosmetic reskin. Mapped race: Geppetin. Mapped subrace: None. Reskin line: All features present as coordinated group behavior, tool use, and shared effort rather than constructed or artificial origin. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Geppetin / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### Gummi Bears

- **ID:** `isekai-25-gummi-bears`
- **Type:** race_reskin
- **Setting:** 2026 file 'Races for the isakei' (the filename's spelling). Later-play container.
- **Design relation:** RESKIN
- **Completeness:** RESKIN_BLOCK
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000189
- **Source:** `sources/later-play/BCS-000189/source.md` line 652. (no URL; Drive or repo text)
- **Anchor:** Mapped Race: Geleton
- **Overview:** Cosmetic reskin. Mapped race: Geleton. Mapped subrace: None. Reskin line: All features present as elastic movement, resilience, and internal structure rather than skeletal or exposed anatomy. The file marks trait mechanics 'Unchanged' in the blocks where that word appears. Renamed feature labels are in the source. This inventory does not copy those bullets and does not invent new mechanics.
- **Mechanics:**
  - Mapped chassis. Geleton / None
- **Note:** Mapped-race strings are copied as printed, including Geppetin and Geleton. They are not corrected to a published species name. These are not the Arcanian bespoke races.

### External content allow-lists

- **ID:** `later-allow-lists`
- **Type:** character_creation_system
- **Setting:** Later-play rulings about published species, classes, feats, spells, and backgrounds from outside this corpus.
- **Design relation:** EXTERNAL_ALLOWLIST
- **Completeness:** POLICY_LIST
- **Draft / published / offered / play-observed:** False / False / True / NOT_ESTABLISHED
- **Corpus:** BCS-000192, BCS-000193, BCS-000194
- **Source:** `sources/later-play/BCS-000192/source.md` line 8. (no URL; Drive or repo text)
- **Anchor:** # Species Species Allowed Location Source Notes
- **Overview:** BCS-000192 is headed Species, Classes Subclasses, Feats, Spells - By Source, and Backgrounds - By Source. BCS-000193 is dated Dec 28 2025 and BCS-000194 is dated May 19 2026. They are allow-lists of external published options. They are not this corpus's homebrew designs. Individual external species, classes, and feats are not given option records here.
- **Note:** Offered means the documents are rulings about what may be used. It does not mean each listed item was played.

### Season 5 character creation

- **ID:** `s5-char-gen`
- **Type:** character_creation_system
- **Setting:** Arcania / Roanoke Season 5 (Legends), published Google Site
- **Design relation:** BESPOKE_FRAMEWORK
- **Completeness:** PUBLISHED_PROCEDURE
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000109, BCS-000145, BCS-000105
- **Source:** `sources/roanoke-s5-legends/google-sites/char-gen/pages/home.md` line 15. https://sites.google.com/view/char-gen/home
- **Anchor:** Character Creation As you make your character, keep in mind that revivify is banned this year (with the exception of Savage Fertility clerics).
- **Overview:** Published player-facing creation rules. Revivify is banned except for Savage Fertility clerics. Stats are rolled only on the official server. Three difficulties (Tenderfoot, Aces, Desperado) change XP, stat method, and death saves. After difficulty: background, then a required Life Path (Miner, Rancher, or Gambler), then race from an approval list, then class. No multiclass. Start at level 6. Track encumbrance (not coin weight), ammunition, and XP rather than milestone.
- **Mechanics:**
  - Tenderfoot. Normal XP. Point buy, or rolled with an optional mulligan for stats under ten. Normal death saves.
  - Aces. 1.3x XP. Rolled stats. No mulligan unless a stat is under 7. Stats may be placed in any order. Death save DC increases by 2 for each fail (10, 12, 14).
  - Desperado. 1.5 XP bonus. Rolled stats placed in the order rolled. No reroll. You may only save from death once. The next time you are downed, you are dead. If rezed, the death save is not replenished.
  - level 6: Start. Starting level is 6. Multiclassing is not allowed.
  - Banned options. Eloquence Bard, Moon druid, and Echo knight are not allowed. Revivify is banned except for Savage Fertility clerics.
- **Conflicts:**
  - Approved Homebrew maps several peoples onto published species (Harengon-Jackalope, Aasimar-Seraph, Tiefling-Seraph, and others) while BCS-000107 also prints bespoke trait blocks. Those are recorded as separate design relations, not collapsed.
  - Char-gen spells the minotaur map 'Tatakan'. The race page heading is 'Tatankan'.
  - Char-gen spells the cleric domain 'Mischiveous Whims'. The cleric site heading is 'Mischievous Whims'.
  - Char-gen spells the centaur map 'Palamino'. The race page heading is 'Palomino Centaur'.
  - Char-gen lists 'Gnorgian Peachpunk' and 'Bullygrung'. The race page heading is 'Peach Punk Gnomes' and does not contain the string Bullygrung.
- **Lineage:**
  - BCS-000145: Drive document 'Season 5 character creation'. States XP advancement, a 30-person cap, race restrictions, a difficulty modifier, and a morality system. It is a related Drive text, not a duplicate of the Site page.
  - BCS-000105: tales-in-legend landing. Published dates and signup cap. Publication is not live play.
- **Note:** Official WotC species on the approved and unapproved lists are character-creation policy, not homebrew designs, and are not enumerated as homebrew options. BCS-000192, BCS-000193, and BCS-000194 are later external-content allow-lists and are recorded separately.

### Harbinger

- **ID:** `s5-class-harbinger`
- **Type:** class
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_CLASS_CHASSIS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000094
- **Source:** `sources/roanoke-s5-legends/google-sites/harbingers5/pages/home.md` line 93. https://sites.google.com/view/harbingers5/home
- **Anchor:** Hit Dice: 1d10 per Harbinger Level
- **Overview:** Full class, not one of the eleven traditional-class subclasses. Hit die 1d10. Hit points at 1st level are 10 + Constitution modifier. The page has a Constitution-Based Spellcasting heading, a ritual-casting heading, and a touch-range limitation discussed in the subclass text. Class features named on the page include Wrist Pocket at 4th level and Vitality at 6th level. Three subclasses follow on the same page.
- **Mechanics:**
  - level 1: Hit die. 1d10 per Harbinger level. Hit points at 1st level: 10 + Constitution modifier.
  - level 4: Harbinger's Wrist Pocket. At 4th level, a permanent extra-dimensional space called the Wrist Pocket.
  - level 6: Harbinger's Vitality. At 6th level, the page says the Harbinger brings forth positive energy in equal amounts to the damage they deal.
- **Discord phrase hits (not play):** empire-city: Harbinger 1
- **Sample message ids:** 866837297255940126 (empire-city, out-of-character, 2021-07-20)
- **Note:** Spell slot table lines are present on the page (Level 1 through Level 9 headings). Read those lines in the source for the numbers. This inventory does not retype the whole table. Discord counts for a common word are phrase hits, not a census of characters.

### Season 5 downtime training

- **ID:** `s5-downtime-training`
- **Type:** character_creation_system
- **Setting:** Arcania / Roanoke Season 5 published training page
- **Design relation:** BESPOKE_FRAMEWORK
- **Completeness:** PUBLISHED_PROCEDURE
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000097
- **Source:** `sources/roanoke-s5-legends/google-sites/s5-training/pages/home.md` line 17. https://sites.google.com/view/s5-training/home
- **Anchor:** Learning skills, tools, instruments, vehicles or languages. (Key terms in bold so you can skim when checking the doc later.)
- **Overview:** Published downtime procedure for learning skills, tools, instruments, vehicles, languages, weapon proficiencies, and armor proficiencies. It is an advancement rule, not a class or feat.
- **Mechanics:**
  - Daily practice. 4 hours of downtime per day, maximum 4 attempts per day. A skill takes 20 passed checks at DC 12. Those checks are a flat 20 and do not gain bonuses, buffs, spells, or help.
  - Weapon or armor proficiency. Also requires 20 checks, plus 10 successful combat attacks with the weapon, or 10 failed melee attacks against your armor while wearing it. No help, inspiration, or feature may be used on those checks.
  - Trainers. PC trainers cannot learn from other players. Training guarantees 1 pass per day and costs 50 dollars per day. An NPC trainer costs 100 dollars per check to give advantage, and exists only in one of three towns.
  - Expertise. Non-skill tool, instrument, and vehicle expertise costs an additional 40 checks (60 total). Weapons, armor, languages, and skills cannot gain expertise this way.

### Enforcer improvised-weapon tables

- **ID:** `s5-enforcer-improvised-table`
- **Type:** class_feature_table
- **Parent:** `s5-sub-enforcer`
- **Setting:** Arcania / Roanoke Season 5
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_TABLE
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000102, BCS-000101
- **Source:** `sources/roanoke-s5-legends/google-sites/improvised-weapon-for-enforcer/pages/home.md` line 1. https://sites.google.com/view/improvised-weapon-for-enforcer/home
- **Anchor:** # Improvised weapon for enforcers s5 - Source URL: https://sites.google.com/view/improvised-weapon-for-enforcer/home
- **Overview:** Separate published page of randomized improvised weapons for the Enforcer. Char-gen points at it. It is not an independent subclass. The table is long; this inventory does not copy it.

### Gambler

- **ID:** `s5-life-gambler`
- **Type:** life_path
- **Setting:** Arcania / Roanoke Season 5
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_LIFE_PATH
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000096, BCS-000109
- **Source:** `sources/roanoke-s5-legends/google-sites/lifepathgambler/pages/home.md` line 1. https://sites.google.com/view/lifepathgambler/home
- **Anchor:** # Life Path, Gambler - Source URL: https://sites.google.com/view/lifepathgambler/home
- **Overview:** Published economic life path. Starting gear on the page: gaudy gambler clothes, 1 Tier One Marker, 1 mutt, 1 pony, 2 pistols, 750 dollars, and a deck of beveled cards or another cheating instrument (the page spells "insturment"). Marker Chips are social currency. Only a gambler may leave a gambling hall with poker chips to use as Marker Chips. Once spent, the magic is depleted. Shops do not accept them. Higher-tier markers' benefits do not stack; the page says the negative tradeoff effects do.
- **Mechanics:**
  - Starting kit. Gaudy clothes, 1 Tier One Marker, 1 mutt, 1 pony, 2 pistols, 750 dollars, beveled cards or another cheating instrument.
  - Marker Chips. Only a gambler leaves a hall with poker chips as Marker Chips. Spent markers become worthless. Shops do not accept them.
- **Discord phrase hits (not play):** roanoke-season-3: Gambler 4; empire-city-dev: Gambler 2
- **Sample message ids:** 738630868528136222 (roanoke-season-3, 🥐-the-mess-hall, 2020-07-31), 739516791147069512 (roanoke-season-3, 🙋-out-of-character, 2020-08-02), 746932926494671041 (empire-city-dev, item-reccomendations, 2020-08-23), 753732646172885043 (empire-city-dev, dm-chat, 2020-09-10)
- **Note:**  Discord counts for a common word are phrase hits, not a census of characters.

### Miner

- **ID:** `s5-life-miner`
- **Type:** life_path
- **Setting:** Arcania / Roanoke Season 5. Required economic choice at character creation. Not a background.
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_LIFE_PATH
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000089, BCS-000109
- **Source:** `sources/roanoke-s5-legends/google-sites/s5mining/pages/home.md` line 15. https://sites.google.com/view/s5mining/home
- **Anchor:** Life Path: Miner Life Path is in addition to your background. It does not replace your background. This choice has major economic impacts for your character. There is no starting cash or equipment outside of this choice.
- **Overview:** The page says a life path is in addition to background and does not replace it, and that there is no starting cash or equipment outside this choice. All miners gain Pick Mining: a Mining Tools check, DC set by the DM from rock type (a table begins with Soft Clay DC 10). Success earns 2d6 gold pieces or 2d8 silver pieces. Critical success adds 3d6 gold nuggets. After a full day, Constitution save DC 12, +2 per further day, or gain exhaustion.
- **Mechanics:**
  - Pick Mining. Mining Tools check. Success: 2d6 gp or 2d8 sp. Critical: additional 3d6 gold nuggets. Fatigue Constitution save, DC starts at 12 and increases by 2 for each day you pick mine.
- **Discord phrase hits (not play):** roanoke-season-3: Miner 1; empire-city: Miner 1
- **Sample message ids:** 745467633880793238 (roanoke-season-3, olala, 2020-08-19), 863301699577446430 (empire-city, the-village⁉, 2021-07-10)
- **Note:** Discord hits for the bare word Miner are not evidence this life path was played. The word is ordinary English. Discord counts for a common word are phrase hits, not a census of characters.

### Rancher

- **ID:** `s5-life-rancher`
- **Type:** life_path
- **Setting:** Arcania / Roanoke Season 5
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_LIFE_PATH
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000090, BCS-000109
- **Source:** `sources/roanoke-s5-legends/google-sites/lifepathrancher/pages/home.md` line 1. https://sites.google.com/view/lifepathrancher/home
- **Anchor:** # Life Path, Rancher - Source URL: https://sites.google.com/view/lifepathrancher/home
- **Overview:** Published economic life path, in addition to background. The page says you start with no money and can begin with a base number of cattle, and it uses the words "let's say 10". It values those cattle at 250 gold dollars per head and says that value is unique to you. Twice per day, a ritual opens an extradimensional barn that holds proficiency bonus times 5 cattle. Cattle are not fed inside it and must be released at least 8 hours a day. Weekly d20 market roll and a separate d20 herd-event roll are on the page. Later catalog items, including spectral cattle, are on the same page and are not copied here.
- **Mechanics:**
  - Starting herd. The page's own wording is "let's say 10" cattle, valued at 250 gold dollars per head, value unique to the rancher.
  - Extradimensional barn. Twice per day ritual. Capacity is proficiency bonus times 5. Cattle must be released at least 8 hours a day.
- **Conflicts:**
  - The page hedges the starting herd with "let's say 10" rather than stating a fixed rule without that phrase.
- **Discord phrase hits (not play):** empire-city-dev: Rancher 1
- **Sample message ids:** 755730132399816724 (empire-city-dev, avrae-playground, 2020-09-16)
- **Note:** Confirm starting cattle count and the barn rule on the page before using a number from a summary. The page is the authority. Discord counts for a common word are phrase hits, not a census of characters.

### Bigfoot

- **ID:** `s5-race-bigfoot`
- **Type:** race
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 705. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Bigfoot The Bigfoot race is known for their incredible strength and ability to blend into natural surroundings. They are a reclusive and peaceful race, often avoiding contact with other races and living deep in the wilderness.
- **Overview:** Arcanian Cryptid. Walk 30. Headings: Natural Camouflage, Keen Senses, Powerful Build, Nature's Guardian, Resilient. Char-gen maps Orc to Bigfoot.
- **Discord phrase hits (not play):** roanoke-season-3: Bigfoot 24; empire-city: Bigfoot 2
- **Sample message ids:** 734198971764965497 (roanoke-season-3, 🕍-the-roseline-temple-of-masons, 2020-07-19), 741932924928262187 (roanoke-season-3, town-square, 2020-08-09), 864920207075967006 (empire-city, out-of-character, 2021-07-14), 864921825032273940 (empire-city, out-of-character, 2021-07-14)
- **Note:**  Discord counts for a common word are phrase hits, not a census of characters.

### Brunelock

- **ID:** `s5-race-brunelock`
- **Type:** race
- **Also printed as:** Brunelocks
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 753. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Brunelocks Ability Score Increase: Your Strength score increases by 2, and your Wisdom score increases by 1.
- **Overview:** The first trait heading block (Ability Score Increase through Survival Instincts and Brown Bear Heritage) is the rules block. Later uses of the word Brunelocks on the same page are narrative sentences, not additional trait lines.
- **Conflicts:**
  - The page uses Brunelocks as a heading and later as a narrative name. Char-gen's approved-homebrew list in the captured page does not include this name.
- **Discord phrase hits (not play):** roanoke-season-3: Brunelock 7; empire-city: Brunelock 1; empire-city-dev: Brunelock 1
- **Sample message ids:** 734091204781932645 (roanoke-season-3, 🦸🏻-character-introduction, 2020-07-18), 734215481329713172 (roanoke-season-3, ⚒-free-masons, 2020-07-19), 876012057332428810 (empire-city, liberty-hall, 2021-08-14), 746973150260232312 (empire-city-dev, dm-style-discussions, 2020-08-23)

### Chinnokin

- **ID:** `s5-race-chinnokin`
- **Type:** race
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107, BCS-000139, BCS-000135, BCS-000143
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 157. https://sites.google.com/view/homebrew-races/home
- **Anchor:** CHINNOKIN RACE DETAILS SLEEK AND PLAYFUL: With their fishy features and scaly skin, these creatures are more at home in water than on land They are slightly shorter than humans on average, ranging from well under 5 feet tall to just over 6 feet. They seem to grow larger as they a
- **Overview:** Amphibious people. The published block includes ability scores, darkvision, Temperate Aquatic Habitat, Soak, languages, Water Shaper, the Dehydrate cantrip, Shape Water, and Wall of Water. Almanac BCS-000143 and verbatim BCS-000139 are earlier wordings and are not the same text.
- **Lineage:**
  - BCS-000139: earlier or related document; not a substitute for the published page
  - BCS-000135: earlier or related document; not a substitute for the published page
  - BCS-000143: earlier or related document; not a substitute for the published page
- **Discord phrase hits (not play):** roanoke-season-3: Chinnokin 141; empire-city: Chinnokin 35; empire-city-dev: Chinnokin 5
- **Sample message ids:** 734759648854278174 (roanoke-season-3, 🙋-out-of-character, 2020-07-20), 735225633784725674 (roanoke-season-3, 🕍-the-roseline-temple-of-masons, 2020-07-21), 863558738807226408 (empire-city, sandys-umbral-cup, 2021-07-10), 863565797666193448 (empire-city, sandys-umbral-cup, 2021-07-10)

### Halfwudgie

- **ID:** `s5-race-halfwudgie`
- **Type:** race
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107, BCS-000119, BCS-000135
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 853. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Halfwudgie Traits Ability Score Increase: Your Wisdom score increases by 2, and your Constitution score increases by 1.
- **Overview:** Trait headings: Ability Score Increase, Age, Alignment, Size, Speed, Cryptid Defense, Cryptid Resilience, Cryptid Ancestry, Quill Barrage, Primal Intuition. Earlier verbatim is BCS-000119. Race edits BCS-000135 discuss size, quills, and a level-4 Quill Barrage.
- **Lineage:**
  - BCS-000119: earlier or related document; not a substitute for the published page
  - BCS-000135: earlier or related document; not a substitute for the published page
- **Discord phrase hits (not play):** roanoke-season-3: Halfwudgie 73; empire-city: Halfwudgie 4; empire-city-dev: Halfwudgie 1
- **Sample message ids:** 739374670502952992 (roanoke-season-3, 🙋-out-of-character, 2020-08-02), 739550444594135102 (roanoke-season-3, hex-b-leviathans-call, 2020-08-02), 863538064982540318 (empire-city, combat-sign-up, 2021-07-10), 863952071333642251 (empire-city, winding-alleys-of-hampstead🔀💫, 2021-07-12)

### Jackalope

- **ID:** `s5-race-jackalope`
- **Type:** race
- **Also printed as:** Jackalope!
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107, BCS-000121, BCS-000135, BCS-000143
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 21. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Jackalope! Somewhat Unreliable: These diminutive and short lived cryptids thrive in the woods and typically have very large families. While many are lost to the brutal nature of Arcania, a successful family (especially those that excel in the use of magic, or the roguish arts) ca
- **Overview:** Small Arcanian Cryptid. Dexterity +2, Charisma +1. The page gives both a 30-foot walk with a 15-foot burrow and, under Prairie Dweller, a burrow equal to half movement, plus hearing advantage in two places.
- **Conflicts:**
  - Char-gen maps Harengon to Jackalope. The race page also prints original traits. Both are kept.
  - Burrow speed is stated as 15 feet under Speed and as half movement under Prairie Dweller.
  - Hearing advantage is stated under Size and again under Prairie Dweller.
  - Almanac BCS-000143 includes a Jackalope sentence beginning 'Beginning at level 5, when you damage a creature'. The Season 5 trait headings do not include that sentence. Do not add it to the published race without comparing the texts.
- **Lineage:**
  - BCS-000121: earlier or related document; not a substitute for the published page
  - BCS-000135: earlier or related document; not a substitute for the published page
  - BCS-000143: earlier or related document; not a substitute for the published page
  - BCS-000121: Jackalope verbatim handout. Compare trait sentences; do not assume identity with the Site.
- **Discord phrase hits (not play):** roanoke-season-3: Jackalope 146; empire-city: Jackalope 173; empire-city-dev: Jackalope 15
- **Sample message ids:** 734512569938870273 (roanoke-season-3, 🙋-out-of-character, 2020-07-19), 734759550653169745 (roanoke-season-3, 🙋-out-of-character, 2020-07-20), 850788738749038632 (empire-city, grand-central🛤, 2021-06-05), 851692513316175903 (empire-city, grand-central🛤, 2021-06-08)

### Peach Punk Gnomes

- **ID:** `s5-race-peach-punk`
- **Type:** race
- **Also printed as:** Gnorgian Peachpunk, Peachpunk
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 665. https://sites.google.com/view/homebrew-races/home
- **Anchor:** "What's truly remarkable is their community spirit. Those Peach Punk Gnomes are a tight-knit bunch, always huddled together in their underground taverns and tinkering guilds. They celebrate their craft, sharing ideas and stories, their laughter echoing amidst the clinking of glas
- **Overview:** Intelligence +2. Headings: Darkvision, Tinkerer's Expertise, Steampunk Resistance, Peach Cider Distillation, Gnomish Engineering. Char-gen maps Autognome to Gnorgian Peachpunk. The string Gnorgian is not on this race page.
- **Conflicts:**
  - Char-gen name 'Gnorgian Peachpunk' does not appear on the homebrew-races page, which says 'Peach Punk Gnomes'.

### Puffkin

- **ID:** `s5-race-puffkin`
- **Type:** race
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 585. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Puffkin : Ability Score Increase Your Constitution and Wisdom scores each increase by 1
- **Overview:** Parent block before the Sunrise and Sunset subraces. Languages, Rapport Spores, and Distress Spores are headings in that parent span. Char-gen maps Pixie to Puffkin.
- **Conflicts:**
  - Char-gen maps Pixie - Puffkin. The page prints spore traits rather than saying the mechanics are unchanged pixie traits.
- **Discord phrase hits (not play):** empire-city: Puffkin 26; empire-city-dev: Puffkin 16
- **Sample message ids:** 852419144267202580 (empire-city, broadway-🎭, 2021-06-10), 852772684881723422 (empire-city, gamebooth-arcadian-idol🎶🎤, 2021-06-11), 747365009516134460 (empire-city-dev, playable-races, 2020-08-24), 749393549426163724 (empire-city-dev, pufkin, 2020-08-29)

### Seraph

- **ID:** `s5-race-seraph`
- **Type:** race
- **Also printed as:** Seraphs
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 271. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Seraphs Seraphs, celestial beings of ethereal grace and wisdom, possess a form of communication that transcends mundane speech. Seraphs have developed a pattern of speech that reflects their profound nature. Instead of relying on vocal inflections or facial expressions, they empl
- **Overview:** Creature type on the page: Divine Outworlder. Medium. Angelic Grace says you cannot be grappled. Also Astral Manifestation, Inherent Radiance, and Astral Connection. Char-gen maps this name to both Aasimar and Tiefling.
- **Conflicts:**
  - Char-gen lists both 'Aasimar - Seraph' and 'Tiefling - Seraph'.

### Tatankan

- **ID:** `s5-race-tatankan`
- **Type:** race
- **Also printed as:** Tatakan
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107, BCS-000138, BCS-000135, BCS-000143
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 83. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Tatankan The Tatankan, a buffalo-headed minotaur-like race, hails from the vast plains of Minnesota, a land steeped in natural beauty and rich history. These noble beings embody the spirit of guardianship and unwavering loyalty, with a unique attribute that sets them apart from o
- **Overview:** Buffalo-headed people of the Minnesota plains in the page's fiction. Strength +2, Wisdom +1, size Medium despite a stated height of 7 to 8 feet. Walking speed 30, but cannot exceed the slowest creature within 5 feet. Horn attack after a 20-foot straight charge. Survival proficiency and advantage against disease and exhaustion. Subraces Plainsguard and Spiritspeaker.
- **Conflicts:**
  - Char-gen spells the approved-homebrew map 'Tatakan' and pairs it with Minotaur.
  - Size is called Medium while the same paragraph says they stand 7 to 8 feet tall.
  - Tatankan verbatim BCS-000138 uses Enhanced smell, Powerful Build, Gentle Reputation, and Gore. The Season 5 page uses Stalwart Protector, Charge of the Buffalo, and Nature's Resilience, plus Plainsguard and Spiritspeaker. These are different wordings, not one rules text.
- **Lineage:**
  - BCS-000138: earlier or related document; not a substitute for the published page
  - BCS-000135: earlier or related document; not a substitute for the published page
  - BCS-000143: earlier or related document; not a substitute for the published page
- **Discord phrase hits (not play):** roanoke-season-3: Tatankan 42, Tatakan 4; empire-city: Tatankan 58; empire-city-dev: Tatankan 3, Tatakan 1
- **Sample message ids:** 734512960558596207 (roanoke-season-3, 🙋-out-of-character, 2020-07-19), 740458871126098012 (roanoke-season-3, hex-b-leviathans-call, 2020-08-05), 742848738267234455 (roanoke-season-3, hex-d-the-pen, 2020-08-11), 743712294885654558 (roanoke-season-3, hex-d-the-pen, 2020-08-14)

### Oath of the Codebound

- **ID:** `s5-sub-codebound`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000111, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/s5-codebound/pages/home.md` line 15. https://sites.google.com/view/s5-codebound/home
- **Anchor:** The Oath of the Codebound "In the vast expanse of the untamed frontier, where lawlessness looms and chaos threatens to consume, the Oath of the Codebound paladins emerge as beacons of honor and integrity. They epitomize the spirit of the cowboy code, their unwavering resolve mirrored in the vast, open skies and rugged 
- **Overview:** Paladin oath. Char-gen calls it an oath to keep the cowboy code. The page states features at 7th, 15th, and 20th. Read the page from the oath heading for any 3rd-level tenets; do not fill a missing level from another paladin oath.
- **Mechanics:**
  - 3rd level:. 3rd level: Sanctuary, Shield of Faith
  - 5th level:. 5th level: Calm Emotions, Zone of Truth
  - 9th level:. 9th level: Aura of Vitality, Aura of Purity
  - 13th level:. 13th level: Banishment, Compulsion
  - 17th level:. 17th level: Circle of Power, Geas
  - Channel Divinity:. Channel Divinity: Codebound's Vow
  - Additionally:. Additionally: your unwavering adherence to the principles of the cowboy code grants you the ability to swiftly respond to threats and protect those under your watch. When a friendly creature within 10 feet of you is hit by an attack, you ca
- **Lineage:**
  - BCS-000113: proof notes, not the published rule

### Oath of the Drifter

- **ID:** `s5-sub-drifter`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000100, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/oath-of-the-drifter/pages/home.md` line 55. https://sites.google.com/view/oath-of-the-drifter/home
- **Anchor:** At 3rd level, you embrace the ways of the lone hunter. You gain proficiency with survival skills and one of the following skills of your choice: Nature, Stealth, or Perception.
- **Overview:** Paladin oath presented by char-gen as the black-hat partner of the Codebound. Captured features include 3rd (lone hunter: Survival and Nature, Stealth, or Perception), 15th (extra damage when you hit with advantage), and 20th. BCS-000113 marks the page's access status as weird.
- **Conflicts:**
  - BCS-000113: access status weird. It also notes Desert's Resilience advantage against frightened is redundant after the paladin's 10th-level aura.
- **Lineage:**
  - BCS-000113: proof notes, not the published rule

### Enforcer

- **ID:** `s5-sub-enforcer`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000101, BCS-000102, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/s5rogueoptions/pages/home.md` line 21. https://sites.google.com/view/s5rogueoptions/home
- **Anchor:** Enforcer Features 3rd Level: Brawler, Menacing
- **Overview:** Rogue subclass. 3rd Brawler (improvised weapons and medium armor, plus a sneak-attack condition) and Menacing (Strength for Intimidation). 9th Distracting Presence. 13th Frightful. 17th Brutality. Improvised-weapon tables are a separate published page, BCS-000102, and are part of this option's equipment procedure, not a second subclass.
- **Mechanics:**
  - 3rd Level: Brawler, Menacing. 3rd Level: Brawler, Menacing 9th Level: Distracting Presence
  - 9th Level: Distracting Presence. 9th Level: Distracting Presence 13th Level: Frightful
  - 13th Level: Frightful. 13th Level: Frightful 17th Level: Brutality
  - 17th Level: Brutality. 17th Level: Brutality Brawler
  - When you choose this archetype at 3rd level, you gain proficiency with improvise. When you choose this archetype at 3rd level, you gain proficiency with improvised weapons and medium armor. Use this to scrounge up a improvised weapon.
  - Starting at 3rd level, you can choose to use Strength for Intimidation skill che. Starting at 3rd level, you can choose to use Strength for Intimidation skill checks instead of Charisma. Distracting Presence
- **Lineage:**
  - BCS-000113: proof notes, not the published rule
- **Discord phrase hits (not play):** roanoke-season-3: Enforcer 3; empire-city: Enforcer 2
- **Sample message ids:** 738903625140535388 (roanoke-season-3, 🦸🏻-character-introduction, 2020-07-31), 742110276161110139 (roanoke-season-3, 🙋-out-of-character, 2020-08-09), 863220255455313960 (empire-city, combat-sign-up, 2021-07-10), 871091114583670784 (empire-city, dm-transparency-log, 2021-07-31)
- **Note:**  Discord counts for a common word are phrase hits, not a census of characters.

### Way of Gun Fu

- **ID:** `s5-sub-gunfu`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000110, BCS-000103, BCS-000114, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/arcanian-monk-options/pages/home.md` line 15. https://sites.google.com/view/arcanian-monk-options/home
- **Anchor:** Monk:Way of Gunfu Way of Gun Fu
- **Overview:** Monk subclass. Published page is arcanian-monk-options (BCS-000110). The earlier URL arcanianmonkoptions (BCS-000103) is only a heading shell, 'The Way of Gun-Fu'. Drive PDF BCS-000114 is the same version family, not a second confirmation. Features: 3rd Path of the Firefight (firearm proficiency; One with the gun), 6th Ki Dodge and Ki-infused Bullets, 11th Interrupting Strike, 17th Focused Beatdown.
- **Mechanics:**
  - level 3: Path of the Firefight. Firearm proficiency, including as improvised weapons, and they are monk weapons. One with the gun: a firearm may replace one unarmed strike from Flurry of Blows, and at 11 both.
  - level 6: Ki Dodge. As a reaction when an attack hits, before damage, spend ki equal to the difference between your AC and the attack. Your AC rises enough to make that attack miss until your next turn.
  - level 6: Ki-infused Bullets. Firearm attacks, including improvised, count as magical.
  - level 11: Interrupting Strike. When you use Ki Dodge, you may also attack the triggering creature if it is in range. The bonus to the attack and damage equals the ki spent.
  - level 17: Focused Beatdown. One additional action. Until the end of that turn, your attacks have advantage. The published site does not contain a rest or ki limit. PDF BCS-000114 requires a short or long rest before using it again.
- **Conflicts:**
  - Names: char-gen 'Way of Gunfu'; thin site 'The Way of Gun-Fu'; PDF title 'Way of GunFu' and 'Way of Gunfu'.
  - BCS-000113 says the published Focused Beatdown has no usage limit. The PDF extract at BCS-000114 says it can be used again only after a short or long rest. The published site page does not contain the phrase 'short or long rest'. Do not import the PDF limit into the published page.
- **Lineage:**
  - BCS-000113: proof notes, not the published rule
- **Discord phrase hits (not play):** empire-city: Gun Fu 1, Gun-Fu 1
- **Sample message ids:** 865952250341359656 (empire-city, dedicated-questions-to-dms-and-mods-go-here, 2021-07-17), 865952250341359656 (empire-city, dedicated-questions-to-dms-and-mods-go-here, 2021-07-17)

### Harbinger of Fated Bonds

- **ID:** `s5-sub-harbinger-bonds`
- **Type:** subclass
- **Parent:** `s5-class-harbinger`
- **Setting:** Arcania / Roanoke Season 5
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000094
- **Source:** `sources/roanoke-s5-legends/google-sites/harbingers5/pages/home.md` line 283. https://sites.google.com/view/harbingers5/home
- **Anchor:** Harbinger of Fated Bonds The Harbinger of Fated Bonds is blends the mystical art of divination with the precise mastery of reach weapons. As a Harbinger of Fated Bonds, you possess an innate ability to perceive the intricate threads of destiny and utilize the extended reach of your weapons to forge powerful connections
- **Overview:** 2nd level Weapon weaver (reach weapons as conduits, tied to the class touch-range limit). 6th Threads of Destiny and Omen's Doom. 9th Omen of Dread. 14th Threads Unleashed. The page uses the word Omenweaver.
- **Mechanics:**
  - 2nd Level: Weapon weaver. 2nd Level: Weapon weaver At 2nd level, you gain proficiency with reach weapons, such as glaives, halberds, or whips. These weapons become conduits for your divinatory powers, allowing you to channel touch-range spells through them. When you
  - 6th Level: Threads of Destiny. 6th Level: Threads of Destiny Omen's Doom:
  - Omen's Doom:. Omen's Doom: Once per short rest, you can unleash a wave of impending doom upon your enemies. As an action, you conjure a swirling vortex of dark energy within 30 feet of you. Each creature of your choice within the vortex must make a Wisdo
  - 9th Level: Omen of Dread. 9th Level: Omen of Dread At 9th level, you gain the ability to unleash a chilling omen that taps into the primal fears of your target, causing them to react in different ways based on a d4 roll. As an action, you can make a touch attack aga
  - 14th Level: Threads Unleashed. 14th Level: Threads Unleashed At 14th level, your command over the threads of destiny becomes absolute. Once per turn, when you hit a creature with a reach weapon attack while a touch-range spell is channeled through it using your Omenweave
- **Conflicts:**
  - The page says Omenweaver. If that name is not defined in the same feature, do not invent a definition. Read the anchored passage.

### Harbinger of Endings

- **ID:** `s5-sub-harbinger-endings`
- **Type:** subclass
- **Parent:** `s5-class-harbinger`
- **Setting:** Arcania / Roanoke Season 5
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000094
- **Source:** `sources/roanoke-s5-legends/google-sites/harbingers5/pages/home.md` line 237. https://sites.google.com/view/harbingers5/home
- **Anchor:** Harbinger of Endings:
- **Overview:** Subclass on the Harbinger page. Named features: 2nd Mortality, 6th Dwindling Hope, 9th Arresting Energy, 14th level heading 'Harbinger of Endings Feature' (the 14th-level feature is not given a separate name in that heading).
- **Mechanics:**
  - Endings:. Endings: An Augur learns to read the omens. Omens are the manifestations of divination magic that settles upon non-sentient creatures and other facets of nature.
  - 2nd Level: Mortality. 2nd Level: Mortality The Harbinger gains an awareness of their own mortality and the death that fate has designed for them.
  - 6th Level: Dwindling Hope.. 6th Level: Dwindling Hope. As an action, the Harbinger can magically force a Large or smaller creature they can see within 60 feet to make a Constitution saving throw against the Harbinger's spell save DC.
  - 9th Level: Arresting Energy. 9th Level: Arresting Energy When another friendly or neutral creature that the Harbinger can see within 60 feet fails a save that would result in damage, the Harbinger can grant resistance to that damage type for up to a minute.
  - 14th Level: Harbinger of Endings Feature. 14th Level: Harbinger of Endings Feature As a reaction, the Harbinger can force the weave to become a physicals barrier, seeping forth from their soul to their skin for 6 seconds.

### Harbinger of Veils

- **ID:** `s5-sub-harbinger-veils`
- **Type:** subclass
- **Parent:** `s5-class-harbinger`
- **Setting:** Arcania / Roanoke Season 5
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000094
- **Source:** `sources/roanoke-s5-legends/google-sites/harbingers5/pages/home.md` line 315. https://sites.google.com/view/harbingers5/home
- **Anchor:** Harbinger of Veils The Harbinger of Veils subclass embodies the secrets and mysteries that lie beyond the perceivable world. Through their unique connection to the ethereal plane and their manipulation of veils, they gain unparalleled sight, stealth, and divinatory prowess. Their abilities allow them to navigate throug
- **Overview:** 2nd Veiled Presence. 6th Veilweaver's Manipulation. 9th Enigmatic Shroud. 14th Master of Illusions.
- **Mechanics:**
  - 2nd Level: Veiled Presence. 2nd Level: Veiled Presence The Harbinger gains proficiency in the Deception and Stealth skills.
  - 6th Level: Veilweaver's Manipulation. 6th Level: Veilweaver's Manipulation The Harbinger gains the ability to manipulate the fabric of reality within a limited area.
  - 9th Level: Enigmatic Shroud. 9th Level: Enigmatic Shroud The Harbinger gains the ability to wrap themselves in an enigmatic shroud of illusion, enhancing their defensive capabilities.
  - 14th Level: Master of Illusions. 14th Level: Master of Illusions The Harbinger becomes a master of illusions, gaining the ability to cast major illusion once per long rest without using a spell slot.
  - Additionally, when they cast an illusion spell of 1st level or higher, they can . Additionally, when they cast an illusion spell of 1st level or higher, they can choose to make it more potent. Creatures that interact with the illusion or try to discern its nature must make an Intelligence saving throw against the Harbing

### Joybringer Domain

- **ID:** `s5-sub-joybringer`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000112, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/s5homebrewclericoptions/pages/home.md` line 43. https://sites.google.com/view/s5homebrewclericoptions/home
- **Anchor:** Joybringer Domain is a cleric subclass devoted to the spirit of celebration, joy, and communal merriment, inspired by the presence of Calico, the Bobcat Patron of Arcania's Southwest. These clerics embody the essence of the Old West, infusing their rituals and blessings with the energy of revelry while remaining true t
- **Overview:** Cleric domain of Calico on the Season 5 cleric site. Domain spells are listed from 1st through 9th level on the page. 1st Bonus Proficiency (Performance and an instrument). 2nd Channel Divinity: Joyful Inspiration. 6th Aura of Merriment. 8th Potent Spellcasting. 17th Euphoric Trance.
- **Mechanics:**
  - 1st Level: Bless, Heroism. 1st Level: Bless, Heroism 3rd Level: Enhance Ability, Prayer of Healing
  - 3rd Level: Enhance Ability, Prayer of Healing. 3rd Level: Enhance Ability, Prayer of Healing 5th Level: Beacon of Hope, Spirit Guardians
  - 5th Level: Beacon of Hope, Spirit Guardians. 5th Level: Beacon of Hope, Spirit Guardians 7th Level: Freedom of Movement, Guardian of Faith
  - 7th Level: Freedom of Movement, Guardian of Faith. 7th Level: Freedom of Movement, Guardian of Faith 9th Level: Mass Cure Wounds, Dream
  - 9th Level: Mass Cure Wounds, Dream. 9th Level: Mass Cure Wounds, Dream Bonus Proficiency
  - At 6th level, your presence exudes an aura of joy and merriment. C. At 6th level, your presence exudes an aura of joy and merriment. C hoose a number of creatures within 30 feet of you, up to your Wisdom modifier (minimum of one creature)
  - Starting at 8th level, you add your Wisdom modifier to the damage you deal with . Starting at 8th level, you add your Wisdom modifier to the damage you deal with any cleric cantrip. Euphoric Trance
- **Lineage:**
  - BCS-000113: proof notes, not the published rule

### Path of the Lumber Jacked

- **ID:** `s5-sub-lumberjacked`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000099, BCS-000113, BCS-000109
- **Source:** `sources/roanoke-s5-legends/google-sites/path-of-the-lumber-jacked/pages/home.md` line 1. https://sites.google.com/view/path-of-the-lumber-jacked/home
- **Anchor:** # Path of the Lumber Jacked - Source URL: https://sites.google.com/view/path-of-the-lumber-jacked/home
- **Overview:** Barbarian subclass. Char-gen also spells it Path of the Lumberjacked. 3rd: Shattering Hew and Heavy Hitter. 6th: Lumbering Charge. 10th: Crosscut. 14th: Devastating March.
- **Mechanics:**
  - 3rd Level: Shattering Hew, Heavy Hitter. 3rd Level: Shattering Hew, Heavy Hitter 6th Level: Lumbering Charge
  - 6th Level: Lumbering Charge. 6th Level: Lumbering Charge 10th Level: Crosscut
  - 10th Level: Crosscut. 10th Level: Crosscut 14th Level: Devastating March
  - 14th Level: Devastating March. 14th Level: Devastating March Shattering Hew
  - Devastating March (Level 14):. Devastating March (Level 14): Starting at 14th level, your immense presence and powerful strides allow you to move through the space of any creature that is unable to move or has been deprived of the ability to move. When you move through t
- **Conflicts:**
  - Char-gen spells 'Lumberjacked' as one word. The site title is 'Path of the Lumber Jacked'.
- **Lineage:**
  - BCS-000113: proof notes, not the published rule
- **Discord phrase hits (not play):** empire-city: Lumberjacked 1, Lumber Jacked 1; empire-city-dev: Lumberjacked 8, Lumber Jacked 1
- **Sample message ids:** 867304389881888798 (empire-city, the-pinkertons, 2021-07-21), 877362847225634857 (empire-city, out-in-the-noir, 2021-08-18), 747065049377406997 (empire-city-dev, chat, 2020-08-23), 754037354683039814 (empire-city-dev, playable-races, 2020-09-11)

### Rail Baron Pact

- **ID:** `s5-sub-rail-baron`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000098, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/s5warlockoptions/pages/home.md` line 17. https://sites.google.com/view/s5warlockoptions/home
- **Anchor:** The Rail Baron Pact As a warlock, you have forged a pact with the powerful and enigmatic beings known as the Rail Barons. These ancient entities are the personification of the rapid industrialization and expansion of railroads in the realm of Arcania. They are shrewd, influential, and possess an insatiable hunger for w
- **Overview:** Warlock option. The page gives patron features at 6th, 10th (Phantom Steed without a slot), and 14th, and a 3rd-level companion called a Railbo under the pact. BCS-000113 discusses a 'Pact of Expansion' temporary-hit-point question. Read that note against the page before deciding the feature's action economy. Do not add a limit the page does not state.
- **Mechanics:**
  - 1st level:. 1st level: Expeditious Retreat, Grease
  - 2nd level:. 2nd level: Enhance Ability, Web
  - 3rd level:. 3rd level: Blink, Haste
  - 4th level:. 4th level: Fabricate, Dimension Door
  - 5th level:. 5th level: Passwall, Teleportation Circle
  - Pact Boon:. Pact Boon: Railbound Companion
  - Railbound Link:. Railbound Link: You can communicate telepathically with your Railbound companion, allowing you to share information and coordinate strategies seamlessly.
  - Mechanized Assistance:. Mechanized Assistance: Your Railbound companion can aid you in various tasks. It can perform simple actions and interact with objects as if it were an independent creature. Additionally, it can use its reaction to provide you with advantage
  - Railhound:. Railhound: The Railhound is a swift and nimble companion, resembling a mechanical hound with razor-sharp claws. It excels in tracking, scouting, and chasing down enemies. While your Railhound companion is active, you gain advantage on Wisdo
  - Iron Drake:. Iron Drake: The Iron Drake is a powerful and imposing companion, resembling a massive mechanical dragon with wings of steel and fire. It excels at being an imposing figure. While your Iron Drake companion is active, you gain a bonus to spel
  - 6 further mechanic lines are in options.jsonl.
- **Conflicts:**
  - Changelog name 'Pact of Expansion' versus the page's Rail Barons / Railbo companion. Keep both names visible until a later revision says one replaced the other. The changelog is a proof note, not the published rule.
- **Lineage:**
  - BCS-000113: proof notes, not the published rule
- **Discord phrase hits (not play):** empire-city-dev: Rail Baron 2
- **Sample message ids:** 758144497375903744 (empire-city-dev, halloween, 2020-09-23), 767271425308229642 (empire-city-dev, halloween, 2020-10-18)

### Domain of Savage Fertility

- **ID:** `s5-sub-savage-fertility`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000112, BCS-000113, BCS-000109
- **Source:** `sources/roanoke-s5-legends/google-sites/s5homebrewclericoptions/pages/home.md` line 95. https://sites.google.com/view/s5homebrewclericoptions/home
- **Anchor:** Domain of Savage Fertility The Domain of Frontier's Blessing is a cleric subclass that embraces the juxtaposition of fertility and the unforgiving nature of the Old West. These clerics are driven by a deep understanding of the preciousness of life and the courage it takes to bring forth new generations in a harsh and p
- **Overview:** Cleric domain. The same page's prose names it 'The Domain of Frontier's Blessing' immediately after the heading 'Domain of Savage Fertility'. Domain spells include Revivify at 5th and Raise Dead at 9th. Char-gen bans revivify except for Savage Fertility clerics. 1st Bonus Proficiency. Further features are on the page at 6th and 17th.
- **Mechanics:**
  - 1st Level:. 1st Level: Bless, Cure Wounds
  - 3rd Level:. 3rd Level: Enhance Ability, Aid
  - 5th Level:. 5th Level: Beacon of Hope, Revivify
  - 7th Level:. 7th Level: Death Ward, Guardian of Faith
  - 9th Level:. 9th Level: Mass Cure Wounds, Raise Dead
- **Conflicts:**
  - The heading is Domain of Savage Fertility. The next prose names Domain of Frontier's Blessing. BCS-000113 says the subclass is named Frontier's Blessing everywhere except the title, and prefers Savage Fertility while noting Frontier's Blessing fits the subclass.
- **Lineage:**
  - BCS-000113: proof notes, not the published rule

### Spellshot

- **ID:** `s5-sub-spellshot`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000095, BCS-000109
- **Source:** `sources/roanoke-s5-legends/google-sites/spellshotwizard/pages/home.md` line 1. https://sites.google.com/view/spellshotwizard/home
- **Anchor:** # Spellshot Wizard. - Source URL: https://sites.google.com/view/spellshotwizard/home
- **Overview:** Wizard subclass. 2nd level: firearm proficiency and a runed firearm as a spellcasting focus; Dexterity may be used for spell attacks the page describes. 10th: ensorcelled bullets out to long range, with a stated limit inside short range. Char-gen points at this page as the wizard option. BCS-000113's subclass headings that were read do not include a Spellshot section.
- **Conflicts:**
  - The Site changelog's subclass headings, as captured, do not include Spellshot. Absence from that proof list is not absence from the published site.

### College of the Trail

- **ID:** `s5-sub-trail`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000092, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/s5bardcolleges/pages/home.md` line 15. https://sites.google.com/view/s5bardcolleges/home
- **Anchor:** Bard: College of the Trail In the world of wandering bards, names hold immense power. These roving minstrels possess a natural talent for granting names, and their spoken words carry a mysterious enchantment. Through their unique ability to bestow names upon others, they weave a tapestry of folk magic that resonates wi
- **Overview:** Bard subclass. Char-gen calls it the kid who gives nicknames that stick. 3rd: Beguiling Diversion and Instruments of the Trail, including a named instrument used as a spellcasting focus. Two different Level 6 blocks: Harmonious Ensemble, and the yclepes (nicknames) including Glory, Fortune, Fame, Resilience, and Prosperity. 14th: The Myth. The Legend., which casts legend lore without a slot twice per long rest.
- **Mechanics:**
  - Note:. Note: The Beguiling Diversion feature provides the bard with a reactive ability to maintain focus on the bard, even if the charmed creatures make Perception checks. The limitation of one reaction per round ensures the feature is balanced an
  - Level 6:. Level 6: Harmonious Ensemble
  - Level 6:. Level 6: An adventurer of any other name.
  - Yclepes of Glory:. Yclepes of Glory: Nicknamed weapons or spellcasting foci gain the following ability: Once during the next minute, the damage type of attacks made with the weapon or through the focus is changed to your choice of psychic, force, necrotic, or
  - Yclepes of Fortune:. Yclepes of Fortune: Nicknamed spellcasting focuses or component pouches gain the following ability: Spells cast using the named focus or component pouch may have their spell save DC increased. The inspired creature may choose one save type:
  - Yclepes of Fame:. Yclepes of Fame: Nicknamed humanoid creatures gain expertise in a pair of skills of their choice for 24 hours. This does not apply to tool, vehicle, or instrument proficiencies or gaming sets.
  - Yclepes of Resilience:. Yclepes of Resilience: As a bonus action, spend one use of bardic inspiration to grant a nickname to a humanoid creature within 60 feet. The creature gains the following benefits for 24 hours:
  - Yclepes of Prosperity:. Yclepes of Prosperity: As a bonus action, spend one use of bardic inspiration to grant a nickname to a humanoid creature within 60 feet. The creature gains the following benefits for 24 hours:
  - Level 14: The Myth. The Legend.. Level 14: The Myth. The Legend. As an action, you can cast the legend lore spell without expending a spell slot. You can use this feature twice per long rest.
- **Conflicts:**
  - BCS-000113 questions whether Glory's damage-type change lasts only a minute, whether Fame can grant expertise in skills the target does not already have, and whether Resilience should affect hit points rolled on level up.
- **Lineage:**
  - BCS-000113: proof notes, not the published rule

### Domain of Mischievous Whims

- **ID:** `s5-sub-whims`
- **Type:** subclass
- **Setting:** Arcania / Roanoke Season 5 published site
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SUBCLASS
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000112, BCS-000113, BCS-000109
- **Source:** `sources/roanoke-s5-legends/google-sites/s5homebrewclericoptions/pages/home.md` line 167. https://sites.google.com/view/s5homebrewclericoptions/home
- **Anchor:** Domain of Mischievous Whims. The Domain of Mischievous Whims is a cleric subclass that embodies the playful and cunning nature of Calico, the bobcat-headed demigoddess of the American Southwest. These clerics embody mercurial cat- like mischief and revel in the unpredictable and unconventional. These clerics combine th
- **Overview:** Cleric domain on the same Calico page. Char-gen spells it 'Mischiveous Whims'. Features continue at 6th and 17th on the page, including a Prank reference at 6th.
- **Mechanics:**
  - 1st level:. 1st level: Disguise Self, Charm Person
  - 3rd level:. 3rd level: Invisibility, Phantasmal Force
  - 5th level:. 5th level: Fear, Major Image
  - 7th level:. 7th level: Confusion, Hallucinatory Terrain
  - 9th level:. 9th level: Modify Memory, Mislead
  - Chaotic Mirror:. Chaotic Mirror: The creature's reflection in nearby reflective surfaces takes on a wicked life of its own. It becomes trapped within the mirror, unable to escape or interact with the real world. During this time, the creature is incapacitat
  - Withering Hex:. Withering Hex: The creature is hexed with an insidious curse that drains its vitality. It suffers disadvantage on attack rolls and ability checks.
  - Pervasive Paranoia:. Pervasive Paranoia: The creature's mind is plagued by twisted illusions and fears, causing it to have disadvantage on Wisdom saving throws and be unable to distinguish friend from foe.
  - Prankster's Delight Improvements:. Prankster's Delight Improvements: At 6th level, the malevolent pranks you unleash become even more potent. While a creature is affected by your Prank, it suffers additional effects depending on the chosen prank:
  - Chaotic Mirror:. Chaotic Mirror: The creature also takes 2d6 psychic damage at the start of each of its turns while trapped within the mirror.
  - 2 further mechanic lines are in options.jsonl.
- **Conflicts:**
  - Char-gen spelling 'Mischiveous' versus the site's 'Mischievous'.
- **Lineage:**
  - BCS-000113: proof notes, not the published rule
- **Discord phrase hits (not play):** empire-city: Mischiveous 1
- **Sample message ids:** 864306006883958785 (empire-city, rochambeaus-glory, 2021-07-13)

### Appalachian Bobcat

- **ID:** `s5-subrace-bobcat`
- **Type:** subrace
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 411. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Tabaxi Subrace: Appalachian Bobcat The Appalachian Bobcat is a unique subrace of Tabaxi that hails from the rugged and untamed mountainous regions. These feline humanoids embody the spirit of the wilderness, possessing characteristics and traits influenced by the rugged terrain a
- **Overview:** Presented as a tabaxi subrace and an Arcanian Cryptid. Medium, walk 30. Trait headings include Stealthy Prowess, Darkvision, Mountaineer's Expertise, Keen Senses, and Natural Weapons.
- **Conflicts:**
  - Char-gen maps Tabaxi to Appalachian Bobcat. The page also prints its own trait headings.

### Gritgiblin

- **ID:** `s5-subrace-gritgiblin`
- **Type:** subrace
- **Also printed as:** Gritgiblins, Otterbobs, Goblins of Grit
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 311. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Goblin Subrace: Gritgiblin (Otterbobs) Gritgiblins, also known as Otterbobs, are a unique subrace of goblins native to the coastal city of Tacoma, Washington. These sea-faring goblins share a striking resemblance to otters, with sleek fur, webbed digits, and a natural affinity fo
- **Overview:** Presented as a goblin subrace, also called Otterbobs, from a coastal city in the page's fiction. Aquatic adaptation, swim speed, amphibious, water vehicles, natural armor 13 + Dexterity when unarmored, and other listed traits. Char-gen maps 'Goblin - Goblins of Grit.'
- **Conflicts:**
  - The heading spells Gritgiblin. The next sentence spells Gritgiblins.

### Klondike Goliath

- **ID:** `s5-subrace-klondike`
- **Type:** subrace
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 523. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Goliath Subrace: Klondike Goliath The Klondike Goliaths are a unique subrace of Goliaths who have adapted to the harsh and unforgiving environment of the Alaskan Klondike. Born amidst frozen tundra, towering mountains, and treacherous icy terrains, they possess the endurance and 
- **Overview:** Presented as a goliath subrace. Medium, walk 30. Cold resistance under Alaskan Adaptation. Other headings: Frost Step, Mountain's Resilience, Salmon Puncher, Klondike Heritage.

### Mississippi Mudskipper

- **ID:** `s5-subrace-mudskipper`
- **Type:** subrace
- **Also printed as:** Mississippi Catfish, Locatha Subrace
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 371. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Locatha Subrace: Mississippi Mudskipper . Society: The Mississippi Mudskippers thrive in a tightly-knit and communal society, where cooperation and interdependence are highly valued. They form close-knit family units known as "Brine Clans," comprising several generations that liv
- **Overview:** Heading says Locatha subrace Mississippi Mudskipper. Ability scores in the next block: Wisdom +2, Charisma +1. Walk 30, swim 30. The age line and the social-advantage line say Mississippi Catfish, not Mudskipper. Underwater blindsight 60 feet. Char-gen maps Locathah to Mississippi Mudskipper.
- **Conflicts:**
  - The same section uses Mississippi Mudskipper in the heading and Mississippi Catfish in the age and social lines.
  - Char-gen spells the base species Locathah. The race page spells Locatha.

### Palomino Centaur

- **ID:** `s5-subrace-palomino`
- **Type:** subrace
- **Also printed as:** Palamino Centaur
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE_ALSO_PRESENTED_AS_RESKIN
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 475. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Centaur Subrace: Palomino Centaur The Palomino Centaurs are a unique subrace of centaurs that hail from the majestic Colorado Rockies, a land teeming with untamed beauty and wild magic. Born within a roving pod of Tarasques, they embody both the indomitable spirit of the mountain
- **Overview:** Presented as a centaur subrace and an Arcanian Cryptid. Medium. Trait headings include Roving Power, Wild Charge, and Unbridled Heart (immunity to paralysis). The speed line is split across the capture.
- **Conflicts:**
  - Char-gen spells the map 'Palamino Centaur'.

### Plainsguard

- **ID:** `s5-subrace-plainsguard`
- **Type:** subrace
- **Parent:** `s5-race-tatankan`
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 133. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Plainsguard: The guardians of the open plains, Plainsguard Tatankan are known for their unyielding endurance and vigilance.
- **Overview:** Tatankan subrace. Constitution +1. Cast Longstrider once per long rest, Wisdom spellcasting.

### Spiritspeaker

- **ID:** `s5-subrace-spiritspeaker`
- **Type:** subrace
- **Parent:** `s5-race-tatankan`
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 145. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Spiritspeaker: Tatankan with a strong connection to the spirits of nature, they are skilled in the ways of druidic magic.
- **Overview:** Tatankan subrace. Wisdom +1. Druidic Affinity is the following feature heading.

### Sunrise Puffkin

- **ID:** `s5-subrace-sunrise-puffkin`
- **Type:** subrace
- **Parent:** `s5-race-puffkin`
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 609. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Sunrise Puffkin Sunrise puffkin often inhabit places like faerie circles and more often interact with other humanoid races, often forming long-lasting relationships with nearby villages. Their smaller appearances tend to make them more endearing than their sunset cousins, though 
- **Overview:** Puffkin subrace. Charisma +1. Headings: Natural Cuteness, Soft Body, Distracting Spores.

### Sunset Puffkin

- **ID:** `s5-subrace-sunset-puffkin`
- **Type:** subrace
- **Parent:** `s5-race-puffkin`
- **Setting:** Arcania, published on the Season 5 Homebrew Races site. Several also have earlier Roanoke documents.
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_TRAIT_BLOCK
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000107
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-races/pages/home.md` line 633. https://sites.google.com/view/homebrew-races/home
- **Anchor:** Sunset Puffkin Sunset puffkin are tougher and hardier than their sunrise cousins, though they are no less kind or benevolent. While not as familiar with other humanoid races, they will form friendships with them all the same, especially with those who keep especially late or espe
- **Overview:** Puffkin subrace. Headings include Ability Score Increase, Darkvision, Bioluminescen (the page's spelling), and Sudden Bloom.
- **Conflicts:**
  - The page spells a heading 'Bioluminescen'.

### Amnesty

- **ID:** `spell-amnesty`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 171. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Amnesty 3rd-level Enchantment Spell
- **Overview:** 3rd-level Enchantment Spell. Parenthetical classes on the page: paladin, cleric, ranger. Material component: a vial worth at least 300 gold pieces, consumed.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Bliss

- **ID:** `spell-bliss`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 95. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Bliss Spell Level:
- **Overview:** The page uses separate lines: Spell Level 1st level, School Enchantment, then a Classes line. Do not collapse that into a parenthetical class list the page did not print in one line.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Boldness

- **ID:** `spell-boldness`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 139. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Boldness 2nd-level Enchantment (Bard, Sorcerer, Warlock, Wizard)
- **Overview:** 2nd-level Enchantment. The page lists Bard, Sorcerer, Warlock, Wizard. Concentration up to 1 minute in the duration line.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Cringe

- **ID:** `spell-cringe`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 15. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Cringe Cantrip (Bard, Sorcerer)
- **Overview:** Cantrip. The page's level line reads 'Cantrip (Bard, Sorcerer)'. BCS-000113 says Cringe has no school and that no classes get it, and compares it to vicious mockery. The changelog is a proof note. The page is the published text.
- **Conflicts:**
  - Published page: Cantrip (Bard, Sorcerer). Changelog BCS-000113: no school, and no classes get it.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Defiance

- **ID:** `spell-defiance`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 211. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Defiance 3rd-level Abjuration
- **Overview:** 3rd-level Abjuration. Read the class line at the anchor rather than inferring a list.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Desolation

- **ID:** `spell-desolation`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 391. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Desolation Level:
- **Overview:** The page says 6th level Necromancy and a parenthetical that includes Bard, Sorcery, Artificer, Ranger, and then a later Classes line that says Wizard. 'Sorcery' is the page's word. Do not correct it to Sorcerer.
- **Conflicts:**
  - The page prints both a parenthetical class list containing 'Sorcery' and a later Classes line 'Wizard'.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Contagious Despair

- **ID:** `spell-despair`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 433. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Spell: Contagious Despair Level:
- **Overview:** 7th level. School line: Enchantment. Read the classes line at the source. At-higher-levels text is on the page.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Dread

- **ID:** `spell-dread`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 37. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Dread 1st-level Enchantment (Bard, Sorcerer, Warlock, Wizard)
- **Overview:** 1st-level Enchantment. The page lists Bard, Sorcerer, Warlock, Wizard.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Dumb Ways to Die

- **ID:** `spell-dumb-ways`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 243. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Dumb Ways to Die 4th-level Necromancy (Bard, Sorcerer, Warlock, Wizard)
- **Overview:** 4th-level Necromancy. The page lists Bard, Sorcerer, Warlock, Wizard. Six numbered results are part of this spell: The Leeching Lunacy, Snake Oil Swindle, Grizzly's Grudge, Tainted Tins, Insurance Fiasco, Dynamite Disarray. They are not separate spells.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Frustration

- **ID:** `spell-frustration`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 65. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Frustration 1st-level Enchantment (Bard, Sorcerer, Warlock, Wizard)
- **Overview:** 1st-level Enchantment. The page lists Bard, Sorcerer, Warlock, Wizard. Has an at-higher-levels line.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Terrifying Pursuit

- **ID:** `spell-pursuit`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 349. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Terrifying Pursuit 4th-level illusion (Warlock, Wizard, Druid)
- **Overview:** The page says 4th-level illusion (Warlock, Wizard, Druid). BCS-000113 says it has no school, suggests transmutation, and says it has no classes, recalling an older warlock or paladin version. Both statements are in the corpus. The page is the published wording. The changelog is a proof note, not a silent edit.
- **Conflicts:**
  - Published page: 4th-level illusion (Warlock, Wizard, Druid). Changelog: no school (transmutation suggested) and no classes.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Shame

- **ID:** `spell-shame`
- **Type:** spell
- **Setting:** Arcania / Roanoke Season 5 homebrew-spells site, page title Blood Magic
- **Design relation:** BESPOKE
- **Completeness:** PUBLISHED_SPELL
- **Draft / published / offered / play-observed:** False / True / True / NOT_ESTABLISHED
- **Corpus:** BCS-000093, BCS-000113
- **Source:** `sources/roanoke-s5-legends/google-sites/homebrew-spells/pages/home.md` line 313. https://sites.google.com/view/homebrew-spells/home
- **Anchor:** Name: Shame School:
- **Overview:** 5th-level Enchantment. Classes line: Bard, Warlock, Wizard. 6d8 psychic damage on a failed Wisdom save, plus the further saves in the description. The name is on its own 'Name:' line after Dumb Ways to Die, which is why a heading scan can miss it.
- **Note:** Integral to player options because the Season 5 spell site publishes them for use. Class-list gaps are conflicts, not permission to assign a class.

### Urucokra

- **ID:** `uru-urucokra`
- **Type:** race
- **Also printed as:** Urukocra
- **Setting:** Roanoke. Verbatim handout and race-edit notes. Not on the Season 5 homebrew-races page.
- **Design relation:** BESPOKE
- **Completeness:** VERBATIM_PLUS_EDIT_NOTE
- **Draft / published / offered / play-observed:** True / False / False / NOT_ESTABLISHED
- **Corpus:** BCS-000120, BCS-000135, BCS-000086
- **Source:** `sources/roanoke/BCS-000120/source.md` line 37. (no URL; Drive or repo text)
- **Anchor:** ### Urucokra traits You have several traits in common with all other Urucokra
- **Overview:** Verbatim trait headings: Ability Scores, Age, Alignment, Size, Speed, Glide, Flight, Talons, Cryptid Carnivore Intuition, The Cover of the Canopy, Languages. BCS-000135 says to move flight to level 5 ('At Level 5 gain a flight speed'). BCS-000086 is lore, not a trait block. The string Urucokra does not occur on the Season 5 homebrew-races page.
- **Mechanics:**
  - Glide. Heading present in BCS-000120. Read that heading for the wording. This inventory does not restate a rule that was not copied here.
  - level 5: Flight (race-edit note). BCS-000135: 'At Level 5 gain a flight speed'. That is an edit note, not the verbatim block.
- **Conflicts:**
  - BCS-000120 spells a heading 'Urukocra hidden names' and the traits heading 'Urucokra'. Discord search also hits the spelling Urukocra.
- **Lineage:**
  - BCS-000135: 2020 race-edit notes, including moving flight later
  - BCS-000086: S3 Uru/Wudgie lore, not a trait block
  - BCS-000136: Rowing Oak mentions Urucokra as vulture-like people who have been seen. Not a trait block.
- **Discord phrase hits (not play):** roanoke-season-3: Urucokra 9, Urukocra 15
- **Sample message ids:** 738962165360361482 (roanoke-season-3, an-empty-beach-crash, 2020-08-01), 739312620510773359 (roanoke-season-3, quartz-rock-hill, 2020-08-02), 734205091485319228 (roanoke-season-3, 🌁-london, 2020-07-19), 735379556961353758 (roanoke-season-3, highgate-cemetery, 2020-07-22)
- **Note:** Not offered on the Season 5 char-gen approved list in the captured page.

## At War's End archetype names

Parent: `awe-wellsprings` in BCS-000066. No level features. Do not write abilities from the role brief.

| Name | Role brief | Line |
|---|---|---|
| Aberrant Enchanters | Voice that fractures reality—murmurs cause objects to contort, minds to unravel. | 435 |
| Arbiters | Instinctively sense magical threats—react to wayward spells or elemental surges before they fully manifest. | 448 |
| Arcane Acrobats | Move with supernatural dexterity—dancing atop ley lines, performing feats of parkour that defy gravity’s strictures. | 449 |
| Arcane Enchanters | Utter sacred formulas that animate runes—words become living spells that shape elemental matter. | 457 |
| Arcane Logicians | Deductively unravel elemental formulas—treat magic as a science, predicting and controlling outcome with precision. | 458 |
| Arcane Wardens | Shoulders bear arcane shields—physically or magically reinforcing barriers to protect allies from disruptive energies. | 450 |
| Astrographers | Speak divine words that realign fates—conveying cosmic patterns through spoken “star‐charts.” | 413 |
| Berserkers | Fearless in the face of any threat—gut instincts drive them into the heart of danger without flinching. | 470 |
| Celestial Sprinters | Move with supernatural grace, outrunning both physical threats and spiritual corruption. | 405 |
| Chanters | Use arcane rhetoric to sway raw elemental currents—words become the incantations that direct flames or gusts. | 459 |
| Devotees of the Grin | Bear eldritch burdens—mental enigmas that warp perception; their very endurance is a testament to chaotic will. | 428 |
| Divine Philosophers | Discern the underpinnings of cosmic morality—guiding communities through the nuanced interplay of faith and reason. | 418 |
| Divine Scholars | Deductively explore theology and spiritual law—mapping the divine code as if it were a cosmic theorem. | 414 |
| Dragoons | Combine martial agility with unwavering resolve—able to charge into battle or execute heroic feats of mobility. | 471 |
| Eldritch Philosophers | Probe the abyss of madness—seeking to understand chaos as a cosmic principle, risking sanity in the process. | 440 |
| Eldritch Scholars | Pursue forbidden reason—decode arcane paradoxes that defy sanity, charting the shape of chaos itself. | 436 |
| Embers & Umbers | Emotions ignite elemental forces—passion or fury that fans arcane energies into roaring magical conflagrations. | 461 |
| Fiery Courage | Emotions blaze with righteous fury—unleashing courage that uplifts allies and burns away despair. | 483 |
| Guardians of Instinct | Rely on divine intuition to sense peril or moral wrongness before it manifests. | 404 |
| Harmonious Artisans | Use sacred music and craftsmanship to reveal divine truths—hands shape both devotion and revelation. | 409 |
| Haunting Persuaders | Words that seep into dreams—planting seeds of doubt, insanity, or revelation in whomever hears them. | 437 |
| Kings & Vagabonds | Bear divine legitimacy—either as ordained rulers or as wanderers whose presence commands loyalty. | 416 |
| Kites | Wings tainted by eldritch flux—able to slip between realms yet vulnerable to sudden reality shifts. | 430 |
| Maddening Embers | Emotions burn with cosmic intensity—wrath or ecstasy that spills into the world like psychic fire. | 439 |
| Maestros | Hands weave complex incantations—fingers conducting literal “symphonies” of elemental magic to shape reality. | 453 |
| Magicrats | Command awe through arcane presence—borne aloft by ley line resonance, commanding respect by sheer mastery of magic. | 460 |
| Noble Champions | Bear the weight of honor—those whose very presence inspires loyalty and whose deeds set the standard of chivalry. | 482 |
| Oracles | Instincts tinged with madness—react to threats by channeling unpredictable psychic visions, seeing unseen dangers. | 426 |
| Order of the Brown Recluse | Hands craft eldritch artifacts—mastering forbidden sigils and unraveling secrets that drag one closer to The Hunger. | 431 |
| Philosophers | Delve into the metaphysics of magic—seeking to decode the foundational laws that underlie elemental balance. | 462 |
| Preachers | Persuade entire congregations to righteous action—words become living sermons that alter hearts and minds. | 415 |
| Psychos | Hands channel eldritch power—fists that distort reality with each strike, warping matter at the point of impact. | 429 |
| Resilient Ascendants | Soar on wings of faith—able to rise above adversity, learning from each fall to inspire others. | 408 |
| Righteous Pugilists | Channel divine power into every strike—fists become sermons, each blow an act of holy judgment. | 407 |
| Runecarved Brawlers | Fists etched with sigils—each strike channels raw elemental force (fire, stone, lightning) into physical blows. | 451 |
| Sanctified Protectors | Bear both physical and emotional burdens with divine resilience—true paragons of compassion. | 406 |
| Scribes | Hands transcribe valorous deeds into legend—crafting weapons, art, or texts that galvanize others to courage. | 475 |
| Sentinels | Stand unbroken against adversity—physically and morally unyielding, a “wall” between danger and those they guard. | 472 |
| Shadowy Aristocrats | Command dark respect—leaders who rule through fear, mystery, and the unsettling gravitas of eldritch presence. | 438 |
| Skyward Champions | Wings fueled by determination—rise above conflict, rallying others through deeds that inspire. | 474 |
| Soldiers | Fists and weapons become symbols of valor—charging headlong into challenges, exemplifying duty through action. | 473 |
| Soulforged | Forge souls in the crucible of passion—emotions serve as sacrificial fires that purify or empower. | 417 |
| Stalkers | Move silently through chaos—blending unpredictability with uncanny speed, as if walking between shadows. | 427 |
| Tactical Heroes | Apply cold strategy to leadership—reasoning that ensures the greatest good for the most, even in wartime. | 480 |
| Tinkers | Wings imbued with Arcane energy—flight that resists elemental extremes (storms, magma flows) and grants craft precision. | 452 |
| Valiant Orators | Rally troops with stirring speeches—turning fear into fervor, forging unity through persuasive address. | 481 |
| Valor Dictators | Speak words that stir battlefield morale—each utterance invigorates allies and steels their resolve. | 479 |
| Valorous Philosophers | Seek deeper meaning in valor—guiding others to bravery through wisdom and ethical reflection. | 484 |

