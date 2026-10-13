# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0038-20261013-003046)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 107 | 1838007 | 1716992 | 93.4% | 94.0% |
| GLM 5.3 Flash | 89 | 1721198 | 1479680 | 86.0% | 86.8% |
| GPT-6.1 Sol | 63 | 1594447 | 1445632 | 90.7% | 92.5% |
| Sonnet 5.5 | 60 | 1317503 | 1241946 | 94.3% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9439 | 111474827 | 63706368 | 57.1% | 57.2% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 761 | 12509105 | 11120576 | 88.9% | 89.6% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8248 | 247551007 | 230629504 | 93.2% | 93.7% |
| Sonnet 5.5 | 8373 | 194255188 | 185734239 | 95.6% | 96.3% |
