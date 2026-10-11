# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0030-20261011-145519)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 246 | 2548414 | 1367040 | 53.6% | 53.5% |
| GPT-6.1 Sol | 245 | 7892061 | 7353984 | 93.2% | 93.6% |
| Sonnet 5.5 | 159 | 3241733 | 3069690 | 94.7% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8070 | 89934781 | 46157312 | 51.3% | 51.3% |
| GPT-6.1 Sol | 6471 | 188516660 | 175556352 | 93.1% | 93.6% |
| Sonnet 5.5 | 6534 | 142603813 | 136065140 | 95.4% | 96.1% |
