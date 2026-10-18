# Analysis: MADR records on a blockchain, as a system of trust

Prepared 2026-10-05 by Claude Opus 5.5, for the owner. Revised twice the same day.

- **First revision.** "Established format" means the mechanism, the purpose is to explore how a
  blockchain establishes trust, and the full MADR records go on-chain, not only a hash.
- **Second revision.** The owner judged about $62 for all records on Ethereum to be too expensive
  next to the other costs of an LLM-written project, and asked whether a separate chain is
  cheaper. This is not planned for the next month or two. It is a look at how the record could
  evolve.

If it ever becomes a decision, the outcome belongs in `docs/decisions/`.

## Summary

**Recommendation: split the record across two chains. The full text of each MADR record goes on
Arweave. A small Ethereum mainnet contract holds each record's hash, number and supersession
link, and enforces the log's rules: append-only, sequential numbers never reused, and change only
by supersession. That would cost about $2.70 for today's 17 records, roughly $0.16 a record,
against about $62 for full text on Ethereum mainnet.**

- **Yes, a separate chain is much cheaper, but each one buys its savings with trust.**
  - **Ethereum rollups (L2s).** Full text in contract state costs $0.09 (OP Mainnet), $0.51
    (Base) or $1.68 (Arbitrum One). But the data these rollups post to Ethereum expires after
    about 18 days. After that, the text survives only as long as the rollup's own operators keep
    it. The leading rollups are rated Stage 1, which means a Security Council can still upgrade
    the system.
  - **A chain of your own.** It is the cheapest option and gives up the point of the exercise: a
    chain is only as independent as the parties who validate it.
- **The split puts each job on the chain built for it.** Arweave exists to store data
  permanently from a single payment. Among these options, Ethereum mainnet gives the strongest
  guarantee that the rules and their order cannot be bent: the rollups rest on it, and the other
  options do not enforce rules at all. The expensive part on mainnet was storing the text, and
  the split stops doing that: the contract writes two storage slots per record instead of about
  80.
- **Where it loses:**
  - **Cost against a rollup.** It costs more than full text on OP Mainnet ($0.09 for all
    records).
  - **Two systems.** There are two tokens to hold (AR and ETH) and two networks to check.
  - **Arweave's permanence is an economic bet.** It assumes storage costs keep falling, not a
    guarantee from consensus.

  It still wins because a rollup's text depends on its operators and its Security Council. That
  fails your criterion of no single actor in control more clearly than Arweave's economics do.
  Whether about $0.16 a record is cheap enough is question 3.

Questions for you:

1. **Who holds the key that may append: you alone, or several people through a multisig?** With
   one key, the chain proves the history was never altered, but one actor still decides what
   enters it.
2. **Do you accept that nothing written can ever be withdrawn?** An edit like #86 would become
   a new entry, and the original text would stay public permanently.
3. **What cost per record is acceptable?** If $0.16 is too much, the remaining options are a
   rollup or a chain of your own, and each gives up trust to save money.

## Why a separate chain is cheaper, and what it gives up

Gas use is set by the EVM and is the same on every chain that runs it. Storing all 17 records in
contract state takes about 30.9M gas anywhere. What differs is the price of each unit of gas,
and that price is lower wherever fewer parties do less work to agree.

- **Ethereum mainnet: 0.741 gwei.** Every validator executes every transaction.
- **Rollups: 0.001 to 0.02 gwei.** One sequencer orders transactions. The rollup posts its state
  and data to Ethereum, and proofs make the state transitions checkable.
- **A chain of your own: as cheap as you choose.** You decide who validates.

What a rollup gives up, for this use:

- **Long-term availability.** Rollups post data to Ethereum as blobs, which are kept for about 18
  days (EIP-4844). After that, Ethereum holds only a commitment to the data. Reading old text
  depends on rollup nodes and archives, the same weakness that ruled out storing text in calldata
  on mainnet.
- **Upgrade control.** At L2BEAT's Stage 1, "the only way (other than bugs) for a rollup to
  indefinitely block an L2→L1 message … is by compromising ≥75% of the Security Council".
  Upgrades from anyone else need a 7-day exit window. Only Stage 2 limits the council to fixing
  bugs adjudicated on-chain. Base, Arbitrum One and OP Mainnet are all Stage 1.

## Options

All costs are for the 17 current records (42,961 bytes), measured on 2026-10-05.

| | Text kept by | Rules enforced by | Cost | Trust it rests on |
|---|---|---|---|---|
| Ethereum mainnet, full text | Every Ethereum node | Mainnet contract | ≈ $62 | Ethereum consensus |
| Rollup, full text | Rollup nodes; Ethereum blobs ~18 days | Rollup contract | $0.09 (OP), $0.51 (Base), $1.68+ (Arbitrum) | Rollup operators and a Security Council (Stage 1) |
| **Arweave text, mainnet rules** | Arweave | Mainnet contract | ≈ $0.25 + ≈ $2.45 | Arweave's endowment for the text, Ethereum consensus for the rules |
| Arweave only | Arweave | None | ≈ $0.25 | Arweave's endowment. The rules stay a promise |
| A chain of your own | Your validators | Your contract | Near zero | You |

