# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0038-20261013-003046)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 56 | 723566 | 637184 | 88.1% | 88.8% |
| GLM 5.3 Flash | 27 | 336223 | 291840 | 86.8% | 88.4% |
| GPT-6.1 Sol | 33 | 849267 | 777728 | 91.6% | 92.2% |
| Sonnet 5.5 | 60 | 1317503 | 1241946 | 94.3% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9388 | 110360386 | 62626560 | 56.7% | 56.7% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 699 | 11124130 | 9932736 | 89.3% | 90.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8218 | 246805827 | 229961600 | 93.2% | 93.7% |
| Sonnet 5.5 | 8373 | 194255188 | 185734239 | 95.6% | 96.3% |
