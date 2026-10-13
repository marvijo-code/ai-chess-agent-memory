# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0039-20261013-051801)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 217 | 4653670 | 4378368 | 94.1% | 94.5% |
| GLM 5.3 Flash | 168 | 2987608 | 2690560 | 90.1% | 90.8% |
| GPT-6.1 Sol | 179 | 5782614 | 5377024 | 93.0% | 93.7% |
| Sonnet 5.5 | 159 | 4253215 | 4071560 | 95.7% | 96.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9741 | 117249958 | 69098880 | 58.9% | 59.0% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 976 | 16042531 | 14234816 | 88.7% | 89.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8635 | 261524572 | 243656576 | 93.2% | 93.7% |
| Sonnet 5.5 | 8794 | 206926556 | 197976500 | 95.7% | 96.4% |
