# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0016-20261010-025717)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 141 | 1580892 | 950784 | 60.1% | 60.3% |
| GPT-6.1 Sol | 75 | 1438402 | 1266048 | 88.0% | 89.2% |
| Sonnet 5.5 | 79 | 1198467 | 1113137 | 92.9% | 94.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4055 | 44209667 | 20765696 | 47.0% | 46.9% |
| GPT-6.1 Sol | 3431 | 99744463 | 92692992 | 92.9% | 93.4% |
| Sonnet 5.5 | 3600 | 79696725 | 76120484 | 95.5% | 96.1% |
