# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0042-20261016-110957)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 88 | 1210784 | 1025664 | 84.7% | 85.7% |
| GLM 5.3 Flash | 63 | 832193 | 698496 | 83.9% | 85.8% |
| GPT-6.1 Sol | 65 | 1466054 | 1297664 | 88.5% | 89.9% |
| Sonnet 5.5 | 98 | 2326339 | 2198402 | 94.5% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10331 | 127928067 | 78734976 | 61.5% | 61.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1366 | 23291025 | 20515136 | 88.1% | 88.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9231 | 278249209 | 258850688 | 93.0% | 93.6% |
| Sonnet 5.5 | 9631 | 231412841 | 221457682 | 95.7% | 96.4% |
