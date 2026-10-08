# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0004-20261008-185340)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 99 | 1075432 | 588160 | 54.7% | 54.8% |
| GPT-6.1 Sol | 108 | 3749885 | 3473280 | 92.6% | 93.0% |
| Sonnet 5.5 | 110 | 2733513 | 2627318 | 96.1% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 990 | 10970109 | 5133056 | 46.8% | 46.7% |
| GPT-6.1 Sol | 816 | 24166696 | 22612224 | 93.6% | 93.9% |
| Sonnet 5.5 | 901 | 20831860 | 19972812 | 95.9% | 96.3% |
