# Kursovoy Forensic Comparison

- PairKey: `ASTERFINANCE:KITEUSDT|COINEX:KITEUSDT`
- Side A: `ASTERFINANCE`
- Side B: `COINEX`
- Canonical symbol: `KITEUSDT`
- Symbol candidates: `KITEUSDT, KITE-USDT, KITE_USDT, KITE/USDT`

## Final row fields

- best_ask_buy: `0.2376`
- best_bid_sell: ``
- kursovoy_left_price: `0.2376`
- kursovoy_right_price: ``
- kursovoy_spread_pct: ``
- kursovoy_has_data: `False`
- kursovoy_missing_reason: `missing_orderbook_side`

## Trace sections present
- Count: `8`
- IsReadOnly: `False`
- Keys: `stages overlay_read_attempts read_payload_attempts read_market_payload_attempts writer_events_after_push writer_events_after_aggregation reader_store_diagnostics hub_runtime_state`
- Values: `True True True True True True True True`
- IsFixedSize: `False`
- SyncRoot: `System.Object`
- IsSynchronized: `False`

## Output files
- results.json
- selected_row.json
- selected_row_summary.json
- results_trace_api.json
- results_trace.json
- trace_*.json
- redis_probe.txt
- redis_values.json
- payload_fragments.json
- comparison.json