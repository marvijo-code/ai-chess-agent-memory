# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0012-20261009-164703)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 35 | 277577 | 177536 | 64.0% | 65.0% |
| GPT-6.1 Sol | 51 | 1507550 | 1414272 | 93.8% | 94.3% |
| Sonnet 5.5 | 51 | 1152505 | 1104317 | 95.8% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2879 | 30962570 | 14013696 | 45.3% | 45.1% |
| GPT-6.1 Sol | 2613 | 77878875 | 72460544 | 93.0% | 93.5% |
| Sonnet 5.5 | 2644 | 58944720 | 56333054 | 95.6% | 96.1% |
