<!-- BFDM_INTEGRITY_PACKET_META
{"dependency_commit": "bdfbbf1a34e142b63b7e752033c67d5b7176c9b2", "evidence_dependency_summary": {"bcs_000045_metadata_sha256": "9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055", "bcs_000045_sha256": "adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166", "discord_s3_database_sha256": "16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d", "identity_assertion_digest": "sha256:24186e4a5215e2d03a38b165067b20cb3ac12b948d4fcc87971d08b2607ea1c9"}, "packet_payload_sha256": "sha256:21bec6da35f72b5b0d0e08494f396f657a02e9d14f110e4a80600cf226d55890", "packet_state_sha256": "sha256:b48504e665c149f743528ded83f9089fac425891dc2cbaf428eb0a7e9f03122b", "proposition_count": 120, "schema": "bfdm_integrity_review_packet/v1", "tranche": "research/roanoke-s3/decision-cases-v1.jsonl", "unit_count": 20}
-->

# Roanoke S3 decision cases v1 — semantic review packet

Generated view only. Historical truth remains in BCS/native sources; canonical audit state remains in research/integrity/audit_ledger.jsonl.

Every proposition is UNVERIFIED unless its nested ledger verdict explicitly says otherwise. Mechanical reconstruction does not certify motive, causality, scope, transfer, or expert principle.

## Tranche facts

- Cases: 20.
- Audit propositions: 120.
- Markdown/JSON relationship: exact synchronized equivalents at staging time; neither declares itself generated from the other.
- BCS-000045 normalized body SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166.
- Canonical S3 Discord database LFS SHA-256: 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d.
- Confirmed Brendon S3 Discord identity: identity:brendon:discord:313689699627696139:roanoke-s3 / immutable user 313689699627696139.

### BDC-S3-004 forensic boundary

The disputed prep locators were already present in the first v1 Markdown commit. PR #2 preserved no BCS-000045 representation. The later preserved normalized and export snapshots both resolve those coordinates to unrelated material and contain no relevant limb-loss/handwave prep passage. Both locators are ORIGINAL_REPRESENTATION_UNAVAILABLE; their current support result is SUPPORT_NOT_FOUND; representation drift is not established.

---

## BDC-S3-001 — A declined hook advances to its failure state

Legacy confidence: high.

**Situation.** A scheduled adventure hook was available, but the players appeared tired and might skip it.
- audit: audit:BDC-S3-001:situation
- proposition: sha256:4ea65e0e474ba802af77778968a8fa913afdd0ac964d24162b9b2b5d31c608c5
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** Player energy/availability mattered more than forcing the day's prepared content.
- audit: audit:BDC-S3-001:noticed
- proposition: sha256:7dbaa2bb33dd64bc08dda7ccadf08193ff19d33dde5d0a13b2f8af36312ad3c6
- semantic status: UNVERIFIED
- flags: none

**What mattered.** player choice, campaign continuity, consequences.
- audit: audit:BDC-S3-001:values
- proposition: sha256:7a769f5306c3f073c0bcd40d7846665776805f0da0bc03ef72cfefad55c4cdf2
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon explicitly told the group they did not have to adventure and noted that he already had a fail condition for leaving the situation unchecked.
- audit: audit:BDC-S3-001:intervention
- proposition: sha256:6a7c6df0f3c6ee3e04665397422637373e839810e7dd7bbae45d874cbebdbd44
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Observed result.** Players immediately volunteered to go; the hook remained voluntary, while the world consequence remained credible.
- audit: audit:BDC-S3-001:observed_result
- proposition: sha256:86ff46a931ecb2f47c880a9a20bf67f2caa456a6330eefb10cde0e57a14370f8
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** Make participation optional while keeping the situation consequential. A hook can be declined; the world does not freeze when it is.
- audit: audit:BDC-S3-001:reusable_judgment
- proposition: sha256:d5f9540048f1234f0a72e05ac4d8b669197cf5de70488314ec46dc33ffb741c9
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L1911-L1923

### Prep excerpt — BCS-000045:L1911-L1923
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:7630b411ee0a85827655067814c0582b7bf78bc6ddf829cf6585780b4cb6411b
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
                                Château du Brûle 
 Knights looking for a group to reclaim an artifact stolen from the temple in the night by a group of Werewolves that killed several members of the order before leaving with the holy symbol of the Sun King [with a secret message in code hidden in it {possible downtime puzzle for players to solve}]. Florian Chapelle seeks out adventurers to help track invisible man down, defeat him, and reclaim the relic. If quest is successfully completed, Florian will elect to have the players join to defend the secrets and bring it to the new world.
Howls are heard in the night and the sound of alarm bells go off. Shouts come from the Chateau  
                                7:30 @ 
                                        Château du Brule 
                                                >Florian Chapelle comes running outside after alarm bells go off in order to find adventurers to help track down a murdering thief.


                                                @ Underground Warrens
                                                >Players follow a blood trail down into the tunnels into some haphazardly laid traps in this mini dungeon. If they get to the end in time, they will corner a group of Werewolves hiding within an old Hag’s ritual chambers.
>Werewolves proceed to attack players. Combat ensues against this powerful enemy. 
>[Victory Conditions] When werewolves[k] are killed the room is able to be explored to see gory sacrifices and witch runes throughout the walls and chambers. Scratch marks are seen prying at the back of a secret door as if there was a hidden compartment. Inside is the holy symbol in the midst of an altar to be corrupted. Symbols that tell a story about the gods fighting Cthulhu line the walls and seem to tell of its power. Florian will tell the players about the order and ask them to consider joining on Friday and to seek out others that may want to join. {Holy Symbol contains two puzzles. 1st is to unlock the compartment with a set of physical puzzles with symbols and stuff. 2nd is to decipher a code that lays out week 3-5 tasks of reclaiming the relics on Roanoke}[l]
>[Failure Conditions] Will try to slip past party and escape back to the surface and into the night where they will turn back into human or dragonborn form. Will attempt to make it to the docks, kill a few sailors, and steal a pontoon to head North.
~~~

