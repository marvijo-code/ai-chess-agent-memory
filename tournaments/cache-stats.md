# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0023-20261010-213538)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 237 | 2709386 | 1691136 | 62.4% | 62.6% |
| GPT-6.1 Sol | 163 | 4609980 | 4306816 | 93.4% | 94.0% |
| Sonnet 5.5 | 168 | 3705400 | 3529462 | 95.3% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6132 | 68212857 | 33941504 | 49.8% | 49.7% |
| GPT-6.1 Sol | 4937 | 142276451 | 132369024 | 93.0% | 93.5% |
| Sonnet 5.5 | 5200 | 115134703 | 109965165 | 95.5% | 96.1% |
