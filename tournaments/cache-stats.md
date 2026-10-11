# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0024-20261011-001419)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 46 | 447638 | 257536 | 57.5% | 57.5% |
| GPT-6.1 Sol | 29 | 585541 | 543360 | 92.8% | 93.3% |
| Sonnet 5.5 | 24 | 330599 | 303666 | 91.9% | 93.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6234 | 69283769 | 34531840 | 49.8% | 49.8% |
| GPT-6.1 Sol | 5011 | 144101363 | 134040704 | 93.0% | 93.5% |
| Sonnet 5.5 | 5268 | 116383812 | 111144574 | 95.5% | 96.1% |
