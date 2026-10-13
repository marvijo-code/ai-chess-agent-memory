# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0040-20261013-090848)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 128 | 2168565 | 1907456 | 88.0% | 89.1% |
| GLM 5.3 Flash | 142 | 2118658 | 1666560 | 78.7% | 79.5% |
| GPT-6.1 Sol | 154 | 4532599 | 4164096 | 91.9% | 92.7% |
| Sonnet 5.5 | 185 | 5404278 | 5190155 | 96.0% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9931 | 120357124 | 71842432 | 59.7% | 59.7% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1118 | 18161189 | 15901376 | 87.6% | 88.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8879 | 268952201 | 250528128 | 93.1% | 93.7% |
| Sonnet 5.5 | 9109 | 216739763 | 207441523 | 95.7% | 96.4% |
