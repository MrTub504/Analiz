# Writer Path Evidence (ASTERFINANCE vs COINEX)

- PairKey: `ASTERFINANCE:KITEUSDT|COINEX:KITEUSDT`
- Symbol: `KITEUSDT`
- Divergence code: `B`
- Reason: COINEX/second exchange required symbols present but no plugin emits for prices/orderbook

## ASTERFINANCE
- required updates: 4
- emits: 636
- redis write attempts: 636
- redis payload keys(non-null): 2

## COINEX
- required updates: 4
- emits: 0
- redis write attempts: 0
- redis payload keys(non-null): 0

## Reader vs Writer keys
- reader expected keys: 2
- writer attempt keys: 30
- reader minus writer: 1