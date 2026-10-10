# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0023-20261010-213538)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 180 | 2035004 | 1242624 | 61.1% | 61.3% |
| GPT-6.1 Sol | 131 | 3878407 | 3621888 | 93.4% | 93.7% |
| Sonnet 5.5 | 136 | 3167415 | 3024972 | 95.5% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6075 | 67538475 | 33492992 | 49.6% | 49.5% |
| GPT-6.1 Sol | 4905 | 141544878 | 131684096 | 93.0% | 93.5% |
| Sonnet 5.5 | 5168 | 114596718 | 109460675 | 95.5% | 96.1% |
