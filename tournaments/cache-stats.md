# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0019-20261010-104326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 56 | 541378 | 243072 | 44.9% | 44.7% |
| GPT-6.1 Sol | 58 | 1978725 | 1884160 | 95.2% | 95.4% |
| Sonnet 5.5 | 62 | 1676819 | 1617590 | 96.5% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4856 | 53438644 | 25537152 | 47.8% | 47.7% |
| GPT-6.1 Sol | 3951 | 114159033 | 106044288 | 92.9% | 93.4% |
| Sonnet 5.5 | 4196 | 92744908 | 88588911 | 95.5% | 96.1% |
