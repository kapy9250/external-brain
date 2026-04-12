# Embracing the Bitter Lesson: How 1,039 AI-Generated Strategies Won Paradigm Autoresearch Hackathon

I barely even read the problem set. Every step of the solution was made by AI.

The autoresearch hackathon was the perfect opportunity to embrace Rich Sutton's Bitter Lesson: let computation beat human domain expertise.

1st Place on the Paradigm Optimization Arena Prediction Market Challenge (April 9, 2026 Hackathon).

[![Image 1](./assets/ryanli-embracing-bitter-lesson-ai-hackathon/image-01.jpg)](#)

* Final Score: $42.32 mean edge (median of 3 runs, each with a fresh random seed)
* Leaderboard Score (during hackathon): $52.03 (200 sims, fixed seed)
* Strategies Generated: 1,039 unique strategy variants
* Evaluation Runs: 2,000+
* Eval Scripts: 47 automated sweep/search scripts
* Final Strategy: ~900 lines of Python (`strategy_3610.py`)

The Optimization Arena Prediction Market Challenge asks you to write a market-making strategy for a simulated binary prediction market. The market has:
* A FIFO limit order book where you can only place passive limit orders
* An arbitrageur (informed trader) who sweeps mispriced quotes before retail arrives
* Retail traders (uninformed) who send random market orders — your profit source
* A static competitor with a hidden ladder that refills consumed levels
* 200 simulations per evaluation, each with random price paths and regimes

Your edge is scored as: `qty × (true_prob - price)` for buys and `qty × (price - true_prob)` for sells. The leaderboard ranks by mean edge across all 200 sims.

Our strategy is a market maker on a simulated binary prediction market order book. Each step, it cancels all previous orders and places a new bid and ask. The core idea:

1. **Don't trade when you'll lose.** Skip the tightest-spread regime (cs=1) entirely — the arbitrageur always eats you.
2. **Estimate the true price.** Info-theoretic mid estimation tracks bid/ask deltas separately to infer where the true price is — this feeds every other decision.
3. **Size based on arb risk.** Per-side Gaussian arb probability model: `size = k × retail_mult × (1 - arb_prob × damping)`. Quote big when the arb is unlikely to hit you (extreme prices, wide spreads), small when it's dangerous (near 50%, tight spreads).
4. **Detect and dodge jumps.** Track price jump frequency and direction. When a jump is detected, suppress orders on the dangerous side for a few steps.
5. **Exploit the 5% floor.** At prices below 5%, retail sell quantity is floored at 5% of notional — creating outsized profit opportunities on the ask side.
6. **Keep quoting when the book is empty.** When the competitor's orders are consumed (bid or ask is `None`), place orders at tick 1/99 instead of canceling — this is the highest-edge moment.
7. **Be cautious early, aggressive late.** Time-varying sizing (0.9× early, 1.15× late) reduces arb exposure while learning the regime.

Inspired by auto-research patterns, I used Claude Code as a team of parallel research agents — each exploring a different optimization direction simultaneously.

**The Loop:**
1. Spawn 8-20 parallel agents, each with a specific hypothesis or search space
2. Each agent independently: reads the current best strategy, creates variants, runs evaluations, reports results
3. Collect results, identify improvements, update the best strategy
4. Repeat with new hypotheses informed by what worked and what didn't

At peak, I had 20 agents running simultaneously, each sweeping different parameter spaces or testing structural changes. This massively parallelized the search — equivalent to weeks of manual experimentation compressed into hours.

A critical part of the challenge was understanding — and not overfitting to — the different evaluation layers:

**Local eval:** 200 sims each on multiple seed-starts (0, 500, 1000, 2000, etc.). Fast iteration. Each run uses 200 consecutive seeds. Testing across different seed-starts avoids overfitting to one batch.
**Leaderboard eval:** 200 sims on one fixed seed (unknown to us). Live ranking during the hackathon. Our best: $52.03. But this is just one seed — possible to overfit.
**Final eval:** Median of 3 runs, each with a fresh random seed. The actual hackathon ranking. Designed to reward consistency over lucky seed draws.

This is why multi-seed robustness became a core focus mid-session. Early on, I optimized only on seed=0 and hit +$44 locally. But when I tested on other seeds, performance varied wildly (+$34 to +$70). I shifted to always evaluating on 4 seeds minimum, often 8-16, and optimizing for the average. This prevented overfitting to any single seed's regime distribution.

For the final strategy, I validated across 16 different seed-starts — that's 3,200 total simulations — to confirm robustness before submitting. The 16-seed average was +$52.08, with individual seeds ranging from +$34 to +$70.

The final scoring (median of 3 fresh seeds) rewarded this approach. During the hackathon, I was #2 on the leaderboard at $52.03 (the top 2 spots were using an exploit and were disqualified). On the final eval with fresh seeds, our strategy held up better than competitors — pushing us to #1 with $42.32. Everyone's scores dropped on fresh seeds, but ours dropped less because we'd optimized for multi-seed consistency rather than chasing one lucky seed.

**Phase 1: Basics (−$15.83 → +$8.95)**
Key insight: Quote inside the competitor and skip toxic regimes.
The competitor spread (cs) determines profitability. At cs=1 (1-tick spread), the arbitrageur eats you alive. At cs=4 (4-tick spread), there's plenty of room to profit.
* Quote at `comp_bid + 1` / `comp_ask - 1` for FIFO priority over the competitor
* Skip cs=1 entirely (gap ≤ 2) — it always loses
* Per-CS sizing constants: k=3/8/16 for cs=2/3/4

**Phase 2: Extreme Price Exploitation (+$8.95 → +$14.61)**
Key insight: Retail quantities are asymmetric at extreme prices.
At low prices (<5%), retail sells only 5% of notional instead of price%. This creates a massive opportunity:
* At p=3%, retail sell = $4.50 / 0.05 = 90 shares (vs 150 normally)
* Your ask at 4 cents captures 90 shares × (0.04 - 0.03) = $0.90/fill
* Aggressive asks at low prices, conservative bids

**Phase 3: None-Handling Breakthrough (+$14.61 → +$25.39)**
Key insight: When the competitor book is empty, DON'T STOP QUOTING.
Every previous strategy returned `CancelAll()` when `comp_bid` or `comp_ask` was `None`. But book emptiness means retail just consumed the competitor — the richest moment to trade!
* Bid at tick 1, ask at tick 99 when book is empty
* Maximum edge per fill, near-zero arb risk
* This single change added +$10 in edge

**Phase 4: From-Scratch Arb-Risk Decomposition (+$25 → +$44)**
Key insight: Decompose the problem into retail capture vs arb avoidance.
A from-scratch agent (ignoring all existing code) discovered a superior architecture:
`size = base_size × retail_mult × (1 - arb_risk × damping)`
Where `arb_risk = exp(-spread² / (2 × ev²))` models the probability of arb execution. This formula naturally:
* Sizes up at extreme prices (high retail, low arb)
* Sizes down near 50% (high arb, low retail)
* Adjusts per-side based on distance from mid

Combined with info-theoretic mid estimation and jump-direction suppression, this jumped edge from +$25 to +$44.

**Phase 5: Marginal Gains Stacking (+$44 → +$52)**
Key insight: Stack many small improvements, each validated across multiple seeds for robustness.
With the architecture locked in, the focus shifted from finding new ideas to anti-overfitting. Every candidate improvement had to hold across multiple seeds, not just one. I launched waves of 20 agents each to find marginal gains:

[![Image 2](./assets/ryanli-embracing-bitter-lesson-ai-hackathon/image-02.jpg)](#)

The parallel agent approach was equally valuable for ruling things out. Across 1,000+ experiments:
* Multi-level quoting (−$3.46): Splitting orders across price levels just gives arb more to eat
* Bayesian/Kalman mid estimation (−$3): Hand-tuned heuristics beat principled approaches
* Retail quantity capping (−$9.62): Retail arrives in bursts — capping loses 2× what it saves in arb
* cs=1 extreme pricing (−$0.05): Even at tick 1/99, arb still eats you in cs=1
* Aggressive cs=4 sizing (−$1.64): More size = proportionally more arb, not more retail
* Spread widening on arb side (−$0.34): Full suppression is better than partial retreat
* Regime confidence boost (0): Regime is already stable — boost = flat size increase
* Parameter sweeps (~0): After 100+ sweep agents, the landscape is confirmed flat

The winning strategy (`strategy_3610`, ~900 lines) has this structure:
1. REGIME DETECTION: `gap = comp_ask - comp_bid` → cs bucket
2. MID ESTIMATION: info-theoretic delta tracking with separate bid/ask EMAs
3. SKIP/GATE: cs=1 skip, cs=2 vol gate, early cautious phase
4. PRICE SELECTION: `comp_bid+1` / `comp_ask-1` (inside competitor)
5. BASE SIZING: `k × retail_mult × arb_risk_factor`
6. FLOOR EXPLOIT: aggressive asks at p<5% (5% floor)
7. HIGH-PRICE ASYMMETRY: dampen bids, boost asks at p>75%
8. THROTTLE: reduce size near p=50% (high vol, high arb)
9. ARB-PROB SIZING: per-side Gaussian arb probability adjustment
10. TIME SCALING: 0.9× early, 1.0× mid, 1.15× late
11. CASH CONSTRAINTS: 88% at extremes, 45% at moderate
12. INVENTORY SKEW: quadratic skew with 3-regime extremity
13. JUMP SUPPRESSION: suppress dangerous side after detected jumps
14. NONE HANDLING: tick 1/99 when competitor book empty

**How I Used Claude Code:**
Each agent was launched with `Agent()` tool calls specifying:
* A specific hypothesis to test
* The base strategy to modify
* The evaluation protocol (seeds, sims, JSON parsing)
* A target to beat

Agents worked independently — reading the strategy file, making modifications, running evaluations, and reporting results. I never had to manually write evaluation scripts or parse results.

**Scale:**
[![Image 3](./assets/ryanli-embracing-bitter-lesson-ai-hackathon/image-03.png)](#)

**Automated Parameter Sweeps**
Agents didn't just create one-off strategies — they wrote 47 automated sweep scripts that systematically searched parameter spaces. Each script would:
1. Take a base strategy
2. Create temp copies with parameters modified
3. Evaluate each variant on multiple seeds
4. Rank by average edge
5. Write the winner as a new strategy file

This infrastructure meant agents could explore thousands of parameter combinations automatically, while the multi-seed evaluation ensured winners were robust rather than overfit to one seed.

**Saving Learnings**
I periodically saved learnings to markdown docs — breakthroughs, dead ends, confirmed-optimal parameters — so new agents could avoid re-exploring failed ideas.

**Starting From Scratch to Escape Local Optima**
The single biggest breakthrough came from telling an agent to ignore all existing code and start fresh. I was stuck at +$25 with incremental improvements stalling. A from-scratch agent — with only the challenge rules and a target to beat — independently discovered the arb-risk-weighted sizing formula that jumped us from +$25 to +$44 in one shot. This was a bigger gain than all previous incremental improvements combined. When progress plateaus, resetting beats iterating.

**Multi-Agent Collaboration: Claude Code + Codex**
When Claude Code agents got stuck, I occasionally ran Codex agents in parallel on the same challenge. The Codex agents independently produced strategies with different architectural ideas. I fed these back into Claude Code agents to cross-pollinate, extracting techniques like the per-side arb-probability sizing and high-probability throttling that became part of the final architecture. This multi-model approach — Claude Code as the primary optimizer, Codex as a source of diverse hypotheses when Claude Code stalled — gave broader coverage of the solution space than either model alone.

**Example: How an Agent Was Briefed**
Each agent got a self-contained prompt with full context. Here's an abbreviated version of the prompt that produced the Phase 4 breakthrough:
"You are trying to win a prediction market making challenge. The current best strategy scores +25 avg. You should try a COMPLETELY DIFFERENT approach from scratch. Key insights that work: skip cs=1, 5% floor exploit, None-handling at tick 1/99. But the SIZING is wrong — try decomposing into retail capture vs arb avoidance. Write to strategy_2020.py. Evaluate on seeds 0, 500, 1000, 2000. Target: beat +25 avg. Iterate up to 3 times."

This agent — starting from zero, with only domain knowledge and a target — independently discovered the arb-risk-weighted sizing formula that jumped edge from +$25 to +$44. It had no access to the 700+ previous strategies. Fresh perspective beat incremental optimization.

**Example: How a Dead End Was Confirmed**
When "retail quantity capping" seemed promising in theory (cap order size at 2× expected retail to reduce arb exposure), an agent tested 5 multipliers across 4 seeds:

[![Image 4](./assets/ryanli-embracing-bitter-lesson-ai-hackathon/image-04.png)](#)

The retail loss was consistently 2× the arb savings. This killed the idea permanently — retail arrives in bursts larger than the per-step average, so capping at any multiple loses more retail than it saves in arb.

The biggest breakthroughs came from from-scratch agents that ignored existing code entirely. When I was stuck at +$25, a fresh agent discovered the arb-risk decomposition that jumped us to +$44. This is the autoresearch equivalent of "don't get trapped in local optima."

The bitter lesson applies: scaling up search with occasional resets beat every clever hand-crafted idea. The winning strategy wasn't designed — it was discovered through 1,039 experiments, 20 parallel agents, and the willingness to throw everything away and start fresh when progress stalled.