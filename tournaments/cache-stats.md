# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0041-20261013-124210)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 150 | 2918412 | 2784128 | 95.4% | 96.0% |
| GLM 5.3 Flash | 117 | 2177895 | 1948352 | 89.5% | 90.3% |
| GPT-6.1 Sol | 92 | 2455600 | 2163456 | 88.1% | 89.1% |
| Sonnet 5.5 | 135 | 3940498 | 3743059 | 95.0% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10134 | 124025247 | 75257088 | 60.7% | 60.7% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1235 | 20339084 | 17849728 | 87.8% | 88.5% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9025 | 272678211 | 253810304 | 93.1% | 93.6% |
| Sonnet 5.5 | 9402 | 225784354 | 216124117 | 95.7% | 96.4% |
