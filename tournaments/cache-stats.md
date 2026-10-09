# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0006-20261009-001831)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 74 | 959031 | 397696 | 41.5% | 41.3% |
| GPT-6.1 Sol | 42 | 1073650 | 964096 | 89.8% | 90.0% |
| Sonnet 5.5 | 45 | 1000793 | 955323 | 95.5% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1468 | 16328622 | 7458432 | 45.7% | 45.6% |
| GPT-6.1 Sol | 1212 | 35912304 | 33559808 | 93.4% | 93.9% |
| Sonnet 5.5 | 1271 | 28990033 | 27750421 | 95.7% | 96.2% |
