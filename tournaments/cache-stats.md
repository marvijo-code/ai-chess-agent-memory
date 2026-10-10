# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0017-20261010-051708)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 103 | 1420969 | 1049216 | 73.8% | 74.2% |
| GPT-6.1 Sol | 79 | 2047215 | 1841280 | 89.9% | 90.2% |
| Sonnet 5.5 | 66 | 1141684 | 1072068 | 93.9% | 94.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4250 | 46580292 | 22227584 | 47.7% | 47.7% |
| GPT-6.1 Sol | 3588 | 103583983 | 96152320 | 92.8% | 93.3% |
| Sonnet 5.5 | 3741 | 82209790 | 78488431 | 95.5% | 96.1% |