Two options from the previous revision are set aside here. Calldata on mainnet expires with
block history. Bitcoin cannot enforce the rules, though that is unchecked (see Not checked).

## What would reverse this

- **A rollup reaches Stage 2, and its old state is archived independently** (for example by
  Ethereum's history archives, or its own data being made permanent). Full text on that rollup
  then beats the split: it is cheaper and one system.
- **Mainnet gas rises sharply.** The split's mainnet part scales with the gas price. At 10× today's
  0.741 gwei it costs about $1.44 a record, and rules enforced on a Stage 2 rollup start to win.
- **Arweave's endowment visibly fails,** for example through falling replication or miners
  leaving. The text would then need another home, and mainnet storage becomes the only place
  with consensus-grade permanence.
- **Ethereum adopts state expiry.** Even contract state then stops being kept by default.
- **No one ever checks the chain against the git copy.** The trust is never used, and the whole
  arrangement is accidental complexity.

## Measured facts

Obtained 2026-10-05. Prices are a snapshot and will have moved by the time this is acted on.
Gas amounts do not move with price, so costs can be recomputed from them.

From this repo:

- There are 17 decision records totalling 42,961 bytes. They need 1,351 32-byte storage slots.
- #86 (`f8199c5`) edited accepted records 0002 and 0014 to remove references to a private
  project.

Gas prices, from `eth_gasPrice` on each network's public RPC:

- **Ethereum mainnet:** 0.741 gwei, at 18:56 UTC.
- **Rollups, at 19:02 UTC:** Base 0.006 gwei, Arbitrum One 0.0200 gwei, OP Mainnet 0.0010
  gwei.
- **Ethereum blob base fee:** 0.032 gwei.

Data fees on OP-stack rollups:

- Base and OP Mainnet charge a separate fee for posting data to Ethereum. It was read from their
  `GasPriceOracle` (`0x42…0F`) with `getL1FeeUpperBound(44661)`, at about $0.005 (Base) and
  $0.008 (OP).
- Arbitrum's equivalent fee was not measured, which is why its cost is marked "+".

Token prices, from CoinGecko's simple price API:

- ETH $2,709–2,710.
- AR $4.49.

Arweave upload price:

- 3,340,175,566 winston for both a 6,509-byte and a 42,961-byte upload, from
  `arweave.net/price/<bytes>`. This appears to be a minimum charge per transaction, about $0.015.

Costs computed:

- **Full text in contract state:** 1,351 slots × (20,000 + 2,100) gas, plus 16 gas per calldata
  byte, plus 21,000 gas per transaction, which comes to 30.9M gas.
- **Split, mainnet part:** for each record, 2 slots × 22,100 gas, plus 21,000, plus about 100
  calldata bytes at 16 gas, plus an estimated 5,000 gas of execution. That is about 71,800 gas a
  record, 1.22M gas in all. The execution figure is an estimate. The contract is not written.

Primary sources:

- **EIP-2200:** "SSTORE_SET_GAS: 20000". EIP-2929 adds a cold-access cost of 2,100.
- **EIP-4844:** blobs are kept for "around 18 days".
- **EIP-4444 (Draft):** clients "SHOULD NOT serve headers, block bodies, and receipts" past the
  retention window. Account state is not on that list.
- **Ethereum Foundation, "Partial history expiry announcement" (2025-07-08):** clients can remove
  pre-Merge block data. "Work on full, rolling history expiry is ongoing."
- **L2BEAT** (`l2beat.com/scaling/summary`, `l2beat.com/stages`): Base, Arbitrum One and OP
  Mainnet are Stage 1. The Stage 1 and Stage 2 quotes above come from the stages page.
- **Optimism docs, transaction fees:** the L1 data fee is the compressed size times a weighted
  base fee and blob base fee.
- **Arweave, via `docs.ar.io`:** "Your fee, based on 200 years of storage for 20 replicas, goes
  mostly into a fund". The model "assumes storage costs drop over time".
- **Bitcoin paper** (`bitcoin.org/bitcoin.pdf`): design "begins with a timestamp server". Its
  references [3]–[5] are by Haber and Stornetta.

## Not checked

- **Who operates each rollup's sequencer, and whether it can censor an append.** Stage 1 covers
  withdrawals to Ethereum, not inclusion of an ordinary transaction.
- **Other blockchains with smart contracts** (Solana and others): their costs, how they handle
  storage rent, and their trust model. Not looked up.
- **Whether Ethereum has an active proposal for state expiry.** This is recalled as having been
  proposed before; its current status is unknown.
- **Whether storing text as contract bytecode (the "SSTORE2" pattern) is cheaper than storage
  slots.** Recalled, not computed. If it is, full text on mainnet would fall below $62.
- **Whether Bitcoin Script can enforce numbering or supersession.** Recalled as no, because
  Script is not Turing-complete.
- **Whether Arweave's compute layers (SmartWeave, AO) could enforce the rules.** If they can, the
  split might fit on one chain.
- **The relative decentralisation of the networks,** such as validator, miner and replica counts.
  Not measured.
- **The contract itself.** It has not been designed, written or tested.
