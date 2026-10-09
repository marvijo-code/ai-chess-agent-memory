# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0012-20261009-164703)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 73 | 653661 | 377216 | 57.7% | 58.1% |
| GPT-6.1 Sol | 93 | 2557406 | 2379776 | 93.1% | 93.7% |
| Sonnet 5.5 | 81 | 1641523 | 1558890 | 95.0% | 95.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2917 | 31338654 | 14213376 | 45.4% | 45.2% |
| GPT-6.1 Sol | 2655 | 78928731 | 73426048 | 93.0% | 93.5% |
| Sonnet 5.5 | 2674 | 59433738 | 56787627 | 95.5% | 96.1% |
