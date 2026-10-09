# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0014-20261009-214817)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 56 | 590651 | 300800 | 50.9% | 51.3% |
| GPT-6.1 Sol | 70 | 2572563 | 2473600 | 96.2% | 96.3% |
| Sonnet 5.5 | 33 | 556202 | 520059 | 93.5% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3370 | 36630586 | 16864512 | 46.0% | 45.9% |
| GPT-6.1 Sol | 2970 | 87346246 | 81146240 | 92.9% | 93.4% |
| Sonnet 5.5 | 3120 | 69946330 | 66848203 | 95.6% | 96.1% |
