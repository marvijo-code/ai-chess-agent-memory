# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0038-20261013-003046)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 192 | 2959468 | 2731136 | 92.3% | 93.0% |
| GLM 5.3 Flash | 136 | 2267016 | 1903360 | 84.0% | 84.9% |
| GPT-6.1 Sol | 271 | 9785398 | 9095680 | 93.0% | 93.6% |
| Sonnet 5.5 | 292 | 9075398 | 8790337 | 96.9% | 97.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9524 | 112596288 | 64720512 | 57.5% | 57.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 808 | 13054923 | 11544256 | 88.4% | 89.1% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8456 | 255741958 | 238279552 | 93.2% | 93.7% |
| Sonnet 5.5 | 8605 | 202013083 | 193282630 | 95.7% | 96.4% |
