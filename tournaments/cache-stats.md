# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0039-20261013-051801)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 173 | 3545193 | 3322880 | 93.7% | 94.3% |
| GLM 5.3 Flash | 168 | 2987608 | 2690560 | 90.1% | 90.8% |
| GPT-6.1 Sol | 135 | 3830445 | 3497216 | 91.3% | 92.3% |
| Sonnet 5.5 | 159 | 4253215 | 4071560 | 95.7% | 96.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9697 | 116141481 | 68043392 | 58.6% | 58.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 976 | 16042531 | 14234816 | 88.7% | 89.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8591 | 259572403 | 241776768 | 93.1% | 93.7% |
| Sonnet 5.5 | 8794 | 206926556 | 197976500 | 95.7% | 96.4% |
