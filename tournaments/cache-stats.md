# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0042-20261016-110957)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 88 | 1210784 | 1025664 | 84.7% | 85.7% |
| GLM 5.3 Flash | 73 | 1096441 | 923392 | 84.2% | 85.6% |
| GPT-6.1 Sol | 65 | 1466054 | 1297664 | 88.5% | 89.9% |
| Sonnet 5.5 | 108 | 2727196 | 2589973 | 95.0% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10331 | 127928067 | 78734976 | 61.5% | 61.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1376 | 23555273 | 20740032 | 88.0% | 88.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9231 | 278249209 | 258850688 | 93.0% | 93.6% |
| Sonnet 5.5 | 9641 | 231813698 | 221849253 | 95.7% | 96.4% |
