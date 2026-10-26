# BCS-000045 metadata rebind

The owner attestation on this branch changes `sources/roanoke/BCS-000045/metadata.json`. The source body is unchanged.

The reviewed hash was `9a6721f0af2bcdadfcecc1ae943f882809befef823aa4f2db5d21a988aef4055`. The attested metadata hash is `a6907ecde563dfc947b8b59402ae19cfa6a0a492c2a7b6f4d03dac8809b2fc8a`.

The ledger's stored metadata hash and the prepared-state hashes were updated to that file. The 78 `PARTIALLY_SUPPORTED` packet-state pointers now name the new global state `sha256:2b0d8b464fa5b0d247d4e26018abd39463b972cece59715dd21d0235cd533ccf`.

Semantic statuses were not reviewed again and were not changed: 78 `PARTIALLY_SUPPORTED`, 38 `SCOPE_OVERCLAIMED`, 4 `CONTEXT_CHANGES_INTERPRETATION`. This is a dependency rebind, not a new audit.
