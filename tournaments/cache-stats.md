# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0044-20261016-161517)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 66 | 3182846 | 2689408 | 84.5% | 84.7% |
| GLM 5.3 Flash | 73 | 3296598 | 2517632 | 76.4% | 76.6% |
| GPT-6.1 Sol | 59 | 1457717 | 1357952 | 93.2% | 94.3% |
| Haiku 5.5 | 66 | 1973077 | 1846378 | 93.6% | 93.9% |
| Sonnet 5.5 | 120 | 6616574 | 6225038 | 94.1% | 94.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10464 | 132825647 | 82877184 | 62.4% | 62.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1515 | 28831338 | 24996416 | 86.7% | 87.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9463 | 286146027 | 266276736 | 93.1% | 93.6% |
| Haiku 5.5 | 66 | 1973077 | 1846378 | 93.6% | 93.9% |
| Sonnet 5.5 | 9851 | 241313918 | 230860542 | 95.7% | 96.4% |
