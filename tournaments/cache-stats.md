# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0020-20261010-134348)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 41 | 335901 | 133120 | 39.6% | 39.3% |
| GPT-6.1 Sol | 25 | 502545 | 438912 | 87.3% | 90.0% |
| Sonnet 5.5 | 21 | 275644 | 250050 | 90.7% | 92.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5120 | 56022887 | 26611072 | 47.5% | 47.4% |
| GPT-6.1 Sol | 4147 | 119931874 | 111374080 | 92.9% | 93.3% |
| Sonnet 5.5 | 4370 | 96222759 | 91886353 | 95.5% | 96.1% |
