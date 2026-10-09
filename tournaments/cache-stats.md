# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0012-20261009-164703)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 58 | 438534 | 254976 | 58.1% | 58.7% |
| GPT-6.1 Sol | 93 | 2557406 | 2379776 | 93.1% | 93.7% |
| Sonnet 5.5 | 69 | 1354559 | 1284901 | 94.9% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2902 | 31123527 | 14091136 | 45.3% | 45.2% |
| GPT-6.1 Sol | 2655 | 78928731 | 73426048 | 93.0% | 93.5% |
| Sonnet 5.5 | 2662 | 59146774 | 56513638 | 95.5% | 96.1% |
