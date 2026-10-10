# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0019-20261010-104326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 221 | 2226879 | 923136 | 41.5% | 41.2% |
| GPT-6.1 Sol | 165 | 4579636 | 4249600 | 92.8% | 93.2% |
| Sonnet 5.5 | 156 | 3229772 | 3071165 | 95.1% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5021 | 55124145 | 26217216 | 47.6% | 47.5% |
| GPT-6.1 Sol | 4058 | 116759944 | 108409728 | 92.8% | 93.3% |
| Sonnet 5.5 | 4290 | 94297861 | 90042486 | 95.5% | 96.1% |
