# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0039-20261013-051801)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 245 | 5038206 | 4727936 | 93.8% | 94.3% |
| GLM 5.3 Flash | 168 | 2987608 | 2690560 | 90.1% | 90.8% |
| GPT-6.1 Sol | 198 | 6145614 | 5703680 | 92.8% | 93.5% |
| Sonnet 5.5 | 179 | 4614408 | 4403967 | 95.4% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9769 | 117634494 | 69448448 | 59.0% | 59.1% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 976 | 16042531 | 14234816 | 88.7% | 89.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8654 | 261887572 | 243983232 | 93.2% | 93.7% |
| Sonnet 5.5 | 8814 | 207287749 | 198308907 | 95.7% | 96.4% |
