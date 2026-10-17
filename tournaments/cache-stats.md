# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0045-20261017-034241)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 226 | 12912031 | 10787072 | 83.5% | 83.8% |
| GLM 5.3 Flash | 154 | 5823740 | 4752384 | 81.6% | 82.0% |
| GPT-6.1 Sol | 263 | 9985873 | 9433472 | 94.5% | 95.0% |
| Haiku 5.5 | 209 | 11543281 | 10974318 | 95.1% | 95.4% |
| Sonnet 5.5 | 240 | 10816701 | 10052463 | 92.9% | 93.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10750 | 147793413 | 95155328 | 64.4% | 64.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1799 | 40894792 | 34646976 | 84.7% | 85.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10010 | 309047342 | 288116864 | 93.2% | 93.8% |
| Haiku 5.5 | 533 | 27969073 | 26724590 | 95.6% | 95.9% |
| Sonnet 5.5 | 10406 | 267824669 | 255683774 | 95.5% | 96.2% |
