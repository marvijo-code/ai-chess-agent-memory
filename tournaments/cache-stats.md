# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0017-20261010-051708)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 144 | 1860814 | 1269632 | 68.2% | 68.5% |
| GPT-6.1 Sol | 101 | 2443727 | 2179072 | 89.2% | 89.4% |
| Sonnet 5.5 | 118 | 2243679 | 2124073 | 94.7% | 95.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4291 | 47020137 | 22448000 | 47.7% | 47.7% |
| GPT-6.1 Sol | 3610 | 103980495 | 96490112 | 92.8% | 93.3% |
| Sonnet 5.5 | 3793 | 83311785 | 79540436 | 95.5% | 96.1% |
