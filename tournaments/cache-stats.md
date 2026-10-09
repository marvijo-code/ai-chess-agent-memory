# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0010-20261009-112258)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 28 | 232445 | 94976 | 40.9% | 40.2% |
| GPT-6.1 Sol | 18 | 273159 | 237312 | 86.9% | 89.1% |
| Sonnet 5.5 | 22 | 272897 | 248961 | 91.2% | 93.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2475 | 27137647 | 12279424 | 45.2% | 45.1% |
| GPT-6.1 Sol | 2094 | 62344779 | 58057856 | 93.1% | 93.6% |
| Sonnet 5.5 | 2213 | 49656886 | 47477091 | 95.6% | 96.2% |
