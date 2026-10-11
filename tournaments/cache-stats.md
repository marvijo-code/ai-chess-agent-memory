# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0027-20261011-075651)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 76 | 714099 | 350208 | 49.0% | 48.8% |
| GPT-6.1 Sol | 85 | 2936663 | 2735488 | 93.1% | 93.5% |
| Sonnet 5.5 | 88 | 2117087 | 2035460 | 96.1% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7120 | 79499561 | 40160256 | 50.5% | 50.5% |
| GPT-6.1 Sol | 5629 | 163090398 | 151858688 | 93.1% | 93.6% |
| Sonnet 5.5 | 5915 | 130549651 | 124660658 | 95.5% | 96.1% |
