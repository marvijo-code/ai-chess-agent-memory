# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0035-20261012-085617)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 115 | 1896942 | 1749888 | 92.2% | 93.1% |
| GLM 5.3 Flash | 122 | 1738861 | 1491968 | 85.8% | 86.4% |
| GPT-6.1 Sol | 91 | 2543120 | 2358656 | 92.7% | 93.4% |
| Sonnet 5.5 | 117 | 2962591 | 2830799 | 95.6% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8846 | 100844964 | 53834496 | 53.4% | 53.3% |
| GLM 5.3 Flash | 256 | 3389501 | 2891008 | 85.3% | 86.0% |
| GPT-6.1 Sol | 7288 | 213485894 | 198710016 | 93.1% | 93.6% |
| Sonnet 5.5 | 7456 | 167184676 | 159642233 | 95.5% | 96.2% |
