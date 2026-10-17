# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0045-20261017-034241)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 34 | 1901469 | 1391872 | 73.2% | 73.3% |
| GLM 5.3 Flash | 35 | 1147742 | 1031424 | 89.9% | 90.3% |
| GPT-6.1 Sol | 36 | 1117066 | 1058176 | 94.7% | 95.4% |
| Haiku 5.5 | 33 | 1180941 | 1108895 | 93.9% | 94.5% |
| Sonnet 5.5 | 36 | 1420092 | 1321671 | 93.1% | 93.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10558 | 136782851 | 85760128 | 62.7% | 62.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1680 | 36218794 | 30926016 | 85.4% | 86.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9783 | 300178535 | 279741568 | 93.2% | 93.7% |
| Haiku 5.5 | 357 | 17606733 | 16859167 | 95.8% | 96.1% |
| Sonnet 5.5 | 10202 | 258428060 | 246952982 | 95.6% | 96.3% |
