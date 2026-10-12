# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0035-20261012-085617)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 92 | 1628570 | 1537024 | 94.4% | 95.1% |
| GLM 5.3 Flash | 78 | 1124906 | 986048 | 87.7% | 88.3% |
| GPT-6.1 Sol | 69 | 2096827 | 1936896 | 92.4% | 92.9% |
| Sonnet 5.5 | 57 | 1226224 | 1154613 | 94.2% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8823 | 100576592 | 53621632 | 53.3% | 53.3% |
| GLM 5.3 Flash | 212 | 2775546 | 2385088 | 85.9% | 86.7% |
| GPT-6.1 Sol | 7266 | 213039601 | 198288256 | 93.1% | 93.6% |
| Sonnet 5.5 | 7396 | 165448309 | 157966047 | 95.5% | 96.2% |