**Claimed live evidence.** `741819860043956335` (2020-08-09, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 741819860043956335
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0249.jsonl:437 @ row sha256:a10432ab7def992cf14da073812ff98145b3b22da8c9b78a3a280d786bcb8330
- timestamp: 2020-08-09T00:47:16.981000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-09T00:43:28.735000Z | KnightOfCydonia [436232470242000916] | I. Have. A. Plus 9. To investigation...
   2020-08-09T00:43:44.202000Z | KnightOfCydonia [436232470242000916] | God being a rogue is amazing
>> 2020-08-09T00:47:16.981000Z | DM radar [313689699627696139] | To be clear, if the players need a break today, thats fine. we don't have to have an adventure. I have a fail condition for not checking it out
   2020-08-09T00:47:45.827000Z | Eloise >:3c [260820438026813440] | I think some of us will be going
   2020-08-09T00:48:11.103000Z | KnightOfCydonia [436232470242000916] | I will be
~~~

**Representative line.** “we don't have to have an adventure. I have a fail condition for not checking it out”

### Mechanical warnings / lineage

- BCS-000045:L1911-L1923: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 741819860043956335

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-002 — Recover momentum by reconnecting an existing unresolved thread

Legacy confidence: high.

**Situation.** Play had drifted and the group asked what was on the agenda.
- audit: audit:BDC-S3-002:situation
- proposition: sha256:c2027bf361eb8bd45ad62b5d6cec6ab017798f0c792cf1e858d9e165055b783c
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The game needed direction, but an existing Chinnokin thread was already alive in the fiction.
- audit: audit:BDC-S3-002:noticed
- proposition: sha256:7c9c30461b8983dae88001fc6e14b0d2b9a0654b48cc283adab464739792a900
- semantic status: UNVERIFIED
- flags: none

**What mattered.** momentum, planned through-line, continuity.
- audit: audit:BDC-S3-002:values
- proposition: sha256:a7c8cb356af21773ead54431f4c1c6a69228606a3bd3f83e38f67877ba956d18
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon chose the Chinnokin storyline as the fastest way back toward planned content, then pointed to the in-world visitor at Fathoms Bridge instead of inventing a new quest.
- audit: audit:BDC-S3-002:intervention
- proposition: sha256:790e7c2113443a34c7c5b53d08be8f0203fc9b3c404d886c2935d39150896d21
- semantic status: UNVERIFIED
- flags: none

**Observed result.** Players immediately recognized the thread and began discussing how to pursue it.
- audit: audit:BDC-S3-002:observed_result
- proposition: sha256:3e43e4c6f5aff0453bdd7a932cecc18fdf4f883dcdb261f2c8cb72b2205d7289
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** When play drifts, steer first through an unresolved thread already present in the world. Prefer reconnection over replacement.
- audit: audit:BDC-S3-002:reusable_judgment
- proposition: sha256:469d8a20575b2be3da2b97de2c8d887032b6ca7c9b91bf1389660c5f497fe086
- semantic status: UNVERIFIED
- flags: none

**Claimed prep evidence.** BCS-000045:L1636-L1647, BCS-000045:L2821-L2825

### Prep excerpt — BCS-000045:L1636-L1647
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:a61b99b82fd4f2d3d62ba127aee7c89d99a9b4fc51cfa53d1fa976d712a8dac3
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Once the hag coven is ended, a decades old conflict between Uru (death worshiping vulture people) and The Chinnokin (Ancient Guardians of the sea) erupts on the island. Both sides start out as hostile to the group. The Chinnokin are attempting to prevent the Deep from rising. The Chinnokin are giving the dead to the deep rather than consuming them. Croatoan has taken the form of something from beneath the waves because it benefits from the motes of divinity that the Uru have been delivering to the deep. 




The story is expressed in daily one shots with a heavy focus on puzzles, cryptography and rp.


Through lines for subplots:


The through line is a series of plot information to be given out in bits and pieces over the course of interaction with the players in your faction.
~~~

### Prep excerpt — BCS-000045:L2821-L2825
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:6da7a16531d0da8316783a727f21faedacc61861dbb8483684c7fe8112eecbaf
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Day 19 Water Rising, TBD Chinnokin Encounter, Storm's A Brewin', Destruction of tree
All water turns dark. It has a metallic taste but does not have any other negative effects. Visibility underwater is cut in half. The Archivist pushes his agenda forward by suggesting that the lode stones should be activated to raise the island.
Day 20 Voting begins, Jackalope Plague.
Uru Cadaver Collector. Cadaver Collecter is picking up all of the dead jackalopes to bring to the ocean. 
Day 21 Voting ends. Hags
~~~

**Claimed live evidence.** `740653504682786826` (2020-08-05, 🗨 Social / 🙋-out-of-character); `740653688552554497` (2020-08-05, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 740653504682786826
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0219.jsonl:23 @ row sha256:7f0e2d39d7ccf9cdda2bad2e00a1da29ebec200d9230dac9179357b86c489af7
- timestamp: 2020-08-05T19:32:36.193000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-05T19:31:56.624000Z | Noah [360967589511561218] | Ayyy
   2020-08-05T19:32:02.089000Z | Noah [360967589511561218] | We will use that time well
>> 2020-08-05T19:32:36.193000Z | DM radar [313689699627696139] | The quickest way to get us back onto story is to pick up the chinnokin storyline
   2020-08-05T19:33:20.031000Z | DM radar [313689699627696139] | That would get us back in the direction of planned Content <@456226577798135808>
   2020-08-05T19:34:00.740000Z | DM radar [313689699627696139] | There was a visitor late last night at fathoms bridge
~~~

### Discord evidence — 740653688552554497
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0219.jsonl:26 @ row sha256:08bd95fc998a5ab61122a8416fa4e89da6911264841939e4df4aeb92f674f7ec
- timestamp: 2020-08-05T19:33:20.031000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-05T19:32:02.089000Z | Noah [360967589511561218] | We will use that time well
   2020-08-05T19:32:36.193000Z | DM radar [313689699627696139] | The quickest way to get us back onto story is to pick up the chinnokin storyline
>> 2020-08-05T19:33:20.031000Z | DM radar [313689699627696139] | That would get us back in the direction of planned Content <@456226577798135808>
   2020-08-05T19:34:00.740000Z | DM radar [313689699627696139] | There was a visitor late last night at fathoms bridge
   2020-08-05T19:34:07.014000Z | Deleted User [456226577798135808] | The chinnokin being the one in the water on the south ya?
~~~

**Representative line.** “The quickest way to get us back onto story is to pick up the chinnokin storyline”

### Mechanical warnings / lineage

- BCS-000045:L1636-L1647: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L2821-L2825: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 740653504682786826

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-003 — Prepared combat is subordinate to current party state

Legacy confidence: high.

**Situation.** Four players were available late in the final week, with mixed resource depletion, and a preplanned fight was ready.
- audit: audit:BDC-S3-003:situation
- proposition: sha256:450c64bf6f29f582f3b3af95a534a4ff73c797c7e9bd362add0f1caf4aea60d7
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The planned encounter assumptions no longer matched the actual party state and available time.
- audit: audit:BDC-S3-003:noticed
- proposition: sha256:04dea366b2e520647d90d2cd4537f73db3db19b47b51040c01c58f5827334a3f
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**What mattered.** felt challenge, satisfaction, fairness, time.
- audit: audit:BDC-S3-003:values
- proposition: sha256:46d62480906c1f974988c74cfe8be17e57d4aa2c3676325ee2620dc625885750
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon declined to default into the preplanned fight and instead considered a mostly-RP version or mobs rather than bosses, explicitly asking whether that would be satisfying.
- audit: audit:BDC-S3-003:intervention
- proposition: sha256:90c17baa7f52274fd1a0dfe347b787e1ac756724f8c142876f6ce3652ea1ad25
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The group discussed what kind of play would feel worthwhile rather than being pushed into the scheduled boss structure.
- audit: audit:BDC-S3-003:observed_result
- proposition: sha256:ae426832373ad381354a65e1a64bc745b1ea679ae1a47d693b31d5d2b5732de8
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** Re-evaluate prepared encounters at the moment of delivery. Preserve the intended experience, not the mere fact that an encounter was prepared.
- audit: audit:BDC-S3-003:reusable_judgment
- proposition: sha256:ca3ce3a2a6b6c22cecf9ef7aca06b2d61b526935e29f4d86d15767c513092eea
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L2840-L2857

### Prep excerpt — BCS-000045:L2840-L2857
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:24853649e78549bb0e6ae80fcda8230f486fbd857a68340af71c939b5d3d1aa7
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Day 29 Aether begins: Island returns to normal water level. Final lodestone summoning ritual.
Day 30 A Meteorite of lodestone is summoned to roanoke to complete the Aether ritual.
Basic Concept: A spell jammer ship whose engine is made of loadstone crashes to the island, bringing with it a bunch Thri Kreen crew, a bunch of Giant Space Hamsters and a ship containing the elder brain orphan raised by the crew. The Elder brain (a good guy npc for our purposes) warns the group that they have been spotted by another ship. A ship of Illithids are chasing them, attempting to reclaim or destroy the elder brain. 


Pilot the spell jammer airship in battle against the Mindflayer bad guys in an action packed adventure. 


Upon the successful destruction of the illithid ship, the thri kreen crew’s ship also crash lands. 


The ship you are piloting can donate its lodestone engine to the island, they will use the rest of the parts to repair the illithid’s much better ship to return to space. 
Day 31 Ossuary opened. The Tinker’s story is told.
Day 32 The legend of the tinker
Day 33 The tinkers return.
Day 34 The infernal well.
Day 35 The Hunger Voice Event.
The Hunger begins by inflicting deafness on the group, and dominates their mind with its voice. Telepathy fails, as it is dominating all of the telepathic lines of communication by speaking to all of you at once.
~~~

**Claimed live evidence.** `746253583552479272` (2020-08-21, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 746253583552479272
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0383.jsonl:27 @ row sha256:cc4737a42df8389fbb66a4a2c459b9c40ddb0e082ae170dd0e8c4925d5800ea6
- timestamp: 2020-08-21T06:25:19.040000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-21T06:25:07.348000Z | Eloise >:3c [260820438026813440] | looks like we have 4 ppl
   2020-08-21T06:25:16.472000Z | Eloise >:3c [260820438026813440] | rockman, web, baeshra, and copper
>> 2020-08-21T06:25:19.040000Z | DM radar [313689699627696139] | So 4 at depleted resources. My gut says don't take you into the preplanned fight.
   2020-08-21T06:25:25.081000Z | Eloise >:3c [260820438026813440] | probably not
   2020-08-21T06:25:32.033000Z | Eloise >:3c [260820438026813440] | rockman and copper are basically full
~~~

**Representative line.** “So 4 at depleted resources. My gut says don't take you into the preplanned fight.”

### Mechanical warnings / lineage

- BCS-000045:L2840-L2857: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 746253583552479272

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-004 — Handwave mechanics when the meaningful outcome is already chosen

Legacy confidence: high.

**Situation.** A player had deliberately asked for a dramatic limb loss, and another player asked whether healing mechanics were still necessary afterward.
- audit: audit:BDC-S3-004:situation
- proposition: sha256:41200c8eb1298ed248bacfc5aecf2576635a4e8196634263dae7b49e1194316b
- semantic status: UNVERIFIED
- flags: KNOWN_LOCATOR_FAILURE

**What Brendon noticed.** The central dramatic outcome was consensual and already achieved; extra resolution risked becoming procedural noise.
- audit: audit:BDC-S3-004:noticed
- proposition: sha256:2469db4425dfee712e3563129e28fb399b9117a8e5579331cb9f6ee2ab937aa8
- semantic status: UNVERIFIED
- flags: KNOWN_LOCATOR_FAILURE

**What mattered.** player intent, dramatic payoff, mechanical relevance.
- audit: audit:BDC-S3-004:values
- proposition: sha256:967f68661bde29f31c3d60704a11f90cb0dcbb973c2aa3f4b1b11cc248e26440
- semantic status: UNVERIFIED
- flags: KNOWN_LOCATOR_FAILURE

**Intervention.** Brendon allowed the bleeding to be stopped if desired but was willing to handwave the remainder because the scene had delivered the requested outcome.
- audit: audit:BDC-S3-004:intervention
- proposition: sha256:eaa27ac4447d386501ab637c76d53024489d915294f739dd50a0fa15b5448265
- semantic status: UNVERIFIED
- flags: CAUSALITY_CLAIM, KNOWN_LOCATOR_FAILURE

**Observed result.** The table treated the result as a successful dramatic moment rather than reopening it through unnecessary rolls.
- audit: audit:BDC-S3-004:observed_result
- proposition: sha256:edeb0115cbd0a0e2de7190a3e2b322a7dc143851e7b6dcecdd70c73d00ec4622
- semantic status: UNVERIFIED
- flags: KNOWN_LOCATOR_FAILURE

**Reusable judgment.** Use mechanics for uncertainty, resistance, cost, or consequences. Do not use them ceremonially after all relevant participants have intentionally chosen the core outcome.
- audit: audit:BDC-S3-004:reusable_judgment
- proposition: sha256:a51890f99736e4d5015bc726c6e553d5acdfe6ed264396ddabe86e6256e29caf
- semantic status: UNVERIFIED
- flags: KNOWN_LOCATOR_FAILURE, NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L1573-L1579, BCS-000045:L4420-L4422

### Prep excerpt — BCS-000045:L1573-L1579
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:3acd316a35c968ff52b5ef1a9b1c2ee678b7bfbb90eb12986356b774d9f8359a
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
What roanoke is:


Rules as written: roanoke is a 5 week long persistent Role Play Environment that seeks to combine the improvisational storytelling ability of tabletop role playing games with the functionality and user interface of video games. This is an rp heavy town drama told in 5 acts. 


Rules as intended: roanoke is a 5 week long deep dive into the daily lives of your characters. The game is centered around staying as a group to build a town, grow in your professions overcome horrific encounters and delve into the mysteries of the secret societies to which the townsfolk belong.
~~~

### Prep excerpt — BCS-000045:L4420-L4422
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:0bdb70355693cb1b5c759f4b27ad4b49c517c127898d536046b57b45bd0ff480
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Brendon Faulkner
The original creator of Roanoke Season One, Brendon Faulkner has decades of experience as a dungeon master. His recent accomplishments include experimenting with the form and boundaries of what Dungeons and Dragons can be, including the 24 hour format of Roanoke, a conversion of bowling into D&D and helping shape the local community in Washington State. 
He first began playing AD&D in the fourth grade.  From there he explored many of the major table top rpg systems with games like rifts, vampire the masquerade, trinity, paranoia and shadow run. Currently he works out of his home in Tacoma Washington where both he and his wife run home games of DdD 5e. Some of his influences include Neil Gaimen's American gods, Patrick Rothfuss' king killer chronicles, stories of True Crime, and others. Sadly this paragraph has a word count limit or that list would be much longers. As a DM he has been described as "Chaotic good" and is usually seen to be on the side of the player, with a preference for improv and a flair taking your actions and exaggerating their consequences.
~~~

**Claimed live evidence.** `736304203265212444` (2020-07-24, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 736304203265212444
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0073.jsonl:364 @ row sha256:3dbb12ed1c246f72c5cff4ca4939e855c4c90a042f96e22f0077db1e90137c37
- timestamp: 2020-07-24T19:30:01.929000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-24T19:29:08.906000Z | Sketchy Bee 🐝 [297577343554158603] | Would healing do literally anything at this point?? Or is it a waste of spell slots 🤔
   2020-07-24T19:29:26.130000Z | DM radar [313689699627696139] | i mean
>> 2020-07-24T19:30:01.929000Z | DM radar [313689699627696139] | stop the bleeding if you want? but im willing to hand wave because your helping a player who asked to loose a limb in glorious fashion
   2020-07-24T19:30:11.738000Z | DM radar [313689699627696139] | and that was a blast
   2020-07-24T19:30:39.580000Z | Sketchy Bee 🐝 [297577343554158603] | Wait that was *asked for??* 😂😂😂
~~~

**Representative line.** “im willing to hand wave because your helping a player who asked to loose a limb in glorious fashion”

### Mechanical warnings / lineage

- BCS-000045:L1573-L1579: ORIGINAL_REPRESENTATION_UNAVAILABLE; current support SUPPORT_NOT_FOUND; representation drift established false.
- BCS-000045:L4420-L4422: ORIGINAL_REPRESENTATION_UNAVAILABLE; current support SUPPORT_NOT_FOUND; representation drift established false.
- representative-message match: 736304203265212444
- The disputed locators were present in the first v1 Markdown commit.
- PR #2 preserved no BCS-000045 source representation at its base, first commit, or final head.
- The later preserved normalized and export representations resolve the cited coordinates to unrelated material.
- Searches of both preserved representations found no relevant limb-loss/handwave prep passage.
- Representation drift is possible in the abstract but is not established by preserved evidence.

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-005 — Do not handwave away a question that has become character arc

Legacy confidence: high.

**Situation.** A Golden Dawn character wanted painful memories removed; players asked whether the required magic could simply be handwaved.
- audit: audit:BDC-S3-005:situation
- proposition: sha256:7f9bebd28232d198c040554bd6e503d143e1a3060e98fb89e43fc57e4dc24e7c
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The request touched faction allegiance, memory, betrayal, and future identity—material with strong downstream story value.
- audit: audit:BDC-S3-005:noticed
- proposition: sha256:bcaaa2bbcb2e86e4cfa04b517acfeaef4665f496b0fdc5e385d4c343348e9da5
- semantic status: UNVERIFIED
- flags: none

**What mattered.** character continuity, faction through-line, player agency, future payoff.
- audit: audit:BDC-S3-005:values
- proposition: sha256:56d9a7d3e98a174e92bb65d9ad7567dfa03ba5d21a9a2071dc3670c6ddc9bb23
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon refused to handwave the question, called it a good arc, then narrowed the effect: the trial could be forgotten without erasing the character's allegiance; if the player still wanted to leave, that choice could be roleplayed for another reason.
- audit: audit:BDC-S3-005:intervention
- proposition: sha256:1d61c93bae4ca7cb235fdb4d681c29352bf3b90bc11def5fbb0ad7d1eaa03b34
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Observed result.** The conversation shifted from bypassing the problem to defining what the character actually wanted to forget and what consequences would remain.
- audit: audit:BDC-S3-005:observed_result
- proposition: sha256:983e5ef50836528769a173fc5a88a1ea789cef765af9183a2290c99cb7ec26a8
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** When a shortcut would erase an emerging character problem with future story value, slow down and preserve the choice-bearing part of the problem.
- audit: audit:BDC-S3-005:reusable_judgment
- proposition: sha256:1c9f39437db9f79d2dc5e13c1d147a547b42c794cc8f42c836d804681abe70b3
- semantic status: UNVERIFIED
- flags: none

**Claimed prep evidence.** BCS-000045:L1644-L1654, BCS-000045:L1688-L1693

### Prep excerpt — BCS-000045:L1644-L1654
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:4991a0c1ae1406c8d95f19b9de4b5f9490701d67c20428fdbf45f6a74b3feb8b
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Through lines for subplots:


The through line is a series of plot information to be given out in bits and pieces over the course of interaction with the players in your faction.


Golden Dawn Through Line:
        The Golden Dawn knows that the world is ending. The ancient legends have foretold that a great evil will rise from the deep and devour all things. The only way to stop this, is to perform a sacrificial ritual at a specific place of power. It looks very much like the same ritual everyone else needs to perform, but it involves sacrificing most of the the players and NPCs at the last minute. This will seal the gate with blood and stop the end of world. (But the scholars have read the prophecy wrong, and doing this ritual will actually release the evil permanently and ensure the end of the world.)
* Dharma Initiative like secret society that is attempting not to get to the New World in General, but to get to Roanoke Island specifically 
* Lovable NPC set up for betrayal.
* All members have golden/amber eyes.
~~~

### Prep excerpt — BCS-000045:L1688-L1693
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:21f9c0adc3dace593125c6f39cac31c62420c3d7ca2ebb0c50004f231a735480
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
The Golden Dawn: NPC ONLY
Week one: Filling the submarine with as many people as possible. 
Week two: Sabotage. A large number of sacrificed npcs to the deep mid voyage to ensure that Croatoan pushes the sub to Roanoke. 
Week three: Never present during hag attacks due to early warning ability.
Week four: Illuminati agent revealed amongst the uru
Week five: Illuminati ending available: All romantic couples are asked to give their first born. This resolves the immediate threat, but the child is immediately born, rapidly grows into an antichrist like figure and battles the group in place of the the deep version of croatoan.
~~~

**Claimed live evidence.** `736855826341560371` (2020-07-26, 👀 Secret societies / 👁-golden-dawn); `736856728213127258` (2020-07-26, 👀 Secret societies / 👁-golden-dawn)

### Discord evidence — 736855826341560371
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0096.jsonl:321 @ row sha256:b43dd833e2598135e68640ac3f912cbcf33520205c6ce1da4e7bd936219dc12d
- timestamp: 2020-07-26T08:01:59.119000Z
- channel: 👀 Secret societies / 👁-golden-dawn (698489628289925130)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-26T08:01:19.815000Z | bobicus [185916549066915852] | (only bards and wizards can cast modify memory, should we recruit one or are we gonna handwave that part)
   2020-07-26T08:01:23.139000Z | Eloise >:3c [260820438026813440] | "I'm telling you this know, as certain as I am about any fact of my life. I cannot do this anymore. It'd all become too much, too fast. And I'd rather not die but if forgetting isn't an option I will. I will not, cannot live with these memories."
>> 2020-07-26T08:01:59.119000Z | DM radar [313689699627696139] | (thats an interesting question. I won't hand wave. this is good arc)
   2020-07-26T08:02:36.183000Z | bobicus [185916549066915852] | "Wait until we are on the island. Grieve not the betrayer. If you wish it, we will see your desire fulfilled in six day's time."
   2020-07-26T08:02:58.981000Z | DM radar [313689699627696139] | (is web asking to forget the trial)
~~~

### Discord evidence — 736856728213127258
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0096.jsonl:347 @ row sha256:29e1df4508da2cd01f0786a245a150356e05b86349f63bcc1f25fc9df64e7147
- timestamp: 2020-07-26T08:05:34.142000Z
- channel: 👀 Secret societies / 👁-golden-dawn (698489628289925130)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-26T08:04:54.557000Z | DM radar [313689699627696139] | (the trial of rah)
   2020-07-26T08:05:07.914000Z | bobicus [185916549066915852] | (Amara and Castor know about all f our names)
>> 2020-07-26T08:05:34.142000Z | DM radar [313689699627696139] | (and player agency. they can choose their story)
   2020-07-26T08:06:07.697000Z | DM radar [313689699627696139] | im the worst
   2020-07-26T08:06:09.033000Z | DM radar [313689699627696139] | sorry
~~~

**Representative line.** “I won't hand wave. this is good arc”

### Mechanical warnings / lineage

- BCS-000045:L1644-L1654: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L1688-L1693: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 736855826341560371

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-006 — Compress low-value transit when time becomes the scarce resource

Legacy confidence: high.

**Situation.** A scene had reached the point where the party only needed to return to town, while real-world session time was running short.
- audit: audit:BDC-S3-006:situation
- proposition: sha256:0dfc3737921f80891bb35254f2a243c4bd890546f535e04d31ebe4d63b9a100f
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The trip no longer promised a meaningful choice or payoff proportional to the time it would consume.
- audit: audit:BDC-S3-006:noticed
- proposition: sha256:b5d39e6171220170a91c9ba32aff7a6b4f0eb748b3abbbeea3bf8eebf92c106d
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**What mattered.** momentum, time, scene value.
- audit: audit:BDC-S3-006:values
- proposition: sha256:91282c401a50533745bde179b4e18fc2ac85278e0f2cbe2e6ae037865d671e20
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon handwaved the trip back to town specifically for time concerns.
- audit: audit:BDC-S3-006:intervention
- proposition: sha256:9df883440e41574fdba33968e4d86fe591667ff5e0a57b77f40e5ad206ebd95b
- semantic status: UNVERIFIED
- flags: none

**Observed result.** Players immediately agreed and play moved on.
- audit: audit:BDC-S3-006:observed_result
- proposition: sha256:a903bdc39c701ec7a8a34b40b2e3a361b060c33c0daf31204ced3104f4b72894
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** Skip transitions once their remaining play value is lower than the time they consume. Persistent worlds do not require simulating every minute.
- audit: audit:BDC-S3-006:reusable_judgment
- proposition: sha256:5418dd37fabac9173cb4ac454da0cadbe020b8e39e6dec6e4eb714f5805c451d
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L4104-L4104, BCS-000045:L4124-L4124

### Prep excerpt — BCS-000045:L4104-L4104
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:b1a8b6761831bc1f8e0c50ad4789a93160b577fecda6cdac5e1f8ac2ad7cee10
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
In crafting a game to be a short term deep dive into the lives of our characters I looked at the constraints of time spent at the table together as a design choice rather than a design restriction. Time is the world's first paintbrush, sculpting mountains and spreading life all over the canvas of our lives. The average tabletop rpg session lasts 6 hours. But with Discord, the tools of a persistent play by post forum from the 90’s and players who craved those deeper stories, a new kind of storytelling emerged for us. Home games evolved into public games and the public games became an annual event.
~~~

### Prep excerpt — BCS-000045:L4124-L4124
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:23e5d7ccad92348a11000deda8d3ad6f5f6513dac4ad371c177adeb55a39bbee
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
The book is broken up chronologically to facilitate the use of a real time role play environment built that you will build on discord, roll 20, skype, or a series of home games. 
~~~

**Claimed live evidence.** `745533785805815829` (2020-08-19, cascadia / olala)

### Discord evidence — 745533785805815829
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0363.jsonl:134 @ row sha256:17f867c7915386af2ee83d6bc72af111095b1900de9d4ac741609a6ac6ca76b0
- timestamp: 2020-08-19T06:45:05.884000Z
- channel: cascadia / olala (745446932037763112)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-19T06:45:01.456000Z | Mistah Noodles [363458590461132800] | "Sound like Purse Viel wisdom.."
   2020-08-19T06:45:02.421000Z | that person logan [519566652824616973] | She giggles
>> 2020-08-19T06:45:05.884000Z | DM radar [313689699627696139] | (I'm willing to hand wave the trip back to town at this point for time concerns.)
   2020-08-19T06:45:12.052000Z | Eloise >:3c [260820438026813440] | (sounds good)
   2020-08-19T06:45:15.786000Z | that person logan [519566652824616973] | She won’t stop giggling
~~~

**Representative line.** “I'm willing to hand wave the trip back to town at this point for time concerns.”

### Mechanical warnings / lineage

- BCS-000045:L4104-L4104: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L4124-L4124: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 745533785805815829

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-007 — Let players choose the granularity of low-stakes play

Legacy confidence: high.

**Situation.** A player wanted routine healing potions while Brendon had only a few minutes available.
- audit: audit:BDC-S3-007:situation
- proposition: sha256:01d89317560c97982a7ee1bf4ee71cb0632941b2596d8e8d6905cbfa11151ddf
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The transaction mattered to inventory, but the player might or might not value the shopping interaction itself.
- audit: audit:BDC-S3-007:noticed
- proposition: sha256:63c9bc4fcab33f7d5c6584efca0fa3c44aeddb37fa9992f5f1fdb2b316b8ce22
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**What mattered.** access, player preference, time, immersion.
- audit: audit:BDC-S3-007:values
- proposition: sha256:3dbec057d1c064e01b290cff13cb8ecbc2a37ced826c993f072648c8d426e0f4
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon offered a fast handwaved purchase at listed prices now, or a full shopping interaction later.
- audit: audit:BDC-S3-007:intervention
- proposition: sha256:ab25120292c635d90358707bedd1ea680268740c9e4bff0245401297bcb6fcfb
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The player chose the simple transaction and got the items without consuming a full scene.
- audit: audit:BDC-S3-007:observed_result
- proposition: sha256:55fcce169fd94ba8d11a493a33d3d0b0c19b33f9d3a38fe377d79de9a65702b9
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Reusable judgment.** For low-stakes procedures, offer resolution at the level of detail the player actually values. Do not confuse simulation detail with roleplay quality.
- audit: audit:BDC-S3-007:reusable_judgment
- proposition: sha256:689674ed7bc8cc09ca368f64adff89a1c48c82dfd6da67fa1b6bcf1ef83036f6
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L1576-L1579

### Prep excerpt — BCS-000045:L1576-L1579
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:dc3c1a92fe4f279edb0c76f88c358ed9cf7bbb33f9a10a3fd37f4de8668d601e
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Rules as written: roanoke is a 5 week long persistent Role Play Environment that seeks to combine the improvisational storytelling ability of tabletop role playing games with the functionality and user interface of video games. This is an rp heavy town drama told in 5 acts. 


Rules as intended: roanoke is a 5 week long deep dive into the daily lives of your characters. The game is centered around staying as a group to build a town, grow in your professions overcome horrific encounters and delve into the mysteries of the secret societies to which the townsfolk belong.
~~~

**Claimed live evidence.** `735253731406381078` (2020-07-21, 🏦 Shopping / 💰-shopping-with-generous-jack)

### Discord evidence — 735253731406381078
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0041.jsonl:434 @ row sha256:46dc3d83650f2af99d865b559005bd4513f517719bb849c4723ad1b52d0ab587
- timestamp: 2020-07-21T21:55:49.921000Z
- channel: 🏦 Shopping / 💰-shopping-with-generous-jack (732919665235591169)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-21T21:15:21.441000Z | Deleted User [456226577798135808] | (Gotcha, they seem busy so I'll wait for the moment)
   2020-07-21T21:15:31.555000Z | nut_wizard [594008151779573762] | He begins to toss the dart up and down idly, except it just teleports into his hand at the zenith of each throw as he guides to the lad himself. But he's busy for now. So it takes a while.
>> 2020-07-21T21:55:49.921000Z | DM radar [313689699627696139] | I only have 6 minutes, but if you know the prices I can hand wave a little shopping to give you access. If you want a shopping trip interaction, <@&725888380331884595> a little later this afternoon.
   2020-07-21T21:56:30.960000Z | Deleted User [456226577798135808] | Just wanna get my hands on a few hp potions for backup healing
   2020-07-21T21:59:37.997000Z | DM radar [313689699627696139] | (Thats cool. Full price in pinned guide)
~~~

**Representative line.** “if you know the prices I can hand wave a little shopping... If you want a shopping trip interaction... later”

### Mechanical warnings / lineage

- BCS-000045:L1576-L1579: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: None

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-008 — Promote emergent player material into bespoke future content

Legacy confidence: high.

**Situation.** Early play was generating side relationships and situations beyond the written daily events.
- audit: audit:BDC-S3-008:situation
- proposition: sha256:2bd3d630a876ca683733e738f855750d109d8aa535ccc08d2aaedce2d7b66248
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** Some unplanned material had enough story energy to justify additional DM attention.
- audit: audit:BDC-S3-008:noticed
- proposition: sha256:57a0214fc2515c36c18f4a355bb1c63536f6e1bdb7b62a82c5b1ab25d776ee7f
- semantic status: UNVERIFIED
- flags: none

**What mattered.** emergent story, intimacy, player-created material.
- audit: audit:BDC-S3-008:values
- proposition: sha256:2e2ee3f2f23e88992de321dc84c8a6839d67cb0c2499c0525b00a87c60862572
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon first said he was considering improv sessions for things that caught his eye story-wise, then formalized DM invitationals as short one-shots initiated by players or DMs to tell unplanned stories created cooperatively.
- audit: audit:BDC-S3-008:intervention
- proposition: sha256:b3458bbe6f58d550e6f56f381f9422a07db11ed8c9deb4aa9e72b4ebcdca6d0a
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The campaign gained an explicit mechanism for converting emergent play into prepared spotlight scenes.
- audit: audit:BDC-S3-008:observed_result
- proposition: sha256:f548264da1979b44c3a7876dc217425aac381099e66a6380113df120c6ccc5ad
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** Watch for player-created details that imply more story than they currently contain. Promote the strongest into future scenes instead of trying to pre-author every worthwhile thread.
- audit: audit:BDC-S3-008:reusable_judgment
- proposition: sha256:edbdacaec6c2c33348e572030f7e786aab0c5eac3d124803265fb30301b8c49f
- semantic status: UNVERIFIED
- flags: none

**Claimed prep evidence.** BCS-000045:L1576-L1579, BCS-000045:L4420-L4422

### Prep excerpt — BCS-000045:L1576-L1579
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:dc3c1a92fe4f279edb0c76f88c358ed9cf7bbb33f9a10a3fd37f4de8668d601e
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Rules as written: roanoke is a 5 week long persistent Role Play Environment that seeks to combine the improvisational storytelling ability of tabletop role playing games with the functionality and user interface of video games. This is an rp heavy town drama told in 5 acts. 


Rules as intended: roanoke is a 5 week long deep dive into the daily lives of your characters. The game is centered around staying as a group to build a town, grow in your professions overcome horrific encounters and delve into the mysteries of the secret societies to which the townsfolk belong.
~~~

### Prep excerpt — BCS-000045:L4420-L4422
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:0bdb70355693cb1b5c759f4b27ad4b49c517c127898d536046b57b45bd0ff480
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Brendon Faulkner
The original creator of Roanoke Season One, Brendon Faulkner has decades of experience as a dungeon master. His recent accomplishments include experimenting with the form and boundaries of what Dungeons and Dragons can be, including the 24 hour format of Roanoke, a conversion of bowling into D&D and helping shape the local community in Washington State. 
He first began playing AD&D in the fourth grade.  From there he explored many of the major table top rpg systems with games like rifts, vampire the masquerade, trinity, paranoia and shadow run. Currently he works out of his home in Tacoma Washington where both he and his wife run home games of DdD 5e. Some of his influences include Neil Gaimen's American gods, Patrick Rothfuss' king killer chronicles, stories of True Crime, and others. Sadly this paragraph has a word count limit or that list would be much longers. As a DM he has been described as "Chaotic good" and is usually seen to be on the side of the player, with a preference for improv and a flair taking your actions and exaggerating their consequences.
~~~

**Claimed live evidence.** `734702546639257610` (2020-07-20, 🗨 Social / 🙋-out-of-character); `735402532171677767` (2020-07-22, ❄ Things you should read. / ❕announcements)

### Discord evidence — 734702546639257610
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0022.jsonl:494 @ row sha256:a35e418e9f959295d92a9a183bd69115e3b0b4116bcaecfaf13e87864cec0678
- timestamp: 2020-07-20T09:25:37.232000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-20T09:25:11.578000Z | DM radar [313689699627696139] | I'm up late anyways.
   2020-07-20T09:25:30.299000Z | DCJJ [629235245291667476] | Haha, what is sleep anyways?
>> 2020-07-20T09:25:37.232000Z | DM radar [313689699627696139] | I'm considering improv sessions if I find things that catch my eye story wise.
   2020-07-20T09:26:21.108000Z | DCJJ [629235245291667476] | Haha, why did my comment get the middle finger?
   2020-07-20T09:26:35.955000Z | DM radar [313689699627696139] | thats the pointer finger.
~~~

### Discord evidence — 735402532171677767
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0047.jsonl:143 @ row sha256:e36dd4070a59a915523d788b0589f925edc259734951ebdc0d49e468a648718f
- timestamp: 2020-07-22T07:47:06.788000Z
- channel: ❄ Things you should read. / ❕announcements (734250210057912344)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-22T07:37:21.273000Z | Nobleindie [361351593292988425] | @everyone  The inky black depths of the the Night Time Thames River:  A ship with no crew, encrusted with ice and salt sails itself into the port of London. The Irish have arrived. Beware the wrath of a prankster god named Lugh, trickster of the Irish Isle.
>> 2020-07-22T07:47:06.788000Z | DM radar [313689699627696139] | Starting tomorrow DM invitationals are back. This is a system we use for the DM's to improv and tell more intimate stories. These may be initiated by either players or DMs, resulting in a shorter one-shot with which we can tell the unplanned stories based on the things that we are cooperatively creating. Typically a dm will approach a player (and though you are free to request them, there are many reasons why we might have to say "no") They will then tell them how many people to invite, and set a date and time. @everyone
   2020-07-22T09:45:01.147000Z | DM radar [313689699627696139] | @everyone your mouth tastes like pillow. Roll a d2. On one, you catch yourself before you swallow. On two, you have consumed some of your pillow. Brush your teeth or risk mouth lice.
   2020-07-22T15:10:18.270000Z | ✨Fuddles✨ [403783497564684291] | @everyone You awaken to a plague of roosters who wont shut up. They aren’t cawing, They are telling you you should have tried harder to prevent that thing you are embarrassed about. This is not the bluebird of happiness. This is the chicken of depression.
~~~

**Representative line.** “improv sessions if I find things that catch my eye story wise”

### Mechanical warnings / lineage

- BCS-000045:L1576-L1579: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L4420-L4422: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 734702546639257610

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-009 — Reduce authored density as campaign history becomes richer

Legacy confidence: high.

**Situation.** The written document still contained a day-by-day Week 5 spine, but four weeks of actual play had produced player priorities, unfinished business, and invitationals.
- audit: audit:BDC-S3-009:situation
- proposition: sha256:d5ee8142f725616973bf69a8253b63b94fc8ff219e6b10b4a4324b147fab397b
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** Accumulated live history had become a better source of relevant content than filling every remaining day with fixed authored material.
- audit: audit:BDC-S3-009:noticed
- proposition: sha256:e61e7cfee7035b4441540cb9f9072a13e858a304a3593d249c82e1bdcd2128ba
- semantic status: UNVERIFIED
- flags: none

**What mattered.** player-led payoff, responsiveness, finale structure.
- audit: audit:BDC-S3-009:values
- proposition: sha256:7a964383c58395adb92746d4a761cb875285e54f2aec5e936e081ac82e890800
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon asked players to DM what they wanted to explore or accomplish and stated that Week 5 was deliberately less written so players could lead and DMs could accommodate more invitationals, while retaining selected major fights.
- audit: audit:BDC-S3-009:intervention
- proposition: sha256:f4ec35a95cdc87e9278299eebab97ee2c9ab2fd8e0bdd4a1d4bd05bfb1cd206e
- semantic status: UNVERIFIED
- flags: none

**Observed result.** Players were later given a menu of outstanding goals and asked to set priorities rather than being marched through a complete fixed schedule.
- audit: audit:BDC-S3-009:observed_result
- proposition: sha256:89ea1900ce3fa880cb16678037d1ae06636e2a1b36dd22bab63b9d39f413be0d
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** Front-load structure when campaign history is thin. As meaningful history accumulates, leave increasing prep capacity available to answer what actually happened.
- audit: audit:BDC-S3-009:reusable_judgment
- proposition: sha256:5f586ef37a9fbe6566a0026f4656919892cdda9cc40b68729beaceb5d091f27c
- semantic status: UNVERIFIED
- flags: none

**Claimed prep evidence.** BCS-000045:L1569-L1587, BCS-000045:L1880-L1884, BCS-000045:L2840-L2856

### Prep excerpt — BCS-000045:L1569-L1587
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:ced710cac7d12db4243251de1c4515d51d7bea34a29aff6247fe689b9c512861
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Tentative Game Play dates: Saturday July 18th 2020- August 21st. [b]
The purpose of this document is to outline season 3 of Roanoke.


What roanoke is:


Rules as written: roanoke is a 5 week long persistent Role Play Environment that seeks to combine the improvisational storytelling ability of tabletop role playing games with the functionality and user interface of video games. This is an rp heavy town drama told in 5 acts. 


Rules as intended: roanoke is a 5 week long deep dive into the daily lives of your characters. The game is centered around staying as a group to build a town, grow in your professions overcome horrific encounters and delve into the mysteries of the secret societies to which the townsfolk belong.


Settings: 
* Week one: London, England. In a fantasy reimagining of Europe.
* Week two: Gnerman Submarine. A voyage across the Atlantic.
* Week three: The Stillwater
* Week four: The Darkwater 
* Week five: The Aether
~~~

### Prep excerpt — BCS-000045:L1880-L1884
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:acee97c2aeb9ca445de369c9e017b3385a218c2afca914b07e56ebff106cc733
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Game breakdown by day:
* Launch Party/0 session irl.
Opening day: The Pall Mall Reform Club.
Day 2. 7/19/20 An Arcanian Werewolf in London-Golden Dawn into.
                Golden Dawn NPC introduced
~~~

### Prep excerpt — BCS-000045:L2840-L2856
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:b5eae6a690bb12cc6e94659d6257abab24941c79e23540cfb820b7d883591f36
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Day 29 Aether begins: Island returns to normal water level. Final lodestone summoning ritual.
Day 30 A Meteorite of lodestone is summoned to roanoke to complete the Aether ritual.
Basic Concept: A spell jammer ship whose engine is made of loadstone crashes to the island, bringing with it a bunch Thri Kreen crew, a bunch of Giant Space Hamsters and a ship containing the elder brain orphan raised by the crew. The Elder brain (a good guy npc for our purposes) warns the group that they have been spotted by another ship. A ship of Illithids are chasing them, attempting to reclaim or destroy the elder brain. 


Pilot the spell jammer airship in battle against the Mindflayer bad guys in an action packed adventure. 


Upon the successful destruction of the illithid ship, the thri kreen crew’s ship also crash lands. 


The ship you are piloting can donate its lodestone engine to the island, they will use the rest of the parts to repair the illithid’s much better ship to return to space. 
Day 31 Ossuary opened. The Tinker’s story is told.
Day 32 The legend of the tinker
Day 33 The tinkers return.
Day 34 The infernal well.
Day 35 The Hunger Voice Event.
~~~

**Claimed live evidence.** `742807517721133056` (2020-08-11, 🗨 Social / 🙋-out-of-character); `742807774383046666` (2020-08-11, 🗨 Social / 🙋-out-of-character); `743577911834968166` (2020-08-13, ❄ Things you should read. / ❕announcements); `745130263914479756` (2020-08-18, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 742807517721133056
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0280.jsonl:472 @ row sha256:f546c34b72eb86dfa5f16ec00f2a0405be95af56a360a24dcb5f3d92ff2f5233
- timestamp: 2020-08-11T18:11:52.921000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-11T18:09:27.948000Z | DM radar [313689699627696139] | Today is a day of environmental factors. I'm not going to be running a main event perse. There are a few ways I can see it going. If the town decided to focus on internal problems, an internal problem will arise. If instead they choose to focus on external problems, then that is where the focus will be. Also there is some chadding that needs to be done.
   2020-08-11T18:10:52.469000Z | DM radar [313689699627696139] | Either way, I'm probably going to be on an off sporadically as some of my attention needs to be on my kid.
>> 2020-08-11T18:11:52.921000Z | DM radar [313689699627696139] | What I need from the group going forward is dms about things you wish to explore or accomplish
   2020-08-11T18:12:02.749000Z | DM radar [313689699627696139] | especially when we move into week 5
   2020-08-11T18:12:54.114000Z | DM radar [313689699627696139] | The game is far less written in week 5 to let the players lead more and the dms to be able to accommodate more invitationals
~~~

### Discord evidence — 742807774383046666
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0280.jsonl:475 @ row sha256:41450876bd9b2b6e17d8f6d8ece5afab9fdee6e16978ccb0081706da30bf0d52
- timestamp: 2020-08-11T18:12:54.114000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-11T18:11:52.921000Z | DM radar [313689699627696139] | What I need from the group going forward is dms about things you wish to explore or accomplish
   2020-08-11T18:12:02.749000Z | DM radar [313689699627696139] | especially when we move into week 5
>> 2020-08-11T18:12:54.114000Z | DM radar [313689699627696139] | The game is far less written in week 5 to let the players lead more and the dms to be able to accommodate more invitationals
   2020-08-11T18:13:16.252000Z | hekiryuu [237577351532249110] | spaaaaaaaace
   2020-08-11T18:13:19.524000Z | hekiryuu [237577351532249110] | jk
~~~

### Discord evidence — 743577911834968166
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0304.jsonl:94 @ row sha256:0d979491d3ea425e2310c9857e6b69923b6e05a1ba16cc8e8ebb389a8dde054b
- timestamp: 2020-08-13T21:13:09.191000Z
- channel: ❄ Things you should read. / ❕announcements (734250210057912344)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-13T19:09:40.408000Z | Noah [360967589511561218] | @everyone One of the most difficult fights yet is on the island for the event tonight. The stakes are high. If the party fails, it will mean the likely death of Mello along with other bad things. Please pre-roll initiative in <#735293812775321650> if you are joining. <@&725888380331884595> please organize it before the event tonight to help us run smoothly.
>> 2020-08-13T21:13:09.191000Z | DM radar [313689699627696139] | @everyone Hell week is almost over. You have done well to make it this far. Next week will be a lot more player led, (I mean, I still have some very bdfm and noah fights planned for you all, but it should be a bit less intense.) Band together. And prepare all that you can for the final fight. It will be the most epic battle we have ever put before you in Roanoke. Tonight and Tomorrow will be rough, but I know you can get through it.
~~~

### Discord evidence — 745130263914479756
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0350.jsonl:480 @ row sha256:6a6c389b532d16dec5a964365ea95f559cca447a3094da27969b2000eb77b54f
- timestamp: 2020-08-18T04:01:38.768000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-18T03:52:26.659000Z | Eloise >:3c [260820438026813440] | I ain't gonna say it here. Is secrets
   2020-08-18T03:52:40.606000Z | Nobleindie [361351593292988425] | join vc
>> 2020-08-18T04:01:38.768000Z | DM radar [313689699627696139] | <@&645664646254297145> Tomorrow is an invitational day. Time to check those to-dos off.  Puckwudgie hunt visit the fishmother the hatch An adventure to another place in arcania - cascadia (longer adventure) Visit the uru to look for the hermit Visit dregen set your priorities and let me know
   2020-08-18T04:01:52.563000Z | DM radar [313689699627696139] | I'm sure noah has more too
   2020-08-18T04:02:53.064000Z | schrödingers dumbass [264570136025890816] | I must fishmother, hatch,  uru
~~~

**Representative line.** “The game is far less written in week 5 to let the players lead more”

### Mechanical warnings / lineage

- BCS-000045:L1569-L1587: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L1880-L1884: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L2840-L2856: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 742807774383046666

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-010 — Use collective attention to select which pressure becomes foreground

Legacy confidence: high.

**Situation.** Roanoke contained simultaneous internal political problems and external threats, and Brendon was not running a single fixed main event that day.
- audit: audit:BDC-S3-010:situation
- proposition: sha256:72f8bd1a365d5936cb2bdff06971e0cd6008376669832c2b01c02ba4fa416196
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**What Brendon noticed.** The group had already generated competing priorities through earlier decisions.
- audit: audit:BDC-S3-010:noticed
- proposition: sha256:c4223221d55d9ca117eb84803fb14b51ea5c61ef6616f3cadc81d2e46a1a510d
- semantic status: UNVERIFIED
- flags: none

**What mattered.** consequences, collective attention, world responsiveness.
- audit: audit:BDC-S3-010:values
- proposition: sha256:13322489fde0bfbd111737de523f7fdf46526823762091c62fd0d1b9406d41fb
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon stated that if the town focused on internal problems, an internal problem would arise; if it focused externally, the day's pressure would emerge there instead.
- audit: audit:BDC-S3-010:intervention
- proposition: sha256:63996510072314dc6f922d45446485e3145d8b161d76a72a711636139e9560b9
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The group's own focus became the selector for which prepared pressure moved on-screen.
- audit: audit:BDC-S3-010:observed_result
- proposition: sha256:6b431aac787e86d8cd005db651dc5bdba6c6120b604317f78b3de444edd49fb7
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** When several legitimate pressures exist, let sustained player attention decide which becomes foreground. Do not force every prepared problem onto the stage at once.
- audit: audit:BDC-S3-010:reusable_judgment
- proposition: sha256:811f2e53fc72c2e9cb3490113b9a695e6def087ae4e317912a68d1cb76d2f7c2
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L1630-L1636, BCS-000045:L2821-L2838

### Prep excerpt — BCS-000045:L1630-L1636
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:2d38d4fa586c9b81fb6ddfeefcb0324474e0a2f067da879312b5fe11a2808360
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
The Island appears to be devoid of life save for the coven of hags.


Hags have actually driven the other races into hiding.


Once the hag coven is ended, a decades old conflict between Uru (death worshiping vulture people) and The Chinnokin (Ancient Guardians of the sea) erupts on the island. Both sides start out as hostile to the group. The Chinnokin are attempting to prevent the Deep from rising. The Chinnokin are giving the dead to the deep rather than consuming them. Croatoan has taken the form of something from beneath the waves because it benefits from the motes of divinity that the Uru have been delivering to the deep. 
~~~

### Prep excerpt — BCS-000045:L2821-L2838
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:b1b223f0ed49c934d3cfd8ac21cece9854a0b529111d2880f6e685363cf95c7b
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Day 19 Water Rising, TBD Chinnokin Encounter, Storm's A Brewin', Destruction of tree
All water turns dark. It has a metallic taste but does not have any other negative effects. Visibility underwater is cut in half. The Archivist pushes his agenda forward by suggesting that the lode stones should be activated to raise the island.
Day 20 Voting begins, Jackalope Plague.
Uru Cadaver Collector. Cadaver Collecter is picking up all of the dead jackalopes to bring to the ocean. 
Day 21 Voting ends. Hags
After the vote, there is a huge party in town to celebrate 
Day 22  
Mumford shows the tatankan plight.
        
Day 23 Hags  Voice Event voting end.
Day 24 Driftwood regatta
        Deathrace 2000 inspired shark chariot races for chinnokin breeding rights.
Day 25
Day 26 Jersey Devil
Parchtongue dries the lake.
Day 27 High water Mark Krynn Dungeon Crawl Mcguffin Hunt
Basic concept. Jousting on the back of metallic dragons against chromatic dragons. 
Day 28 Levialich voice event
~~~

**Claimed live evidence.** `742806909660168193` (2020-08-11, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 742806909660168193
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0280.jsonl:463 @ row sha256:30fdd8f276587cf90b948d676b619d3e4875a16505174941c2809f98016835a8
- timestamp: 2020-08-11T18:09:27.948000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-11T18:05:32.977000Z | Aerith [260949833773219840] | Yus. Just how I like it
   2020-08-11T18:06:29.961000Z | hekiryuu [237577351532249110] | Honestly, this has been a good day for gil, as he has put a lot of obligation he was internalizing on others to have to deal with
>> 2020-08-11T18:09:27.948000Z | DM radar [313689699627696139] | Today is a day of environmental factors. I'm not going to be running a main event perse. There are a few ways I can see it going. If the town decided to focus on internal problems, an internal problem will arise. If instead they choose to focus on external problems, then that is where the focus will be. Also there is some chadding that needs to be done.
   2020-08-11T18:10:52.469000Z | DM radar [313689699627696139] | Either way, I'm probably going to be on an off sporadically as some of my attention needs to be on my kid.
   2020-08-11T18:11:52.921000Z | DM radar [313689699627696139] | What I need from the group going forward is dms about things you wish to explore or accomplish
~~~

**Representative line.** “If the town decided to focus on internal problems, an internal problem will arise.”

### Mechanical warnings / lineage

- BCS-000045:L1630-L1636: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L2821-L2838: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 742806909660168193

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-011 — Accommodation stops when the DM starts taking over the player's fun

Legacy confidence: medium-high.

**Situation.** Players were joking that creating the dating-sim layer was their job, while Brendon was excitedly offering to build more of it.
- audit: audit:BDC-S3-011:situation
- proposition: sha256:614a6051304d2dfd924a5c2656d6999e7ae194d48e267122c3f1c2bb260c77c0
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** His instinct to accommodate could cross from enabling player play into authoring the activity for them.
- audit: audit:BDC-S3-011:noticed
- proposition: sha256:4575f5d66de86f0431d6bce2466222bf66886d7b06aa151d52f3352859ae2a40
- semantic status: UNVERIFIED
- flags: none

**What mattered.** player ownership, DM enthusiasm, restraint.
- audit: audit:BDC-S3-011:values
- proposition: sha256:6d4028c5d2dedcd6740297a90518896ae413af07610a7851619aeeadd4a8fc02
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon explicitly caught himself and backed off: player agency came first, and he recognized that excitement to accommodate was driving the overreach.
- audit: audit:BDC-S3-011:intervention
- proposition: sha256:b218955cef9551268c862882b6300076686371ead32bb17e4022160ae332f1ae
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The players retained ownership of the emergent dating-sim behavior.
- audit: audit:BDC-S3-011:observed_result
- proposition: sha256:1192136d0565ea51e0f9716308037d98cd1eae9132f1b61429589e2c6400e425
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** Accommodation is not automatically good. If helping starts replacing the player's authorship of the thing they enjoy doing, stop helping and give it back.
- audit: audit:BDC-S3-011:reusable_judgment
- proposition: sha256:5ec945f73ffacb977b023e815655ec0cd0a4f1d70999da0cb18696da5b82d423
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L4420-L4422

### Prep excerpt — BCS-000045:L4420-L4422
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:0bdb70355693cb1b5c759f4b27ad4b49c517c127898d536046b57b45bd0ff480
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Brendon Faulkner
The original creator of Roanoke Season One, Brendon Faulkner has decades of experience as a dungeon master. His recent accomplishments include experimenting with the form and boundaries of what Dungeons and Dragons can be, including the 24 hour format of Roanoke, a conversion of bowling into D&D and helping shape the local community in Washington State. 
He first began playing AD&D in the fourth grade.  From there he explored many of the major table top rpg systems with games like rifts, vampire the masquerade, trinity, paranoia and shadow run. Currently he works out of his home in Tacoma Washington where both he and his wife run home games of DdD 5e. Some of his influences include Neil Gaimen's American gods, Patrick Rothfuss' king killer chronicles, stories of True Crime, and others. Sadly this paragraph has a word count limit or that list would be much longers. As a DM he has been described as "Chaotic good" and is usually seen to be on the side of the player, with a preference for improv and a flair taking your actions and exaggerating their consequences.
~~~

**Claimed live evidence.** `736688057113378928` (2020-07-25, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 736688057113378928
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0086.jsonl:450 @ row sha256:370211afd4581f72fe65b0631e72ec3f3535520e251411b8990a5be4e5dc54f6
- timestamp: 2020-07-25T20:55:19.818000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-25T20:54:43.773000Z | nut_wizard [594008151779573762] | no no no keep doing what you're doing
   2020-07-25T20:54:48.726000Z | nut_wizard [594008151779573762] | the dating sim is _our_ job
>> 2020-07-25T20:55:19.818000Z | DM radar [313689699627696139] | right. sorry. player agency. I just get excited trying to accommodate.
   2020-07-25T20:55:20.960000Z | izar [566079740591603714] | Yep
   2020-07-25T20:55:24.296000Z | justjack420 [592252026226999306] | I ship <@313689699627696139> and <@360967589511561218>
~~~

**Representative line.** “right. sorry. player agency. I just get excited trying to accommodate.”

### Mechanical warnings / lineage

- BCS-000045:L4420-L4422: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 736688057113378928

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-012 — Consent boundaries remove some actions from adjudication entirely

Legacy confidence: high.

**Situation.** PvP conflict emerged in a persistent social game where players could otherwise attempt many actions.
- audit: audit:BDC-S3-012:situation
- proposition: sha256:eb2e0de99105ecaf0d0a1e16a01654f8d77c4761f569b801c02116f16fbd0d0e
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** Treating unwanted PvP as an ordinary contested check would make a safety boundary depend on dice.
- audit: audit:BDC-S3-012:noticed
- proposition: sha256:7bc336787642eb824361bdee7296a7bd25bc3e8bdfcb02c4ba6cfeb29a2a4ea1
- semantic status: UNVERIFIED
- flags: none

**What mattered.** consent, player control, fair adjudication.
- audit: audit:BDC-S3-012:values
- proposition: sha256:4186edb600faba0f4daca2f80d0eb5808a3c7279cf6f3f75b2a206d95429474e
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon established that PvP required both players' consent plus a DM, then later applied the rule by refusing even to roll whether one PC could physically stop another when consent had not been granted.
- audit: audit:BDC-S3-012:intervention
- proposition: sha256:c85ac8bf542932019103f6dbe31386068f98bb40a2a85241f457cb1b7069761c
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Observed result.** The scene proceeded through allowed actions such as following rather than converting the dispute into unauthorized PvP.
- audit: audit:BDC-S3-012:observed_result
- proposition: sha256:0bc86042853576a7be3fb8652fd1a490ca4c74325a96df9445d383a53eb10709
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** Some table boundaries are preconditions for adjudication, not modifiers to it. If consent is absent, do not roll to see whether the prohibited interaction happens.
- audit: audit:BDC-S3-012:reusable_judgment
- proposition: sha256:5fa252f259c530ee4f5ef0bd057be626ca45df50e239e8926e470b40d34eb4d9
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L1576-L1579

### Prep excerpt — BCS-000045:L1576-L1579
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:dc3c1a92fe4f279edb0c76f88c358ed9cf7bbb33f9a10a3fd37f4de8668d601e
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Rules as written: roanoke is a 5 week long persistent Role Play Environment that seeks to combine the improvisational storytelling ability of tabletop role playing games with the functionality and user interface of video games. This is an rp heavy town drama told in 5 acts. 


Rules as intended: roanoke is a 5 week long deep dive into the daily lives of your characters. The game is centered around staying as a group to build a town, grow in your professions overcome horrific encounters and delve into the mysteries of the secret societies to which the townsfolk belong.
~~~

**Claimed live evidence.** `735726761437823086` (2020-07-23, 🗨 Social / 🙋-out-of-character); `737751675762114581` (2020-07-28, 🚢 Week two, The Tir Na Nog / 🔭-the-observation-deck)

### Discord evidence — 735726761437823086
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0057.jsonl:14 @ row sha256:af2eae3696221ecbde4f907afe7d4a02c8f60b4c5185fe17a503fe0a6e2149c2
- timestamp: 2020-07-23T05:15:29.069000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-23T05:14:06.655000Z | KnightOfCydonia [436232470242000916] | ^that is correct
   2020-07-23T05:15:25.542000Z | Sketchy Bee 🐝 [297577343554158603] | In game the roofgang feels a bit... Displaced and is now on the red road instead.
>> 2020-07-23T05:15:29.069000Z | DM radar [313689699627696139] | ok. So. There is a clear rule that I'd like to restate. The rule is that there is no PVP with out a dm. That means with out a DM's consent. If there is a fight that is to be resolved between two parties by combat, that is something that we accommodate. But not with out consent from both players and a dm.
   2020-07-23T05:18:41.328000Z | DM radar [313689699627696139] | Additionally. I'm a little disappointed that players were pressuring other players to play in a way that they didn't want to. I understand the joy of trying to get others to come play. But consent is more than just a consideration. No means no.
   2020-07-23T05:22:03.671000Z | DM radar [313689699627696139] | Very early this morning I blessed the roof tops with tea lights to show that I deemed it a safe zone from shenanigans. Even mine.
~~~

### Discord evidence — 737751675762114581
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0125.jsonl:211 @ row sha256:ccfb8c84a0433a1990dad4c76888433e94800dbd7b12baa17f087fa64d3b6bcf
- timestamp: 2020-07-28T19:21:46.265000Z
- channel: 🚢 Week two, The Tir Na Nog / 🔭-the-observation-deck (636019335231569940)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-28T19:20:10.763000Z | AlfaMuffin [176404876983664640] | (And they can ask their questions, never agreed to stick around)
   2020-07-28T19:21:17.357000Z | Sketchy Bee 🐝 [297577343554158603] | (I told Trax to be ready for something like this. Plans have changed a bit but does that still apply?)
>> 2020-07-28T19:21:46.265000Z | DM radar [313689699627696139] | (I have to obey player agency. PvP was not granted for anything other than casting. I can't roll to let you stop him. No rolls to stop him, but following is not pvp.)
   2020-07-28T19:22:21.073000Z | AlfaMuffin [176404876983664640] | The moment Goan is out of the door:
   2020-07-28T19:22:24.413000Z | KnightOfCydonia [436232470242000916] | Castor follows Goan "Everyone lets go"
~~~

**Representative line.** “I can't roll to let you stop him. No rolls to stop him, but following is not pvp.”

### Mechanical warnings / lineage

- BCS-000045:L1576-L1579: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 737751675762114581

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-013 — Stop using DM knowledge when it starts choosing a player's story

Legacy confidence: high.

**Situation.** Brendon was helping reason through who could serve as a witness in a conspiracy/trial thread and realized his DM knowledge could determine another player's involvement.
- audit: audit:BDC-S3-013:situation
- proposition: sha256:3b08c0a82e3e84fe950672c2a0e8d58c549448ec8bd99cc0f78dad1a99abad19
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** His meta-level problem solving was starting to substitute for the player's own decision.
- audit: audit:BDC-S3-013:noticed
- proposition: sha256:875f0fc8004710c86f62a830f6afd006ebe225ac018a7405139980e0c2eeb89b
- semantic status: UNVERIFIED
- flags: none

**What mattered.** agency, information boundaries, immersion.
- audit: audit:BDC-S3-013:values
- proposition: sha256:2275f9798e06388d82fbdc4630f45180e6f9bb0088aa2431f185a250ae6113ed
- semantic status: UNVERIFIED
- flags: none

**Intervention.** He stopped the meta-solving, explicitly called it a slippery slope, and put the choice to Web's player instead.
- audit: audit:BDC-S3-013:intervention
- proposition: sha256:ed9d2c8f51f42f5050d164b543e39cf43868fc3ada2a4555c2ab67796c3dea84
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The player answered for the character and the channel returned to RP-only mode.
- audit: audit:BDC-S3-013:observed_result
- proposition: sha256:0d8e9835c686de6d0dde7d5ca8d076db7f153783955e8b0730e98358fd802247
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** Use DM knowledge to maintain the world, not to solve player decisions. When you notice yourself optimizing a player's move from behind the screen, hand the decision back.
- audit: audit:BDC-S3-013:reusable_judgment
- proposition: sha256:ffac88bd0f6943e94226a37e81ae484038b4a3149b3de1b3270c58b7eca80b65
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L1644-L1647

### Prep excerpt — BCS-000045:L1644-L1647
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:aa2b57c5ca29af26214b3ff6f677ead4c7ceb072387946d9b45f32c67ac50c3e
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Through lines for subplots:


The through line is a series of plot information to be given out in bits and pieces over the course of interaction with the players in your faction.
~~~

**Claimed live evidence.** `737569808396058654` (2020-07-28, 👀 Secret societies / 👁-golden-dawn)

### Discord evidence — 737569808396058654
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0121.jsonl:456 @ row sha256:38516c391124957e92f967c57c8dba6facf206b31a07b2aee2875935fa6fbd9f
- timestamp: 2020-07-28T07:19:05.706000Z
- channel: 👀 Secret societies / 👁-golden-dawn (698489628289925130)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-07-28T07:17:44.355000Z | DM radar [313689699627696139] | (or is this breaking immersion. does Amara know much about web? Your call)
   2020-07-28T07:18:26.877000Z | Nobleindie [361351593292988425] | (She knows something is off about them)
>> 2020-07-28T07:19:05.706000Z | DM radar [313689699627696139] | (lets let web have some player agency I'm meta gaming and its a slippery slope)
   2020-07-28T07:19:06.621000Z | Nobleindie [361351593292988425] | (Like they said she didn't know I was even in the group. Amara knows web thinks they is a real member.)
   2020-07-28T07:19:35.916000Z | bobicus [185916549066915852] | (another option is discrediting Wynne with Copper)
~~~

**Representative line.** “lets let web have some player agency I'm meta gaming and its a slippery slope”

### Mechanical warnings / lineage

- BCS-000045:L1644-L1647: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 737569808396058654

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-014 — A cool image is insufficient reason to break established play

Legacy confidence: high.

**Situation.** A player proposed stacking effects to create a visually spectacular oversized battlefield creature.
- audit: audit:BDC-S3-014:situation
- proposition: sha256:34e102d05b75ddd1616361c989b2770742d6b649cdf0d6caf8b3a7a547b804c5
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The proposal was exciting but its mechanical implications were unclear and approving it would change precedent.
- audit: audit:BDC-S3-014:noticed
- proposition: sha256:1b51728946da0b9de7bafdcf665ab327ea14afdc40c590d041db567bd6774a69
- semantic status: UNVERIFIED
- flags: none

**What mattered.** coherence, rules consistency, co-DM alignment, player creativity.
- audit: audit:BDC-S3-014:values
- proposition: sha256:b4abda72ac597fd443291bf359d9a9a38dfcdfd4364994266d9af7fd792c1c06
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon expressed enthusiasm for the image but withheld approval pending rules research and Noah's input, weighting the answer toward no because it conflicted with established gameplay.
- audit: audit:BDC-S3-014:intervention
- proposition: sha256:cef98edc51e83738bd8c7acf3e28342405d8ca580da0f6778e01624076befa7b
- semantic status: UNVERIFIED
- flags: CAUSALITY_CLAIM, NEGATIVE_OR_ABSENCE_CLAIM

**Observed result.** The player accepted the ruling without the cool idea being treated as automatically valid.
- audit: audit:BDC-S3-014:observed_result
- proposition: sha256:c141b2472fba8047b0dd7e200139440bb1075724c4eb10b682980f6b5dad750d
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Reusable judgment.** Reward creativity by seriously considering it, not by automatically approving it. Check implications, precedent, and shared-GM consistency before changing the world to fit the image.
- audit: audit:BDC-S3-014:reusable_judgment
- proposition: sha256:a9b0786338c5983d5d2d845aa1d73372be0f617dce471219fe328369b0b9812d
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L1576-L1579

### Prep excerpt — BCS-000045:L1576-L1579
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:dc3c1a92fe4f279edb0c76f88c358ed9cf7bbb33f9a10a3fd37f4de8668d601e
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Rules as written: roanoke is a 5 week long persistent Role Play Environment that seeks to combine the improvisational storytelling ability of tabletop role playing games with the functionality and user interface of video games. This is an rp heavy town drama told in 5 acts. 


Rules as intended: roanoke is a 5 week long deep dive into the daily lives of your characters. The game is centered around staying as a group to build a town, grow in your professions overcome horrific encounters and delve into the mysteries of the secret societies to which the townsfolk belong.
~~~

**Claimed live evidence.** `746496793772163183` (2020-08-21, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 746496793772163183
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0387.jsonl:441 @ row sha256:20541d2be09adc2a2ea0875a7bbee880cc507127e028b81de07c2ce98c191148
- timestamp: 2020-08-21T22:31:44.875000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-21T22:30:20.066000Z | Mistah Noodles [363458590461132800] | Meteorite of the Kaiju
   2020-08-21T22:30:30.292000Z | DM radar [313689699627696139] | lolol
>> 2020-08-21T22:31:44.875000Z | DM radar [313689699627696139] | i want the image. but i'd need to read up to know what the implications of a creature that big on the battlefield would be, also it would be a rule change inconsistent with established game play so I can't say yes with out talking to noah. I love the flavor but this is a maybe weighted with a probably no.
   2020-08-21T22:32:18.805000Z | Mistah Noodles [363458590461132800] | I understand. I shall proceed to pray.
   2020-08-21T22:32:26.509000Z | DM radar [313689699627696139] | lolol
~~~

**Representative line.** “I love the flavor but this is a maybe weighted with a probably no.”

### Mechanical warnings / lineage

- BCS-000045:L1576-L1579: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 746496793772163183

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-015 — When danger lands wrong, fix the telegraph before erasing the consequence

Legacy confidence: high.

**Situation.** A dangerous sequence caused distress, and players questioned whether the campaign's pressure was becoming harmful or unfair.
- audit: audit:BDC-S3-015:situation
- proposition: sha256:c6c398a7a92393f4de3abfc8cbfdb95973143e645453e511b4f52c5ea8c1668d
- semantic status: UNVERIFIED
- flags: CAUSALITY_CLAIM

**What Brendon noticed.** The danger itself fit the campaign's intended pressure, but the fictional signaling had not made the lethality legible enough.
- audit: audit:BDC-S3-015:noticed
- proposition: sha256:7fd25a3617f81898559595de1b02411b5ec4500365f756ed914be3950f76c4a0
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**What mattered.** challenge, trust, telegraphing, player experience.
- audit: audit:BDC-S3-015:values
- proposition: sha256:1c8a19ef4cb67ebe7e79b592e56d4d2a354e8628cd3e248182cc42666c533eaf
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon kept the legitimate consequence, acknowledged that he should have signaled the danger better through RP, and shifted to transparent discussion of intent.
- audit: audit:BDC-S3-015:intervention
- proposition: sha256:344861d9e77ad8e90b6fb43f38b441d35919b3f1d656cf2ab21a7d7e7419ccd1
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The conversation moved from arguing the outcome toward rebuilding trust and clarifying what kind of pressure the campaign was trying to create.
- audit: audit:BDC-S3-015:observed_result
- proposition: sha256:9d8105b21d9885c55c082ae83ab0671efb81d427110bfd590de6c5c80e2ad16f
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** If a dangerous outcome surprises players for the wrong reason, diagnose the information failure. Improve future telegraphing before deciding that the consequence itself must be undone.
- audit: audit:BDC-S3-015:reusable_judgment
- proposition: sha256:ba26f5f1c47c7ef277f018ff7acfd3eb613f2c83a41b6f5e7c2099d78bf3928a
- semantic status: UNVERIFIED
- flags: none

**Claimed prep evidence.** BCS-000045:L4113-L4124

### Prep excerpt — BCS-000045:L4113-L4124
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:a7e522893409b856f289825a326476e9331ef07227010d2e099978eb92b18ed6
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
The Thames is full of boats bringing in goods, and full of refuse being washed away from the city’s masses. The constant grey skies shade every shadow a little deeper. The fog would have been enough to obscure the faces of those unlucky enough to be on foot rather than riding carriages. However the plague masks worn by the populace guarantee nearly constant anonymity. 


A world of secrets and fear. Our version of London is a mixture of Gothic Horror and SteamPunk. But, besides the physical look of the city and tropes and features we have all come to expect, the city performs the function of raising the tension amongst the group. It should always feel for the first week of play as if the city itself is struggling to keep you from moving forward, from seeing the whole picture, and from seeing the real terrors that it veils. The London fog and the fear of the plague has led to a population rocked fear and ripe with opportunities for scandal. While riding through the streets in a carriage full of wealthy masked aristocrats you hear a sound. Was that a bump in the road? Or did someone sneeze? It is well known that sneezing is the first sign that you might be one of the afflicted. Do you acknowledge the sneeze and therefore the short life expectancy of your carriage mate? Do you risk speaking to them? What if they struggle to make themselves heard and in so doing take off their mask


Text like this:
The Pall Mall Red Road is laid out through London like a red carpet leading straight to the gates of Buckingham.
Is meant to be copied and pasted to the players.  


The book is broken up chronologically to facilitate the use of a real time role play environment built that you will build on discord, roll 20, skype, or a series of home games. 
~~~

**Claimed live evidence.** `740071292127936623` (2020-08-04, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 740071292127936623
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0198.jsonl:466 @ row sha256:010e39a5c9ef758c7d9938425ff94df9ab6345637a80d5a9ab10e8ee1c9f3153
- timestamp: 2020-08-04T04:59:05.903000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-04T04:57:19.380000Z | Aerith [260949833773219840] | Please dont go 🙁
   2020-08-04T04:57:25.624000Z | that person logan [519566652824616973] | Love you too Friend BFDM
>> 2020-08-04T04:59:05.903000Z | DM radar [313689699627696139] | The pressure of the ship and now the haven of your home are meant to turn you from survivors to capable adventuring parties. It was never my intention to cause Web or Baeshra harm.
   2020-08-04T04:59:29.127000Z | DM radar [313689699627696139] | It was a crit.
   2020-08-04T04:59:42.455000Z | Basil [339235123759153162] | We're all here for each other. A d&d group isn't vs in competition(unless everyone agrees) but working together with reminders and communication. We all fall off that horse it's just a matter of getting back on it.
~~~

**Representative line.** “I know I should have signaled better how deadly through rp.”

### Mechanical warnings / lineage

- BCS-000045:L4113-L4124: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: None

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-016 — The event schedule yields when the table is no longer in a good state to play

Legacy confidence: high.

**Situation.** After a difficult interpersonal/mental-health discussion, a scheduled hunt was still due to happen.
- audit: audit:BDC-S3-016:situation
- proposition: sha256:a118d82300c3b4ec8b42e134760f6717ffcbe69feff4f53616b63f3b8af77486
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** Continuing the event would turn the schedule itself into a roadblock and the DM was no longer in a good state to run it.
- audit: audit:BDC-S3-016:noticed
- proposition: sha256:a0a8328e48ab25d327a792962eb70ebbdebc8cdb608b27528d46b7e623b26df5
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**What mattered.** table health, future play, schedule flexibility.
- audit: audit:BDC-S3-016:values
- proposition: sha256:38131cf45972c2324689b621d751fe578df0c8bab7a7411dbe4b82daed787b01
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon offered a mulligan on a painful memory if needed, deferred to the player about their own story, then canceled the night's event rather than forcing the timetable.
- audit: audit:BDC-S3-016:intervention
- proposition: sha256:64cb24c1c333d6149dff14c65feb3aa2746a48c38b8b70d38a880d45f1d47b11
- semantic status: UNVERIFIED
- flags: none

**Observed result.** Players accepted postponement and explicitly suggested returning to the game later.
- audit: audit:BDC-S3-016:observed_result
- proposition: sha256:957105f8d3aea88e267048b27c1f828312575f4cd62e08e99782cd067bdb3438
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** A schedule coordinates play; it does not outrank the humans playing. Cancel or defer content when the current table state would make running it destructive.
- audit: audit:BDC-S3-016:reusable_judgment
- proposition: sha256:3796f667e321481cc6f8e28e69112d3f036363f98bd5f3a83c1e8a507e768c6c
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L1569-L1587, BCS-000045:L1880-L1884

### Prep excerpt — BCS-000045:L1569-L1587
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:ced710cac7d12db4243251de1c4515d51d7bea34a29aff6247fe689b9c512861
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Tentative Game Play dates: Saturday July 18th 2020- August 21st. [b]
The purpose of this document is to outline season 3 of Roanoke.


What roanoke is:


Rules as written: roanoke is a 5 week long persistent Role Play Environment that seeks to combine the improvisational storytelling ability of tabletop role playing games with the functionality and user interface of video games. This is an rp heavy town drama told in 5 acts. 


Rules as intended: roanoke is a 5 week long deep dive into the daily lives of your characters. The game is centered around staying as a group to build a town, grow in your professions overcome horrific encounters and delve into the mysteries of the secret societies to which the townsfolk belong.


Settings: 
* Week one: London, England. In a fantasy reimagining of Europe.
* Week two: Gnerman Submarine. A voyage across the Atlantic.
* Week three: The Stillwater
* Week four: The Darkwater 
* Week five: The Aether
~~~

### Prep excerpt — BCS-000045:L1880-L1884
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:acee97c2aeb9ca445de369c9e017b3385a218c2afca914b07e56ebff106cc733
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Game breakdown by day:
* Launch Party/0 session irl.
Opening day: The Pall Mall Reform Club.
Day 2. 7/19/20 An Arcanian Werewolf in London-Golden Dawn into.
                Golden Dawn NPC introduced
~~~

**Claimed live evidence.** `740073630666457099` (2020-08-04, 🗨 Social / 🙋-out-of-character); `740073982539333702` (2020-08-04, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 740073630666457099
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0199.jsonl:24 @ row sha256:72f1ea1d536d85abe2316b6aaa2ab3795e2e17121412ec6205d54d3a419c8f99
- timestamp: 2020-08-04T05:08:23.454000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-04T05:07:16.323000Z | DM radar [313689699627696139] | Take care.
   2020-08-04T05:08:01.781000Z | Eloise >:3c [260820438026813440] | headcanon: Arc just spends all their time working on heaven's eye and doing astronomy stuff, which is why they're never around now
>> 2020-08-04T05:08:23.454000Z | DM radar [313689699627696139] | Cato. If you need to take a mulligan on the memory of Arc, let me know.
   2020-08-04T05:08:33.493000Z | Eloise >:3c [260820438026813440] | (oof)
   2020-08-04T05:08:46.999000Z | Mistah Noodles [363458590461132800] | A peaceful Roanoke? Wild
~~~

### Discord evidence — 740073982539333702
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0199.jsonl:32 @ row sha256:ed226b02473115d8810b88452d520fe9b581e99deaa5f9757891e6a801d092a0
- timestamp: 2020-08-04T05:09:47.347000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-04T05:08:56.650000Z | schrödingers dumbass [264570136025890816] | Arc becomes an NPC
   2020-08-04T05:09:25.208000Z | DM radar [313689699627696139] | I don't want this to become the next road block. And we are all feeling the effects of mental health.
>> 2020-08-04T05:09:47.347000Z | DM radar [313689699627696139] | But its your story.
   2020-08-04T05:09:55.247000Z | Aerith [260949833773219840] | I feel lost. Can we talk about it later...
   2020-08-04T05:10:03.088000Z | DM radar [313689699627696139] | yes
~~~

**Representative line.** “I don't want this to become the next road block... I'm canceling tonight's event.”

### Mechanical warnings / lineage

- BCS-000045:L1569-L1587: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L1880-L1884: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: None

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-017 — Rewrite campaign architecture when reality destroys the assumptions it depended on

Legacy confidence: very-high.

**Situation.** Season 3 was designed around four active faction stories, but two DMs became less active. The remaining structure collapsed into a binary, winner-take-all rivalry that was generating real table drama.
- audit: audit:BDC-S3-017:situation
- proposition: sha256:5a4644e7fea5d392ad70cbbfabdb7933982ff45a67efb9d1bbf951cf6f2ec856
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The original ending architecture no longer produced the intended multi-faction experience because its staffing assumptions had failed.
- audit: audit:BDC-S3-017:noticed
- proposition: sha256:caf0f71c443b6d070522aa259487497f559a7a9837d9076e3ad7454cd08b1981
- semantic status: UNVERIFIED
- flags: CAUSALITY_CLAIM, NEGATIVE_OR_ABSENCE_CLAIM

**What mattered.** table health, campaign ending, faction meaning, cooperation.
- audit: audit:BDC-S3-017:values
- proposition: sha256:ee8de36aa62545566277f1e2933fc7571926316e82bd901d756ba5836cf525c6
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon and Noah explicitly removed the bipartisan structure and rewrote the Mason and Knight endings so they could function as complementary defense and offense instead of mutually exclusive winners.
- audit: audit:BDC-S3-017:intervention
- proposition: sha256:ffbb580d381b9bac8065c686f67be0c0cdde218fa477e33ccf944014cb8dec78
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The finale acquired an in-world reason for the town to cooperate while preserving distinct faction contributions.
- audit: audit:BDC-S3-017:observed_result
- proposition: sha256:2be145c94aa7f42e6de2b92578ddef07c798ebf06526aa17ee108611bb934c28
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** When an implementation assumption fails, preserve the purpose of the design rather than its original topology. Rewrite the structure that is now producing the wrong experience.
- audit: audit:BDC-S3-017:reusable_judgment
- proposition: sha256:a1886a1e7a70e26b4b53945801118577ba38a423ed5a793135694a1924bd95e5
- semantic status: UNVERIFIED
- flags: none

**Claimed prep evidence.** BCS-000045:L1603-L1618, BCS-000045:L1680-L1705

### Prep excerpt — BCS-000045:L1603-L1618
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:848ba748694b013c823e07294af96ea122147dd283dac9e264ce8d44d6bdab2c
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Answering the call are four different organizations with four different reasons to travel to the New World


The Free Masons - This British Secret Organization of Artisan Builders is modeled after the real-life Masons. They seek to lay the foundations for a foothold in the Arcanian Society. They function as a foreign legion?


Knights du Roi Soleil (Knights of the Sun King) - A religious order dedicated to uncovering holy relics to use against power hungry forces of evil. They are modeled after the Knights Templar and seek to reunite lost artifacts of the Gods that sacrificed themselves to stave off a great evil to the West. They want to use this artifact to combat the rising supernatural evils that are growing, the ones beginning to look towards Europe.


The Order of Kairo (on a search and rescue mission around the world in 80 days style adventure club for the aristocracy -hufflepuff) and the NPC organization 


The Golden Dawn (Illuminati front who wish to lay claim to the wealth of Arcania) 


The groups encounter something underwater that throws them off course and wrecks the sub on the island.
~~~

### Prep excerpt — BCS-000045:L1680-L1705
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:bcc3d7312f16dd50e0a0100a241b072e52cbb56e8413dbbd3b5787361baa22a6
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
The freemasons:   
Week one: Recruitment.
Week two: Organization for building the colony along the lines of the ancient tradition of free masonry
Week three: Evidence of Ancient Free Masonry and the introduction of Hiram Bigfoot and Pym
Week four: Conflict can be influenced by adding masonic structures to the two warring tribes’ villages.
Week five:Masonic Ending available: The rite of the tinker.


The Golden Dawn: NPC ONLY
Week one: Filling the submarine with as many people as possible. 
Week two: Sabotage. A large number of sacrificed npcs to the deep mid voyage to ensure that Croatoan pushes the sub to Roanoke. 
Week three: Never present during hag attacks due to early warning ability.
Week four: Illuminati agent revealed amongst the uru
Week five: Illuminati ending available: All romantic couples are asked to give their first born. This resolves the immediate threat, but the child is immediately born, rapidly grows into an antichrist like figure and battles the group in place of the the deep version of croatoan.


The Order of Kairo- Adventure Club
Week one: Exposition given concerning reasons for travel. British History Museum
Week two: “Mantapolis, Schmantopolis. I see gold down there!” Kairo’s
Week three: Stillwater
Week four: Darkwater
Week five: Aether 


The Knights of the Roi Soleil - Monastic Order for Religious Artifact Recovery
Notable gods to the Knights' order:
~~~

**Claimed live evidence.** `745737396804518020` (2020-08-19, ❄ Things you should read. / ❕announcements)

### Discord evidence — 745737396804518020
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0365.jsonl:406 @ row sha256:e75934329d191f0f888a06b1dd8a0f863269423a7385091f458a7f9e99764b88
- timestamp: 2020-08-19T20:14:10.529000Z
- channel: ❄ Things you should read. / ❕announcements (734250210057912344)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
>> 2020-08-19T20:14:10.529000Z | DM radar [313689699627696139] | @everyone When we designed this game it was intended to have 4 active factions. 4 separate stories, each with their own separate quests to work toward influencing the ending. Through no fault of their own two of the DMs had to become less active. This left us with a Bi-Partisan system winner take all scenario. Its toxic and has been the source of much of the drama that we have had to address. Noah and I are making the choice to eliminate the bipartisan aspect of the game. The mason ending is altered from poisoning the hunger to bringing back the barrier after the Old Gods escape, the Knights will continue their quest to bind it and kill it. One representing offense, the other defense. Repeatedly we have been asked if the town can work together. The answer now has an in game reason for "Yes.".
~~~

**Representative line.** “Noah and I are making the choice to eliminate the bipartisan aspect of the game.”

### Mechanical warnings / lineage

- BCS-000045:L1603-L1618: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L1680-L1705: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 745737396804518020

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-018 — Protect the campaign's thematic center when an emergent subsystem begins consuming it

Legacy confidence: high.

**Situation.** Town politics and the mayoral race had become a dominant emergent activity, while the intended Mason through-line was about building, fellowship, and eventually the Tinker ending.
- audit: audit:BDC-S3-018:situation
- proposition: sha256:c39c0d83521b6bdba96b9eda71f94007dc8213540b5ae6c4f296fcdff42b1f97
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The political layer was becoming all-or-nothing and pulling attention away from the relationship/family theme Brendon wanted the season to resolve around.
- audit: audit:BDC-S3-018:noticed
- proposition: sha256:bc0f03396d32812bacfc95ac183d34defc97b4992eb5b941be9b346272492e6b
- semantic status: UNVERIFIED
- flags: none

**What mattered.** theme, table cohesion, faction identity, emergent play.
- audit: audit:BDC-S3-018:values
- proposition: sha256:0b27cc06a60aa4d171e3c267dfa349e44191d4abb465899b22eef340125807c9
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon articulated that the season's focus was bringing people together as friends and family, moved the Mason symbolism toward the rebuilt pub rather than governance, and resisted blame-focused politics in the final week.
- audit: audit:BDC-S3-018:intervention
- proposition: sha256:3be003f6642aaad35716b18223a95c6a3d1c40fb2c184e03a2965328d5c9f478
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The Mason story was reframed around rebuilding/community while final-week messaging emphasized coming back together.
- audit: audit:BDC-S3-018:observed_result
- proposition: sha256:97f2b13cd6fb0b3db0027e90ff6059d16405dfcf5a7292321300335db3ac7573
- semantic status: UNVERIFIED
- flags: none

**Reusable judgment.** Let emergent systems grow while they enrich the campaign. Redirect them when they begin cannibalizing the story's central concern or damaging table cohesion.
- audit: audit:BDC-S3-018:reusable_judgment
- proposition: sha256:3c27f0ab03ef40ffd86bd4aefe05f7c8b0ec7a027bd92c427fca6ba5af95180c
- semantic status: UNVERIFIED
- flags: none

**Claimed prep evidence.** BCS-000045:L1576-L1579, BCS-000045:L1680-L1685

### Prep excerpt — BCS-000045:L1576-L1579
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:dc3c1a92fe4f279edb0c76f88c358ed9cf7bbb33f9a10a3fd37f4de8668d601e
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Rules as written: roanoke is a 5 week long persistent Role Play Environment that seeks to combine the improvisational storytelling ability of tabletop role playing games with the functionality and user interface of video games. This is an rp heavy town drama told in 5 acts. 


Rules as intended: roanoke is a 5 week long deep dive into the daily lives of your characters. The game is centered around staying as a group to build a town, grow in your professions overcome horrific encounters and delve into the mysteries of the secret societies to which the townsfolk belong.
~~~

### Prep excerpt — BCS-000045:L1680-L1685
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:f33427113990c26165982843ac5ce810ff668bd4782a2d95c9a297dc98e58c76
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
The freemasons:   
Week one: Recruitment.
Week two: Organization for building the colony along the lines of the ancient tradition of free masonry
Week three: Evidence of Ancient Free Masonry and the introduction of Hiram Bigfoot and Pym
Week four: Conflict can be influenced by adding masonic structures to the two warring tribes’ villages.
Week five:Masonic Ending available: The rite of the tinker.
~~~

**Claimed live evidence.** `743967418824523836` (2020-08-14, 🗨 Social / 🙋-out-of-character); `745053207327277106` (2020-08-17, 🗨 Social / 🙋-out-of-character); `745054916850221076` (2020-08-17, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 743967418824523836
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0317.jsonl:122 @ row sha256:184951b767b2c53f6a5ca262ba54e49fe8286295b5b1d824542caaada63c881d
- timestamp: 2020-08-14T23:00:54.894000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-14T22:59:42.196000Z | DM radar [313689699627696139] | The intention, if you look back at the very beginning of that channel to distinguish this game from last year.
   2020-08-14T23:00:10.079000Z | DM radar [313689699627696139] | The pub is a dnd trope that is near and dear to my heart
>> 2020-08-14T23:00:54.894000Z | DM radar [313689699627696139] | and this years focus has been about bringing you all together not through governance, but by you all coming together as friends and family.
   2020-08-14T23:01:16.955000Z | DM radar [313689699627696139] | Thats why Heki (gil) was given the bar.
   2020-08-14T23:01:49.832000Z | DM radar [313689699627696139] | The way he is rebuilding over the cornerstone that daysong set is pretty moving to me
~~~

### Discord evidence — 745053207327277106
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0346.jsonl:478 @ row sha256:d44ef3f1c189ab4de67db51d1142720ea171f48f17ac52a3cbd6c3b3ba9ff1c3
- timestamp: 2020-08-17T22:55:27.046000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-17T22:54:56.587000Z | KnightOfCydonia [436232470242000916] | 🤪
   2020-08-17T22:55:23.818000Z | schrödingers dumbass [264570136025890816] | Simply go to the council member that focuses on the issue you have
>> 2020-08-17T22:55:27.046000Z | DM radar [313689699627696139] | The last week is about coming back together. Blame throwing for players might bring back some of the Toxicity from previous weeks that we have been trying to calm.
   2020-08-17T22:55:29.797000Z | DM radar [313689699627696139] | ❤️
   2020-08-17T22:55:53.859000Z | schrödingers dumbass [264570136025890816] | And then big issues discussed by the entire council
~~~

### Discord evidence — 745054916850221076
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0347.jsonl:6 @ row sha256:9c88a8d4c2a0772ca57a2643ef0287c32eec99bbf3ca8ed143a20079e9d20bb0
- timestamp: 2020-08-17T23:02:14.628000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-17T23:00:13.461000Z | Mistah Noodles [363458590461132800] | "For the Watch"
   2020-08-17T23:01:20.983000Z | Ozen [321508500138360843] | <@!519566652824616973> Skitter and i are ready whenever
>> 2020-08-17T23:02:14.628000Z | DM radar [313689699627696139] | The masons were designed to be further away from politics anyways. I put copper in the running because he is a capable and wise player. But I set the cornerstone on the pub, because our story was meant to be about something other than governance. But the mayoral race became bipartisan. And bipartisanship is allways all or nothing.
   2020-08-17T23:02:33.121000Z | Ozen [321508500138360843] | <@!363458590461132800> you are brilliant
   2020-08-17T23:03:00.545000Z | D (they/them) [692746345387130900] | Skitter should've become a mason much sooner, he had no idea.
~~~

**Representative line.** “our story was meant to be about something other than governance.”

### Mechanical warnings / lineage

- BCS-000045:L1576-L1579: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- BCS-000045:L1680-L1685: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 745054916850221076

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-019 — Correct a broken rule prospectively while honoring outcomes already earned under it

Legacy confidence: high.

**Situation.** A resurrection house rule proved too strong in actual play.
- audit: audit:BDC-S3-019:situation
- proposition: sha256:4f08536939513150366c3f1937109de1d7ab5f5d07da647c6d84ac2333b86a1b
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The rule was creating a balance problem that could not remain in the campaign as written.
- audit: audit:BDC-S3-019:noticed
- proposition: sha256:2c491cb76c8b333911ef7fc2e9bbc2b3cd28a010f7c56dde2341ec597225c7d5
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**What mattered.** game balance, fairness, trust in rulings.
- audit: audit:BDC-S3-019:values
- proposition: sha256:8acc540721dd98058fb57090ba2f29a00be86c022ff0999067d4926cbdd71d2b
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon publicly called the rule a genuine mistake, nerfed it going forward, and explicitly let that night's resurrections stand.
- audit: audit:BDC-S3-019:intervention
- proposition: sha256:38384fd1a149d5e325793cf1986ff1e62ef5a8b465ad5c92ae348ac04dca67d7
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The system changed without retroactively invalidating player outcomes that had been legal when they occurred.
- audit: audit:BDC-S3-019:observed_result
- proposition: sha256:8fb273b0d65a2b71f139c98864bcf2c1554642aada7ac8c9c6785ca59f2b0fa2
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Reusable judgment.** When a house rule fails in live play, fix it. Prefer prospective correction and preserve already-resolved outcomes unless the existing result is itself intolerable.
- audit: audit:BDC-S3-019:reusable_judgment
- proposition: sha256:b31a59dc34a60f818b342d36c25777840f5c8796da59adf8b0c450f0d990d5b9
- semantic status: UNVERIFIED
- flags: none

**Claimed prep evidence.** No direct pre-session rule located; runtime evidence only.

**Claimed live evidence.** `744056939096571924` (2020-08-15, ❄ Things you should read. / ❕announcements)

### Discord evidence — 744056939096571924
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0320.jsonl:440 @ row sha256:a07f997e31e9b90293c3d1160cf954cc93ebd2c5ec0ada85f10594ddd94ad391
- timestamp: 2020-08-15T04:56:38.190000Z
- channel: ❄ Things you should read. / ❕announcements (734250210057912344)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
>> 2020-08-15T04:56:38.190000Z | DM radar [313689699627696139] | @everyone I made a genuine mistake with my res rule. I'm going to have to nerf that ability for game balance reasons. Tonight's rez's still stand but the once per day rule can't stay in the game.
~~~

**Representative line.** “Tonight's rez's still stand but the once per day rule can't stay in the game.”

### Mechanical warnings / lineage

- representative-message match: 744056939096571924

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
---

## BDC-S3-020 — Downgrade encounter mode when turnout cannot support the intended challenge

Legacy confidence: high.

**Situation.** A dangerous tree encounter was planned, but the available player count was uncertain.
- audit: audit:BDC-S3-020:situation
- proposition: sha256:f5758a86869f86086b336939509feef9098feb1d6c4927cb5ab616d3b4fa43f7
- semantic status: UNVERIFIED
- flags: none

**What Brendon noticed.** The encounter's combat form depended on enough participants to make the risk and pacing work.
- audit: audit:BDC-S3-020:noticed
- proposition: sha256:3c64e3f167be08091078bb953fa30a70d7a6670e4e976d638b87beb24c8add99
- semantic status: UNVERIFIED
- flags: none

**What mattered.** challenge validity, attendance, continuity.
- audit: audit:BDC-S3-020:values
- proposition: sha256:1fdc120ab7f42142974f25e296a68b7cd415ce0135c2f3ff2e60c85673f272ee
- semantic status: UNVERIFIED
- flags: none

**Intervention.** Brendon declared in advance that insufficient turnout would convert the event to exploration only and that the fight could be skipped until later.
- audit: audit:BDC-S3-020:intervention
- proposition: sha256:6b91c0a2a03fadf15641cb1adf979ba1b43cf0870af70fb4ed06642b5f72af4e
- semantic status: UNVERIFIED
- flags: none

**Observed result.** The world remained explorable without forcing an understrength party into the combat merely because the encounter was scheduled.
- audit: audit:BDC-S3-020:observed_result
- proposition: sha256:3d84cd9a8805b4be5e6a088888214a03b2e2ffc3d0d239f29e43f8a40cf53a9c
- semantic status: UNVERIFIED
- flags: CAUSALITY_CLAIM, NEGATIVE_OR_ABSENCE_CLAIM

**Reusable judgment.** Treat encounter mode as conditional on the table state. If the group cannot support the intended challenge, preserve exploration/information and defer the fight.
- audit: audit:BDC-S3-020:reusable_judgment
- proposition: sha256:de5f63025374443e46596bd503d3d18bae85842726285a7a318f2cf7b360d571
- semantic status: UNVERIFIED
- flags: NEGATIVE_OR_ABSENCE_CLAIM

**Claimed prep evidence.** BCS-000045:L2802-L2815

### Prep excerpt — BCS-000045:L2802-L2815
- representation: sources/roanoke/BCS-000045/source.md
- representation SHA-256: adb0a8dbfe38fea3aa1c9eebf09a4a1f9c577bbd3c478b294454305c2488e166
- source metadata SHA-256: 9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055
- excerpt digest: sha256:9fe5fc9f354bf26b005972684502d8056f563cdd452759cad6e341a5ce0b42c7
- source quality: {"authorship": {"basis": "Not established; uploader and file ownership do not establish authorship.", "status": "UNKNOWN"}, "capture_status": {"assets": "NONE_EXTRACTED", "comments": "PRESERVED", "current_body": "CAPTURED", "revision_bodies": "NOT_PRESENT", "revision_metadata": "NOT_PRESENT"}, "normalization_method": "Donor normalized body preserved byte-for-byte except a corpus_id frontmatter remap when required.", "normalization_warnings": ["Google-native DOCX is an export snapshot, not the native Google document."], "not_established": [{"basis": "This pass did not find a message-level or channel-level Discord locator for this source. Publication, preparation, or a later campaign is not treated as live use.", "question": "live_use", "status": "NOT_ESTABLISHED"}], "production_stages": [{"basis": "The text is a rough campaign manuscript, with an unfinished table of contents, not a live record.", "confidence": "STRONG", "stage": "PREPRODUCTION", "support_refs": ["BCS-000045"]}], "reconciliation": {"canonical_corpus_id": "BCS-000045", "donor_branch": "ingest/drive-project-v3", "donor_corpus_id": "BCS-000045", "id_collision_remap": false, "preservation_note": "Native Drive identity and captured source artifacts preserved. Source wording was not rewritten."}, "source_kind": "google_drive_native"}

~~~text
Day 18 Ozark Howler (perhaps drawn out by hag rituals)
The Archivist: 
.So... You want to hear a story, eh? One about treasure hunters? Haha, have I got a story for you! Roanoke... This is our home. But make no mistake - this is not an island of peace and love. They say it's a no-man’s land, that it's dangerous, that only a fool would search for something of value here. Then perhaps I am a fool. But do not be fooled by what Roanoke appears to be. There was a legend... Many people tell it. The legend of the Howler. My father would always go on about the Howler; even with his dying breath. Advanced arcanian magic. Infinite wealth. Fame. Power. Women. So you can understand why some little kiddos who hear the stories grow up to become hunters. Well, I have a story you may not believe. But I tell you it is true. The legend of the Howler is real! And it is here on Roanoke. 


Now we have seen the hags that have always been associated with the myth of the howler. This tells me that the time is night. The howler is loosed upon the island, and great fame and renown comes to the slayer of the Howler. I have with me a piece of its ancestor and a spell to locate it. But it will only work for a few short hours. Make yourselves ready for a real adventure. 


When the time comes for the event, The Archivist casts “Find the path” Which leads the adventurers to the Uru Plateau. The plains are windswept and full of tumbleweeds and barren trees. Small patches of dead grass stand near small mosquito infected ponds.The sounds of insect life is loud and droning as a cool mist begins to rise from the ground. The ground turns from arid to swampy as the cracked earth begins to soak up water. Movement is cut in half as this becomes difficult terrain. The Find the path spell still shows them the most direct path, but staying on it will cause them to need to roll a con save every 15 minutes or take a level of exhaustion. 


Hex B 
Mud geyser.
The players come across a fountain of erupting mud and steam. The Howler howls and the fight begins. 
~~~

**Claimed live evidence.** `740004240600072299` (2020-08-04, 🗨 Social / 🙋-out-of-character)

### Discord evidence — 740004240600072299
- canonical source: discord/roanoke-season-3/roanoke-season-3.sqlite @ LFS SHA-256 16d47fa7c4f38d18670fc7fc2639614b0b61c31f716d8e6ecba86f1f87412b4d
- retrieval projection: model-index/discord/roanoke-season-3/messages-0196.jsonl:192 @ row sha256:551d1a7d56468e7901a493b89feff0f2dcff51f5b2463d9519da11e0be0385a7
- timestamp: 2020-08-04T00:32:39.573000Z
- channel: 🗨 Social / 🙋-out-of-character (636012145204527127)
- immutable author: 313689699627696139 — DM radar / bfdm

Bounded same-channel context:

~~~text
   2020-08-04T00:32:02.144000Z | DM radar [313689699627696139] | Head count for tonight's encounter?
   2020-08-04T00:32:20.218000Z | DCJJ [629235245291667476] | I’m a super solid maybe
>> 2020-08-04T00:32:39.573000Z | DM radar [313689699627696139] | (If there aren't enough players to to take on the tree it will be exploration only.)
   2020-08-04T00:33:26.232000Z | DCJJ [629235245291667476] | Question, would we be able to acquire her body from the tree if we killed it? For burial purposes
   2020-08-04T00:33:49.935000Z | DM radar [313689699627696139] | That seems like a solid possibility.
~~~

**Representative line.** “If there aren't enough players to to take on the tree it will be exploration only.”

### Mechanical warnings / lineage

- BCS-000045:L2802-L2815: UNRESOLVED; current support UNRESOLVED; representation drift established false.
- representative-message match: 740004240600072299

### Semantic review questions

1. Which field-level propositions are directly supported, strongly reconstructed, suggestive, contradicted, or unresolved by the staged evidence?
2. Does the case attribute Brendon's noticing, motive, choice, or causal effect more strongly than primary evidence permits?
3. Does chronology support the asserted intervention -> observed-result relationship, or is causality being inferred?
4. What evidence confidence survives?
5. What claim scope survives? One event does not become general-current-practice by default.
6. If a prep locator is broken, does the live evidence independently preserve any proposition, or must it be downgraded?
