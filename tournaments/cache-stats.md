# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0039-20261013-051801)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 245 | 5038206 | 4727936 | 93.8% | 94.3% |
| GLM 5.3 Flash | 168 | 2987608 | 2690560 | 90.1% | 90.8% |
| GPT-6.1 Sol | 236 | 7824488 | 7306112 | 93.4% | 94.0% |
| Sonnet 5.5 | 217 | 6137107 | 5890733 | 96.0% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9769 | 117634494 | 69448448 | 59.0% | 59.1% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 976 | 16042531 | 14234816 | 88.7% | 89.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8692 | 263566446 | 245585664 | 93.2% | 93.7% |
| Sonnet 5.5 | 8852 | 208810448 | 199795673 | 95.7% | 96.4% |
