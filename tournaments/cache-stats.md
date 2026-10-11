# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0028-20261011-102906)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 138 | 1782832 | 1129984 | 63.4% | 63.4% |
| GPT-6.1 Sol | 135 | 5621771 | 5390464 | 95.9% | 96.0% |
| Sonnet 5.5 | 58 | 970117 | 908382 | 93.6% | 94.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7400 | 82829292 | 42175488 | 50.9% | 50.9% |
| GPT-6.1 Sol | 5966 | 174848497 | 163004672 | 93.2% | 93.7% |
| Sonnet 5.5 | 6092 | 133986865 | 127913102 | 95.5% | 96.1% |
