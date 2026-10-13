# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0038-20261013-003046)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 159 | 2481522 | 2302720 | 92.8% | 93.4% |
| GLM 5.3 Flash | 136 | 2267016 | 1903360 | 84.0% | 84.9% |
| GPT-6.1 Sol | 174 | 5378213 | 4936192 | 91.8% | 92.5% |
| Sonnet 5.5 | 156 | 3999353 | 3832320 | 95.8% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9491 | 112118342 | 64292096 | 57.3% | 57.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 808 | 13054923 | 11544256 | 88.4% | 89.1% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8359 | 251334773 | 234120064 | 93.2% | 93.7% |
| Sonnet 5.5 | 8469 | 196937038 | 188324613 | 95.6% | 96.3% |
